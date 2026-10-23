---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent/
title: Configuring an IP masquerade agent in Standard clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:17.860893+00:00
---

# Configuring an IP masquerade agent in Standard clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configuring an IP masquerade agent in Standard clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to configure clusters created in Google Kubernetes Engine (GKE) Standard mode to perform [IP masquerade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) with the `ip-masq-agent`. For more information about IP masquerading in GKE [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), see [Use Egress NAT Policy to configure IP masquerade in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster. If you need one, [create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).



## Checking `ip-masq-agent` status

This section shows you how to:

  * Determine whether your cluster has an `ip-masq-agent` DaemonSet.
  * Check the `ip-masq-agent` [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) resource.



### Check the `ip-masq-agent` DaemonSet

To check if your cluster is running the `ip-masq-agent` DaemonSet, use the Google Cloud CLI or the Google Cloud console.

### gcloud

  1. Get the credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your cluster.

  2. Search for the `ip-masq-agent` in the `kube-system` namespace:
         
         kubectl get daemonsets/ip-masq-agent -n kube-system
         

If the `ip-masq-agent` DaemonSet exists, then the output is similar to the following:
         
         NAME            DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
         ip-masq-agent   3         3         3       3            3           <none>          13d
         

If the `ip-masq-agent` DaemonSet does not exist, then the output is similar to the following:
         
         Error from server (NotFound): daemonsets.apps "ip-masq-agent" not found
         

  3. Check if the `ip-masq-agent` DaemonSet is running the latest version:
         
         kubectl get daemonsets/ip-masq-agent -n kube-system -o jsonpath='{.spec.template.spec.containers[].image}'
         

This command must return the same container image as specified in Deploying the ip-masq-agent DaemonSet.




### Console

  1. Go to the **Workloads** page in the Google Cloud console.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. For filter_list _Filter_ , do the following:

     1. Click cancel to clear the **Is system object: False** filter.
     2. Filter the following properties: 
        * **Name** : `ip-masq-agent`.
        * **Cluster** : the name of your cluster.

If `ip-masq-agent` DaemonSet exists, then you can see the DaemonSet record in the table. If `ip-masq-agent` DaemonSet does not exist, then no rows are displayed.




To create the `ip-masq-agent` ConfigMap and deploy the `ip-masq-agent` DaemonSet, refer to Configuring and deploying the `ip-masq-agent`.

### Checking the `ip-masq-agent` ConfigMap

To check if your cluster is running the `ip-masq-agent` ConfigMap, use the Google Cloud CLI or the Google Cloud console.

### gcloud

  1. Get the credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your cluster.

  2. Describe the `ip-masq-agent` ConfigMap in the `kube-system` namespace:
         
         kubectl describe configmaps/ip-masq-agent -n kube-system
         

If the `ip-masq-agent` ConfigMap exists, then the output is similar to the following:
         
         Name:         ip-masq-agent
         Namespace:    kube-system
         Labels:       <none>
         Annotations:  <none>
         
         Data
         ====
         config:
         ----
         nonMasqueradeCIDRs:
           - 198.15.5.92/24
           - 10.0.0.0/8
         masqLinkLocal: false
         resyncInterval: 60s
         
         BinaryData
         ====
         
         Events:  <none>
         

If the `ip-masq-agent` ConfigMap does not exist, then the output is similar to the following:
         
         Error from server (NotFound): configmaps "ip-masq-agent" not found
         




### Console

  1. Go to the **Configuration** page in the Google Cloud console.

[Go to Configuration](https://console.cloud.google.com/kubernetes/config)

  2. For filter_list _Filter_ , do the following:

     1. Click cancel to clear the **Is system object: False** filter.
     2. Filter the following properties: 
        * **Name** : `ip-masq-agent`.
        * **Cluster** : the name of your cluster.

If `ip-masq-agent` ConfigMap exists, then you can see the ConfigMap record in the table. If `ip-masq-agent` ConfigMap does not exist, then no rows are displayed.




If the cluster already has the `ip-masq-agent` ConfigMap, you can configure and deploy it.

## Configuring and deploying the `ip-masq-agent`

This section shows you how to create or edit the `ip-masq-agent` ConfigMap and how to deploy or delete the `ip-masq-agent` DaemonSet. To determine which tasks you need to perform, you must first determine whether your cluster already has the `ip-masq-agent` ConfigMap and `ip-masq-agent` DaemonSet.

### Creating the `ip-masq-agent` ConfigMap

The following steps show how to create the `ip-masq-agent` ConfigMap. If your cluster already has the `ip-masq-agent` ConfigMap, edit an existing ip-masq-agent ConfigMap instead.

  1. Create a configuration file using the following template and save it locally. You can use any name for the local copy of this configuration file.
         
         nonMasqueradeCIDRs:
           - CIDR_1
           - CIDR_2
         masqLinkLocal: false
         resyncInterval: SYNC_INTERVALUNIT_OF_TIME
         

Replace the following:

     * `CIDR_1` and `CIDR_2`: the IP address ranges in [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). When packets are sent to these destinations, your cluster does not masquerade IP address sources and preserves source Pod IP addresses. If you need more than two CIDRs, add more entries to the `nonMasqueradeCIDRs` list following the same format. At minimum, the `nonMasqueradeCIDRs` property should include the node and Pod IP address ranges of your cluster.

     * `SYNC_INTERVAL`: the amount of time after which each `ip-masq-agent` Pod checks the contents of the `ip-masq-agent` ConfigMap and writes any changes to its local `/etc/config/ip-masq-agent` file. Defaults to `60`.

     * `UNIT_OF_TIME`: the unit of time for the resyncInterval. Valid values include `s` (for seconds) or `ms` (for milliseconds). Defaults to `s`.

Set `masqLinkLocal` to false (the default) unless you need to enable masquerading for packets sent to link local IPv4 addresses. For more information, see [Masquerading to link-local destinations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#masqLinkLocal).

**Caution:** A custom `nonMasqueradeCIDRs` must at least include the cluster's node and Pod IP address range(s). This is especially important if you enable [intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility). If the Pod IP address range(s) are not present in `nonMasqueradeCIDRs` and you have intranode visibility turned on, Pods won't be able to properly communicate with each other.
  2. Create the ConfigMap resource:
         
         kubectl create configmap ip-masq-agent \
            --namespace=kube-system \
            --from-file=config=LOCAL_CONFIG_FILE_PATH
         

Replace `LOCAL_CONFIG_FILE_PATH` with the path to the config file you created in the previous step.

**Note:** The ConfigMap content must be associated with a named key that the `ip-masq-agent` DaemonSet expects when reading the `ip-masq-agent` ConfigMap to parse it as a volume. In the following example, and for standard `ip-masq-agent` DaemonSets, the key is `config`. Specifying the `--from-file=config=LOCAL_CONFIG_FILE_PATH` flag helps ensure that the IP masquerade configuration information is associated with the `config` key.
  3. Describe the `ip-masq-agent` ConfigMap in the `kube-system` namespace:
         
         kubectl describe configmaps/ip-masq-agent -n kube-system
         

The output is similar to the following:
         
         Name:         ip-masq-agent
         Namespace:    kube-system
         Labels:       <none>
         Annotations:  <none>
         
         Data
         ====
         config:
         ----
         nonMasqueradeCIDRs:
           - 198.15.5.92/24
           - 10.0.0.0/8
         masqLinkLocal: false
         resyncInterval: 60s
         
         BinaryData
         ====
         Events:  <none>
         
         

This output includes the `config` parameter with your configuration changes. You can now deploy the `ip-masq-agent` DeamonSet.




### Editing an existing `ip-masq-agent` ConfigMap

You can modify the contents of an existing `ip-masq-agent` ConfigMap by completing the following steps:

  1. Open the ConfigMap in a text editor:
         
         kubectl edit configmap ip-masq-agent --namespace=kube-system
         

  2. Edit the content of the ConfigMap file:
         
         apiVersion: v1
         data:
           config: |
             nonMasqueradeCIDRs:
               - CIDR_1
               - CIDR_2
             masqLinkLocal: false
             resyncInterval: SYNC_INTERVALUNIT_OF_TIME
         kind: ConfigMap
         metadata:
           name: ip-masq-agent
           namespace: kube-system
         

Replace the following:

     * `CIDR_1` and `CIDR_2`: the IP address ranges in [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). When packets are sent to these destinations, your cluster does not masquerade IP address sources and preserves source Pod IP addresses. If you need more than two CIDRs, add more entries to the `nonMasqueradeCIDRs` list following the same format. At minimum, the `nonMasqueradeCIDRs` property should include the node and Pod IP address ranges of your cluster.

     * `SYNC_INTERVAL`: the amount of time after which each `ip-masq-agent` Pod checks the contents of the `ip-masq-agent` ConfigMap and writes any changes to its local `/etc/config/ip-masq-agent` file. Defaults to `60`.

     * `UNIT_OF_TIME`: the unit of time for the resyncInterval. Valid values include `s` (for seconds) or `ms` (for milliseconds). Defaults to `s`.

Set `masqLinkLocal` to false (the default) unless you need to enable masquerading for packets sent to link local IPv4 addresses. For more information, see [Masquerading to link-local destinations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#masqLinkLocal).

**Caution:** A custom `nonMasqueradeCIDRs` must at least include the cluster's node and Pod IP address range(s). This is especially important if you enable [intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility). If the Pod IP address range(s) are not present in `nonMasqueradeCIDRs` and you have intranode visibility turned on, Pods won't be able to properly communicate with each other.
  3. Describe the `ip-masq-agent` ConfigMap in the `kube-system` namespace:
         
         kubectl describe configmaps/ip-masq-agent -n kube-system
         

The output is similar to the following:
         
         Name:         ip-masq-agent
         Namespace:    kube-system
         Labels:       <none>
         Annotations:  <none>
         
         Data
         ====
         config:
         ----
         nonMasqueradeCIDRs:
           - 198.15.5.92/24
           - 10.0.0.0/8
         masqLinkLocal: false
         resyncInterval: 60s
         
         BinaryData
         ====
         
         Events:  <none>
         

This output includes the `config` parameter which matches the configuration value from the file you created.




### Deploying the `ip-masq-agent` DaemonSet

After you create or edit your `ip-masq-agent` ConfigMap, deploy the `ip-masq-agent` DaemonSet.

  1. Save the following manifest as a YAML file:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: ip-masq-agent
           namespace: kube-system
         spec:
           selector:
             matchLabels:
               k8s-app: ip-masq-agent
           template:
             metadata:
               labels:
                 k8s-app: ip-masq-agent
             spec:
               hostNetwork: true
               containers:
               - name: ip-masq-agent
                 image: gke.gcr.io/ip-masq-agent:v2.12.6-gke.15@sha256:c51e89bdc5073fdbaaff8bf42b32765f7f1eb0fec7d6189de5f14c48ac489448
                 args:
                 - --v=2
                 - --logtostderr=false
                 - --log_file=/dev/stdout
                 - --log_file_max_size=0
                 # The masq-chain must be IP-MASQ
                 - --masq-chain=IP-MASQ
                 # To non-masquerade reserved IP ranges by default,
                 # uncomment the following line.
                 # - --nomasq-all-reserved-ranges
                 # Must be set to false when using Dataplane V2.
                 - --random-fully=false
                 securityContext:
                   privileged: false
                   capabilities:
                     drop: ["ALL"]
                     add: ["NET_ADMIN", "NET_RAW"]
                   allowPrivilegeEscalation: false
                   seccompProfile:
                     type: RuntimeDefault
                 volumeMounts:
                 - name: config-volume
                   mountPath: /etc/config
               volumes:
               - name: config-volume
                 configMap:
                   name: ip-masq-agent
                   optional: true
                   items:
                   - key: config
                     path: ip-masq-agent
               tolerations:
               - effect: NoSchedule
                 operator: Exists
               - effect: NoExecute
                 operator: Exists
               - key: "CriticalAddonsOnly"
                 operator: "Exists"

This manifest creates a volume named `config-volume` which is mounted as specified by the container's volumeMount.

If you need to edit this manifest, consider the following conditions:

     * The volume name can be anything but must match the container's `volumeMount` name.

     * The ConfigMap name must match the name of the `configMap` referenced in the `config-volume` Volume in the Pod.

     * The name of the chain (`--masq-chain`) must be `IP-MASQ`. Otherwise, GKE does not override the default masquerading rules.

     * DaemonSet Pods read from the `ip-masq-agent` file. The `ip-masq-agent` file content is the value of the `config` key in the ConfigMap.

     * If you use non-masquerade reserved IP ranges by default, uncomment the `- --nomasq-all-reserved-ranges` line in the `arg` section.

  2. Deploy the DaemonSet:
         
         kubectl apply -f LOCAL_FILE_PATH
         

Replace `LOCAL_FILE_PATH` with the path to the file you created in the previous step.




You can manually update the `ip-masq-agent` DaemonSet you created. To learn more, see [Updating a DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/#updating-a-daemonset).

## Deleting the `ip-masq-agent`

This section shows you how to delete the `ip-masq-agent` DaemonSet and the `ip-masq-agent` ConfigMap. Deleting the `ip-masq-agent` doesn't revert the existing IP masquerading settings on the nodes.

### Deleting the `ip-masq-agent` DaemonSet

If you manually created the `ip-masq-agent` DaemonSet, you can delete it by running the following command:
    
    
    kubectl delete daemonsets ip-masq-agent -n kube-system
    

**Note:** If the `ip-masq-agent` DaemonSet was deployed automatically, GKE will automatically recreate it.

### Deleting the `ip-masq-agent` ConfigMap

To completely delete the `ip-masq-agent` ConfigMap, run the following command:
    
    
    kubectl delete configmap ip-masq-agent -n kube-system
    

## Troubleshooting

The following sections provide troubleshooting advice.

### General troubleshooting

The following steps help you diagnose issues with IP address masquerading:

  * Confirm the status of the `ip-masq-agent`. If the ConfigMap is not defined, traffic to all default destinations is [not masqueraded](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#how_ipmasq_works) and preserves the Pod IP address. Traffic to other destinations preserves the node IP address.
  * Confirm the version of the `ip-masq-agent` image specified in the DaemonSet. If the version of the `ip-masq-agent` DaemonSet is not the latest, follow the deployment steps to update the DaemonSet.
  * Check whether the IP-MASQ chain is correctly populated in the NAT IP tables by running the `sudo iptables -t nat -L IP-MASQ` command in the impacted node. If the `nonMasqueradeCIDRs` defined in the ConfigMap is not showing up on the NAT IP Tables, verify that there are no typos in the config file that was used to create the ConfigMap.
  * Confirm that the destination allows both the node and Pod IP address ranges.
  * If traffic is not accessible from the node or Pod, [run a connectivity test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).



### Issue: Pod IP address changes to node IP address

While using an IP masquerade agent, you might notice the Pod's source IP address unexpectedly use the node's IP address when your Pods communicate with external destinations.

The issue is caused by a missing or incomplete custom Source Network Address Translation (SNAT) list. When you use an IP masquerade agent, the default SNAT of the cluster is used when the ConfigMap is missing or it doesn't contain a `nonMasqueradeCIDRs` list. When a packet leaves a Pod, the default SNAT changes the source IP address from the Pod's IP address to the node's internal IP address. To learn more about SNAT, see [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent).

To resolve the issue, configure a custom SNAT list by defining a `nonMasqueradeCIDRs` list in the `ip-masq-agent` ConfigMap:

  1. Open the `ip-masq-agent` ConfigMap:
         
         kubectl edit configmap ip-masq-agent --namespace=kube-system
         

  2. Review the `nonMasqueradeCIDRs` list within the ConfigMap. The `nonMasqueradeCIDRs` list should be present and complete. For example:
         
         ...
         nonMasqueradeCIDRs:
           - 35.100.0.0/16
         ...
         

  3. If the list is missing or incomplete, add or modify the `nonMasqueradeCIDRs` list to include the destination IP ranges for which you want to preserve source Pod IP addresses. This list should also include the addresses that you want to use Cloud NAT.

If you don't want any external traffic to use SNAT, set the `nonMasqueradeCIDRs` field to `0.0.0.0/0`. For example:
         
         ...
         nonMasqueradeCIDRs:
           - 0.0.0.0/0
         ...
         

When your traffic doesn't use SNAT, all packets sent from Pods retain the Pod's IP address as their source IP address, regardless of destination.

  4. Check the source IP address of outbound packets from your Pods. To check this address, take a packet capture. If that's not feasible, you can check the IP address of the node, which should be the source IP address of outbound packets subject to SNAT, with the following command:
         
         kubectl get nodes -o wide
         




## What's next

  * Learn how to [use Egress NAT Policy to configure IP masquerade in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot).
  * Learn how to [create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * Read the [GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * Learn about [configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
