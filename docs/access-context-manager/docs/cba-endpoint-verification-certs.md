---
url: https://docs.cloud.google.com/access-context-manager/docs/cba-endpoint-verification-certs/
title: Enable certificate-based access with Endpoint Verification certificates \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:18.635483+00:00
---

# Enable certificate-based access with Endpoint Verification certificates  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/cba-endpoint-verification-certs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Enable certificate-based access with Endpoint Verification certificates Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable [certificate-based access (CBA)](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access) with your Endpoint Verification provisioned certificates.

You can use Endpoint Verification to automatically provision self-signed certificates for a device. Endpoint Verification provisioned certificates let you use CBA without a PKI infrastructure. These certificates are stored in keychain on macOS, in certificate stores on Windows, and in file systems on Linux.

If you have a PKI infrastructure, see [Enable certificate-based access with your enterprise certificates](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-enterprise-certificates) to enable CBA.

You can enable Endpoint Verification provisioned certificates on the following operating systems: 

  * macOS and Windows using the Chrome browser
  * macOS, Windows, and Linux using the Google Cloud CLI



If your operating system is not listed, see Using operating systems not fully supported.

## Before you begin

Before continuing, ensure that you meet the following requirements:

  * You [created CBA access levels](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels) for your Google Cloud project.

  * You enforce CBA on your Google Cloud resources using one of the following methods:

    * (Recommended) Configure rules around users by [enforcing certificate-based access with Context-Aware Access policies](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-user-groups).
    * Configure rules around data by [enforcing certificate-based access with VPC Service Controls](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vpcsc).
  * You are authorized to go through the [mTLS connection process](https://docs.cloud.google.com/access-context-manager/docs/understand-mtls) using a valid client certificate.




## Set up Endpoint Verification

Follow the instructions to [install the Chrome Endpoint Verification extension](https://docs.cloud.google.com/endpoint-verification/docs/quickstart#install-extension) for all user devices in your organization. The extension provisions self-signed certificates onto your devices and syncs certificate metadata to Google Cloud.

Install the [Endpoint Verification helper app](https://docs.cloud.google.com/endpoint-verification/docs/deploying-with-admin-console#install-native-helper). This app is required for using Endpoint Verification with CBA.

## Configure users' Chrome browser

To configure users' Chrome browser to use Endpoint Verification provisioned certificates, you must configure the AutoSelectCertificateForURLs Chrome policy to allow Endpoint Verification to search for the device certificate and collect it through Chrome.

  1. Ensure that users' Chrome browser is [managed by Chrome Browser Cloud Management](https://support.google.com/chrome/a/answer/9301891).
  2. In the [Google Admin console](https://admin.google.com/), add the AutoSelectCertificateForUrls policy.

     1. Go to **Devices > Chrome > Settings > User & Browser Settings > Client certificates**.
     2. Select the appropriate organizational unit.
     3. Add a policy. The following example adds the AutoSelectCertificateForUrls policy:
            
            {"pattern":"https://[*.]clients6.google.com","filter":{"ISSUER":{"CN":"Google Endpoint Verification"}}}
            {"pattern":"https://console-secure.cloud.google.com","filter":{"ISSUER":{"CN":"Google Endpoint Verification"}}}
            {"pattern":"https://storage.mtls.cloud.google.com","filter":{"ISSUER":{"CN":"Google Endpoint Verification"}}}
            




After you complete the configuration, users can access protected Google Cloud resources with the Chrome browser at [console-secure.cloud.google.com](https://console.cloud.google.com/).

### (Optional) Verify the policy configuration

  1. In the Chrome browser, enter `chrome://policy`.
  2. Verify that AutoSelectCertificateForUrls is listed under **Chrome Policies**.
  3. Verify that the value for **Applies to** is **Machine**. On ChromeOS, the value for **Applies to** is **Current User**.
  4. Ensure that the status for the policy does not have a conflict. If the status has a conflict, see [Understand Chrome policy management](https://support.google.com/chrome/a/answer/9037717) for information.



## Configure command-line tools

You can configure the following tools to use Endpoint Verification provisioned certificates:

  * The Google Cloud CLI
  * The Terraform CLI (The gcloud CLI is needed to install and configure helper components.)



Because device certificates are stored in macOS and Windows keystores, the gcloud CLI is bundled with the [Enterprise Certificate Proxy (ECP)](https://github.com/googleapis/enterprise-certificate-proxy) open source component to interact with the key management APIs.

If you're using a Windows system, you must have the Visual Studio C++ runtime library installed.

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). Install with the bundled Python option enabled.
  2. [Enable CBA](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-client-apps).
  3. For macOS and Linux, download and then run the `install.sh` script.
         
         ./google-cloud-sdk/install.sh
         

  4. Linux users, go to the Enable CBA and Endpoint Verification provisioned certificates  step. macOS and Windows users, complete the following steps.

     1. Install the ECP helper component with the gcloud CLI.
            
            gcloud components install enterprise-certificate-proxy
            

     2. Initialize the ECP certificate configuration with the gcloud CLI.

###  macOS 
            
            gcloud auth enterprise-certificate-config create macos \
            --issuer="Google Endpoint Verification"
            

###  Windows 
            
            gcloud auth enterprise-certificate-config create windows \
            --issuer="Google Endpoint Verification" \
            --provider=current_user \
            --store=MY
            

(Optional) Configure the ECP certificate manually by running the following command.

###  macOS 

The ECP configuration is stored in a JSON file, located in `~/.config/gcloud/certificate_config.json`.
            
            {
              "cert_configs": {
                  "macos_keychain": {
                    "issuer": "Google Endpoint Verification"
                  }
              },
              "libs": {
                "ecp": "<YOUR_GCLOUD_INSTALL_PATH>/google-cloud-sdk/bin/ecp",
                "ecp_client": "<YOUR_GCLOUD_INSTALL_PATH>/google-cloud-sdk/platform/enterprise_cert/libecp.dylib",
                "tls_offload": "<YOUR_GCLOUD_INSTALL_PATH>/google-cloud-sdk/platform/enterprise_cert/libtls_offload.dylib"
              }
            }
            

###  Windows 

The ECP configuration is stored in a JSON file, located in `%APPDATA%\gcloud\certificate_config.json`.
            
            {
              "cert_configs": {
                "windows_store": {
                  "store": "MY",
                  "provider": "current_user",
                  "issuer":"Google Endpoint Verification"
                }
              },
              "libs": {
                "ecp": "C:/Users/<USERNAME>/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin/ecp.exe",
                "ecp_client": "C:/Users/<USERNAME>/AppData/Local/Google/Cloud SDK/google-cloud-sdk/platform/enterprise_cert/libecp.dll",
                "tls_offload": "C:/Users/<USERNAME>/AppData/Local/Google/Cloud SDK/google-cloud-sdk/platform/enterprise_cert/libtls_offload.dll"
              }
            }
            

  5. Enable CBA and Endpoint Verification provisioned certificates.

     * For the gcloud CLI, run the following command.
           
           gcloud config set context_aware/use_client_certificate true
           

     * For all other command-line tools, including Terraform, set the environment variable.
           
           export GOOGLE_API_USE_CLIENT_CERTIFICATE=true
           




## Using operating systems not fully supported

If your operating system is not in the list of supported operating systems, and you want to use Endpoint Verification provisioned certificates, you can exempt the environments from certificate-based enforcement and instead protect them using other types of enforcement. For example, by using a company owned device policy.

Note that certificate-based enforcement offers stronger protection over other types of enforcement because it enforces every request coming from a device through the mTLS handshake.

Following is an example of how to exempt environments from certificate-based enforcement and protect them using another type of enforcement.

In this example, an organization uses macOS, Windows, and ChromeOS devices. The organization wants to protect access originating from the Google Cloud console.

  1. [Create an access level](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels) that enforces certificate-based access for all of the devices, except for ChromeOS devices where a company owned device policy is required. Replace the YAML file with the following custom expression:
         
         certificateBindingState(origin, device) == CertificateBindingState.CERT_MATCHES_EXISTING_DEVICE
          || (device.os_type == OsType.DESKTOP_CHROME_OS && device.is_corp_owned_device)
         

  2. Complete the steps in the previous procedures.

     1. Create a context-aware policy
     2. Set up Endpoint Verification
     3. Configure users' Chrome browser to use Endpoint Verification provisioned certificates



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
