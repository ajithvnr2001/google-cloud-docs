---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/standard-cluster-traffic/
title: Create Kubernetes network policies for standard clusters \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:48.553842+00:00
---

# Create Kubernetes network policies for standard clusters  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/k8s-network-policy/standard-cluster-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create Kubernetes network policies for standard clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure intra-cluster traffic for a standard cluster using Kubernetes network policies in Google Distributed Cloud (GDC) air-gapped.

A Kubernetes `NetworkPolicy` is a specification of how groups of pods are allowed to communicate with each other and other network endpoints. `NetworkPolicy` resources use labels to select pods, and define rules which specify what traffic is allowed to the selected pods. These policies are scoped locally and apply only to traffic within the cluster where they are defined, unless an allow-all policy is created, which also allows communication with endpoints from other standard and shared clusters.

## Before you begin

To configure Kubernetes network policies, you must have the necessary permissions within the cluster to create, modify, and delete `NetworkPolicy` resources in the relevant namespaces.

## Create an intra-cluster pod-to-pod policy

These policies control traffic between pods within the same standard cluster.

### Create an intra-cluster pod-to-pod ingress policy

  * To allow intra-cluster pod-to-pod ingress traffic, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-intra-cluster-ingress-traffic
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Ingress
          ingress:
          - from:
            - namespaceSelector:
                matchLabels:
                  Kubernetes.io/metadata.name: PEER_NAMESPACE
              podSelector:
                matchLabels:
                  PEER_LABEL_KEY: PEER_LABEL_VALUE
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
    * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads.
    * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
    * `PORT`: the port on the subject workload where traffic is allowed.



### Create an intra-cluster pod-to-pod egress policy

  * To allow intra-cluster pod-to-pod egress traffic, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-egress-intra-cluster-traffic
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Egress
          egress:
          - to:
            - namespaceSelector:
                matchLabels:
                  Kubernetes.io/metadata.name: PEER_NAMESPACE
              podSelector:
                matchLabels:
                  PEER_LABEL_KEY: PEER_LABEL_VALUE
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
    * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads.
    * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
    * `PORT`: the port on the peer workload where traffic is allowed.



## Create an intra-cluster pod-to-pod policy using a load balancer

These policies control traffic between pods within the same cluster when traffic is routed through an external load balancer.

### Create an intra-cluster pod-to-pod ingress policy using a load balancer

  * To allow intra-cluster pod-to-pod ingress traffic using a load balancer, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-intra-cluster-ingress-traffic-via-elb
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Ingress
          ingress:
          - from:
            - ipBlock:
                cidr: EGRESS_NAT_IP/32
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
    * `EGRESS_NAT_IP`: the egress NAT IP of the source pod.
    * `PORT`: the port on the subject workload where traffic is allowed.



### Create an intra-cluster pod-to-pod egress policy using a load balancer

  * To allow intra-cluster pod-to-pod egress traffic using a load balancer, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-intra-cluster-egress-traffic-via-elb
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Egress
          egress:
          - to:
            - ipBlock:
                cidr: ELB_EXTERNAL_IP/32
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
    * `ELB_EXTERNAL_IP`: the external IP address of the load balancer.
    * `PORT`: the port on the external endpoint to which traffic is allowed.



## Create an intra-cluster node policy

Intra-cluster node policies control ingress and egress traffic between pods and specific nodes within the same standard cluster, such as control plane (API server) nodes or worker nodes.

You can use the `ipBlock` field in a `NetworkPolicy` resource to specify individual node IP addresses or node CIDR ranges ([Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview)).

### Create an ingress policy from cluster nodes to a pod

You can create an ingress policy to allow traffic from specific cluster nodes to a pod. For example, you can allow control plane (API server) nodes to reach a pod running a custom Kubernetes admission webhook.

  * To allow ingress traffic from cluster nodes to a pod, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-ingress-from-node-to-pod
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Ingress
          ingress:
          - from:
            - ipBlock:
                cidr: NODE_IP_CIDR
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `webhook`, then workloads with the label `app: webhook` receive the traffic.
    * `NODE_IP_CIDR`: the IP address or CIDR range of the source cluster node or nodes, such as a control plane node IP in `/32` notation (for example, `10.200.0.10/32`). To list control plane node IP addresses, run `kubectl --kubeconfig CLUSTER_API_SERVER get nodes -l node-role.kubernetes.io/control-plane -o wide`.
    * `PORT`: the port on the subject workload where traffic is allowed (for example, `8443` or `443`).



### Create an egress policy from a pod to cluster nodes

You can create an egress policy to allow a pod to communicate with specific cluster nodes. For example, you can allow egress traffic from a pod to control plane (API server) nodes while default-deny rules block egress traffic to worker nodes.

**Note:** To enforce default-deny egress to worker nodes, you must also disable [data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration) for the project. While data exfiltration protection is enabled, a predefined base egress policy permits pod egress to all cluster nodes.

  * To allow egress traffic from a pod to specific cluster nodes, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-egress-from-pod-to-node
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Egress
          egress:
          - to:
            - ipBlock:
                cidr: NODE_IP_CIDR
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `controller`, then workloads with the label `app: controller` send the traffic.
    * `NODE_IP_CIDR`: the IP address or CIDR range of the destination cluster node or nodes, such as a control plane node IP in `/32` notation (for example, `10.200.0.10/32`). To list control plane node IP addresses, run `kubectl --kubeconfig CLUSTER_API_SERVER get nodes -l node-role.kubernetes.io/control-plane -o wide`.
    * `PORT`: the port on the destination node to which traffic is allowed (for example, `6444` or `443`).



### Scale considerations

When configuring Kubernetes network policies to target specific nodes or using broad CIDR ranges, your policy configuration choices might affect scalability and performance:

  * **Behavior of`0.0.0.0/0`**: Using a broad CIDR range such as `0.0.0.0/0` in an `ipBlock` rule matches all nodes in the cluster, in addition to external IP addresses.
  * **Scale** : Each node in the cluster has a unique CIDR identity, and each pod endpoint has an internal policy table that stores its network rules. In large clusters, broad `ipBlock` rules such as `0.0.0.0/0` increase policy table usage in proportion to the number of nodes because the system must create entries for every unique node CIDR identity.
  * **Warning** : Avoid using overly broad CIDR ranges in `ipBlock` rules if your cluster has a high node count or many complex policies, because you risk hitting the policy table limit for an endpoint. If an endpoint exceeds this limit, new network policies fail to apply, which can disrupt network connectivity or prevent policy enforcement for that pod.



## Create an organization-external policy

These policies control traffic between a pod in a standard cluster and an external endpoint (any IP address outside the cluster).

**Caution:** Using a broad CIDR range such as `0.0.0.0/0` in an `ipBlock` rule matches all nodes in the cluster, in addition to external IP addresses. In large clusters, this can cause endpoints to hit policy table limits. For more information, see Scale considerations.

### Create an ingress policy for organization-external traffic

  * To allow ingress traffic from an organization-external endpoint, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-ingress-from-organization-external-to-standard-cluster-pod
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Ingress
          ingress:
          - from:
            - ipBlock:
                cidr: EXTERNAL_CIDR
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
    * `EXTERNAL_CIDR`: the external CIDR, for example: `20.0.0.0/16`.
    * `PORT`: the port on the subject workload where traffic is allowed.



### Create an egress policy for organization-external traffic

  * To allow egress traffic to an organization-external endpoint, create and apply the following resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-egress-from-standard-cluster-pod-to-organization-external
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector:
            matchLabels:
              SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          policyTypes:
          - Egress
          egress:
          - to:
            - ipBlock:
                cidr: EXTERNAL_CIDR
            ports:
            - protocol: TCP
              port: PORT
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
    * `EXTERNAL_CIDR`: the external CIDR, for example: `20.0.0.0/16`.
    * `PORT`: the port on the external endpoint to which traffic is allowed.



## Create an allow-all policy

The following policies can be used to explicitly allow all traffic. This allows communication with endpoints from other standard and shared clusters.

### Create an ingress allow-all policy

  * To allow all incoming traffic, create and apply the following the resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-all-ingress-traffic
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector: {}
          policyTypes:
          - Ingress
          ingress:
          - {}
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.



### Create an egress allow-all policy

  * To allow all outgoing traffic, create and apply the following the resource:
        
        kubectl --kubeconfig CLUSTER_API_SERVER apply -f - <<EOF
        apiVersion: networking.k8s.io/v1
        kind: NetworkPolicy
        metadata:
          name: allow-all-egress-traffic
          namespace: SUBJECT_NAMESPACE
        spec:
          podSelector: {}
          policyTypes:
          - Egress
          egress:
          - {}
        EOF
        

Replace the following:

    * `CLUSTER_API_SERVER`: the cluster API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
