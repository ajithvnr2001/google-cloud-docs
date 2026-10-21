---
url: https://docs.cloud.google.com/migrate/containers/docs/mounting-external-volumes/
title: Mount external volumes \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:33.548400+00:00
---

# Mount external volumes  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/mounting-external-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Mount external volumes

This topic explains how to mount additional volumes to a workload migrated with Migrate to Containers. You might want to do this when your workload depends on an external volume that is not copied to a Persistent Volume.

To add external volumes to a Migrate to Containers workload:

  1. Add the volume to the `StatefulSet` in `spec.containers.volumeMounts`. See [Kubernetes Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) for more information.
  2. Mount the volume in the container at the mount point you would like. This will vary depending on the container's operating system.



The example below mounts the volume `emptydir` to `/tmp`.
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      creationTimestamp: null
      labels:
        app: app-my-vm-instance-1
        migrate-for-anthos-type: workload
      name: app-my-vm-instance-1
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: app-my-vm-instance-1
          migrate-for-anthos-type: workload
      serviceName: app-my-vm-instance-1
      template:
        metadata:
          creationTimestamp: null
          labels:
            app: app-my-vm-instance-1
            migrate-for-anthos-type: workload
        spec:
          containers:
          - image: gcr.io/my-project/my-vm-instance-1:v1.0.0
            name: app-my-vm-instance-1
            readinessProbe:
              exec:
                command:
                - /code/ready.sh
            resources: {}
            securityContext:
              privileged: true
            volumeMounts:
            - name: emptydir
              mountPath: /tmp
            - mountPath: /sys/fs/cgroup
              name: cgroups
            - mountPath: /code/config/logs/
              name: logs-config
            - mountPath: /<folder>
              name: pvc-my-vm-instance-1
              subPath: <folder>
          volumes:
          - name: emptydir
            emptyDir: {}
          - hostPath:
              path: /sys/fs/cgroup
              type: Directory
            name: cgroups
          - configMap:
              name: app-my-vm-instance-1
            name: logs-config
          - name: pvc-my-vm-instance-1
            persistentVolumeClaim:
              claimName: pvc-my-vm-instance-1
      updateStrategy: {}
    status:
      replicas: 0
    

## What's next

  * Learn how to [deploy a Linux workload to a target cluster](https://docs.cloud.google.com/migrate/containers/docs/deploying-to-target-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
