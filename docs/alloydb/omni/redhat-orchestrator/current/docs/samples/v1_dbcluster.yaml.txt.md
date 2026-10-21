---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_dbcluster.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_dbcluster.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-14T22:07:57.576245+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_dbcluster.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_dbcluster.yaml.txt


    DBCluster:
      metadata:
        name: alloydb-prod
      spec:
        databaseVersion: 18.1.0
        primarySpec:
          adminUser:
            passwordRef:
              name: db-pw-alloydb-prod
          resources:
            disks:
            - name: DataDisk
              path: /mnt/disks/pgsql
    
