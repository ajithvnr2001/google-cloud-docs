---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin/
title: Configure prepared credentials for an admin cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:51.578512+00:00
---

# Configure prepared credentials for an admin cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure prepared credentials for an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to configure prepared credentials for an admin cluster in Google Distributed Cloud.

With prepared credentials, you can store credentials for your admin cluster in a Secret in your admin cluster. This provides an element of security, because you don't have to keep passwords and service account keys on your admin workstation.

Note the following limitation with advanced clusters:

  * Version 1.31: prepared credentials aren't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field).
  * Version 1.32 and higher: prepared credentials are supported on advanced clusters.



## Overview of the procedure

  1. Fill in a Secrets configuration file.

  2. In your admin cluster configuration file, set enabled to true.

  3. Run `gkectl prepare`

  4. Create the admin cluster. 




## Fill in your secrets configuration file

Generate a template for a Secrets configuration file:
    
    
    gkectl create-config secrets
    

The preceding command generates a file named `secrets.yaml`. You can change the name and location of this file if you like.

Familiarize yourself with the configuration file by reading the [Secrets configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file) document. You might want to keep this document open in a separate tab or window.

Here's an example of a Secrets configuration file. The one Secret group has values for vCenter credentials and four service account keys:
    
    
    apiVersion: v1
    kind: ClusterSecrets
    secretGroups:
    - secrets
      vCenter:
        username: "my-vcenter-account"
          password: "U$icUKEW#INE"
        componentAccessServiceAccount:
          serviceAccountKeyPath: "my-key-folder/component-access-key.json"
        registerServiceAccount:
          serviceAccountKeyPath: "my-key-folder/connect-register-key.json"
        stackdriverServiceAccount:
          serviceAccountKeyPath: "my-key-folder/log-mon-key.json"
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: "my-key-folder/audit-log-key.json"
    

## Admin cluster configuration file

Create an admin cluster configuration file as described in [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster).

In your admin cluster configuration file, set [`preparedSecrets.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials-admin/) to `true`:
    
    
    preparedsecrets:
      enabled: true
    

In your admin cluster configuration file, do not specify values for the following fields. These fields are not needed, because Google Distributed Cloud will get credentials and keys from your prepared Secrets.

  * `vCenter.credentials.fileRef.path`
  * `componentAccessServiceAccountKeyPath`
  * `loadBalancer.f5BigIP.credentials.fileRef.path`
  * `gkeConnect.registerServiceAccountKeyPath`
  * `stackdriver.serviceAccountKeyPath`
  * `cloudAuditLogging.serviceAccountKeyPath`
  * `privateRegistry.credentials.fileRef.path`



## Initialize the environment

Import OS images to vSphere, and push container images to a private registry if one has been specified.:
    
    
    gkectl prepare --config ADMIN_CLUSTER_CONFIG --secret-config SECRETS_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_CONFIG: the path of your admin cluster configuration file

  * SECRETS_CONFIG: the path of your Secrets configuration file




## Create the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config ADMIN_CLUSTER_CONFIG --secret-config SECRETS_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_CONFIG: the path of your admin cluster configuration file

  * SECRETS_CONFIG: the path of your Secrets configuration file




## Rotate credentials

To rotate credentials, you need a Secrets configuration file. There are two approaches you can take:

  * Run `gkectl create-config secrets` to generate a new Secrets configuration file. Fill in the file with new service account keys.

  * Generate a Secrets configuration file from the admin cluster. Then replace selected service account keys with new ones.

To generate a Secrets configuration file from the admin cluster:
        
        gkectl get-config admin --export-secrets-config \
          --bundle-path BUNDLE \
          --kubeconfig ADMIN_CLUSTER_KUBECONFIG
        

Replace the following:

    * BUNDLE: the path of the Google Distributed Cloud bundle file

    * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file




Rotate the credentials:
    
    
    gkectl update credentials CREDENTIAL_TYPE \
        --config ADMIN_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --secret-config SECRETS_CONFIG \
        --admin-cluster
    

Replace the following:

  * CREDENTIAL_TYPE: One of the following: vsphere, f5bigip, privateregistry, componentaccess, register, stackdriver, cloudauditlogging.

  * ADMIN_CLUSTER_CONFIG: the path of the admin cluster configuration file

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * SECRETS_CONFIG: the path of the Secrets configuration file




## Update

To update an admin cluster that uses prepared credentials, you can, in many cases, follow the instructions in as written in [Updating a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general).

However, if you want to enable [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-section) or [Cloud Audit Logs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#cloudauditlogging-section) as part of the update, follow these steps:

  1. Generate a Secrets configuration file.

  2. In your Secrets configuration file, provide values for `stackdriverServiceAccount.serviceAccountKeyPath` and `cloudAuditLoggingServiceAccount.serviceAccountKeyPath` or both.

  3. Update the cluster:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config ADMIN_CLUSTER_CONFIG \
           --secret-config SECRETS_CONFIG
         




## Related documents

  * [Secrets configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file)
  * [Admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest)
  * [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster)
  * [Create service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts)
  * [Prepared credentials for a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
