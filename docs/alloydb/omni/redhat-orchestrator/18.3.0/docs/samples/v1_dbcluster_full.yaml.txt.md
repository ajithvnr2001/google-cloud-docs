---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/samples/v1_dbcluster_full.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/samples/v1_dbcluster_full.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:55:00.681562+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/samples/v1_dbcluster_full.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/samples/v1_dbcluster_full.yaml.txt

DBCluster: metadata: name: alloydb-prod spec: databaseVersion: 18.1.0 loadBalancerPort: 5433 readOnlyPort: 5434 mode: "" availability: numberOfStandbys: 2 enableAutoFailover: true enableAutoHeal: true enableStandbyAsReadReplica: true autoFailoverTriggerThreshold: 2 autoHealTriggerThreshold: 2 healthcheckPeriodSeconds: 10 primarySpec: adminUser: passwordRef: name: db-pw-alloydb-prod port: 5432 monitorPort: 9187 parameters: max_connections: "100" max_wal_size: "2GB" max_worker_processes: "32" log_connections: "on" log_disconnections: "on" log_hostname: "on" log_statement: "none" resources: cpu: 16 memory: 32Gi limits: memory: 64Gi disks: \- name: DataDisk path: /mnt/disks/pgsql \- name: ObsDisk path: /obs dbLoadBalancerOptions: onprem: loadBalancerIP: 10.1.0.95 loadBalancerType: "internal" loadBalancerInterface: "eth0" features: columnarSpillToDisk: cacheSize: "50Gi" localVolume: path: "/mnt/disks/ssd1" ultraFastCache: cacheSize: "100Gi" localVolume: path: "/mnt/disks/ssd2" googleMLExtension: enabled: true config: vertexAIKeyRef: "vertex-ai-key" vertexAIRegion: "us-central1" 
