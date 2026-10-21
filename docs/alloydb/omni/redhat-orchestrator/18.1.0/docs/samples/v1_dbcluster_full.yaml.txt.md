---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/v1_dbcluster_full.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/v1_dbcluster_full.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:15:45.489792+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/v1_dbcluster_full.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/v1_dbcluster_full.yaml.txt

DBCluster: metadata: name: alloydb-prod spec: databaseVersion: 18.1.0 mode: "" availability: numberOfStandbys: 2 enableAutoFailover: true enableAutoHeal: true autoFailoverTriggerThreshold: 2 autoHealTriggerThreshold: 2 healthcheckPeriodSeconds: 10 primarySpec: adminUser: passwordRef: name: db-pw-alloydb-prod parameters: max_connections: "100" max_wal_size: "2GB" max_worker_processes: "32" log_connections: "on" log_disconnections: "on" log_hostname: "on" log_statement: "none" huge_pages: "off" tcp_keepalives_idle: "10" tcp_keepalives_interval: "10" tcp_keepalives_count: "10" resources: cpu: 16 memory: 64Gi disks: \- name: DataDisk path: /mnt/disks/pgsql \- name: ObsDisk path: /obs dbLoadBalancerOptions: onprem: loadBalancerIP: 10.1.0.95 loadBalancerType: "internal" loadBalancerInterface: "eth0" 
