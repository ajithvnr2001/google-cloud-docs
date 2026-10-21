---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:20:25.819008+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1 kind: BackupPlan metadata: name: backupplan1 namespace: db spec: dbclusterRef: dbcluster-sample backupRetainDays: 14 paused: false backupSchedules: # Full backup at 00:00 on every Sunday. full: "0 0 * * 0" # Incremental backup at 21:00 every day. incremental: "0 21 * * *" backupLocation: type: S3 s3Options: bucket: dbcluster-sample-backups-s3 key: /backup region: "us-east-1" endpoint: "https://s3.storage.com" secretRef: name: s3-access-secret namespace: db # You can optionally provide the cert to be used to connect to the S3 with TLS. # If not provided, TLS verification will be skipped. certRef: name: server-tls namespace: server-ns \--- apiVersion: v1 kind: Secret metadata: namespace: db name: "s3-access-secret" type: Opaque data: # Update the following with your S3 access keys. access-key-id: "Q2hhbmdlTWUxMjM=" # access-key-id is ChangeMe123 access-key: "Q2hhbmdlTWUxMjM=" # access-key is ChangeMe123 
