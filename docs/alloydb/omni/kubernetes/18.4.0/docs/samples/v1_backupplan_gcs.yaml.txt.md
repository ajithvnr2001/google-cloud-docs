---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:19:48.407633+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1 kind: BackupPlan metadata: name: backupplan1 namespace: db spec: dbclusterRef: dbcluster-sample backupRetainDays: 14 paused: false backupSchedules: # Full backup at 00:00 on every Sunday. full: "0 0 * * 0" # Incremental backup at 21:00 every day. incremental: "0 21 * * *" backupLocation: type: GCS gcsOptions: bucket: dbcluster-sample-backups key: /backup # You can optionally provide a key for accessing your GCS bucket. # The key.json needs to be base64 encoded and stored in the given secret under data[key.json]. # Or comment out below, which will then use the GKE cluster service account # to access the GCS bucket (you need to make sure the service account has # the right permission to R/W the GCS bucket). secretRef: name: gcs-key namespace: db \--- apiVersion: v1 kind: Secret metadata: name: gcs-key namespace: db data: key.json: | 
