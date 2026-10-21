---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/samples/v1_dbcluster_scheduling_config.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/samples/v1_dbcluster_scheduling_config.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:21:27.807736+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/samples/v1_dbcluster_scheduling_config.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/samples/v1_dbcluster_scheduling_config.yaml.txt

apiVersion: v1 kind: Secret metadata: name: db-pw-dbcluster-sample type: Opaque data: dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123 \--- apiVersion: alloydbomni.dbadmin.goog/v1 kind: DBCluster metadata: name: dbcluster-sample spec: databaseVersion: "15.17.0" availability: numberOfStandbys: 1 enableStandbyAsReadReplica: true primarySpec: schedulingconfig: topologySpreadConstraints: \- maxSkew: 1 topologyKey: "topology.kubernetes.io/zone" whenUnsatisfiable: DoNotSchedule adminUser: passwordRef: name: db-pw-dbcluster-sample resources: memory: 5Gi cpu: 1 disks: \- name: DataDisk size: 10Gi 
