---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/grant-obtain-storage-access/
title: Grant and obtain storage bucket access for projects \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:12:09.498320+00:00
---

# Grant and obtain storage bucket access for projects  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/grant-obtain-storage-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Grant and obtain storage bucket access for projects Stay organized with collections  Save and categorize content based on your preferences. 

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

Once you grant access to a bucket, it creates the access credentials in a Secret.

The format of the secret name is `object-storage-key-STORAGE_CLASS-SUBJECT_TYPE-SUBJECT_HASH`.

  * Values for `STORAGE_CLASS` are: 
    * `std` for the `Standard` storage class.
  * Values for `SUBJECT_TYPE` are: 
    * `user` for User.
    * `sa` for ServiceAccount.
  * `SUBJECT_HASH` is the base32-encoded SHA256 hash of the subject name.



As an example, the user `bob@foo.com` has two secrets named:

  1. `object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja`



### Obtain user access

For a user subject, the Secret is in the `object-storage-access-keys` namespace in the Management API server.

  1. Run the following command to find the secret name:
         
         kubectl auth can-i --list --namespace object-storage-access-keys | grep "object-storage-key-"
         

You receive an output similar to the following:
         
         secrets        []        [object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja]        [get]
         

  2. Get the contents of the corresponding secret to access buckets in the `Standard` storage class:
         
         kubectl get -o yaml --namespace object-storage-access-keys secret object-storage-key-std-user-oy6jdqd6bxfoqcecn2ozv6utepr5bgh355vfku7th5pmejqubdja
         

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
         

  4. Follow the section, [Configure the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/install-configure-storage-cli#gdcloud-storage-configure), with the resulting information.




### Obtain service account access

The S3 secret credentials are only created and available to be obtained if a bucket exists in the project namespace.

**Note:** Users are not allowed to run workloads, which run as service accounts, in the Management API server where the service accounts' access key Secrets were initially created. Users won't be able to grant workloads access to those Secrets in the Management API server. Those Secrets will be propagated to the Project namespaces in the appropriate user clusters, where users will be able to access them (if they have the appropriate RBAC roles within that Project).

For a service account (SA) subject, find the secret name from the user cluster.

  1. For standard storage class, run the following command to get the secret name:
         
         kubectl get -n=<PROJECT-NAME> serviceaccount <SA-NAME> -o json | jq -r '.secrets[] | select(.name | test("object-storage-key-std"))'
         

  2. Then, you can manually look through the listed secret names or use `grep` to find `object-storage-key-(std|nl)`. For the latter option, run the following:
         
         kubectl get -n=<PROJECT-NAME> serviceaccount <SA-NAME> -o=jsonpath='{.secrets}{"\n"}' | grep object-storage-key-(std|nl)
         

  3. You can reference the Secret in your pod as [environment variables](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables) or [files](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod).




### Preset role permissions

Predefined roles are available in the global API server for administrative and operational access to dual-zone buckets. These roles also grant access to zonal buckets, but only if an `IAMRoleBinding` resource is used rather than a `RoleBinding` or `ClusterRoleBinding` resource. For more information about role bindings, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/set-up-role-bindings).

#### project-bucket-object-viewer permissions

This role grants permissions to get and list objects and objects' metadata in the bucket.

A list of all object storage permissions the project-bucket-object-viewer `Role` grants are the following:

  * **Bucket API permissions** :

    1. get
    2. list
    3. watch
  * **S3 object storage permissions** :

    1. GetObject
    2. GetObjectAcl
    3. GetObjectLegalHold
    4. GetObjectRetention
    5. GetObjectTagging
    6. GetObjectVersion
    7. GetObjectVersionTagging
    8. ListBucket
    9. ListBucketVersions
    10. ListBucketMultipartUploads
    11. ListMultipartUploadParts



#### project-bucket-object-admin permissions

This role grants permissions to put and delete objects, and object versions and tags in the bucket. Additionally, it also grants all permissions in the `project-bucket-object-viewer`.

A list of all additional object storage permissions the `Role` grants are the following:

  * **S3 Object storage permissions** :

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

This role grants permissions to create, update, or delete `Bucket` resources in the project namespace. Additionally, it also grants all permissions in `project-bucket-object-admin`.

A list of additional permissions the `Role` grants are the following:

  * **Bucket API permissions** :

    1. Create
    2. Update
    3. Delete



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
