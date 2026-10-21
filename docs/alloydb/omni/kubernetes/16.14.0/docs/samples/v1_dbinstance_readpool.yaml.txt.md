---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_dbinstance_readpool.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_dbinstance_readpool.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:23:02.898748+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_dbinstance_readpool.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_dbinstance_readpool.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1 kind: DBInstance metadata: name: dbcluster-sample-rp-1 spec: instanceType: ReadPool dbcParent: name: dbcluster-sample nodeCount: 2 resources: memory: 6Gi cpu: 2 disks: \- name: DataDisk size: 15Gi schedulingconfig: tolerations: \- key: "node-role.kubernetes.io/control-plane" operator: "Exists" effect: "NoSchedule" nodeaffinity: preferredDuringSchedulingIgnoredDuringExecution: \- weight: 1 preference: matchExpressions: \- key: another-node-label-key operator: In values: \- another-node-label-value podAffinity: preferredDuringSchedulingIgnoredDuringExecution: \- weight: 1 podAffinityTerm: labelSelector: matchExpressions: \- key: app operator: In values: \- store topologyKey: "kubernetes.io/hostname" podAntiAffinity: preferredDuringSchedulingIgnoredDuringExecution: \- weight: 1 podAffinityTerm: labelSelector: matchExpressions: \- key: security operator: In values: \- S1 topologyKey: "topology.kubernetes.io/zone" 
