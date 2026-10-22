---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap/
title: Configure LDAP providers to authenticate to clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:57.105391+00:00
---

# Configure LDAP providers to authenticate to clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Configure LDAP providers to authenticate to clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document is for **platform administrators** , or whoever manages identity setup in your organization. It explains how to configure your chosen [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/) identity provider for authentication to Kubernetes clusters that aren't on Google Cloud.

You can use LDAP to authenticate to [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem) and [Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal) only.

## Before you begin

Throughout this setup, you might need to refer to the documentation for your LDAP server. The following administrator guides explain configuration for some popular LDAP providers, including where to find the information you need to log in to the LDAP server:

  * [OpenLDAP](https://www.openldap.org/doc/)
  * [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id)
  * [Microsoft Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/active-directory-overview)
  * [Google LDAP](https://support.google.com/a/topic/9173976?ref_topic=9048334)



## Get LDAP login details

During the authentication flow for users, the cluster uses a service account secret to authenticate to the LDAP server and retrieve user details. There are two types of service accounts permitted in LDAP authentication, basic auth (using a username and password to authenticate to the server) or client certificate (using a client private key and client certificate). To find out which type is supported in your specific LDAP server, see its documentation. Generally, Google LDAP only supports a client certificate as the service account. OpenLDAP, Microsoft Active Directory and Microsoft Entra ID support only basic auth natively.

The following instructions show you how to create a client and get LDAP server login details for some popular providers. For other LDAP providers, see the server's administrator documentation.

### Microsoft Entra ID/Active Directory

  1. Follow the UI instructions to create a new user account.
  2. Save the full user distinguished name (DN) and password for later.



### Google LDAP

  1. Ensure that you are logged in to your Google Workspace or Cloud Identity account in [accounts.google.com](https://accounts.google.com).
  2. Log in to the [Google Admin console](https://admin.google.com) with the account.
  3. Select **Apps** \- **LDAP** from the left menu.
  4. Click **Add client**.
  5. Add your chosen client name and description and click **Continue**.
  6. In the **Access permissions** section, ensure that the client has the appropriate permissions to read your directory and access user information.
  7. Download the client certificate and complete client creation. Downloading the certificate also downloads the corresponding key.
  8. Run the following commands in the relevant directory to base64 encode the certificate and key, substituting the file names of your downloaded certificate and key:
         
         cat CERTIFICATE_FILENAME.crt | base64
         cat KEY_FILENAME.key | base64
         

  9. Save the encrypted certificate and key strings for later.




### OpenLDAP

  1. Use the [`ldapadd`](https://man7.org/linux/man-pages/man1/ldapadd.1.html) command to add a new service account entry into the directory. Make sure that the account has permission to read the directory and access user information.
  2. Save the full user distinguished name (DN) and password for later.



## What's next

  * [Configure authentication for individual clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster)
  * [Configure authentication for your fleet](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
