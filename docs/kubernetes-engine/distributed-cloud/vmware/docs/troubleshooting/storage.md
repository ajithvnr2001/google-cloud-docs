---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/storage/
title: Troubleshooting storage \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:39.496954+00:00
---

# Troubleshooting storage  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshooting storage Stay organized with collections  Save and categorize content based on your preferences. 

This document gives troubleshooting guidance for storage issues.

## Volume fails to attach

This issue can occur if a virtual disk is attached to the wrong virtual machine, and might be due to [Issue #32727](https://github.com/kubernetes/kubernetes/issues/32727) in Kubernetes 1.12.

The output of `gkectl diagnose cluster` looks like the following example:
    
    
    Checking cluster object...PASS
    Checking machine objects...PASS
    Checking control plane pods...PASS
    Checking gke-connect pods...PASS
    Checking kube-system pods...PASS
    Checking gke-system pods...PASS
    Checking storage...FAIL
        PersistentVolume pvc-776459c3-d350-11e9-9db8-e297f465bc84: virtual disk "[datastore_nfs] kubevols/kubernetes-dynamic-pvc-776459c3-d350-11e9-9db8-e297f465bc84.vmdk" IS attached to machine "gsl-test-user-9b46dbf9b-9wdj7" but IS NOT listed in the Node.Status
    1 storage errors
    

In this example, one or more Pods are stuck in the `ContainerCreating` state, and show warnings like the following example output:
    
    
    Events:
      Type     Reason              Age               From                     Message
      ----     ------              ----              ----                     -------
      Warning  FailedAttachVolume  6s (x6 over 31s)  attachdetach-controller  AttachVolume.Attach failed for volume "pvc-776459c3-d350-11e9-9db8-e297f465bc84" : Failed to add disk 'scsi0:6'.
    

If a virtual disk is attached to the wrong virtual machine, you can manually detach it by using the following steps:

  1. [Drain a node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/). You can optionally include the `--ignore-daemonsets` and `--delete-local-data` flags in your [kubectl drain](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#drain). command.

  2. [Power off the VM](https://kb.vmware.com/s/article/1004340).

  3. Edit the VM's hardware config in vCenter to remove the volume.

  4. [Power on the VM](https://kb.vmware.com/s/article/1003738).

  5. [Uncordon the node](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#uncordon).




## Volume is lost

This issue can occur if a virtual disk was permanently deleted. This situation can happen if an operator manually deletes a virtual disk or deletes the VM the disk is attached to.

If you see a "not found" error related to your VMDK file, it's likely that the virtual disk was permanently deleted.

The output of `gkectl diagnose cluster` looks like the following output:
    
    
    Checking cluster object...PASS
    Checking machine objects...PASS
    Checking control plane pods...PASS
    Checking gke-connect pods...PASS
    Checking kube-system pods...PASS
    Checking gke-system pods...PASS
    Checking storage...FAIL
        PersistentVolume pvc-52161704-d350-11e9-9db8-e297f465bc84: virtual disk "[datastore_nfs] kubevols/kubernetes-dynamic-pvc-52161704-d350-11e9-9db8-e297f465bc84.vmdk" IS NOT found
    1 storage errors
    

One or more Pods are stuck in the `ContainerCreating` state, as shown in the following example output:
    
    
    Events:
      Type     Reason              Age                   From                                    Message
      ----     ------              ----                  ----                                    -------
      Warning  FailedAttachVolume  71s (x28 over 42m)    attachdetach-controller                 AttachVolume.Attach failed for volume "pvc-52161704-d350-11e9-9db8-e297f465bc84" : File []/vmfs/volumes/43416d29-03095e58/kubevols/
      kubernetes-dynamic-pvc-52161704-d350-11e9-9db8-e297f465bc84.vmdk was not found
    

To prevent this issue from occurring, manage your virtual machines as described in [Resizing a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resizing-a-user-cluster) and [Upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

To resolve this issue, you can manually clean up related Kubernetes resources:

  1. Delete the PVC that referenced the PV by running `kubectl delete pvc [PVC_NAME]`.

  2. Delete the Pod that referenced the PVC by running `kubectl delete pod [POD_NAME]`.

  3. Repeat step 2 due to [Kubernetes issue #74374](https://github.com/kubernetes/kubernetes/issues/74374).




## vSphere CSI Volume fails to detach

This issue occurs if the `CNS > Searchable` privilege has not been granted to the vSphere user.

If you find Pods stuck in the `ContainerCreating` phase with `FailedAttachVolume` warnings, it could be due to a failed detach on a different node.

To check for CSI detach errors, run the following command:
    
    
    kubectl get volumeattachments -o=custom-columns=NAME:metadata.name,DETACH_ERROR:status.detachError.message
    

The output is similar to the following example:
    
    
    NAME                                                                   DETACH_ERROR
    csi-0e80d9be14dc09a49e1997cc17fc69dd8ce58254bd48d0d8e26a554d930a91e5   rpc error: code = Internal desc = QueryVolume failed for volumeID: "57549b5d-0ad3-48a9-aeca-42e64a773469". ServerFaultCode: NoPermission
    csi-164d56e3286e954befdf0f5a82d59031dbfd50709c927a0e6ccf21d1fa60192d   <none>
    csi-8d9c3d0439f413fa9e176c63f5cc92bd67a33a1b76919d42c20347d52c57435c   <none>
    csi-e40d65005bc64c45735e91d7f7e54b2481a2bd41f5df7cc219a2c03608e8e7a8   <none>
    

To resolve this issue, add the `CNS > Searchable` privilege to your [vCenter user account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements). The detach operation automatically retries until it succeeds.

## vSphere CSI driver not supported on ESXi host

This issue occurs when an ESXi host in the vSphere cluster is running a version lower than ESXi 6.7U3.

The output of `gkectl check-config` includes the following warning:
    
    
    The vSphere CSI driver is not supported on current ESXi host versions.
    CSI requires ESXi 6.7U3 or above. See logs for ESXi version details.
    

To resolve this issue, upgrade your ESXi hosts to version 6.7U3 or later.

## CSI volume creation fails with `NotSupported` error

This issue occurs when an ESXi host in the vSphere cluster is running a version lower than ESXi 6.7U3.

The output of `kubectl describe pvc` includes the following error:
    
    
    Failed to provision volume with StorageClass <standard-rwo>: rpc error:
    code = Internal desc = Failed to create volume. Error: CnsFault error:
    CNS: Failed to create disk.:Fault cause: vmodl.fault.NotSupported
    

To resolve this issue, upgrade your ESXi hosts to version 6.7U3 or later.

## vSphere CSI volume fails to attach

This [Kubernetes known issue](https://github.com/kubernetes-sigs/vsphere-csi-driver/issues/526) in the open source vSphere CSI driver occurs when a node is shut down, deleted, or fails.

The output of `kubectl describe pod` looks like the following:
    
    
    Events:
     Type    Reason                 From                     Message
     ----    ------             ... ----                     -------
     Warning FailedAttachVolume ... attachdetach-controller  Multi-Attach error for volume
                                                             "pvc-xxxxx"
                                                             Volume is already exclusively attached to one
                                                             node and can't be attached to another
    

To resolve this issue, complete the following steps:

  1. Note the name of the PersistentVolumeClaim (PVC) in the preceding output, and find the VolumeAttachments that are associated with the PVC:
         
         kubectl get volumeattachments | grep pvc-xxxxx
         

The following example output shows the names of the VolumeAttachments:
         
         csi-yyyyy   csi.vsphere.vmware.com   pvc-xxxxx   node-zzzzz ...
         

  2. Describe the VolumeAttachments:
         
         kubectl describe volumeattachments csi-yyyyy | grep "Deletion Timestamp"
         

Make a note of the deletion timestamp, like in the following example output:
         
         Deletion Timestamp:   2021-03-10T22:14:58Z
         

  3. Wait until the time specified by the deletion timestamp, and then force delete the VolumeAttachment. To do this, edit the VolumeAttachment object and delete the finalizer.
         
         kubectl edit volumeattachment csi-yyyyy
         

Delete the finalizer:
         
         [...]
           Finalizers:
            external-attacher/csi-vsphere-vmware-com
         




## vSphere CSI VolumeSnapshot not ready because of version

This issue occurs when the version of vCenter Server or ESXi host lower than 7.0 Update 3.

The output of `kubectl describe volumesnapshot` includes errors like the following example:
    
    
    rpc error: code = Unimplemented desc = VC version does not support snapshot operations.
    

To resolve this issue, upgrade vCenter Server and the ESXi hosts to version 7.0 Update 3 or later.

## vSphere CSI VolumeSnapshot not ready, maximum snapshots per volume

This issue occurs when the number of snapshots per volume reaches the maximum value for the vSphere Container Storage driver. The default value is three.

The output of `kubectl describe volumesnapshot` includes the errors like the following example:
    
    
    rpc error: code = FailedPrecondition desc = the number of snapshots on the source volume 5394aac1-bc0a-44e2-a519-1a46b187af7b reaches the configured maximum (3)
    

To resolve this issue, use the following steps to update the maximum number of snapshots per volume:

  1. Get the name of the Secret that supplies the vSphere configuration to the vSphere CSI controller:
         
         kubectl --kubeconfig <var class="edit">ADMIN_CLUSTER_KUBECONFIG</var> get deployment vsphere-csi-controller \
             --namespace <var class="edit">USER_CLUSTER_NAME</var> \
             --output json \
             | jq -r '.spec.template.spec.volumes[] \
             | select(.name=="vsphere-secret") .secret.secretName'
         

Replace the following:

     * ADMIN_KUBECONFIG: the path of your admin cluster kubeconfig file
     * USER_CLUSTER_NAME: the name of your user cluster
  2. Get the value of `data.config` from the Secret, base64 decode it, and save it in a file named `config.txt`:
         
         kubectl --kubeconfig <var class="edit">ADMIN_CLUSTER_KUBECONFIG</var> get secret <var class="edit">SECRET_NAME</var> \
             --namespace <var class="edit">USER_CLUSTER_NAME </var> \
             --output json | jq -r '.data["config"]' | base64 -d > config.txt
         

Replace  SECRET_NAME with the name of the Secret from the previous step.

  3. Open `config.txt` for editing:

Edit or add the `global-max-snapshots-per-block-volume` field in the `[Snapshot]` section, like the following example:
         
         [Global]
         cluster-id = "my-user-cluster"
         insecure-flag = "0"
         user = "my-account.local"
         password = "fxqSD@SZTUIsG"
         [VirtualCenter "my-vCenter"]
         port = "443"
         datacenters = "my-datacenter1"
         [Snapshot]
         global-max-snapshots-per-block-volume = 4
         

  4. Delete and re-create the Secret:
         
         kubectl --kubeconfig <var class="edit">ADMIN_CLUSTER_KUBECONFIG</var> delete secret <var class="edit">SECRET_NAME</var> \
             --namespace <var class="edit">USER_CLUSTER_NAME</var>
         
         kubectl --kubeconfig <var class="edit">ADMIN_CLUSTER_KUBECONFIG</var> create secret generic <var class="edit">SECRET_NAME</var> \
             --namespace <var class="edit">USER_CLUSTER_NAME</var> \
             --from-file=config
         

  5. Restart the `vsphere-csi-controller` Deployment:
         
         kubectl --kubeconfig <var class="edit">ADMIN_CLUSTER_KUBECONFIG</var> rollout restart deployment vsphere-csi-controller \
             --namespace <var class="edit">USER_CLUSTER_NAME</var>
         




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
