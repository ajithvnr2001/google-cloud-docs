---
url: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-web-apps/
title: Enable certificate-based access for web applications \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:18.307967+00:00
---

# Enable certificate-based access for web applications  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-web-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Enable certificate-based access for web applications Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable [certificate-based access](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access) (CBA) for your web applications. You can use CBA to secure access from trusted devices to enterprise web applications running on Google Cloud.

## Overview

CBA for web applications uses the Chrome Enterprise Premium Context-Aware Access features and Google Cloud networking to secure access using [mutual TLS](https://docs.cloud.google.com/access-context-manager/docs/understand-mtls) (mTLS). Following are the main components that you work with to enable CBA for web applications:

  * Access Context Manager: lets you create access levels that require certificates when determining access to web applications.
  * Identity-Aware Proxy (IAP): authenticates user access to web applications.
  * Google Cloud HTTPS load balancer: provides mutual authentication (mTLS) between users and web applications.
  * Chrome Enterprise Policy: provides mutual authentication (mTLS) between users and web applications when using the Chrome browser.



## Before you begin

Verify that you have a current version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) by running the following command:
    
    
    gcloud components update
    

## Set up mTLS for the external HTTPS load balancer

Follow the [instructions](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https) to set up the HTTPS external load balancer. Note the name of the target HTTPS proxy that is created, because you will need it in a later step.

### Create a trust config

Create a [trust config](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#trust-configs) to represent your type of Public Key Infrastructure (PKI).

To complete this task, you must have the [`certificatemanager.trustconfigs.create`](https://docs.cloud.google.com/iam/docs/roles-permissions/certificatemanager) permission on the target Google Cloud project.

You can create a trust config using a Google-issued certificate (Method 1), using your own certificate (Method 2), or using a self-signed certificate with Endpoint Verification (Method 3).

### Method 1

Use a Google-issued certificate to create a trust config.

  1. Complete the steps to [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-root-ca).
  2. Fetch the PEM file contents:
         
         gcloud privateca roots describe ROOT_CA_ID \
             --pool=POOL_ID \
             --location=CA_LOCATION \
             --format='value(pemCaCertificates)'
         

Replace the following:

     * ROOT_CA_ID: The root certificate ID.
     * POOL_ID: The root certificate [pool](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool) ID.
     * CA_LOCATION: The CA location.
  3. Retrieve the root certificate, returned in the `pemCaCertificates` field. The certificate is the string between the `BEGIN CERTIFICATE` and `END CERTIFICATE` markers, and includes both markers.

  4. Save the root certificate in PEM format to a file.

  5. Create a trust config:

     1. Set the following environment variables:
            
            ROOT_PEM_FILE=TRUST_ANCHOR_PATH
            INT_PEM_FILE1=IM_CERT_PATH
            INT_PEM_FILE2=SECOND_IM_CERT_PATH
            

Replace the following:

        * TRUST_ANCHOR_PATH: The path to your PEM-encoded trust anchor.
        * IM_CERT_PATH: The path to your PEM-encoded intermediate certificate.
        * SECOND_IM_CERT_PATH: The path to your second PEM-encoded intermediate certificate.
     2. Prepare the contents of the trust config YAML file:
            
            ROOT=$(cat ROOT_PEM_FILE | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
            INT_1=$(cat INT_PEM_FILE1 | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
            INT_2=$(cat INT_PEM_FILE2 | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
            

     3. Create the trust config YAML file:
            
            cat << EOF > trust_config.yaml
            name: "${TRUST_CONFIG_NAME?}"
            trustStores:
            - trustAnchors:
              - pemCertificate: "${ROOT?}"
              intermediateCas:
              - pemCertificate: "${INT_1?}"
              - pemCertificate: "${INT_2?}"
             EOF
            

This YAML file defines a trust config named `TRUST_CONFIG_NAME`. The trust config contains one trust store, which includes the root certificate and two intermediate certificates.

     4. Import the trust config into Google Cloud Certificate Manager:
            
            gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME \
              --project=GCP_PROJECT \
              --source=${PWD?}/trust_config.yaml
            

Replace the following:

        * TRUST_CONFIG_NAME: The name of your trust config.
        * GCP_PROJECT: The Google Cloud project ID.



If you deploy a more complex structure with intermediate CAs signed by the root, ensure that you add your intermediates as `intermediateCAs`.

### Method 2

Use your own PKI deployment with existing certificates to create a trust config.

This type of trust config assumes a basic trust store with a single trust anchor representing a root certificate. No intermediate certificates are specified.

Create a trust config:

  1. Set the following environment variables:
         
         ROOT_PEM_FILE=TRUST_ANCHOR_PATH
         INT_PEM_FILE1=IM_CERT_PATH
         INT_PEM_FILE2=SECOND_IM_CERT_PATH
         

Replace the following:

     * TRUST_ANCHOR_PATH: The path to your PEM-encoded trust anchor.
     * IM_CERT_PATH: The path to your PEM-encoded intermediate certificate.
     * SECOND_IM_CERT_PATH: The path to your second PEM-encoded intermediate certificate.
  2. Prepare the contents of the trust config YAML file:
         
         ROOT=$(cat ROOT_PEM_FILE | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
         INT_1=$(cat INT_PEM_FILE1 | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
         INT_2=$(cat INT_PEM_FILE2 | sed 's/^[ ]*//g' | tr '\n' $ | sed 's/\$/\\n/g')
         

  3. Create the trust config YAML file:
         
         cat << EOF > trust_config.yaml
         name: "${TRUST_CONFIG_NAME?}"
         trustStores:
         - trustAnchors:
           - pemCertificate: "${ROOT?}"
           intermediateCas:
           - pemCertificate: "${INT_1?}"
           - pemCertificate: "${INT_2?}"
         EOF
         

This YAML file defines a trust config named `TRUST_CONFIG_NAME`. The trust config contains one trust store, which includes the root certificate and two intermediate certificates.

  4. Import the trust config into Google Cloud Certificate Manager:
         
         gcloud certificate-manager trust-configs import TRUST_CONFIG_NAME \
           --project=GCP_PROJECT \
           --source=${PWD?}/trust_config.yaml
         

Replace the following:

     * TRUST_CONFIG_NAME: The name of your trust config.
     * GCP_PROJECT: The Google Cloud project ID.



### Method 3

If you are using a Chrome browser, and want to use a self-signed certificate with Endpoint Verification, follow the instructions in this section.

Follow the [instructions](https://docs.cloud.google.com/endpoint-verification/docs/quickstart) to deploy Endpoint Verification for your organization. Endpoint Verification automatically deploys a Google-issued, self-signed certificate to your devices and you don't have to create a trust config.

### Create a TLS policy to enable mTLS on your external load balancer

If you used Method 3, you can skip this step.

To complete this task, you must have the following permissions:

  * [`certificatemanager.trustconfigs.use`](https://docs.cloud.google.com/iam/docs/roles-permissions) on the trust config you created for this `ServerTlsPolicy`
  * [`networksecurity.serverTlsPolicies.create`](https://docs.cloud.google.com/iam/docs/roles-permissions) on the target Google Cloud project


  1. Create the server [TLS policy](https://docs.cloud.google.com/load-balancing/docs/mtls#architecture) YAML file:
         
         cat << EOF > server_tls_policy.yaml
         name: "SERVER_TLS_POLICY_NAME"
         mtlsPolicy:
           clientValidationMode: ALLOW_INVALID_OR_MISSING_CLIENT_CERT
           clientValidationTrustConfig: projects/GCP_PROJECT/locations/global/trustConfigs/TRUST_CONFIG_NAME
         EOF
         

Replace the following:

     * SERVER_TLS_POLICY_NAME: The name of the server TLS policy.
     * GCP_PROJECT: The Google Cloud project ID.
     * TRUST_CONFIG_NAME: The trust config that you created in a previous step.

For information about the client validation options for `clientValidationMode`, see [MTLS client validation modes](https://docs.cloud.google.com/load-balancing/docs/mtls#mtls_errors).

  2. Import the server TLS policy YAML to the Google Cloud project:
         
         gcloud network-security server-tls-policies import ${SERVER_TLS_POLICY_NAME?} \
           --project=GCP_PROJECT \
           --source=${PWD?}/server_tls_policy.yaml \
           --location=global
         

Replace GCP_PROJECT with the Google Cloud project ID.




After you create a TLS policy, you cannot modify it. If you want to make changes to an existing TLS policy, delete the existing TLS policy and create new one.

### Attach a TLS policy to a target HTTPS policy

To complete this task, you must have the [`compute.targetHttpsProxies.get`](https://docs.cloud.google.com/iam/docs/roles-permissions) permission on the target Google Cloud project.

  1. Export your existing target HTTPS proxy into a local file:
         
         gcloud compute target-https-proxies export TARGET_HTTPS_PROXY_NAME \
             --project=GCP_PROJECT \
             --global \
             --destination=${PWD?}/xlb-mtls-target-proxy.yaml
         

Replace the following:

     * TARGET_HTTPS_PROXY_NAME: The target HTTPS proxy.
     * GCP_PROJECT: The Google Cloud project ID.
  2. Append the `ServerTlsPolicy` to the target HTTPS proxy configuration:

To complete this task, you must have the following permissions:

     * [`networksecurity.serverTlsPolicies.use`](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) on the `ServerTlsPolicy` you created for the target HTTPS proxy
     * [`compute.targetHttpsProxies.update`](https://docs.cloud.google.com/iam/docs/understanding-roles) on the target Google Cloud project
    
    echo "serverTlsPolicy:
    //networksecurity.googleapis.com/projects/GCP_PROJECT/locations/global/serverTlsPolicies/SERVER_TLS_POLICY_NAME" >> xlb-mtls-target-proxy.yaml
    

Replace the following:

     * GCP_PROJECT: The Google Cloud project ID.
     * SERVER_TLS_POLICY_NAME: The server TLS policy.
  3. Update the target HTTPS proxy by importing the new config from the local file:
         
         gcloud compute target-https-proxies import TARGET_HTTPS_PROXY_NAME \
             --project=GCP_PROJECT \
             --global \
             --source=${PWD?}/xlb-mtls-target-proxy.yaml
         

Replace the following:

     * TARGET_HTTPS_PROXY_NAME: The target HTTPS proxy.
     * GCP_PROJECT: The Google Cloud project ID.



## Create an access level that requires certificates

###  Console 

  1. Follow the instructions to [create a custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level).
  2. Add the following expression to your custom access level:

If you created a trust config (Method 1 or Method 2), add the following expression in the **Conditions** field of your custom access level to use PKI-attestation binding when authenticating:
         
         certIsPkiAttested(origin, ["TLS_POLICY_FULL_RESOURCE_PATH1", "TLS_POLICY_FULL_RESOURCE_PATH2", …]) == true
         

Where TLS_POLICY_FULL_RESOURCE_PATH1 and TLS_POLICY_FULL_RESOURCE_PATH2  are the paths that represent multiple trust configs: `certificatemanager.googleapis.com/projects/GCP_PROJECT/locations/global/trustConfigs/TRUST_CONFIG_NAME`.

You must provide at least one trust config path.

Replace the following:

     * GCP_PROJECT: The Google Cloud project ID.
     * TRUST_CONFIG_NAME: The name of your trust config.

If you used a Google-issued, self-signed certificate (Method 3), add the following expression in the **Conditions** field of your custom access level to use the certificate binding when authenticating:
    
    certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE
    




### gcloud

If you created a trust config (Method 1 or Method 2), run the following command to create a custom access level that uses PKI-attestation binding when authenticating:
    
    
    gcloud access-context-manager levels create ACCESS_LEVEL_NAME \
        --title=TITLE \
        --custom-level-spec=FILE \
        --description=DESCRIPTION \
        --policy=POLICY_NAME
    

Replace the following:

  * ACCESS_LEVEL_NAME: A unique name for the access level.
  * TITLE: A human-readable title.
  * FILE: A YAML file that contains the following expression:

`certIsPkiAttested(origin, ["TLS_POLICY_FULL_RESOURCE_PATH1", "TLS_POLICY_FULL_RESOURCE_PATH2", …]) == true`

Where TLS_POLICY_FULL_RESOURCE_PATH1 and TLS_POLICY_FULL_RESOURCE_PATH2  are the paths that represent multiple trust configs: `certificatemanager.googleapis.com/projects/GCP_PROJECT/locations/global/trustConfigs/TRUST_CONFIG_NAME`.

You must provide at least one trust config path.

Replace the following:

    * GCP_PROJECT: The Google Cloud project ID.
    * TRUST_CONFIG_NAME: The name of your trust config.
  * DESCRIPTION: A long-form description of the access level.

  * POLICY_NAME: Your organization's access policy.




If you don't have a trust config, because you are using a self-signed certificate with Endpoint Verification (Method 3), add the following expression to your custom access level:
    
    
    certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE
    

## Enforce certificate-based access using Identity-Aware Proxy (IAP)

In the CBA for web applications architecture, IAP provides [principal-based](https://docs.cloud.google.com/iap/docs/enabling-compute-howto#iap-access) policy enforcement to protect your web applications from untrusted devices.

Complete the following steps to enable IAP and configure the CBA policy:

  1. If you don't have IAP set up, follow the [instructions](https://docs.cloud.google.com/iap/docs/enabling-compute-howto) to set up IAP.
  2. Go to IAP to attach the access level you created earlier:  
[Go to IAP](https://console.cloud.google.com/security/iap/)
  3. Select the resource that you want to secure with CBA, and then click **Settings**.
  4. In the **Access Levels** field, enter the name of the access level you created.



To use the Google Cloud CLI to configure a CBA policy in IAP, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy).

## Configure the browser to automatically select the certificate

To have your browser automatically select the certificate when determining access, complete the steps for your browser.

###  Chrome 

Configure the `AutoSelectCertificateForURLs` Chrome policy so that Chrome uses the correct certificate during the mTLS handshake.

  1. Ensure that the Chrome browser is managed by the Chrome browser cloud management or Windows group policy:

     * Windows, macOS, Linux: Complete the steps to [set up a managed Chrome profile](https://support.google.com/chrome/a/answer/9025411).
     * Chrome: [Enroll](https://support.google.com/chrome/a/answer/1360534) the device to the enterprise.
  2. Add the `AutoSelectCertificateForUrls` policy:

     1. In the [admin console](https://admin.google.com/), go to **Devices** > **Chrome** > **Settings** > **User & Browser Settings** > **Client certificates**.
     2. Select an organization.
     3. Add an `AutoSelectCertificateForUrls` policy for your web application URL and root certificate information.



For more information, see the documentation on the [policy schema](https://chromeenterprise.google/policies/?policy=AutoSelectCertificateForUrls). Following is an example policy configuration that uses the certificate from Endpoint Verification:
    
    
    {
      "pattern":"https://[*.].mysite.com",
      "Filter":{
        "ISSUER":{
          "CN":"Google Endpoint Verification"
        }
      }
    }
    

###  Safari 

Configure the identity preference:

  1. Open the Keychain Access app, and then select **All Items**.
  2. Select the certificate that you want to configure.
  3. Click **File** > **New Identity Preference**.
  4. Enter the URL and click **Add**.



This creates a new identity preference entry in your Keychain that you can update.

###  Edge 

Set the `AutoSelectCertificateForUrls` Edge policy by following the instructions in the [Edge documentation](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#content-settings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
