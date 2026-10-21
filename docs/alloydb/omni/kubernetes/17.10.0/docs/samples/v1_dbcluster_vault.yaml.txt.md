---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_dbcluster_vault.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_dbcluster_vault.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:16:49.004001+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_dbcluster_vault.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_dbcluster_vault.yaml.txt

apiVersion: v1 kind: Secret metadata: name: db-pw-dbcluster-sample type: Opaque data: # dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123 dbcluster-sample: "ZGhhcm1hbGluZ2Ft" \--- apiVersion: v1 kind: Secret metadata: name: alloydbadmin-pw-dbcluster-sample type: Opaque data: # dbcluster-sample: "Q2hhbmdlTWUxMjM=" dbcluster-sample: "ZGhhcm1hbGluZ2Ft" # dbcluster-sample: "YXJhdmluZGFuCg==" \--- apiVersion: alloydbomni.dbadmin.goog/v1 kind: DBCluster metadata: name: dbcluster-sample spec: databaseVersion: "17.9.0" # availability: # numberOfStandbys: 1 # enableStandbyAsReadReplica: true primarySpec: adminUser: passwordRef: name: db-pw-dbcluster-sample systemUserPasswordRefs: alloydbadmin: alloydbadmin-pw-dbcluster-sample resources: memory: 5Gi cpu: 1 disks: \- name: DataDisk size: 10Gi parameters: omni_password_provider: "/samwise-scripts/credfetcher" 
