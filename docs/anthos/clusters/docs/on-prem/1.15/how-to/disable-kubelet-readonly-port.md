---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/disable-kubelet-readonly-port/
title: Disable Kubelet readonly port \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:03.541643+00:00
---

# Disable Kubelet readonly port  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/disable-kubelet-readonly-port/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Disable Kubelet readonly port Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/disable-kubelet-readonly-port)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/disable-kubelet-readonly-port)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



## Overview

This document shows how to deploy a privileged daemonset in each node of Google Distributed Cloud to modify kubelet parameters to disable read-only ports.

## Prerequisite

Make sure your Google Distributed Cloud is healthy before running the following patch script. This solution can be used to patch both admin clusters and user clusters. And it should work for all Google Distributed Cloud versions.

## Save the following Daemonset YAML to your local file (e.g. patch.yaml)
    
    
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
              value: "0"
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
                  sed -E -i 's/readOnlyPort: [0-9]+/readOnlyPort: 0/g' ${configfile}
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
    

## Patch on the admin cluster
    
    
       kubectl apply -f patch.yaml \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

## Patch on the user cluster
    
    
       kubectl apply -f patch.yaml \
        --kubeconfig USER_CLUSTER_KUBECONFIG
    

## Restore

  * To re-enable the read-only port, manually edit the environment variable `KUBELET_READONLY_PORT` in the Daemonset YAML.

  * Once you save the changes, the daemonset will be re-run to modify the kubelet accordingly.




## Caveats

  * This patch has the same lifecycle as your installed 3P apps. You can run it anytime as a day 2 operation. But it might not persist after you re-create the cluster. To make this change persistent, deploy this daemonset as a step in the Google Distributed Cloud post-initialization action.

  * After running once, the Kubelet config file should be modified and reloaded. You can safely run `kubectl delete -f patch.yaml` to clean up daemonset resources.

  * Anthos running on Windows does not currently support this patch.

  * The following metrics are lost for 1.13 and older cluster versions:

    * [Resource utilization metrics](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/metrics-anthos#find_a_metric)
    * [Kubelet metrics](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/metrics-anthos#find_a_metric)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
