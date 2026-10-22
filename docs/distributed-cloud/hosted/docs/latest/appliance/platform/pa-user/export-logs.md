---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/export-logs/
title: Export logs to a remote bucket \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:56.270918+00:00
---

# Export logs to a remote bucket  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/export-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Export logs to a remote bucket Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export the audit and operational logs in Google Distributed Cloud (GDC) air-gapped appliance to a remote bucket by using the storage transfer tool.

## Obtain IAM roles

To get the permissions that you need to export logs, ask your Organization IAM Admin to grant you the Logs Transfer Admin (`logs-transfer-admin`) role in the `obs-system` namespace in the infra cluster and the Logs Bucket Viewer (`logs-bucket-viewer)` role in the `obs-system` namespace in the management plane.

For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

## Obtain the endpoint and fully qualified name of the source bucket

  1. Set `KUBECONFIG` to the Org Management API:
         
         export KUBECONFIG=MANAGEMENT_API_KUBECONFIG_PATH
         

  2. Get the endpoint of the source bucket:

     * For audit logs:
           
           kubectl get bucket audit-logs-loki-all -n obs-system -o json | jq '.status.endpoint'
           

     * For operational logs:
           
           kubectl get bucket ops-logs-loki-all -n obs-system -o json | jq '.status.endpoint'
           

  3. Get the fully qualified name of the source bucket:

     * For audit logs:
           
           kubectl get bucket audit-logs-loki-all -n obs-system -o json | jq '.status.fullyQualifiedName'
           

     * For operational logs:
           
           kubectl get bucket ops-logs-loki-all -n obs-system -o json | jq '.status.fullyQualifiedName'
           




## Obtain source bucket's access credentials

  1. Set KUBECONFIG to the Org Infra cluster:
         
         export KUBECONFIG=INFRA_CLUSTER_KUBECONFIG_PATH
         

  2. Obtain the access key ID of the source bucket:

     * For audit logs:
           
           kubectl get secret audit-logs-loki-all-s3-auth -n obs-system -o json | jq -r '.data."access-key-id"' | base64 -di
           

     * For operational logs:
           
           kubectl get secret ops-logs-loki-all-s3-auth -n obs-system -o json | jq -r '.data."access-key-id"' | base64 -di
           

  3. Get the secret access key of the source bucket:

     * For audit logs:
           
           kubectl get secret audit-logs-loki-all-s3-auth -n obs-system -o json | jq -r '.data."secret-access-key"' | base64 -di
           

     * For operational logs:
           
           kubectl get secret ops-logs-loki-all-s3-auth -n obs-system -o json | jq -r '.data."secret-access-key"' | base64 -di
           




## Transfer logs

  1. Set `KUBECONFIG` to the Org Infra cluster:
         
         export KUBECONFIG=INFRA_CLUSTER_KUBECONFIG_PATH
         

  2. Create a secret with the access credentials of the source bucket:
         
         kubectl create secret generic -n obs-system SRC_BUCKET_SECRET_NAME
         --from-literal=access-key-id=SRC_BUCKET_ACCESS_KEY_ID
         --from-literal=secret-access-key=SRC_BUCKET_SECRET_ACCESS_KEY
         

  3. Create a secret with the access credentials of the destination bucket:
         
         kubectl create secret generic -n obs-system DST_BUCKET_SECRET_NAME 
         --from-literal=access-key-id=DST_BUCKET_ACCESS_KEY_ID   
         --from-literal=secret-access-key=DST_BUCKET_SECRET_ACCESS_KEY
         

  4. Create a secret with certificate authority for authenticating the endpoint of the destination bucket:
         
         kubectl create secret generic -n obs-system DST_BUCKET_CA_SECRET_NAME 
         --from-file="ca.crt"=CA_FILE
         

To proceed, obtain the `CA_FILE`, `DST_BUCKET_ACCESS_KEY_ID`, and `DST_BUCKET_SECRET_ACCESS_KEY` from the remote bucket. The data transfer tool's operation depends on the specific locations of the transfer endpoints.

  5. Create a log transfer job:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: JOB_NAME
           namespace: obs-system
         spec:
           template:
             spec:
               serviceAccountName: logs-transfer-sa
               containers:
                 - name: storage-transfer-pod
                   image: gcr.io/private-cloud-staging/storage-transfer:latest
                   imagePullPolicy: Always
                   command:
                     - /storage-transfer
                   args:
                     - '--src_endpoint=SRC_BUCKET_ENDPOINT'
                     - '--dst_endpoint=DST_BUCKET_ENDPOINT'
                     - '--src_path=SRC_BUCKET_FULLY_QUALIFIED_NAME'
                     - '--dst_path=DST_BUCKET_FULLY_QUALIFIED_NAME'
                     - '--src_credentials=obs-system/SRC_BUCKET_SECRET_NAME'
                     - '--dst_credentials=obs-system/DST_BUCKET_SECRET_NAME'
                     - '--dst_ca_certificate_reference=obs-system/DST_BUCKET_CA_SECRET_NAME'
                     - '--src_ca_certificate_reference=obs-system/trust-store-root-ext'
                     - '--src_type=s3'
                     - '--dst_type=s3'
                     - '--bandwidth_limit=1G'
               restartPolicy: OnFailure.
         ---
         

  6. Wait for the transfer job to complete:
         
         kubectl wait --for=condition=complete job/JOB_NAME -n obs-system
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
