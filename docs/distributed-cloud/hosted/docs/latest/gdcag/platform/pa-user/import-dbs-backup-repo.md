---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/import-dbs-backup-repo/
title: Import backup repository for Database Services \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:50:56.546923+00:00
---

# Import backup repository for Database Services  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/import-dbs-backup-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Import backup repository for Database Services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to import backup repositories for Database Services (DBS) from a source instance to a target instance for disaster recovery. You must do this for each organization you want to restore database clusters in.

To import a backup repository, you create a `BackupRepository` resource on the target instance's management API server, pointing to the object storage bucket that contains DBS backups from the source instance.

For general instructions on setting up `BackupRepository`, see [Create a backup repository for Database Service](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-back-repo). This page contains specific instructions for importing a repository for disaster recovery.

## Before you begin

Before starting, ensure you have the following prerequisites:

  * **Project:** You must know the [project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project) that hosted the source bucket, typically named `database-backups`, with only service account access.
  * **Access:** Sufficient permissions to interact with the management API server. 
    * The user must have the following Organization level roles to create the backup repository: 
      * Bucket Admin (`bucket-admin`)
      * Project Creator (`project-creator`)
      * Organization Backup Admin (`organization-backup-admin`)
    * Within the target project: 
      * Project IAM Admin (`project-iam-admin`)
      * Project Bucket Object Viewer (`project-bucket-object-viewer`)
      * Project Bucket Object Admin (`project-bucket-object-admin`)
      * Project Bucket Admin (`project-bucket-admin`)
      * Namespace Admin (`namespace-admin`)
      * Backup Creator (`backup-creator`)
  * **Tools:**
    * The GDC console.
    * [kubectl CLI configured](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig) to access the management API server.
    * The `jq` command-line JSON processor.



## Find source backup details and credentials

You need to find backup bucket details and S3 credentials from the source instance. If you followed [Create a backup repository for Database Service](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-back-repo), the namespace is `backups`, bucket name is `dbs-backups`, and service account `dbs-backup-sa` is used for bucket access.

Run the following commands against the management API server of the source gdcloud CLI instance to get bucket details and credentials:
    
    
    export NAMESPACE=backups
    export BUCKET_NAME=dbs-backups
    export SA_NAME="dbs-backup-sa"
    export FULL_BUCKET_NAME=$(kubectl --kubeconfig SOURCE_KUBECONFIG get bucket -n ${NAMESPACE} ${BUCKET_NAME} -o jsonpath='{.status.fullyQualifiedName}')
    export ENDPOINT=$(kubectl --kubeconfig SOURCE_KUBECONFIG get bucket -n ${NAMESPACE} ${BUCKET_NAME} -o jsonpath='{.status.endpoint}')
    export REGION=$(kubectl --kubeconfig SOURCE_KUBECONFIG get bucket -n ${NAMESPACE} ${BUCKET_NAME} -o jsonpath='{.status.region}')
    export BUCKET_CRED_SECRET_NAME=$(kubectl --kubeconfig SOURCE_KUBECONFIG get secret \
        -n "${NAMESPACE}" -l object.gdc.goog/subject-type=ServiceAccount -o json | \
        jq -r --arg SA_NAME "${SA_NAME}" \
        '.items[] | select(.metadata.annotations["object.gdc.goog/subject"] == $SA_NAME and (.metadata.name |startswith("object-storage-key-std-sa-"))) | .metadata.name')
    export ACCESS_KEY_ID=$(kubectl --kubeconfig SOURCE_KUBECONFIG get secret ${BUCKET_CRED_SECRET_NAME} -n ${NAMESPACE} -o jsonpath='{.data.access-key-id}' | base64 -d)
    export SECRET_ACCESS_KEY=$(kubectl --kubeconfig SOURCE_KUBECONFIG get secret ${BUCKET_CRED_SECRET_NAME} -n ${NAMESPACE} -o jsonpath='{.data.secret-access-key}' | base64 -d)
    
    echo "FULL_BUCKET_NAME: ${FULL_BUCKET_NAME}"
    echo "ENDPOINT: ${ENDPOINT}"
    echo "REGION: ${REGION}"
    echo "ACCESS_KEY_ID: ${ACCESS_KEY_ID}"
    echo "SECRET_ACCESS_KEY: ${SECRET_ACCESS_KEY}"
    

Replace `SOURCE_KUBECONFIG` with the path to the kubeconfig file of the source management API server.

## Import repository to target instance

Run the following commands against the management API server of the target gdcloud CLI instance.

  1. Create namespace `dbs-dr`:
         
         kubectl --kubeconfig TARGET_KUBECONFIG create namespace dbs-dr
         

  2. Create a secret named `secret` in `dbs-dr` namespace with S3 credentials for accessing backup bucket on source instance:
         
         kubectl --kubeconfig TARGET_KUBECONFIG create secret generic secret --namespace dbs-dr \
           --from-literal=access-key-id=${ACCESS_KEY_ID} \
           --from-literal=secret-access-key=${SECRET_ACCESS_KEY}
         

  3. Create a `BackupRepository` resource which points to the same bucket used to store DBS backups in the source gdcloud CLI instance. Use bucket details collected in the previous section.
         
         kubectl --kubeconfig TARGET_KUBECONFIG apply -f - <<EOF
           apiVersion: backup.gdc.goog/v1
           kind: BackupRepository
           metadata:
             name: dbs-backup-repository
           spec:
             secretReference:
               namespace: dbs-dr
               name: secret
             endpoint: ${ENDPOINT}
             type: S3
             s3Options:
               bucket: ${FULL_BUCKET_NAME}
               region: ${REGION}
               forcePathStyle: true
             importPolicy: ReadWrite
             force: true
           EOF
         

  4. Verify backups are successfully imported to the management API server of the target gdcloud CLI instance:
         
         kubectl --kubeconfig TARGET_KUBECONFIG get backups.backup.gdc.goog -n dbs-dr
         

Successful backups are imported and have a state of `Succeeded`.




Replace `TARGET_KUBECONFIG` with the path to the kubeconfig file of the target management API server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
