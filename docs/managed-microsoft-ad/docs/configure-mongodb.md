---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/configure-mongodb/
title: Connect MongoDB \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:34.637448+00:00
---

# Connect MongoDB  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/configure-mongodb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Connect MongoDB Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to configure MongoDB for integration with Managed Service for Microsoft Active Directory. The following procedure is verified for MongoDB Enterprise, versions 4.0 and 4.2.

## Before you begin

Before configuring MongoDB, [create a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-create-domain).

## Deploying MongoDB

First, deploy MongoDB to Google Cloud. For compatibility with Active Directory, be sure to install a version of MongoDB that supports LDAP authentication, such as MongoDB Enterprise Edition. You can install MongoDB on a Compute Engine instance or you can deploy MongoDB on Google Kubernetes Engine.

### On a Compute Engine instance

To install MongoDB as a standalone package on a Compute Engine instance, [complete the steps in the MongoDB Enterprise installation](https://docs.mongodb.com/manual/administration/install-enterprise/).

### On a Google Kubernetes Engine container

To deploy MongoDB on Google Kubernetes Engine container, complete the following steps:

  1. Complete the [Running a MongoDB Database in Kubernetes with StatefulSets Codelab](https://codelabs.developers.google.com/codelabs/cloud-mongodb-statefulset/index.html?index=..%2F..index#0).
  2. Go to the `./mongo-k8s-sidecar/example/StatefulSet/` directory.
  3. Open `mongo-statefulset.yaml`
  4. Replace `image: mongo` with `image: path to gcr`



## Configuring Authentication

Next, configure authentication. Managed Microsoft AD can be used as an LDAP backend for authentication. You can choose LDAP or Kerberos.

To configure authentication, use the configuration values to complete one of the following setup procedures:

  * To set up authentication using LDAP, [complete the MongoDB LDAP tutorial](https://docs.mongodb.com/v4.0/tutorial/authenticate-nativeldap-activedirectory/). 
  * To set up authentication using Kerberos, [complete the MongoDB Kerberos tutorial](https://docs.mongodb.com/v4.0/tutorial/kerberos-auth-activedirectory-authz/).



### Authentication configuration values

Use the following values to configure authentication:

  * `security.ldap.server`: Use the FQDN you provided for the domain during setup.
  * `security.ldap.userToDNMapping`: Use the domain name of domain provided in `ldapQuery`. 
    * Example: `ldapQuery: "DC=cloudad,DC=gke,DC=com??sub?(userPrincipalName={0})"`
  * `security.ldap.server.authz`: Use domain name of domain provided in `queryTemplate`. 
    * Example: `queryTemplate: "DC=cloudad,DC=gke,DC=com??sub?(&(objectClass=group)(member:1.2.840.113556.1.4.1941:={USER}))"`
  * `security.ldap.transportSecurity`: Set to `none` to disable TLS/SSL.



In Managed Microsoft AD, users are created under `Cloud OU`. You should use the distinguished name for the resources and groups created under `Cloud OU`. For example, for user `dba`, you would use the distinguished name, `"CN=dba,OU=Cloud,DC=cloudad,DC=gke,DC=com"`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
