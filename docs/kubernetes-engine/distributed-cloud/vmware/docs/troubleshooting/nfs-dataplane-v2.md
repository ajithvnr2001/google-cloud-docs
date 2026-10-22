---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/nfs-dataplane-v2/
title: Troubleshoot Google Distributed Cloud NFS and DataPlane v2 issues \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:22.437682+00:00
---

# Troubleshoot Google Distributed Cloud NFS and DataPlane v2 issues  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/nfs-dataplane-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot Google Distributed Cloud NFS and DataPlane v2 issues Stay organized with collections  Save and categorize content based on your preferences. 

This document details a manual procedure for Google Distributed Cloud if you have issues with NFS mounts with a stuck volume or Pod and you created your cluster with DataPlane v2 enabled.

This issue has been fixed for the following versions:

  * For minor version 1.16, version 1.16.4-gke.37 and higher.
  * For minor version 1.28, version 1.28.200-gke.111 and higher.



We recommend that you [upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrade-overview) to a version where this issue is fixed. If you're unable to upgrade, use the procedures outlined in the following sections.

If you're using a version where this issue isn't fixed, you might encounter issues if you have workloads using `ReadWriteMany` volumes powered by storage drivers that are susceptible to this issue, such as (but not limited to):

  * Robin.io
  * Portworx (`sharedv4` service volumes)
  * `csi-nfs`



NFS mounts on some storage architectures might become stuck when they're connected to an endpoint using a Kubernetes Service (ClusterIP) and DataPlane v2. This behavior is because of the limitations in how Linux kernel socket code interacts with Cillium's eBPF program. Containers might become blocked on I/O or even be unkillable, as the defunct NFS mount can't be unmounted.

You might experience this issue if you use `RWX` storage hosted on NFS servers that run on a Kubernetes node, including software-defined or hyperconverged storage solutions like as Ondat, Robin.io, or Portworx.

## Review existing cluster configuration

Get some existing configuration values from your cluster. You use the values from these steps to create a `kube-proxy` manifest in the next section.

  1. Get the `ClusterCIDR` from `cm/cilium-config`:
         
         kubectl get cm -n kube-system cilium-config -o yaml | grep native-routing-cidr
         

The following example output shows that you would use `192.168.0.0/16` as the `ClusterCIDR`:
         
         ipv4-native-routing-cidr: 192.168.0.0/16
         native-routing-cidr: 192.168.0.0/16
         

  2. Get the `APIServerAdvertiseAddress` and `APIServerPort` from the `anetd` DaemonSet:
         
         kubectl get ds -n kube-system  anetd -o yaml | grep KUBERNETES -A 1
         

The following example output show that you would use `21.1.4.119` as the `APIServerAdvertiseAddress` and `443` as the `APIServerPort`:
         
         - name: KUBERNETES_SERVICE_HOST
           value: 21.1.4.119
         - name: KUBERNETES_SERVICE_PORT
           value: "443"
         

  3. Get the `RegistryCredentialsSecretName` from the `anetd` DaemonSet:
         
         kubectl get ds -n kube-system  anetd -o yaml | grep imagePullSecrets -A 1
         

The following example output shows that you would use `private-registry-creds` as the `RegistryCredentialsSecretName`:
         
         imagePullSecrets:
           - name: private-registry-creds
         

  4. Get the `Registry` from the `anetd` DameonSet:
         
         kubectl get ds -n kube-system  anetd -o yaml | grep image
         

The following example output shows that you would use `gcr.io/gke-on-prem-release` as the `Registry`:
         
         image: gcr.io/gke-on-prem-release/cilium/cilium:v1.12.6-anthos1.15-gke4.2.7
         

  5. Get the `KubernetesVersion` from the image tag for `kube-apiserver` in the cluster namespace of the admin cluster:
         
         KUBECONFIG=ADMIN_KUBECONFIG
         kubectl get sts -n CLUSTER_NAME kube-apiserver -o yaml | grep image
         

Replace `ADMIN_KUBECONFIG` with the kubeconfig file for your admin cluster and `CLUSTER_NAME` with the name of your user cluster.

The following example output shows that you would use `v1.26.2-gke.1001` as the `KubernetesVersion`:
         
         image: gcr.io/gke-on-prem-release/kube-apiserver-amd64:v1.26.2-gke.1001
         imagePullPolicy: IfNotPresent
         




## Prepare `kube-proxy` manifests

Use the values obtained in the previous section to create and apply a YAML manifest that will deploy `kube-proxy` to your cluster.

  1. Create a manifest named `kube-proxy.yaml` in the editor of your choice:
         
         nano kube-proxy.yaml
         

  2. Copy and paste the following YAML definition:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           labels:
             k8s-app: kube-proxy
           name: kube-proxy
           namespace: kube-system
         spec:
           selector:
             matchLabels:
               k8s-app: kube-proxy
           template:
             metadata:
               annotations:
                 scheduler.alpha.kubernetes.io/critical-pod: ""
               labels:
                 k8s-app: kube-proxy
             spec:
               containers:
               - command:
                 - kube-proxy
                 - --v=2
                 - --profiling=false
                 - --iptables-min-sync-period=10s
                 - --iptables-sync-period=1m
                 - --oom-score-adj=-998
                 - --ipvs-sync-period=1m
                 - --ipvs-min-sync-period=10s
                 - --cluster-cidr=ClusterCIDR
                 env:
                 - name: KUBERNETES_SERVICE_HOST
                   value:APIServerAdvertiseAddress
                 - name: KUBERNETES_SERVICE_PORT
                   value: "APIServerPort"
                 image: Registry/kube-proxy-amd64:KubernetesVersion
                 imagePullPolicy: IfNotPresent
                 name: kube-proxy
                 resources:
                   requests:
                     cpu: 100m
                     memory: 15Mi
                 securityContext:
                   privileged: true
                 volumeMounts:
                 - mountPath: /run/xtables.lock
                   name: xtables-lock
                 - mountPath: /lib/modules
                   name: lib-modules
               imagePullSecrets:
               - name: RegistryCredentialsSecretName
               nodeSelector:
                 kubernetes.io/os: linux
               hostNetwork: true
               priorityClassName: system-node-critical
               serviceAccount: kube-proxy
               serviceAccountName: kube-proxy
               tolerations:
               - effect: NoExecute
                 operator: Exists
               - effect: NoSchedule
                 operator: Exists
               volumes:
               - hostPath:
                   path: /run/xtables.lock
                   type: FileOrCreate
                 name: xtables-lock
               - hostPath:
                   path: /lib/modules
                   type: DirectoryOrCreate
                 name: lib-modules
           ---
           apiVersion: rbac.authorization.k8s.io/v1
           kind: ClusterRoleBinding
           metadata:
             name: system:kube-proxy
           roleRef:
             apiGroup: rbac.authorization.k8s.io
             kind: ClusterRole
             name: system:node-proxier
           subjects:
             - kind: ServiceAccount
               name: kube-proxy
               namespace: kube-system
           ---
           apiVersion: v1
           kind: ServiceAccount
           metadata:
             name: kube-proxy
             namespace: kube-system
         

In this YAML manifest, set the following values:

     * `APIServerAdvertiseAddress`: the value of `KUBERNETES_SERVICE_HOST`, such as `21.1.4.119`.
     * `APIServerPort`: the value of `KUBERNETES_SERVICE_PORT`, such as `443`.
     * `Registry`: the prefix of the Cilium image, such as `gcr.io/gke-on-prem-release`.
     * `RegistryCredentialsSecretName`: the image pull secret name, such as `private-registry-creds`.
  3. Save and close the manifest file in your editor.




## Prepare `anetd` patch

Create and prepare an update for `anetd`:

  1. Create a manifest named `cilium-config-patch.yaml` in the editor of your choice:
         
         nano cilium-config-patch.yaml
         

  2. Copy and paste the following YAML definition:
         
         data:
           kube-proxy-replacement: "disabled"
           kube-proxy-replacement-healthz-bind-address: ""
           retry-kube-proxy-healthz-binding: "false"
           enable-host-reachable-services: "false"
         

  3. Save and close the manifest file in your editor.




## Deploy `kube-proxy` and reconfigure `anetd`

Apply your configuration changes to your cluster. Create backups of your existing configuration before you apply the changes.

  1. Back up your current `anetd` and `cilium-config` configuration:
         
         kubectl get ds -n kube-system anetd > anetd-original.yaml
         kubectl get cm -n kube-system cilium-config > cilium-config-original.yaml
         

  2. Apply `kube-proxy.yaml` using `kubectl`:
         
         kubectl apply -f kube-proxy.yaml
         

  3. Check that the Pods are `Running`:
         
         kubectl get pods -n kube-system -o wide | grep kube-proxy
         

The following example condensed output shows that the Pods are running correctly:
         
         kube-proxy-f8mp9    1/1    Running   1 (4m ago)    [...]
         kube-proxy-kndhv    1/1    Running   1 (5m ago)    [...]
         kube-proxy-sjnwl    1/1    Running   1 (4m ago)    [...]
         

  4. Patch the `cilium-config` ConfigMap using `kubectl`:
         
         kubectl patch cm -n kube-system cilium-config --patch-file cilium-config-patch.yaml
         

  5. Edit `anetd` using `kubectl`:
         
         kubectl edit ds -n kube-system anetd
         

In the editor that opens up, edit the spec of `anetd`. Insert the following as the first item under `initContainers`:
         
         - name: check-kube-proxy-rules
           image: Image
           imagePullPolicy: IfNotPresent
           command:
           - sh
           - -ec
           - |
             if [ "$KUBE_PROXY_REPLACEMENT" != "strict" ]; then
               kube_proxy_forward() { iptables -L KUBE-FORWARD; }
               until kube_proxy_forward; do sleep 2; done
             fi;
           env:
           - name: KUBE_PROXY_REPLACEMENT
             valueFrom:
               configMapKeyRef:
                 key: kube-proxy-replacement
                 name: cilium-config
                 optional: true
           securityContext:
             privileged: true
         

Replace `Image` with the same image used in the other Cilium containers in the `anetd` DaemonSet, such as `gcr.io/gke-on-prem-release/cilium/cilium:v1.12.6-anthos1.15-gke4.2.7`.

  6. Save and close the manifest file in your editor.

  7. To apply these changes, reboot of all nodes in your cluster. To minimize disruption, you can attempt to drain each node prior to the reboot. However, Pods using RWX volumes may be stuck in a `Terminating` state due to broken NFS mounts that block the drain process.

You can force delete blocked Pods and allow the Node to correctly drain:
         
         kubectl delete pods -–force -–grace-period=0 --namespace POD_NAMESPACE POD_NAME
         

Replace `POD_NAME` with the Pod you are trying to delete and `POD_NAMESPACE` with its namespace.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
