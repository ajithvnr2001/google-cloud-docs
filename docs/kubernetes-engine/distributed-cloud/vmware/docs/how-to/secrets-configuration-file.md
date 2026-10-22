---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file/
title: Secrets configuration file \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:07.454580+00:00
---

# Secrets configuration file  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Secrets configuration file Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the fields in a Secrets configuration file. You use a Secrets configuration file when you create [prepared Secrets](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials).

A Secrets configuration file holds a set of Secret groups. Each group has the name of a Kubernetes namespace and credentials for one or more of the following:

  * vCenter Server
  * F5 BIG-IP
  * A [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account)
  * A [connect-register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account)
  * A [logging-monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account)
  * An [audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account)
  * A [usage metering service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#usage_metering_service_account)
  * Private registry



You provide a Secrets configuration file as input to the `gkectl create secrets` command. For each Secret group, the command creates Kubernetes Secrets: one Secret for each of the credentials in the group. The command creates the Secrets in an admin cluster in the specified Kubernetes namespace.

To get started, create a template for your Secrets configuration file:
    
    
    gkectl create-config secrets
    

**Template**

Click to see the generated template.
    
    
    apiVersion: v1
    kind: ClusterSecrets
    # List of secret groups; for admin clusters it allows only one group
    secretGroups:
    # (Required for user clusters only) A unique name for secret namespace; it needs to
    # have prefix 'gke-onprem-secrets-' (example: gke-onprem-secrets-test)
    ‐ namespace: ""
      # Secrets in this namespace
      secrets:
        # The credentials for vCenter
        vCenter:
          username: ""
          password: ""
        # The credentials for f5BigIP
        f5BigIP:
          username: ""
          password: ""
        # The GCP service account key used to pull GKE images
        componentAccessServiceAccount:
          serviceAccountKeyPath: ""
        # The GCP service account key used to register the cluster
        registerServiceAccount:
          serviceAccountKeyPath: ""
        # The GCP service account key used to send logs and metrics from the cluster
        stackdriverServiceAccount:
          serviceAccountKeyPath: ""
        # The GCP service account key used to send audit logs from the cluster
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: ""
        # The credentials for private registry
        privateRegistry:
          username: ""
          password: ""  

## Filling in the fields in a Secrets configuration file

## `secretGroups`

An array of objects. Each object has the name of a Kubernetes namespace and a set of credentials.

For an admin cluster, only one Secret group is allowed.

### `secretGroups[i].namespace`

User cluster only.

A name of your choice for a Kubernetes namespace that will hold a set of Secrets. The name must begin with `gke-onprem-secrets-`.

Example:
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        ...
    - namespace: "gke-onprem-secrets-alice"
      secrets:
        ...
    

### `secretGroups[i].secrets.vCenter`

The username and password of a vCenter account.

Example:
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        vCenter:
          username: "vc-bob"
          password: "U$icUKEW#INE"
    

### `secretGroups[i].secrets.f5BigIP`

The username and password of an F5 BIG-IP account.

Example:
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        f5BigIP:
          username: "f5-bob"
          password: "exvQVx^@L%F1"
    

### `secretGroups[i].secrets.componentAccessServiceAccount.serviceAccountKeyPath`

The path of a JSON key file for a [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account).
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        componentAccessServiceAccount:
          serviceAccountKeyPath: "my-folder/component-access-key.json"
    

### `secretGroups[i].secrets.registerServiceAccount.serviceAccountKeyPath`

The path of a JSON key file for a [connect-register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account).
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        registerServiceAccount:
          serviceAccountKeyPath: "my-folder/connect-register-key.json"
    

### `secretGroups[i].secrets.stackdriverServiceAccount.serviceAccountKeyPath`

The path of a JSON key file for a [logging-monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account).

Example:
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        stackdriverServiceAccount:
          serviceAccountKeyPath: "my-folder/log-mon-key.json"
    

### `secretGroups[i].secrets.cloudAuditLoggingServiceAccount.serviceAccountKeyPath`

The path of a JSON key file for an [audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account).
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: "my-folder/audit-log-key.json"
    

### `secretGroups[i].secrets.privateRegistry`

The username and password of the **private** registry if using the private registry.

Example:
    
    
    secretGroups:
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        privateRegistry:
          username: "registry-user-bob"
          password: "f[vuV3^@L*4g"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
