---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown/
title: Shut down and power up the device \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:39.432396+00:00
---

# Shut down and power up the device  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Shut down and power up the device Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to shut down and powerup Google Distributed Cloud (GDC) air-gapped appliance. For example: to move the device to a new location.

You might use GDC air-gapped appliance in transient operational locations, where it is necessary to shut the device for transport in order to move the device between locations. You might also need to restore the device from a power failure, as generators might power it in rugged environments.

### Before you begin

Ensure you stop all workloads before proceeding further. Google cannot guarantee what will happen if workloads are active during a shutdown.

### Prerequisites

  1. You can execute this runbook on a laptop or workstation connected to Google Distributed Cloud (GDC) air-gapped appliance's network. Alternatively, you can connect a laptop or workstation to switch by following [Connect the device](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device).
  2. Make sure that you have the access to the kubeconfig for the root-admin cluster.
  3. Set the correct KUBECONFIG environment variable by running `export KUBECONFIG=PATH_TO_KUBECONFIG`.
  4. Ensure that you have the [SSH key and certificate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#ssh-bm03).



## Shut down the blades

  1. Get info of nodes by running `kubectl get nodes -A -o wide`.

  2. Pause BareMetalHost sync by running the following command _for all nodes_ one by one. Replace `NODE_NAME` with the node names obtained in the previous step:
         
         kubectl annotate bmhost -n gpc-system NODE_NAME "baremetalhost.metal3.io/paused=true" --overwrite
         

The output might look like this example:
         
         baremetalhost.metal3.io/**-**-bm01 annotated
         baremetalhost.metal3.io/**-**-bm02 annotated
         baremetalhost.metal3.io/**-**-bm03 annotated
         

  3. Get ONTAP Select (OTS) credentials. You need these credentials to shut down OTS nodes later.

Run the following command to identify the OTS management IP address listed under the MGMTIP (Management IP) column:
         
         export KUBECONFIG=/root/release/root-admin/kube-admin-remote-kubeconfig
         
          kubectl get storagecluster -n gpc-system
         

Run the following commands to retrieve the OTS administrator password:
         
         export KUBECONFIG=/root/release/root-admin/root-admin-kubeconfig
         
          # Find the secret name
          SECRET_NAME=$(kubectl get secrets -n gpc-system -o name | grep 'ontap-.*-stge01-credential')
         
          # Decode the password from that secret
          OTS_PASSWORD=$(kubectl get $SECRET_NAME -n gpc-system -o jsonpath='{.data.netapp_password}' | base64 --decode)
         
          echo $OTS_PASSWORD
         

Save the OTS management IP and password.

  4. Cordon all nodes one by one:
         
         kubectl cordon NODE_NAME
         

The output might look like this example:
         
         node/**-**-bm01 cordoned
         node/**-**-bm02 cordoned
         node/**-**-bm03 cordoned
         

  5. Shut down the ONTAP Select (OTS) nodes

Establish an SSH connection to the OTS cluster using the management IP address and administrator password you retrieved:
         
         ssh admin@<ots-management-ip>
         

Shut down the OTS nodes (VMs). The following is an example:
         
         bn-aa-stge01::> cluster show
          Node                  Health  Eligibility
          --------------------- ------- ------------
          bn-aa-stge01-01       true    true
          bn-aa-stge01-02       true    true
         
          bn-aa-stge01::> set diag
         
          Warning: These diagnostic commands are for use by NetApp personnel only.
          Do you want to continue? {y|n}: y
         
          bn-aa-stge01::> system node halt -node *
         

  6. To prevent the gatekeeper webhook from blocking the node drains when its pods go offline, temporarily set its failure policy to `Ignore`:
         
         kubectl patch validatingwebhookconfiguration gatekeeper-validating-webhook-configuration -p '{"webhooks":[{"name":"validation.gatekeeper.sh","failurePolicy":"Ignore"}]}'
         

  7. To determine etcd leader node and follower nodes, run this step one by one for all nodes:

     1. Find target IPs for SSH by noting values under `INTERNAL-IP` column of output from `kubectl get nodes -A -o wide`. Establish an SSH connection:
            
            ssh root@INTERNAL-IP
            

     2. To determine whether current node is etcd leader or follower, run following command inside the SSH terminal:
            
            ETCDCTL_API=3 etcdctl \
                --cacert /etc/kubernetes/pki/etcd/ca.crt \
                --cert /etc/kubernetes/pki/etcd/server.crt \
                --key /etc/kubernetes/pki/etcd/server.key \
                --write-out=table endpoint status
            

Pay attention to the `IS LEADER` field.

The output might look like this example for the etcd leader node:
            
            [root@**-**-bm0* ~]# ETCDCTL_API=3 etcdctl \
            >      --cacert /etc/kubernetes/pki/etcd/ca.crt \
            >      --cert /etc/kubernetes/pki/etcd/server.crt \
            >      --key /etc/kubernetes/pki/etcd/server.key \
            >      --write-out=table endpoint status
            +----------------+------------------+--------------+---------+-----------+------------+-----------+------------+--------------------+--------+
            |    ENDPOINT    |        ID        |   VERSION    | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
            +----------------+------------------+--------------+---------+-----------+------------+-----------+------------+--------------------+--------+
            | ************** | **************** | 3.4.30-gke.1 |  162 MB |      true |      false |      3641 |   12957958 |           12957958 |        |
            +----------------+------------------+--------------+---------+-----------+------------+-----------+------------+--------------------+--------+
            

The output might look like this example for the two etcd follower nodes:
            
            [root@**-**-bm0* ~]# ETCDCTL_API=3 etcdctl \
            >      --cacert /etc/kubernetes/pki/etcd/ca.crt \
            >      --cert /etc/kubernetes/pki/etcd/server.crt \
            >      --key /etc/kubernetes/pki/etcd/server.key \
            >      --write-out=table endpoint status
            +----------------+------------------+--------------+---------+-----------+------------+-----------+------------+--------------------+--------+
            |    ENDPOINT    |        ID        |   VERSION    | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
            +----------------+------------------+--------------+---------+-----------+------------+-----------+------------+--------------------+--------+
            | ************** | **************** | 3.4.30-gke.1 |  163 MB |     false |      false |      3641 |   12957404 |           12957404 |        |
            +----------------+------------------+--------------+---------+-----------+------------+-----------+------------+--------------------+--------+
            

Note down the etcd-leader and etcd-follower status of the nodes.

  8. Drain the nodes.

Drain the two etcd follower nodes. Do _not_ drain the etcd leader node
         
         kubectl drain NODE_NAME --delete-emptydir-data --grace-period 900 --ignore-daemonsets --disable-eviction
         

The output might look like this:
         
         node/**-**-bm01 already cordoned
         WARNING: ignoring DaemonSet-managed Pods: kube-system/anetd-krj2z, kube-system/etcd-defrag-xh469, kube-system/ipam-controller-manager-2f4dz, kube-system/istio-cni-node-cgqv4, kube-system/kube-proxy-5mwf2, kube-system/localpv-mn2jh, kube-system/metallb-speaker-6l7sv, mon-system/mon-node-exporter-backend-nd8mp, netapp-trident/netapp-trident-node-linux-rrlmd, obs-system/anthos-audit-logs-forwarder-tpfqv, obs-system/anthos-log-forwarder-npjh4, obs-system/kube-control-plane-metrics-proxy-wp8nh, obs-system/log-failure-detector-crbnv, obs-system/oplogs-forwarder-sqwvj, vm-system/macvtap-v9pgp, vm-system/virt-handler-86khx
         pod/grafana-0 deleted
         pod/capi-kubeadm-bootstrap-controller-manager-1.30.400-gke.136lvgtf deleted
         pod/grafana-0 deleted
         pod/grafana-proxy-server-86d8fc4758-mkc4f deleted
         .
         .
         .
         
         node/**-**-bm02 already cordoned
         WARNING: ignoring DaemonSet-managed Pods: kube-system/anetd-v75jz, kube-system/etcd-defrag-t5jnc, kube-system/ipam-controller-manager-5958m, kube-system/istio-cni-node-ggv4c, kube-system/kube-proxy-r6x46, kube-system/localpv-g56xc, kube-system/metallb-speaker-tmw72, mon-system/mon-node-exporter-backend-9rs7k, netapp-trident/netapp-trident-node-linux-9jmfp, obs-system/anthos-audit-logs-forwarder-bwns9, obs-system/anthos-log-forwarder-lbskj, obs-system/kube-control-plane-metrics-proxy-grthl, obs-system/log-failure-detector-dzh4v, obs-system/oplogs-forwarder-vdn7z, vm-system/macvtap-mjwtc, vm-system/virt-handler-dlqvv
         pod/vai-web-plugin-backend-5dfd6d6597-nxxgn
         pod/vai-web-plugin-frontend-6b5468968b-mrr7g
         pod/grafana-proxy-server-64b759fbf6-b8pl8
         pod/iam-bundledidp-backend-0
         .
         .
         .
         

  9. Gracefully shutdown the two etcd follower nodes. Follow next step _one by one_ for both node.

  10. Turn off `NODE_NAME` using iLO:

     1. Retrieve the username for iLO:
            
            kubectl get secret bmc-credentials-NODE_NAME -n gpc-system -o jsonpath="{.data.username}" | base64 --decode
            

     2. Retrieve the password for iLO:
            
            kubectl get secret bmc-credentials-NODE_NAME -n gpc-system -o jsonpath="{.data.password}" | base64 --decode
            

     3. Retrieve the `BMC-IP` address for `NODE_NAME` from values in `BMC-IP` column:
            
            kubectl get servers -A
            

     4. Visit the `BMC-IP` address obtained in the previous step and sign in by entering the username and password obtained.

     5. Hover over first button on top row. It should display `Power: ON`. Click it. A drop-down menu will appear, click first item labelled `Momentary Press`. The button colour will change from Green to Orange, meaning node is shutting down. Wait for the button to change color to yellow, indicating the machine has powered off. This will take a few minutes.

  11. After both etcd-follower nodes have shutdown, finally repeat the step to drain the node for the etcd leader node.




### Remove Yubikeys for transport

If you need to transport the system after installation completes, remove the Yubikeys and transport the Yubikeys separately. Ensure that you tag the keys yourself.

## Power up and connect

If power was lost unexpectedly, such as a hard shutdown, the device automatically comes back up. In this case, you can skip the steps to power on and connect the device and start directly from the step to uncordon each node. After an unexpected power loss, you may experience data loss, even after restarting.

### Plan of action

  1. Insert the Yubikeys in each node.

  2. Plug the GDC air-gapped appliance machine into power, and press the power button on node `**-**-bm03` to start the OTS mediator server.

  3. After node `**-**-bm03` becomes available, verify that the OTS mediator server is active by checking the status of the SCSI target subsystem (SCST) services. This service should show `Active: active (running)`:
         
         sudo systemctl status scst.service
         

  4. Press the power button on the remaining two nodes in any order.

  5. After the nodes are powered up, wait for a few minutes for the control plane to connect. `kubectl` can connect to the control plane in under 30 minutes.

  6. Get the names of nodes by running `kubectl get nodes -A`.

  7. Uncordon each node to enable scheduling:
         
         kubectl uncordon NODE_NAME
         

  8. Resume sync of the bare metal hosts for each node:
         
         kubectl annotate bmhost -n gpc-system NODE_NAME "baremetalhost.metal3.io/paused=false" --overwrite
         

  9. Revert the gatekeeper validating webhook configuration back to `Fail` to restore cluster security policies:
         
         kubectl patch validatingwebhookconfiguration gatekeeper-validating-webhook-configuration -p '{"webhooks":[{"name":"validation.gatekeeper.sh","failurePolicy":"Fail"}]}'
         

  10. Check the status of the nodes using `kubectl get nodes -A`.

After all nodes are `Ready`, wait 2 hours to allow the base stack to finish reconciling before troubleshooting.

The output might look like this:
         
         NAME         STATUS     ROLES           AGE     VERSION
         **-**-bm01   Ready      control-plane   4d13h   v1.30.6-gke.300
         **-**-bm02   Ready      control-plane   4d13h   v1.30.6-gke.300
         **-**-bm03   Ready      control-plane   4d13h   v1.30.6-gke.300
         

In this case, no further action is needed.

  11. If one or more nodes are in the `NotReady` state, note the name of each node that isn't ready and complete the following steps:
         
         NAME         STATUS     ROLES           AGE     VERSION
         **-**-bm01   Ready      control-plane   4d13h   v1.30.6-gke.300
         **-**-bm02   Ready      control-plane   4d13h   v1.30.6-gke.300
         **-**-bm03   NotReady   control-plane   4d13h   v1.30.6-gke.300
         

     1. Establish an SSH connection into the `NotReady` node. The target IP addresses for SSH are the values under the `INTERNAL-IP` column of the output from `kubectl get nodes -A -o wide`:
            
            ssh root@INTERNAL-IP
            

     2. Restart the `containerd` and `kubelet` services on the `NotReady` node. Run the following commands on the node, _not_ on the laptop or workstation connected to GDC air-gapped appliance:
            
            systemctl stop containerd
            systemctl daemon-reload
            systemctl restart containerd
            systemctl stop kubelet
            systemctl start kubelet
            

     3. Verify the status of the `containerd` and `kubelet` services by running the following commands on the `NotReady` node:
            
            systemctl status kubelet
            systemctl status containerd
            

The output might look like this:
            
            # systemctl status kubelet
            ● kubelet.service - kubelet: The Kubernetes Node Agent
            Loaded: loaded (/usr/lib/systemd/system/kubelet.service; enabled; vendor preset: disabled)
            Drop-In: /etc/systemd/system/kubelet.service.d
                    └─00-standalone_containerd.conf, 10-kubeadm.conf
            Active: active (running) since Thu 2025-03-27 07:58:27 UTC; 34s ago
            .
            .
            .
            
            # systemctl status containerd
            ● containerd.service - containerd container runtime
            Loaded: loaded (/etc/systemd/system/containerd.service; disabled; vendor preset: disabled)
            Active: active (running) since Thu 2025-03-27 07:58:17 UTC; 52s ago
            .
            .
            .
            

Once the `containerd` and `kubelet` services are running and all nodes are `Ready`, wait 2 hours to allow the base stack to finish reconciling before troubleshooting.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
