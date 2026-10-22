---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown-a-blade/
title: Shut down one blade \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:17.173135+00:00
---

# Shut down one blade  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown-a-blade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Shut down one blade Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to shut down and reboot any one blade of Google Distributed Cloud (GDC) air-gapped appliance, for example to move the device to maintain a blade.

## Before you begin

Ensure you stop all workloads before proceeding further. Google cannot guarantee what will happen if workloads are active during a shutdown.

If you want to shut down all the blades, follow [Shut down the device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown). When following these instructions, shut down _only_ one blade and keep Google Distributed Cloud (GDC) air-gapped appliance running with two active blades.

### Prerequisites

  1. You can execute this runbook on a laptop or workstation connected to Google Distributed Cloud (GDC) air-gapped appliance's network. Alternatively, you can connect a laptop or workstation to switch by following [Connect the device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device).
  2. Make sure you have the access to Kubeconfig for the root-admin cluster.
  3. Set correct KUBECONFIG environment variable by running `export KUBECONFIG=<path to kubeconfig>`.



### Shut down the blade

  1. Get the node information by running `kubectl get nodes -A`. Determine `NODE_NAME` of blade to shut down.

  2. Pause BareMetalHost sync by running following command for the blade to be shut down:
         
         kubectl annotate bmhost -n gpc-system NODE_NAME "baremetalhost.metal3.io/paused=true" --overwrite
         

Sample output of this command is:
         
         baremetalhost.metal3.io/**-**-bm** annotated
         

  3. Cordon the target node:
         
         kubectl cordon NODE_NAME
         

Sample output is:
         
         node/**-**-bm** cordoned
         

  4. Drain the target node:
         
         kubectl drain NODE_NAME --delete-emptydir-data --grace-period 900 --ignore-daemonsets --disable-eviction
         

Sample output:
         
         node/**-**-bm** already cordoned
         WARNING: ignoring DaemonSet-managed Pods: kube-system/anetd-krj2z, kube-system/etcd-defrag-xh469, kube-system/ipam-controller-manager-2f4dz, kube-system/istio-cni-node-cgqv4, kube-system/kube-proxy-5mwf2, kube-system/localpv-mn2jh, kube-system/metallb-speaker-6l7sv, mon-system/mon-node-exporter-backend-nd8mp, netapp-trident/netapp-trident-node-linux-rrlmd, obs-system/anthos-audit-logs-forwarder-tpfqv, obs-system/anthos-log-forwarder-npjh4, obs-system/kube-control-plane-metrics-proxy-wp8nh, obs-system/log-failure-detector-crbnv, obs-system/oplogs-forwarder-sqwvj, vm-system/macvtap-v9pgp, vm-system/virt-handler-86khx
         pod/grafana-0 deleted
         pod/capi-kubeadm-bootstrap-controller-manager-1.30.400-gke.136lvgtf deleted
         pod/grafana-0 deleted
         pod/grafana-proxy-server-86d8fc4758-mkc4f deleted
         .
         .
         .
         

  5. Gracefully shutdown the target node:

  6. Turn off `NODE_NAME` using iLO:

     * Retrieve the credentials to access the iLO:

       1. Get the username:
              
              kubectl get secret bmc-credentials-NODE_NAME -n gpc-system -o jsonpath="{.data.username}" | base64 --decode
              

       2. Get the password:
              
              kubectl get secret bmc-credentials-NODE_NAME -n gpc-system -o jsonpath="{.data.password}" | base64 --decode
              

       3. Retrieve the `BMC-IP` address for `NODE_NAME` from values in `BMC-IP` column:
              
              kubectl get servers -A
              

     * Visit the `BMC-IP` address obtained in the previous step and sign in by entering the username and password obtained.

     * Hover over first button on top row. It should display `Power: ON`. Click it. A drop-down menu will appear, click first item labelled `Momentary Press`. The button colour will change from Green to Orange, meaning node is shutting down. Wait for the button to change color to yellow, indicating the machine has powered off. This will take a few minutes.

  7. Wait for 30 minutes for the reconciliation to complete.




## Reboot the blade

This section describes steps to boot up a blade which was shut down earlier.

### Prerequisites

You can execute this runbook on a laptop or workstation connected to Google Distributed Cloud (GDC) air-gapped appliance's network. Alternatively, you can connect a laptop or workstation to switch by following [Connect the device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device). Make sure you have the access to Kubeconfig for the root-admin cluster. And set correct KUBECONFIG environment variable by running `export KUBECONFIG=<path to kubeconfig>`.

### Plan of action

  1. Press the power button on the blade. Once the blade is powered up, wait for a few minutes for the control plane to connect. `kubectl` should be able to connect to control plane in under 30 minutes.

  2. Determine name of the target node by running `kubectl get nodes -A`.

  3. Uncordon the target node to enable scheduling:
         
         kubectl uncordon `NODE_NAME`
         

  4. Resume sync of BareMetalHost for the target node:
         
         kubectl annotate bmhost -n gpc-system NODE_NAME "baremetalhost.metal3.io/paused=false" --overwrite
         

  5. Wait for 30 minutes for the reconciliation to complete.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
