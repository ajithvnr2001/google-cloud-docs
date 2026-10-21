---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_sidecar_commvault.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_sidecar_commvault.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:04.411679+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_sidecar_commvault.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_sidecar_commvault.yaml.txt

apiVersion: v1 kind: Secret metadata: name: db-pw-dbcluster-sample type: Opaque data: dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123 \--- apiVersion: alloydbomni.dbadmin.goog/v1 kind: DBCluster metadata: name: dbcluster-sample spec: databaseVersion: "15.15.0" primarySpec: adminUser: passwordRef: name: db-pw-dbcluster-sample resources: memory: 5Gi cpu: 1 disks: \- name: DataDisk size: 10Gi \- name: LogDisk size: 10Gi walArchiveSetting: location: wal/log # enable WAL archiving and archive logs to /archive/wal/log sidecarRef: name: cv-sidecar-config 
