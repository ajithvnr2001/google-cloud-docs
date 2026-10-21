---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_sidecar.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_sidecar.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-17T10:20:13.295093+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_sidecar.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_sidecar.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Sidecar
    metadata:
      name: sidecar-sample
    spec:
      sidecars:
      - image: busybox
        name: sidecar-sample
        volumeMounts:
          - name: obsdisk
            mountPath: /logs
        command: ["/bin/sh"]
        args:
        - -c
        - |
          while [ true ]
          do
          date
          set -x
          ls -lh /logs/diagnostic
          set +x
          done
    
