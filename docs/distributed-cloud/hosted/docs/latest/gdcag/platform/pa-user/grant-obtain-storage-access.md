---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access/
title: Grant and obtain storage bucket access \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:52.107258+00:00
---

# Grant and obtain storage bucket access  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Grant and obtain storage bucket access Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to manage access to storage buckets within Google Distributed Cloud (GDC) air-gapped projects, so the right people have the right permissions. It covers the prerequisites and steps for obtaining and granting user and service account access using role bindings and predefined roles. This information lets you effectively control access to your storage resources and maintain both security and operational efficiency.

This page is for audiences such as IT administrators within the infrastructure operator group or developers within the application operator group who manage access settings for storage buckets in GDC air-gapped environments. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

A project namespace manages bucket resources in the Management API server. You must have a [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/project-management) to work with buckets and objects.

## Grant bucket access

You can grant access to S3 API resources, such as buckets and objects in those buckets, to `User` and `ServiceAccount` subjects by creating and applying RoleBindings that reference predefined Roles in the Management API server.

**Note:** `Group` subjects are not supported for granting S3 API permissions. If you specify a `Group` subject in a RoleBinding, _S3 API_ permissions won't be granted to the group's members, but _Kubernetes API_ permissions can still be applied to `Group` subjects in this manner.**Note:** Group access is not supported by the object access control system. It only recognizes and acts on subjects of the `User` or `ServiceAccount` types.

### Predefined roles

  * **project-bucket-object-viewer:** This lets a user list all buckets in the project, list objects in those buckets, and read objects and object metadata. It does not let you write operations on objects. For example: uploading, overwriting, deleting. Has read-only on dual-zone buckets within the organization and its projects, as well as read-only on the objects in those buckets.

  * **project-bucket-object-admin:** This lets a user list all buckets in the project, and write and read operations on objects. For example: uploading, overwriting, deleting. Has read-only on dual-zone buckets within the organization and its projects, as well as read-write on the objects in those buckets.

  * **project-bucket-admin:** This lets users manage all buckets in the given namespace, as well as all the objects in those buckets. Has read-only on dual-zone buckets within the organization and its projects, as well as read-write on the objects in those buckets.




To see a complete list of the permissions granted for the preceding roles, see the predefined role permissions section.

You must have the Project IAM Admin role for the project in order to create role bindings in that project. The following is an example of creating a `RoleBinding` resource that grants access to a user and a service account:

  1. Create a YAML file on your system, such as `rolebinding-object-admin-all-buckets.yaml`.
         
         # Example file name:
         # rolebinding-object-admin-all-buckets.yaml
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           namespace: PROJECT_NAMESPACE
           name: readwrite-all-buckets
         roleRef:
           kind: Role
           name: project-bucket-object-admin
           apiGroup: rbac.authorization.k8s.io
         subjects:
         - kind: ServiceAccount
           namespace: PROJECT_NAMESPACE
           name: SA_NAME
         - kind: User
           namespace: PROJECT_NAMESPACE
           name: bob@example.com
           apiGroup: rbac.authorization.k8s.io
           # Could be bob or bob@example.com based on your organization settings.
         

Replace the following: 

     * `PROJECT_NAMESPACE`: the name of the project namespace
     * `SA_NAME`: the name of the service account
  2. Apply the YAML file:
         
         kubectl apply \
         -f rolebinding-object-admin-all-buckets.yaml
         




## Obtain bucket access credentials

Once you grant access to a bucket, it creates the access credentials in a Secret. Credentials are required to configure Distributed Cloud CLI and run commands to interact with the bucket.

The format of the secret name is `object-storage-key-STORAGE_CLASS-SUBJECT_TYPE-SUBJECT_HASH`.

  * Values for `STORAGE_CLASS` are: 
    * `std` for the `Standard` storage class.
  * Values for `SUBJECT_TYPE` are: 
    * `user` for User.
    * `sa` for ServiceAccount.
  * `SUBJECT_HASH` is the base32-encoded SHA256 hash of the subject name.



As an example, the user `bob@foo.com` has has a secret named:

`object-storage-key-std-user-l74gbpyrsbmwy4mivocr3nur6dzrnhcfhe3otyplul42i732aama`

### Obtain user access credentials

For a user subject, the Secret is in the `object-storage-access-keys` namespace in the Management API server.

  1. Run the following command to list the Secret resources you have permission to view in the namespace `object-storage-access-keys`:
         
         kubectl auth can-i --list --namespace object-storage-access-keys | grep "object-storage-key-"
         

If you can view any Secrets in this namespace, you see output that contains one or more Secret names starting with `object-storage-key-`, similar to the following:
         
         secrets        []        [object-storage-key-std-user-l74gbpyrsbmwy4mivocr3nur6dzrnhcfhe3otyplul42i732aama]        [get]
         

     * NOTE: If you are an administrator with permission to view all Secret resources or impersonate other users, you can run one of the following commands to find the name of Secrets for a specified user:

List all Secrets belonging to a specified user:
           
           export USER_NAME=bob@example.com
           kubectl get secrets --namespace object-storage-access-keys -o json | jq  -r --arg USER_NAME "${USER_NAME:?}" '.items[] | select( (.metadata.annotations."object.gdc.goog/subject"==$USER_NAME)) | .metadata.name'
           

Impersonate a user to see which Secrets they can view:
           
           export USER_NAME=bob@example.com
           kubectl auth can-i --list --namespace object-storage-access-keys --as "${USER_NAME:?} | grep "object-storage-key-"
           

  2. Get the contents of the corresponding Secret:
         
         kubectl get -o yaml --namespace object-storage-access-keys secret SECRET_NAME
         

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
         

  4. Follow the section, [Configure the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/install-configure-storage-cli#gdcloud-storage-configure), with the resulting information.




### Obtain service account access

The S3 secret credentials are only created and available to be obtained if a bucket exists in the project namespace.

**Note:** Users are not allowed to run workloads, which run as service accounts, in the Management API server where the service accounts' access key Secrets were initially created. Users aren't able to grant workloads access to those Secrets in the Management API server. Those Secrets will be propagated to the Project namespaces in the appropriate user clusters, where users will be able to access them (if they have the appropriate RBAC Roles within that Project).

For a service account (SA) subject, the Secret is created in the same namespace as the service account.

Run the following command to verify that you can get and list Secret resources in the namespace, contact your administrator if this is not the case:
    
    
    export SA_NAMESPACE=PROJECT_NAMESPACE
    kubectl auth can-i --list --namespace $SA_NAMESPACE
    

To find the Secret name, run:
    
    
    export SA_NAME=SA_NAME
    kubectl get secrets --namespace $SA_NAMESPACE  -o json | jq  -r --arg USER_NAME "${SA_NAME:?}" '.items[] | select( (.metadata.annotations."object.gdc.goog/subject"==$USER_NAME)) | .metadata.name'
    

You receive an output similar to the following:
    
    
    object-storage-key-std-sa-mng3olp3vsynhswzasowzu3jgzct2ert72pjp6wsbzqhdwckwzbq
    

You can reference the Secret in your pod as [environment variables](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables) or [files](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod).

### Predefined role permissions

Note that predefined roles are also available in the global API server for administrative and operational access to dual-zone buckets.

#### project-bucket-object-viewer permissions

This role grants permissions to get and list objects and objects' metadata in the bucket.

A list of all object storage permissions the project-bucket-object-viewer verb grants are the following:

  * **Bucket API permissions** :

    1. get
    2. list
    3. watch
  * **S3 object storage permissions** :

    1. GetBucketVersioning
    2. GetObject
    3. GetObjectAcl
    4. GetObjectLegalHold
    5. GetObjectRetention
    6. GetObjectTagging
    7. GetObjectVersion
    8. GetObjectVersionTagging
    9. ListBucket
    10. ListBucketVersions
    11. ListBucketMultipartUploads
    12. ListMultipartUploadParts



#### project-bucket-object-admin permissions

This role grants permissions to put and delete objects, and object versions and tags in the bucket. Additionally, it also grants all permissions in the `project-bucket-object-viewer`.

A list of all additional object storage permissions the Role grants are the following:

  * **S3 object storage permissions** :

    1. AbortMultipartUpload
    2. DeleteObject
    3. DeleteObjectTagging
    4. DeleteObjectVersion
    5. DeleteObjectVersionTagging
    6. PutObject
    7. PutObjectTagging
    8. PutObjectVersionTagging
    9. PutOverwriteObject
    10. RestoreObject



#### project-bucket-admin permissions

This role grants permissions to create, update, or delete Bucket resources in the project namespace. Additionally, it also grants all permissions in `project-bucket-object-admin`.

A list of additional permissions the Role grants are the following:

  * **Bucket API permissions** :

    1. Create
    2. Update
    3. Delete



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
