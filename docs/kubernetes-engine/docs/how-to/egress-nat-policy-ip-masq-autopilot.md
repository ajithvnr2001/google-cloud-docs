---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot/
title: Use Egress NAT Policy to configure IP masquerade in Autopilot clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:02.167372+00:00
---

# Use Egress NAT Policy to configure IP masquerade in Autopilot clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Use Egress NAT Policy to configure IP masquerade in Autopilot clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page explains how to configure clusters created in the Google Kubernetes Engine (GKE) Autopilot mode to perform [IP masquerade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent) with the Egress NAT Policy.

For more information about IP masquerading in GKE Standard mode, see [Configure an IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

## Overview

The GKE _Egress NAT policy_ lets you configure the IP masquerade behavior for Autopilot clusters.

GKE supports two automatically generated Egress NAT policies:

  * Managed by GKE that are fixed and are not editable.
  * Default policies that are editable.



This page shows you how to edit and deploy an Egress NAT policy by either editing the default policy or by creating an Egress NAT policy. This page also shows you how to delete a created Egress NAT policy.

For more information about Egress NAT policy behavior, see the [traffic masquerade behavior for Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#egress-nat-policy).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an Autopilot cluster running version 1.23.4-gke.1600 or later, or 1.22.7-gke.1500 or later. Your cluster must have [GKE Dataplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2#create-cluster).

  * Ensure that your cluster has a workload running. For more information, see [how to request resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#how-to-request).


**Note:** The Egress NAT policy is automatically enabled on Autopilot clusters.

## Check Egress NAT policy status

You can check if your cluster is running the Egress NAT policy custom resource definition (CRD) by using the Google Cloud CLI tool:

  1. Get the credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER-NAME
         

Replace `CLUSTER_NAME` with the name of the cluster.

  2. Check if the Egress NAT policy is running:
         
         kubectl get crds egressnatpolicies.networking.gke.io
         

**Note:** If the command returns an error indicating that the `egressnatpolicies.networking.gke.io` custom resource definition is not found, this indicates the Egress NAT policy is not active on your cluster. This situation is expected if your cluster does not meet all prerequisites. Review the Before you begin section and ensure your cluster meets all specified requirements, including a running workload. The Egress NAT policy is automatically enabled on eligible clusters.

If the Egress NAT policy is running, then the output is similar to the following:
         
         NAME                                  CREATED AT
          egressnatpolicies.networking.gke.io   2022-03-16T21:05:43Z
         

  3. Get the list of the created Egress NAT policies:
         
         kubectl get egressnatpolicies
         

The output is similar to the following:
         
         NAME             AGE
           default          44h
           gke-bbfa6c0e-1   44h
         




## Edit the existing default policy

GKE supports two automatically generated NAT policies, [default policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-policy) and [managed by GKE policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#managed-by-gke-policy). The default policy is editable and it configures the [default non-masquerade destinations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-non-masq-dests).

To edit the existing default policy, perform the following steps:

  1. Get the credentials for your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of your cluster.

  2. Edit the default Egress NAT policy:
         
         kubectl edit egressnatpolicies default
         

  3. Add or remove destinations with the NoSNAT action as a `cidr` attribute in [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing):
         
         apiVersion: networking.gke.io/v1
           kind: EgressNATPolicy
           metadata:
             name: default
           spec:
             action: NoSNAT
             destinations:
             - cidr:  10.0.0.0/8
             - cidr:  172.16.0.0/12
             - cidr:  192.168.0.0/16
             - cidr:  240.0.0.0/4
             - cidr:  192.0.2.0/24
             - cidr:  198.51.100.0/24
             - cidr:  203.0.113.0/24
             - cidr:  100.64.0.0/10
             - cidr:  198.18.0.0/15
             - cidr:  192.0.0.0/24
             - cidr:  192.88.99.0/24
         

When packets are sent to these destinations, your cluster does not masquerade IP address sources and preserves source Pod IP addresses.

  4. Verify the edited default policy is deployed by checking the Kubernetes events:
         
         kubectl get events
         

The output is similar to the following:
         
         LAST SEEN   TYPE     REASON           OBJECT                    MESSAGE
         13s         Normal   EnsuringPolicy   egressnatpolicy/default   Ensuring IP masquerade config for policy "default"
         

Your changes might take up to three minutes to apply.




## Deploy a new Egress NAT policy

To add new destinations with the NoSNAT action, you can use one of the following options:

  * You can edit the existing default policy.
  * You can create a new Egress NAT policy.



To create a new Egress NAT policy that is not part of the default policy, perform the following steps:

  1. Save the following manifest as `egress_nat_policy.yaml`:
         
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: POLICY_NAME
         spec:
           action: NoSNAT
           destinations:
           - cidr: CIDR_1
           - cidr: CIDR_2
         

Replace the following:

     * `POLICY_NAME`: the name of your new policy.
     * `CIDR_1` and `CIDR_2`: the IP address ranges in [CIDR format](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). When packets are sent to these destinations, your cluster does not masquerade IP address sources and preserves source Pod IP addresses. If you need more than two CIDRs, add more entries to the `destinations` list following the same format.
  2. Deploy the new policy:
         
         kubectl create -f egress_nat_policy.yaml
         

  3. Verify your policy is deployed by checking the Kubernetes events:
         
         kubectl get events
         

The output is similar to the following:
         
         LAST SEEN   TYPE     REASON           OBJECT                              MESSAGE
         13s         Normal   EnsuringPolicy   egressnatpolicy/mypolicy            Ensuring IP masquerade config for policy "mypolicy"
         




## Delete an Egress NAT policy

To completely delete an Egress NAT policy, run the following command:
    
    
    kubectl delete egressnatpolicies POLICY_NAME
    

Replace `POLICY_NAME` with the name the policy you want to delete.

**Note:** We recommend that you don't delete the default Egress NAT policy because it contains the default ranges of CIDR that might be required for the cluster to preserve its operation. For more information about default the Egress NAT policy, see [Egress NAT automatically generated policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#automatically_generated_policies)

## What's next

  * [Learn how to create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * [Learn about configuring authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
