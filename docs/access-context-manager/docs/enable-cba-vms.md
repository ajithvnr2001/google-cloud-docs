---
url: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vms/
title: Enable certificate-based access for VMs \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:18.545301+00:00
---

# Enable certificate-based access for VMs  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Enable certificate-based access for VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable [certificate-based access (CBA)](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access) for your Google Cloud VMs. You can use CBA to secure access from trusted devices to Google Cloud VMs.

## Overview

CBA for VMs uses the Google Cloud Context-Aware Access feature to secure access using Mutual TLS (mTLS). Following are the main components that you work with to enable and use CBA for VMs:

  * Access Context Manager: Lets you create access levels that require certificates when determining access to web applications.
  * Identity-Aware Proxy (IAP): [IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) lets you establish an encrypted tunnel over which you can forward SSH, RDP, and other traffic to VM instances. In addition, an IAP policy provides you with fine-grained control over which users are allowed to establish tunnels to specific VM instances and what access conditions the users must meet to use such tunnels.
  * Chrome Enterprise Policy: Provides mutual authentication (mTLS) between users and VMs when using the Chrome browser.
  * Google Cloud CLI: Provides mutual authentication (mTLS) between users and VMs when using the gcloud CLI.



## Before you begin

Ensure that you [created CBA access levels](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels) for your Google Cloud project.

## Grant roles for accessing VMs through IAP TCP forwarding

You must grant the appropriate Identity and Access Management (IAM) roles on a project to let users or user groups use IAP TCP forwarding to access VMs.

The following table shows the predefined roles that you need to grant to trusted administrators for TCP forwarding and related tasks. 

Task | Roles | More information  
---|---|---  
TCP forwarding |  IAP-secured Tunnel User (`roles/iap.tunnelResourceAccessor`)  |  Grant access to all VM instances in a project or Grant access to a specific VM  
SSH access |  Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`)   
OS Login (Recommended) | Various |  [ Configuring OS Login roles on user accounts](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access#configure_users)  
Use a service account | Service Account User (`roles/iam.serviceAccountUser`) | [ The serviceAccountUser role](https://docs.cloud.google.com/compute/docs/access/iam#the_serviceaccountuser_role)  
  
For more information about granting roles for IAP TCP forwarding, see [Grant roles for IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#grant-permission).

## Configure certificate-based access to a VM

Although IAP-TCP lets you grant access to all VM instances in a project, you must configure certificate-based access for each individual VM instance.

To grant a user or user group certificate-based access to a VM, grant the `roles/iap.tunnelResourceAccessor` role on the VM instance. The other roles can be granted on the project.

###  Console 

  1. Open the IAP Admin page, and then select the **SSH and TCP Resources** tab.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Select the VM instances that you want to configure. Click **Show info panel** if the info panel is not visible.

  3. Click **Add principal** and configure the following:

     * **New principals** : Specify the user or user group that you want to grant access to.
     * **Select a role** : Select **Cloud IAP > IAP-Secured Tunnel User**.
  4. Click **Add IAM condition** and configure a condition:

     * **Title** : Enter a name for the condition.
     * **Condition Builder** : Select **Access level** from the **Condition Type** drop-down, and then select the certificate-based access level created earlier.
  5. Click **Save**.




###  API 

To configure certificate-based access to a VM, modify your application's `policy.json` file.

See [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access#managing_access_with_the_api) for more information about using the IAM API to manage access policies.

  1. Export the following variables.
         
         export IAP_BASE_URL=https://iap.googleapis.com/v1/projects/PROJECT_NUMBER/iap_tunnel
         # Replace POLICY_FILE.JSON with the name of JSON file to use for setIamPolicy
         export JSON_NEW_POLICY=POLICY_FILE.JSON
         

  2. Get the IAM policy for the Compute Engine instance using the `getIamPolicy` method. The empty data bit at the end turns the curl request into `POST` instead of `GET`.
         
         curl -i -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              ${IAP_BASE_URL}/zones/ZONE_NAME/instances/INSTANCE_ID or INSTANCE_NAME:getIamPolicy \
              -d ''
         

  3. Grant the `iap.tunnelResourceAccessor` role and certificate-based access to your principals by modifying the [IAM policy JSON file](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#modify_policy).

Following is an example of a `policy.json` file that grants the `iap.tunnelResourceAccessor` role to a group of VM instance admins, giving them certificate-based access to IAP-secured tunnel resources.

Note that if a principal has the Owner role, they have permission to use IAP for TCP forwarding.
         
         {
           "policy": {
             "bindings": [
               {
                 "role": "roles/iap.tunnelResourceAccessor",
                 "members": ["group:instance-admins@example.com"],
                 "condition": {
                   "expression": "\"accessPolicies/POLICY_NAME/accessLevels/CERTIFICATE_BASED_ACCESS_LEVEL_NAME\" in request.auth.access_levels,
                   "title": "CERTIFICATE_BASED_CONDITION_NAME"
                 }
               }
             ]
           }
         }
         

To find a [policy name](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy), call the [`accessPolicies.list`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/list) method.
         
         GET https://accesscontextmanager.googleapis.com/v1/accessPolicies
         

  4. Set your new `policy.json` file using the `setIamPolicy` method.
         
         curl -i -H "Content-Type:application/json" \
                   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                   ${IAP_BASE_URL}/zones/ZONE_NAME/instances/INSTANCE_ID or INSTANCE_NAME:setIamPolicy \
                   -d @${JSON_NEW_POLICY}
         




## Access VMs using client certificates

To access VMs using client certificates, use one of the following methods.

  * [Use enterprise certificates](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-enterprise-certificates): Use this method if you have a PKI infrastructure.
  * [Use Endpoint Verification provisioned certificates](https://docs.cloud.google.com/access-context-manager/docs/cba-endpoint-verification-certs): Use this method if you don't have a PKI infrastructure. Endpoint Verification automatically provisions and registers self-signed certificates with Google Cloud for every device.



## Use client certificates on the Chrome browser to access VMs

  1. Configure the Chrome browser using one of the following options. 
     * [Configure the Chrome browser to use enterprise certificates](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-enterprise-certificates).
     * [Configure the Chrome browser to use Endpoint Verification provisioned certificates](https://docs.cloud.google.com/access-context-manager/docs/cba-endpoint-verification-certs).
  2. In the Chrome browser, enter the following domain to access the Google Cloud console: `console-secure.cloud.google.com`.
  3. Access Google Cloud VMs using [IAP tunneling](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#tunneling_ssh_connections).



## Use client certificates on the gcloud CLI to access VMs

  1. Configure the gcloud CLI using one of the following methods.

     * [Configure the gcloud CLI to use enterprise certificates](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-enterprise-certificates#configure_command-line_tools_to_use_your_enterprise_certificate)
     * [Configure the gcloud CLI to use endpoint verification provisioned certificates](https://docs.cloud.google.com/access-context-manager/docs/cba-endpoint-verification-certs#configure-cli-ev-certs)
  2. Access Google Cloud VMs using [IAP tunneling](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#tunneling_ssh_connections).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
