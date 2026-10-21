---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_ml.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_ml.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:25:31.672386+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_ml.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_ml.yaml.txt

apiVersion: v1 kind: Secret metadata: name: db-pw-dbcluster-sample type: Opaque data: dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123 \--- apiVersion: v1 kind: Secret metadata: name: vertex-ai-key-alloydb type: Opaque data: private-key.json: "" \--- apiVersion: alloydbomni.dbadmin.goog/v1 kind: DBCluster metadata: name: dbcluster-sample spec: databaseVersion: "16.13.0" primarySpec: features: googleMLExtension: enabled: true config: vertexAIKeyRef: vertex-ai-key-alloydb vertexAIRegion: us-central1 adminUser: passwordRef: name: db-pw-dbcluster-sample resources: memory: 5Gi cpu: 1 disks: \- name: DataDisk size: 10Gi 
