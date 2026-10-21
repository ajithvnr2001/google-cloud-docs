---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enable-kubelet-readonly-port/
title: Enable kubelet readonly port \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:12.022679+00:00
---

# Enable kubelet readonly port  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enable-kubelet-readonly-port/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Enable kubelet readonly port Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This document shows how to deploy a privileged DaemonSet in each node of Google Distributed Cloud to modify kubelet parameters to enable read-only ports. In version 1.16 and later, the kubelet read-only port is disabled by default.

## Prerequisite

Make sure your Google Distributed Cloud is healthy before running the following patch script. You can use this solution to patch 1.16 and later admin clusters and user clusters.

## Create a DaemonSet file

Create and save a DaemonSet file named patch.yaml in your current directory, with the following content:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: onprem-node-patcher
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          name: onprem-node-patcher
      updateStrategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            name: onprem-node-patcher
        spec:
          tolerations:
          - operator: Exists
          volumes:
          - name: host
            hostPath:
              path: /
          hostPID: true
          initContainers:
          - name: read-only-patcher
            image: "ubuntu"
            env:
            - name: KUBELET_READONLY_PORT
              value: "10255"
            # Number of 1G hugepages. Update the value as desired.
            command:
            - /bin/bash
            - -c
            - |
              set -xeuo pipefail
              configfile="/host/var/lib/kubelet/config.yaml"
              kubeletservice="/host/etc/systemd/system/kubelet.service"
              # $1: The read-only port for the kubelet to serve on with no
              #     authentication/authorization (set to 0 to disable)
              function set-readonly-port-in-config() {
                [[ "$#" -eq 1 ]] || return
                local readonlyport; readonlyport="$1"
                local actual; actual="$(grep readOnlyPort "${configfile}")"
                if [[ "${actual}" == "" ]]; then
                  echo "readOnlyPort: ${readonlyport}" >> "${configfile}"
                else
                  sed -E -i 's/readOnlyPort: [0-9]+/readOnlyPort: '"${readonlyport}"'/g' ${configfile}
                fi
                echo "Successfully append readOnlyPort: ${readonlyport} to ${configfile}"
              }
              sed -E -i 's/--read-only-port=[0-9]+/--read-only-port='"${KUBELET_READONLY_PORT}"'/g' ${kubeletservice}
              [[ -f ${configfile} ]] && set-readonly-port-in-config "${KUBELET_READONLY_PORT}"
              echo "Restarting kubelet..."
              chroot /host nsenter -a -t1 -- systemctl daemon-reload
              chroot /host nsenter -a -t1 -- systemctl restart kubelet.service
              echo "Success!"
            volumeMounts:
            - name: host
              mountPath: /host
            resources:
              requests:
                memory: 5Mi
                cpu: 5m
            securityContext:
              privileged: true
          containers:
          - image: gcr.io/google-containers/pause:3.2
            name: pause
          # Ensures that the pods will only run on the nodes having the correct
          # label.
          nodeSelector:
            "kubernetes.io/os": "linux"
    

## Update the read-only port number

  * To change the port number, manually edit the environment variable `KUBELET_READONLY_PORT` in the DaemonSet YAML.

  * The default read-only port is `10255`, you should not pick `10250` as it will conflict with the predefined secure port.




## Patch the admin cluster
    
    
       kubectl apply -f patch.yaml \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

## Patch the user cluster
    
    
       kubectl apply -f patch.yaml \
        --kubeconfig USER_CLUSTER_KUBECONFIG
    

## Restore

  * To disable the read-only port, manually edit the environment variable `KUBELET_READONLY_PORT` in the DaemonSet YAML.

  * After you save the changes, the DaemonSet will be re-run to modify the kubelet accordingly.




## Caveats

  * This patch has the same lifecycle as your installed 3P apps. You can run it anytime as a day 2 operation. But it might not persist after you re-create the cluster. To make this change persistent, deploy this DaemonSet as a step in the Google Distributed Cloud post-initialization action.

  * After running once, the kubelet configuration file should be modified and reloaded. You can safely run `kubectl delete -f patch.yaml` to clean up DaemonSet resources.

  * Google Distributed Cloud running on Windows does not support this patch.

  * Kubernetes does not perform any authentication or authorization checks on this insecure port `10255`. Enabling it will leave kubelet data unprotected and exposed to unauthorized users. The kubelet serves the same endpoint on the more secure, authenticated port `10250`, consider migrating to that secure port. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
