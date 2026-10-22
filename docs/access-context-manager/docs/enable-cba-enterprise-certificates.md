---
url: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-enterprise-certificates/
title: Enable certificate-based access with your enterprise certificates \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:52.033625+00:00
---

# Enable certificate-based access with your enterprise certificates  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-enterprise-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Enable certificate-based access with your enterprise certificates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable [certificate-based access (CBA)](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access) with your enterprise certificates.

If you don't have a Public Key Infrastructure (PKI), you can use [certificates provisioned by Endpoint Verification](https://docs.cloud.google.com/access-context-manager/docs/cba-endpoint-verification-certs).

An important requirement of the zero trust access model is to only allow access to authorized devices. Context-Aware Access CBA uses certificates and their private keys stored in a secure keystore on the device to determine whether the device is authorized. To enable this feature, complete the following procedures.

## Before you begin

Ensure that you have created CBA access levels for your Google Cloud project. If you need to create access levels, see [Create access levels for certificate-based access](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels).

Ensure that you enforce CBA on your Google Cloud resources using one of the following methods:

  * (Recommended) [Enforce certificate-based access with Context-Aware Access policies](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-user-groups): Configure rules around users.

  * [Enforce certificate-based access with VPC Service Controls](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vpcsc): Configure rules around data.




When you enforce CBA on your Google Cloud resources, accessing your Google Cloud resources requires an authorized user to also present a valid device certificate.

## Upload the trust anchors

To allow Context-Aware Access to collect and validate the enterprise certificate of a device, you must upload the trust anchors that are used to issue the device certificate. The trust anchors are the self-signed root CA certificate and the relevant intermediate and subordinate certificates. To upload the trust anchors, complete the following steps:

  1. In the [Google Admin console](https://admin.google.com/), go to **Devices** > **Networks** > **Certificates** , and then select the organizational unit for which to upload the trust anchors. Ensure that the organizational unit you select contains the users to which you want to grant access.

  2. Select **Add Certificate** , and then enter a name for your root certificate.

  3. Click **Upload** to upload the certificate.

  4. Select **Enable the Endpoint Verification** , and then click **Add**.




The certificate to be uploaded should be the CA certificate, which is the issuer of the client certificates installed on your corporate devices. If your company doesn't have a CA certificate and the corresponding client certificates, you can create them through the Google Cloud [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities). The steps to install client certificates into native keystores are different for each operating system and are outside of the scope of this document.

## Configure users' Chrome browser to use your enterprise certificate

Follow the instructions at [Set Up Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/quickstart) to install the Endpoint Verification extension for Chrome for all users in your organization. This extension syncs certificate metadata to Google Cloud's backend.

After you set up the browser extension, configure the `AutoSelectCertificateForURLs` Chrome policy to allow Endpoint Verification to search for the device certificate and collect it through Chrome.

  1. Ensure that Chrome Browser Cloud Management manages the users' Chrome browser.

     * [Set up Chrome Browser Cloud Management](https://support.google.com/chrome/a/answer/9301891)
  2. In the Admin console, add the `AutoSelectCertificateForUrls` policy:

     1. Go to **Devices** > **Chrome** > **Settings** > **User & Browser Settings** > **Client certificates**.

     2. Select the appropriate organizational unit.

     3. Add a policy.

The following example adds the `AutoSelectCertificateForUrls` policy:
            
            {"pattern":"https://[*.]clients6.google.com","filter":{"ISSUER":{"CN":"CERT_ISSUER"}}}
            {"pattern":"https://console-secure.cloud.google.com","filter":{"ISSUER":{"CN":"CERT_ISSUER"}}}
            {"pattern":"https://storage.mtls.cloud.google.com","filter":{"ISSUER":{"CN":"CERT_ISSUER"}}}
            

In the example, `CERT_ISSUER` is the common name of your CA certificate.




After this configuration, users can access protected Google Cloud resources with the Chrome browser at `console-secure.cloud.google.com`.

### Verify policy configuration (optional)

  1. In the Chrome browser, enter `chrome://policy`.

  2. Verify that `AutoSelectCertificateForUrls` is listed under **Chrome Policies**.

  3. Verify that the value for **Applies to** is **Machine**. On ChromeOS, the value for **Applies to** is **Current User**.

  4. Ensure that the **Status** for the policy does not have a **Conflict**. If the status does have a conflict, see [Understand Chrome policy management](https://support.google.com/chrome/a/answer/9037717) for information.




## Configure command-line tools to use your enterprise certificate

If users in your organization need to access Google Cloud resources from the command line, they must complete the following procedures to enable CBA with your enterprise certificate in their command-line tools.

Supported command-line tools include the following:

  * Google Cloud CLI

  * Terraform CLI (gcloud CLI is required to install and configure helper components.




Because the device certificates are stored in native keystores, the Google Cloud CLI is bundled with an open source component called _Enterprise Certificate Proxy_ (ECP) to interact with key management APIs.

If you're using a Windows system, you must have the [Visual Studio C++ runtime library installed](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

Supported operating systems and their respective built-in keystores include the following:

  * macOS with Keychain

  * Microsoft Windows with CryptoAPI

  * Linux with PKCS #11




ECP must be configured with the necessary metadata information to locate the certificate in the keystores.

### Install and configure ECP with the Google Cloud CLI

  1. [Install the Google Cloud CLI and enable CBA](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-client-apps). Install with the `bundled python` option enabled.

  2. For macOS and Linux, run the `install.sh` script after downloading it:
         
         $ ./google-cloud-sdk/install.sh
         

  3. Install the ECP helper component with the Google Cloud CLI:
         
         gcloud components install enterprise-certificate-proxy
         

  4. Initialize ECP certificate configuration with the Google Cloud CLI:




###  Linux 
    
    
    $ gcloud auth enterprise-certificate-config create linux
      --label=<CERT_LABEL> --module=<PKCS11_MODULE_PATH> --slot=<SLOT_ID>
    

Example:
    
    
    $ gcloud auth enterprise-certificate-config create linux
      --label="Google Endpoint Verification" --module=/usr/lib/x86_64-linux-gnu/pkcs11/libcredentialkit_pkcs11.so.0 --slot=0x1234567
    

###  macOS 
    
    
    $ gcloud auth enterprise-certificate-config create macos
      --issuer=<CERT_ISSUER>
    

Example:
    
    
    $ gcloud auth enterprise-certificate-config create macos
      --issuer="Google Endpoint Verification"
    

###  Windows 
    
    
    $ gcloud auth enterprise-certificate-config create windows
      --issuer=<CERT_ISSUER> --provider=<PROVIDER> --store=<STORE>
    

Example:
    
    
    $ gcloud auth enterprise-certificate-config create windows
      --issuer="Google Endpoint Verification" --provider=current_user --store=MY
    

The ECP configuration can also be manually configured. It is stored as a JSON file at the following location on the user's device:

  * Linux and macOS: `~/.config/gcloud/certificate_config.json`

  * Windows: `%APPDATA%\gcloud\certificate_config.json`




See the [ECP documentation on GitHub](https://github.com/googleapis/enterprise-certificate-proxy/blob/main/README.md#certificate-configuration) for additional examples of the configuration and schema.

###  Linux 
    
    
    {
      "cert_configs": {
        "pkcs11": {
          "label": "<CERT_LABEL>",
          "slot": "<SLOT_ID>",
          "module": "<PKCS11_MODULE_PATH>"
        }
      },
      "libs": {
        "ecp": "/usr/lib/google-cloud-sdk/bin/ecp",
        "ecp_client": "/usr/lib/google-cloud-sdk/platform/enterprise_cert/libecp.so",
        "tls_offload": "/usr/lib/google-cloud-sdk/platform/enterprise_cert/libtls_offload.so"
      }
    }
    

###  macOS 
    
    
    {
      "cert_configs": {
          "macos_keychain": {
            "issuer": "<CERT_ISSUER>"
          }
      },
      "libs": {
        "ecp": "<YOUR_GCLOUD_INSTALL_PATH>/google-cloud-sdk/bin/ecp",
        "ecp_client": "<YOUR_GCLOUD_INSTALL_PATH>/google-cloud-sdk/platform/enterprise_cert/libecp.dylib",
        "tls_offload": "<YOUR_GCLOUD_INSTALL_PATH>/google-cloud-sdk/platform/enterprise_cert/libtls_offload.dylib"
      }
    }
    

###  Windows 
    
    
    {
      "cert_configs": {
        "windows_store": {
          "store": "MY",
          "provider": "current_user",
          "issuer": "<CERT_ISSUER>"
        }
      },
      "libs": {
        "ecp": "C:/Users/<USERNAME>/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin/ecp.exe",
        "ecp_client": "C:/Users/<USERNAME>/AppData/Local/Google/Cloud SDK/google-cloud-sdk/platform/enterprise_cert/libecp.dll",
        "tls_offload": "C:/Users/<USERNAME>/AppData/Local/Google/Cloud SDK/google-cloud-sdk/platform/enterprise_cert/libtls_offload.dll"
      }
    }
    

After this configuration, users can access protected Google Cloud resources using command-line tools by enabling the CBA flag.

To enable CBA for the Google Cloud CLI, run the following command to set the `context_aware/use_client_certificate` property to `true`:
    
    
    $ gcloud config set context_aware/use_client_certificate true
    

To enable CBA for all other command-line tools, including Terraform, set the environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` to `true`.

## What's next

  * [Certificate-based access overview](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access)

  * [Understand mutual TLS at Google Cloud](https://docs.cloud.google.com/access-context-manager/docs/understand-mtls)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
