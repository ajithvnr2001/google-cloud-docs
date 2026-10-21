---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials/
title: Configure prepared credentials for user clusters \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:52.195078+00:00
---

# Configure prepared credentials for user clusters  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure prepared credentials for user clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to configure prepared credentials for user clusters in Google Distributed Cloud.

With prepared credentials, you can store credentials for your user clusters in Secrets in your admin cluster. This provides an element of security, because you don't have to keep passwords and service account keys on your admin workstation as you create your user clusters.

Note the following limitation with advanced clusters:

  * Version 1.31: prepared credentials aren't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).
  * Version 1.32 and higher: prepared credentials are supported on advanced clusters.



You prepare Secrets in the admin cluster ahead of time. Then as you create user clusters, you can specify that certain credentials should be taken from the prepared Secrets in the admin cluster. You can also use the prepared Secrets when you rotate credentials in a user cluster.

## Before you begin

[Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) if you don't already have one.

## Overview of the procedure

  1. Fill in a Secrets configuration file.

  2. In your admin cluster, create groups of Secrets. Each Secret group is in its own Kubernetes namespace.

  3. Create a user cluster. In the user cluster configuration file, indicate that you want credentials to be taken from Secrets in a particular namespace in the admin cluster.

  4. Create additional Secret groups and additional versions of your Secrets as needed.

  5. Update credentials for an existing user cluster as needed.

  6. Create additional user clusters as desired. In each user cluster configuration file, specify a Secrets namespace. You can also specify which version of a Secret you want to use for a particular credential.




## Fill in your secrets configuration file

Generate a template for a Secrets configuration file:
    
    
    gkectl create-config secrets
    

The preceding command generates a file named `secrets.yaml`. You can change the name and location of this file if you like.

Familiarize yourself with the configuration file by reading the [Secrets configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file) document. You might want to keep this document open in a separate tab or window.

In your Secrets configuration file, fill in the values that are relevant for your situation. You must fill in a value for `namespace` that begins with `gke-onprem-secrets-`.

Here's an example of a Secrets configuration file that has one Secret group. The group has values for vCenter credentials and four service account keys:
    
    
    apiVersion: v1
    kind: ClusterSecrets
    secretGroups:
    - namespace: "gke-onprem-secrets-user-cluster-1"
      secrets
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
    

## Create prepared Secrets

Create prepared Secrets in your admin cluster:
    
    
    gkectl prepare secrets --kubeconfig ADMIN_CLUSTER_KUBECONFIG --secret-config SECRETS_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * SECRETS_CONFIG: the path of your Secrets configuration file




### View your prepared Secrets

List the prepared Secrets in the admin cluster:
    
    
    gkectl list secrets --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Example output:
    
    
    The following secrets have been found:
    - namespace: gke-onprem-secrets-user-cluster-1
      - secrets with name prefix: component-access-sa-creds
        name: component-access-sa-creds.1, version 1, age: 58s
      - secrets with name prefix: cloud-audit-logging-service-account-creds
        name: cloud-audit-logging-service-account-creds.1, version: 1, age: 58s
      - secrets with name prefix: register-service-account-creds
        name: register-service-account-creds.1, version: 1, age: 58s
      - secrets with name prefix: stackdriver-service-account-creds
        name: stackdriver-service-account-creds.1, version: 1, age: 58s
      - secrets with name prefix: vsphere-creds
        name: vsphere-creds.1, version: 1, age: 58s
    

You can also run `kubectl get secrets` to list the Secrets in a namespace. For example:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secrets --namespace gke-onprem-secrets-user-cluster-1
    

Example output:
    
    
    component-access-sa-creds ...
    cloud-audit-logging-service-account-creds ...
    register-service-account-creds.1 ...
    stackdriver-service-account-creds.1 ...
    vsphere-creds.1 ...
    

In the preceding output, you can see that each Secret name has an extension that indicates the version of the Secret. In this example, all the Secrets have a version of 1.

## Create a user cluster

Follow the instructions in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

As you fill in your user cluster configuration file, enter a value for `preparedSecrets.namespace`. This value must match a namespace that you specified previously in a Secrets configuration file.

Example:
    
    
    preparedSecrets:
      namespace: "gke-onprem-secrets-user-cluster-1"
    

In your user cluster configuration file, do not specify values for the following fields. These fields are not needed, because Google Distributed Cloud gets the credentials and keys from your prepared Secrets.

  * `vCenter.credentials.fileRef.path`
  * `componentAccessServiceAccountKeyPath`
  * `loadBalancer.f5BigIP.credentials.fileRef.path`
  * `gkeConnect.registerServiceAccountKeyPath`
  * `stackdriver.serviceAccountKeyPath`
  * `usageMetering.bigQueryServiceAccountKeyPath`
  * `cloudAuditLogging.serviceAccountKeyPath`
  * `privateRegistry.credentials.fileRef.path`



In your user cluster configuration file, specify versions for the prepared Secrets that you intend to use. Here is an example that specifies version 1 for each of five Secrets:
    
    
    vCenter:
      credentials:
        secretRef:
          version "1"
    ...
    componentAccessServiceAccountKey:
      secretRef:
        version: "1"
    ...
    gkeConnect:
      registerServiceAccountKey:
        secretRef:
          version: "1"
    ...
    stackdriver:
      serviceAccountKey:
        secretRef:
          version: "1"
    ...
    cloudAuditLogging:
      serviceAccountKey:
        secretRef:
          version: "1"
    

The value for `version` must be an integer string or the string "latest". If you do not specify a value for `version`, the latest version is used.

Finish creating your user cluster as described in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

## Create additional prepared Secrets

This section shows how to create version 2 of some of the Secrets in an existing namespace.

Create a new Secrets configuration file named `secrets-2.yaml`. Specify an existing namespace, and provide credentials for selected Secrets.

Example:
    
    
    apiVersion: v1
    kind: ClusterSecrets
    secretGroups:
    - namespace: "gke-onprem-secrets-user-cluster-1"
      secrets:
        stackdriverServiceAccount:
          serviceAccountKeyPath: "log-mon-sa-2.json"
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: "audit-log-sa-2.json"
    

The preceding example provides key paths for the following Secrets in the `gke-onprem-secrets-user-cluster-1` namespace.

  * Version 2 of the `stackdriver-service-account-creds` Secret
  * Version 2 of the `cloud-audit-logging-service-account-creds` Secret



Create the new Secrets:
    
    
    gkectl prepare secrets --kubeconfig ADMIN_CLUSTER_KUBECONFIG --secret-config secrets-2.yaml
    

List the prepared Secrets in the admin cluster:
    
    
    gkectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG list secrets
    

Example output:
    
    
    The following secrets have been found:
    - namespace: gke-onprem-secrets-user-cluster-1
      - secrets with name prefix: component-access-sa-creds
        name: component-access-sa-creds.1, version 1, age: 11h
      - secrets with name prefix: cloud-audit-logging-service-account-creds
        name: cloud-audit-logging-service-account-creds.1, version: 1, age: 11h
        name: cloud-audit-logging-service-account-creds.2, version: 2, age: 33m
      - secrets with name prefix: register-service-account-creds
        name: register-service-account-creds.1, version: 1, age: 11h
      - secrets with name prefix: stackdriver-service-account-creds
        name: stackdriver-service-account-creds.1, version: 1, age: 11h
        name: stackdriver-service-account-creds.2, version: 2, age: 33m
      - secrets with name prefix: vsphere-creds
        name: vsphere-creds.1, version: 1, age: 11h
    

In the preceding output, you can see that there are two versions of the `stackdriver-service-account-creds` Secret and two versions of the `cloud-audit-logging-service-account-creds` Secret.

## Rotate credentials for a user cluster

This section shows how to rotate selected credentials for an existing user cluster.

Before rotating credentials, check the current Secret versions used in the cluster:
    
    
    gkectl list secrets cluster --cluster-name USER_CLUSTER_NAME  kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Example output:
    
    
    The following prepared secrets have been used for cluster "user-cluster-1":
    - namespace: gke-onprem-secrets-user-cluster-1
      secret: vsphere-creds.1, version: 1
      secret: f5-creds.1, version: 1
      secret: component-access-sa-creds.1, version 1
      secret: register-service-account-creds.1, version: 1
      secret: stackdriver-service-account-creds.1, version: 1
      secret: cloud-audit-logging-service-account-creds.1, version: 1
    

Copy your user cluster configuration file to a file named `user-cluster-update.yaml`.

In `user-cluster-update.yaml`, add `serviceAccountKey` sections. For example, the following example has `serviceAccountKey` sections under `stackdriver` and `cloudAuditLogging`:
    
    
    stackdriver:
      projectID: "my-project-123"
      clusterLocation: "us-central1"
      serviceAccountKey:
        secretRef:
          version: "2"
    cloudAuditLogging:
      projectID: "my-project-123"
      clusterLocation: "us-central-1"
      serviceAccountKey:
        secretRef:
          version: "latest"
    

The preceding example specifies that when the user cluster is updated, it will use:

  * Version 2 of the `stackdriver-service-account-creds` Secret

  * The latest version of the `cloud-audit-logging-service-account-creds` Secret. In this example, that is version 2.


**Note:** When you update a Secret, the value that you provide for `secretRef.version` must be "latest" or an integer string. You cannot omit `secretRef.version`, and you cannot set it to the empty string.

Update the credentials for the user cluster:
    
    
    gkectl update credentials stackdriver --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config user-cluster-2.yaml
    
    gkectl update credentials cloudauditlogging --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config user-cluster-2.yaml
    

Now the user cluster uses the following prepared Secrets:

  * Version 1 of `vsphere-creds`
  * Version 1 of `component-access-sa-creds`
  * Version 1 of `register-service-account-creds`
  * Version 2 of `stackdriver-service-account-creds`
  * Version 2 of `cloud-audit-logging-service-account-creds`



## Create additional Secrets and user clusters

If you plan to create additional user clusters, think about how you want to organize your prepared Secrets. You might want to create a separate namespace in your admin cluster for each user cluster. Or you might want to share the same prepared Secret namespace for several or all user clusters.

For example, suppose Alice, Bob, and Carol will each have a user cluster. You could create three Secret groups as shown in this example:
    
    
    apiVersion: v1
    kind: ClusterSecrets
    secretGroups:
    - namespace: "gke-onprem-secrets-alice"
      secrets:
        vCenter:
          username: "alice"
          password: "zC7r^URDPq2t"
        componentAccessServiceAccount:
          serviceAccountKeyPath: "component-access-sa-a.json"
        registerServiceAccount:
          serviceAccountKeyPath: "register-sa-a.json"
        stackdriverServiceAccount:
          serviceAccountKeyPath: "log-mon-sa-a.json"
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: "audit-log-sa-a.json"
    - namespace: "gke-onprem-secrets-bob"
      secrets:
        vCenter:
          username: "bob"
          password: "zC8r^URDPq2t"
        componentAccessServiceAccount:
          serviceAccountKeyPath: "component-access-sa-b.json"
        registerServiceAccount:
          serviceAccountKeyPath: "register-sa-b.json"
        stackdriverServiceAccount:
          serviceAccountKeyPath: "log-mon-sa-b.json"
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: "audit-log-sa-b.json"
    - namespace: "gke-onprem-secrets-carol"
      secrets:
        vCenter:
          username: "carol"
          password: "zC9r^URDPq2t"
        componentAccessServiceAccount:
          serviceAccountKeyPath: "component-access-sa-c.json"
        registerServiceAccount:
          serviceAccountKeyPath: "register-sa-c.json"
        stackdriverServiceAccount:
          serviceAccountKeyPath: "log-mon-sa-c.json"
        cloudAuditLoggingServiceAccount:
          serviceAccountKeyPath: "audit-log-sa-c.json"
    

Over time you could create additional versions of the Secrets in each Secret group.

In your user cluster configuration files, provide values for `serviceAccountKey.secretRef.version` to specify which versions of your Secrets you want to use. You can set the value to `"latest"`, the empty string, or an integer string.

For example, suppose all your Secrets have versions 1, 2, and 3. And suppose this is a portion of the user cluster configuration file for Alice.
    
    
    apiVersion: v1
    kind: UserCluster
    name: "user-cluster-alice"
    preparedSecrets:
      namespace: "gke-onprem-secrets-alice"
    ...
    vCenter:
      credentials:
    gkeConnect:
      projectID: "project-a"
      serviceAccountKey:
        secretRef:
          version: "2"
    stackdriver:
      projectID: "project-a"
      clusterLocation: "us-central1"
      serviceAccountKey:
        secretRef:
          version: "latest"
    cloudAuditLogging:
      projectID: "project-a"
      clusterLocation: "us-central-1"
      serviceAccountKey:
        secretRef:
          version: ""
    
    

In the preceding example, we can see:

  * There is no `secretRef` specified for vCenter, so the cluster will use the latest version of the `vsphere-creds` Secret in the `gke-onprem-secrets-alice` namespace.

  * The cluster will use version 2 of the `register-service-account-creds` Secret in the `gke-onprem-secrets-alice` namespace.

  * The cluster will use the latest version of the `stackdriver-service-account-creds` Secret in the `gke-onprem-secrets-alice` namespace. In this example, that is version 3.

  * The version for `cloudAuditLogging` is the empty string, so the cluster will use the latest version of the `cloud-audit-logging-service-account-creds` Secret in the `gke-onprem-secrets-alice` namespace. In this example, that is version 3.

  * There is no `secretRef.version` specified for the component access service account, so the cluster will use the latest version.




## Delete prepared Secrets

To list all the prepared Secrets and their namespaces:
    
    
    gkectl list secrets --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

If a prepared Secret namespace is not being used by any user cluster, you can delete the namespace.

To delete a prepared Secret namespace and all the Secrets in it:
    
    
    gkectl delete secret –namespace PREPARED_SECRET_NAMESPACE \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

If an individual prepared Secret is not being used by any user cluster, you can delete the Secret.

To delete an individual prepared Secret:
    
    
    gkectl delete secret –namespace PREPARED_SECRET_NAMESPACE \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --secret-name SECRET
    

## Related documents

  * [Secrets configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file)
  * [User cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest)
  * [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster)
  * [Create service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
