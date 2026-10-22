---
url: https://docs.cloud.google.com/config-connector/docs/how-to/secrets/
title: Using Secrets to store sensitive data \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:37.121829+00:00
---

# Using Secrets to store sensitive data  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using Secrets to store sensitive data

You can use a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to store sensitive configuration information, such as passwords and access keys, in your GKE cluster. This page describes how Config Connector uses Secret values when configuring your Google Cloud resources.

## Overview

This section presents an overview on using Secrets with Config Connector.

### Security and Secret encryption at rest

Because Kubernetes Secrets contain sensitive credentials and connection strings, enable [application-layer secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets) on your cluster. GKE encrypts Secrets at rest by default. Application-layer secrets encryption adds another layer of security by using Cloud Key Management Service envelope encryption.

Additionally, use role-based access control (RBAC) to restrict read access to Secrets only to authorized cluster administrators. Apply the same restriction to Config Connector resources that store sensitive values in their `status` fields, such as `IAMServiceAccountKey`.

### Using a Secret when creating a resource

You can use the data inside a Secret when you create a resource. In Passing a Secret to a resource, you create a Secret that contains a password, then reference the Secret for a user on a Cloud SQL database.

### Updating Secrets

When you apply an update to a Secret, Config Connector updates the resource when it next reconciles your desired state. For example, if you update the Secret that is referenced as the password for an `SQLUser`, Config Connector will then update the user's password.

### Deleting Secrets

If you delete a Secret that is in use by a resource, Config Connector will not remove the resource's reference to the Secret. For example, if you create an SQLUser with a password that references a Secret and then delete the Secret, the password will remain on the SQLUser.

### Troubleshooting

If you create a resource that references a Secret that does not exist, Config Connector will create a `DependencyNotFound` or `DependencyInvalid` [Event](https://docs.cloud.google.com/config-connector/docs/how-to/viewing-events).

### Secrets and Kubernetes namespaces

Because Kubernetes does not allow access to secrets across Namespaces, if you are using the same secret value for resources from different Namespaces, you must apply secrets in every Namespace.

## Passing a Secret to a resource

In this section, you will create a Cloud SQL server and set the default user's password with a Secret.

### Before you begin

To complete these steps, you need the following:

  * Config Connector installed on a Kubernetes cluster
  * The Cloud SQL Admin API enabled in your project. To confirm that the API is enabled, run the following `gcloud` command:
        
        gcloud services list --filter=sqladmin.googleapis.com
        

If the command prints `Listed 0 items.`, you need to enable the API. You can enable the API with Config Connector and the Resource Manager API, or a `gcloud` command.




### Service Usage API

  1. Config Connector uses the Service Usage API to enable service APIs. To perform these steps, you need to enable the [Service Usage](https://console.cloud.google.com/apis/library/serviceusage.googleapis.com) API. You can enable this API by using the Google Cloud CLI: 
         
         gcloud services enable serviceusage.googleapis.com

**Note:** Enabling the API might take several minutes. 
  2. Copy the following YAML into a file named `enable-sql.yaml`
         
         apiVersion: serviceusage.cnrm.cloud.google.com/v1beta1
         kind: Service
         metadata:
           name: sqladmin.googleapis.com
         

  3. Apply `enable-sql.yaml` to your cluster with `kubectl`:
         
         kubectl apply -f enable-sql.yaml --namespace CC_NAMESPACE
         

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.




### gcloud

To enable the SQL Admin API with the Google Cloud CLI, run the following command:
    
    
    gcloud services enable sqladmin.googleapis.com
    

### Creating a Cloud SQL Server

  1. Copy the YAML below into a file named `sql-server-example.yaml`. This creates a Cloud SQL server named `sqlserver-1` and a user named `sqluser-sample`. The password for `sqluser-sample` is set by a [resource reference](https://docs.cloud.google.com/config-connector/docs/how-to/creating-resource-references) to a secret named `secret-1`.
         
         apiVersion: sql.cnrm.cloud.google.com/v1beta1
         kind: SQLInstance
         metadata:
           labels:
             label-one: "sql-server-example"
           name: sqlserver-1
         spec:
           region: us-central1
           databaseVersion: MYSQL_5_7
           settings:
             tier: db-g1-small
         ---
         apiVersion: sql.cnrm.cloud.google.com/v1beta1
         kind: SQLUser
         metadata:
           name: sqluser-sample
         spec:
           instanceRef:
             name: sqlserver-1
           host: "%"
           password:
             valueFrom:
               secretKeyRef:
                 name: secret-1  # Name of the Secret object to extract a value from
                 key: password   # Key that identifies the value to be extracted
         

  2. Copy the YAML below into a file named `example-secret.yaml`. Edit the value for `password` before saving. This declares `secret-1`, referenced in the prior section.
         
         apiVersion: v1
         kind: Secret
         metadata:
           name:  secret-1
         stringData:
           password: PASSWORD
         

  3. Apply the configurations to your cluster.
         
         kubectl apply -n CC_NAMESPACE -f example-secret.yaml
         kubectl apply -n CC_NAMESPACE -f sql-server-example.yaml
         

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

Config Connector creates the Cloud SQL instance and a user with the password you specified. This might take several minutes.

  4. Wait several minutes, and confirm the instance is available:
         
         gcloud sql instances list --filter="name=sqlserver-1"

The output should include a server with a `STATUS` of `RUNNABLE`.

  5. Confirm that you can connect to the SQL instance:
         
         gcloud sql connect sqlserver-1 --user=sqluser-sample

You are prompted for your password.




### Cleaning up

If you do not wish to keep the instance, delete the Cloud SQL instance, user, and secret with `kubectl`.
    
    
        kubectl delete -n CC_NAMESPACE -f sql-server-example.yaml
        kubectl delete -n CC_NAMESPACE -f example-secret.yaml
    

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

## What's next

  * Learn how to specify [Resource references](https://docs.cloud.google.com/config-connector/docs/how-to/creating-resource-references) between Config Connector resources.

  * Take a deep dive into [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
