---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-back-repo/
title: Create a backup repository for Database Service \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:18.422905+00:00
---

# Create a backup repository for Database Service  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-back-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a backup repository for Database Service Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to configure the required `BackupRepository` for Google Distributed Cloud (GDC) air-gapped Database Service (DBS). This repository, mandatorily named `dbs-backup-repository`, is a custom resource within Kubernetes that directs the GDC backup service to an S3-compatible object storage bucket for storing database backups.

**Important:** Backup repository setup for GDC DBS must be done _once_ by the Platform Administrator for each organization. After it's created and ready, don't attempt to update it, otherwise, it will cause unexpected DBS backup and restore behavior.

Proper setup is crucial for enabling backup and restore functionalities for DBS instances such as PostgreSQL, Oracle, and AlloyDB Omni.

**Note:** All resources described in this document are created in the management API server.

## Before you begin

Before starting, ensure you have the following prerequisites:

  * **Project:** A [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project) to host the bucket, typically named `backups`, with only service account access.
  * **Access:** Sufficient permissions to interact with the management API server. 
    * The user must have the following Organization level roles to create the backup repository: 
      * Bucket Admin (`bucket-admin`)
      * Project Creator (`project-creator`)
      * Organization Backup Admin (`organization-backup-admin`)
    * Within the target project: 
      * Project IAM Admin (`project-iam-admin`)
      * Bucket Object Project Viewer (`project-bucket-object-viewer`)
      * Bucket Object Project Admin (`project-bucket-object-admin`)
      * Bucket Project Admin (`project-bucket-admin`)
      * Secret Viewer (`secret-viewer`)
      * Namespace Admin (`namespace-admin`)
      * Backup Creator (`backup-creator`)
  * **Tools:**
    * The GDC console.
    * [kubectl CLI configured](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) to access the management API server.



## Create an object storage bucket

All proceeding steps are performed in the management API server. Define and create a `Bucket` resource. The recommended name `dbs-backups` for this storage bucket is assumed for the remainder of this document, located within the `backups` project namespace. Ensure the bucket does _not_ have any retention policy.

###  Console 

  1. Sign in to the GDC console for the organization.
  2. Ensure you are in the `backups` project.
  3. Navigate to **Object Storage** > **Buckets**.
  4. Click **Create Bucket**.
  5. Set the bucket name as `dbs-backups`.
  6. Set the description as `Bucket for DBS backups`.
  7. Configure the storage class as required. For example, `Standard`.
  8. For **Security** , ensure you do _not_ set a retention policy, as this will cause databases and their backups to be retained errantly.
  9. Click **Create**.



###  API 

  * Apply the following manifest to the management API server:


    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f -
    <<EOF
    apiVersion: object.gdc.goog/v1
    kind: Bucket
    metadata:
      name: dbs-backups
      namespace: backups
    spec:
      description: "Bucket for DBS backups"
      storageClass: "Standard"
    EOF
    

## Create service account and set permissions

Create a `ProjectServiceAccount` and grant it permissions to access the bucket.

###  Console 

  1. In the `backups` project, navigate to **Identity & Access > Service identities**.
  2. Click **Create Service Identity**. The **Service Identity details** page opens.
  3. In the **Service identity name** field, enter `dbs-backup-sa`.
  4. Click **Create**.
  5. Go to **Identity & Access > Access**.
  6. In the **Member** list, click **Add member**. You see the **Users and roles** page.
  7. Select **Service identity** in the **Member type** list.
  8. In the **Service identity** list, select `dbs-backup-sa` to assign a role binding.
  9. In the **Role** list, select **Bucket Object Project Admin** to assign to the service identity.
  10. Click **Add**.



###  API 

  * Apply these manifests to the management API server:


    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f -
    <<EOF
    apiVersion: resourcemanager.gdc.goog/v1
    kind: ProjectServiceAccount
    metadata:
      name: dbs-backup-sa
      namespace: backups
    spec: {}
    EOF
    
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f -
    <<EOF
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: dbs-backups-readwrite-rolebinding
      namespace: backups
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: project-bucket-object-admin
    subjects:
    - kind: ServiceAccount
      name: dbs-backup-sa
      namespace: backups
    EOF
    

## Identify the service account's credential secret and bucket details

Upon granting bucket access to the `dbs-backup-sa`, GDC automatically creates a secret in the _same namespace_ , `backups`, containing the S3 access credentials. You need to find this secret's name and the bucket details using the kubectl CLI (API).

  1. Set environment variables:
         
         export SA_NAMESPACE="backups"
         export SA_NAME="dbs-backup-sa"
         export KUBECONFIG=MANAGEMENT_API_SERVER
         

  2. Find the secret name:
         
         export BUCKET_CRED_SECRET_NAME=$(kubectl --kubeconfig=${KUBECONFIG} get secret \
             -n "${SA_NAMESPACE}" -l object.gdc.goog/subject-type=ServiceAccount -o json | \
             jq -r --arg SA_NAME "${SA_NAME}" \
             '.items[] | select(.metadata.annotations["object.gdc.goog/subject"] == $SA_NAME and (.metadata.name |startswith("object-storage-key-std-sa-"))) | .metadata.name')
         echo "Bucket Credential Secret Name: ${BUCKET_CRED_SECRET_NAME}"
         

This command filters secrets in the `backups` namespace to find the one annotated for the `dbs-backup-sa` service account and matching the standard naming convention. To run this command, you must have the Secret Viewer (`secret-viewer`) role in the `backups` project, or ask the Platform Administrator who created the service account to provide the secret name.

  3. Get bucket endpoint and region details:
         
         export BUCKET_NAME=dbs-backups
         export FULL_BUCKET_NAME=$(kubectl --kubeconfig=${KUBECONFIG} get bucket -n ${SA_NAMESPACE} ${BUCKET_NAME} -o jsonpath='{.status.fullyQualifiedName}')
         export ENDPOINT=$(kubectl --kubeconfig=${KUBECONFIG} get bucket -n ${SA_NAMESPACE} ${BUCKET_NAME} -o jsonpath='{.status.endpoint}')
         export REGION=$(kubectl --kubeconfig=${KUBECONFIG} get bucket -n ${SA_NAMESPACE} ${BUCKET_NAME} -o jsonpath='{.status.region}')
         
         echo "FULL_BUCKET_NAME: ${FULL_BUCKET_NAME}"
         echo "ENDPOINT: ${ENDPOINT}"
         echo "REGION: ${REGION}"
         




## Create the `BackupRepository`

Create the `BackupRepository` resource, referencing the secret identified in the previous section, [Identify the service account's credential secret and bucket details](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-back-repo#find-secret). This step must be completed using the kubectl CLI (API).

  * Create the YAML file such as `backup-repo.yaml`, substituting the variables found in the previous section:
        
        kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f -
        <<EOF
        apiVersion: backup.gdc.goog/v1
        kind: BackupRepository
        metadata:
          name: dbs-backup-repository # This specific name is required for DBS
        spec:
          secretReference:
            namespace: "backups" # Namespace of the Service Account and the auto-generated secret
            name: BUCKET_CRED_SECRET_NAME
          endpoint: ENDPOINT
          type: "S3"
          s3Options:
            bucket: FULL_BUCKET_NAME
            region: REGION
            forcePathStyle: true
          importPolicy: "ReadWrite"
          force: true
          EOF
        

Replace the following:

    * `BUCKET_CRED_SECRET_NAME`: the secret name.
    * `ENDPOINT`: the endpoint of the bucket.
    * `FULL_BUCKET_NAME`: the fully qualified bucket name.
    * `REGION`: the region of the bucket.



## Verify the backup repository

Check the repository status to ensure it was set up correctly.

  1. Print the information for your backup repository:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER get backuprepository dbs-backup-repository -ojson | jq .status
         

  2. Verify that your output looks similar to the following. A `NoError` message is the signal that the repository was set up as expected:
         
         NAME                    TYPE   POLICY      ERROR
         dbs-backup-repository   S3     ReadWrite   NoError
         status:
           conditions:
           - lastTransitionTime: "2025-11-13T00:36:09Z"
             message: Backup Repository reconciled successfully
             reason: Ready
             status: "True"
             type: Ready
           initialImportDone: true
           reconciliationError: NoError
           sentinelEtag: 9b82fbb7-6ea2-444d-8878-ab91397ae961
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
