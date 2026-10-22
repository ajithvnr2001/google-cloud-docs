---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access/
title: Grant and obtain storage bucket access \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:58.360479+00:00
---

# Grant and obtain storage bucket access  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/grant-obtain-storage-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Grant and obtain storage bucket access Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to manage access to storage buckets within Google Distributed Cloud (GDC) air-gapped appliance projects, so the right people have the right permissions. It covers the prerequisites and steps for obtaining and granting user and service account access using role bindings and predefined roles. This information lets you effectively control access to your storage resources and maintain both security and operational efficiency.

This page is for audiences such as IT administrators within the infrastructure operator group or developers within the application operator group who manage access settings for storage buckets in GDC air-gapped environments.

## Before you begin

A project namespace manages bucket resources in the Management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project) to work with buckets and objects.

## Grant bucket access

You can provide bucket access to other users or service accounts by creating and applying RoleBindings with predefined Roles.

### Predefined roles

  * **project-bucket-object-viewer:** This role lets a user list all buckets in the project, list objects in those buckets, and read objects and object metadata. This role does not let you write operations on objects, such as uploading, overwriting, or deleting.

  * **project-bucket-object-admin:** This role lets a user list all buckets in the project, and write and read operations on objects, such as uploading, overwriting, or deleting.

  * **project-bucket-admin:** This role lets users manage all buckets in the given namespace, as well as all the objects in those buckets.




To see a complete list of the permissions granted for these roles, see the preset role permissions section.

To get the permissions that you need to create project role bindings, ask your Project IAM Admin to grant you the Project IAM Admin (`project-iam-admin`) role.

The following is an example of creating a `RoleBinding` for granting access to a user and a service account:

  1. Create a YAML file on your system, such as `rolebinding-object-admin-all-buckets.yaml`.
         
         apiVersion: rbac.authorization.k8s.io/v1
          kind: RoleBinding
          metadata:
            namespace: NAMESPACE_NAME
            name: readwrite-all-buckets
          roleRef:
            kind: Role
            name: project-bucket-object-admin
            apiGroup: rbac.authorization.k8s.io
          subjects:
          - kind: ServiceAccount
            namespace: NAMESPACE_NAME
            name: SA_NAME
          - kind: User
            namespace: NAMESPACE_NAME
            name: bob@example.com  # Could be bob or bob@example.com based on your organization settings.
            apiGroup: rbac.authorization.k8s.io
          ```
         

  2. Apply the YAML file:
         
         kubectl apply \
         -f rolebinding-object-admin-all-buckets.yaml
         




## Get bucket access credentials

When you grant access to a bucket, the access credentials are created in a Secret.

The format of the secret name is `object-storage-key-std-SUBJECT_TYPE-SUBJECT_HASH`.

  * Values for `SUBJECT_TYPE` are the following: 
    * `user`: the user.
    * `sa`: the `ServiceAccount`.
  * `SUBJECT_HASH` is the base32-encoded SHA256 hash of the subject name.



As an example, the user `bob@foo.com` has the secret named:
    
    
    object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja
    

### Access the user secret

For a user subject, the Secret is in the `object-storage-access-keys` namespace in the Management API server.

  1. Find the secret name:
         
         kubectl auth can-i --list --namespace object-storage-access-keys | grep object-storage-key-std
         

You receive an output similar to the following:
         
         secrets        []        [object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja,object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja]        [get]
         

  2. Get the contents of the corresponding Secret to access buckets:
         
         kubectl get -o yaml --namespace object-storage-access-keys secret
         object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja
         

You receive an output similar to the following:
         
         data:
           access-key-id: MEhYM08wWUMySjcyMkVKTFBKRU8=
           create-time: MjAyMi0wNy0yMiAwMTowODo1OS40MTQyMTE3MDMgKzAwMDAgVVRDIG09KzE5OTAuMzQ3OTE2MTc3
           secret-access-key: Ump0MVRleVN4SmhCSVJhbmlnVDAwbTJZc0IvRlJVendqR0JuYVhiVA==
         

  3. Decode the access key ID and secret:
         
         echo "MEhYM08wWUMySjcyMkVKTFBKRU8=" | base64 -d \
             && echo \
             && echo "Ump0MVRleVN4SmhCSVJhbmlnVDAwbTJZc0IvRlJVendqR0JuYVhiVA==" | base64 -d
         

You receive an output similar to the following:
         
         0HX3O0YC2J722EJLPJEO
         Rjt1TeySxJhBIRanigT00m2YsB/FRUzwjGBnaXbT
         

  4. Follow the section, [Configure s3cmd](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/install-configure-storage-cli#s3cmd_configure), with the resulting information.




### Access the service account secret

For a service account (SA) subject, the Secret is created in the same namespace as the service account. To find the name, run:
    
    
      kubectl get --namespace NAMESPACE_NAME secrets -o=jsonpath=
      '{.items[?(@.metadata.annotations.object\.gdc\.goog/subject=="SA_NAME")].metadata.name}'
    

You receive an output similar to the following:
    
    
      object-storage-key-std-sa-mng3olp3vsynhswzasowzu3jgzct2ert72pjp6wsbzqhdwckwzbq
    

You can reference the Secret in your pod as environment variables (<https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables>) or files (<https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod>).

## Preset role permissions

When working with object storage, you might need to request the following roles.

### project-bucket-object-viewer permissions

This role grants permissions to get and list objects and objects' metadata in the bucket.

The `project-bucket-object-viewer` role has the following permissions:

  * **Bucket API permissions** :

    1. Get
    2. List
    3. Watch
  * **S3 object storage permissions** :

    1. `GetObject`
    2. `GetObjectAcl`
    3. `GetObjectVersion`
    4. `ListBucket`
    5. `ListBucketVersions`
    6. `ListBucketMultipartUploads`
    7. `ListMultipartUploadParts`



### project-bucket-object-admin permissions

This role grants permissions to put and delete objects, object versions, and tags in the bucket. Additionally, it also grants all permissions in the `project-bucket-object-viewer`.

The `project-bucket-object-admin` role has the following object storage permissions:

  * **S3 Object storage permissions** :

    1. `AbortMultipartUpload`
    2. `DeleteObject`
    3. `PutObject`



### project-bucket-admin permissions

This role grants permissions to create, update, or delete `Bucket` resources in the project namespace. Additionally, it also grants all permissions in `project-bucket-object-admin`.

The `project-bucket-object-admin` role has the following permissions:

  * **Bucket API permissions** :

    1. Create
    2. Update
    3. Delete



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
