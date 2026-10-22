---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic/
title: Create intra-project network policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:27.462016+00:00
---

# Create intra-project network policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create intra-project network policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure intra-project traffic network policies in Google Distributed Cloud (GDC) air-gapped.

Project network policies define either ingress or egress rules. You can define policies that allow communication within projects, between projects, and to external IP addresses.

By default, these policies apply globally across all zones. For more information on global resources in a GDC universe, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

If intra-project traffic enforcement is needed within a single zone, see [Create a single zone workload-level intra-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#single-zone-workload-level-intra-project).

## Before you begin

To configure intra-project traffic network policies, you must have the following:

  * The necessary identity and access roles. To manage traffic network policies, you need the **Project Network Policy Admin** (`global-project-networkpolicy-admin`) role. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * For egress network policies, you must also disable [data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration) for the project.



## Create an intra-project policy

For traffic within a project, GDC applies a predefined project network policy, the intra-project policy, to each project by default. By default, workloads in a project namespace have the ability to communicate with each other without exposing anything to external resources.

By default, there is no egress policy, so outbound traffic is allowed for all intra-project traffic. However, when you set a single egress policy, only the traffic that the policy specifies is allowed.

**Note:** The policies defined in this section apply to both shared and standard clusters.

### Create an ingress intra-project policy

When you create a project, you implicitly create a default base `ProjectNetworkPolicy` resource that allows intra-project communication. This policy allows inbound traffic from other workloads in the same project.

You can remove the default policy, but be aware that this removal results in denying intra-project communication for all services and workloads within the project. To remove the policy, use the `kubectl delete` command:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER delete pnp base-policy-allow-intra-project-traffic -n PROJECT
    

You can add the default policy back by applying the following manifest:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: base-policy-allow-intra-project-traffic
    spec:
      policyType: Ingress
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of your project.



To verify the policy is ready, see Verify policy readiness.

### Create an egress intra-project policy

When you disable data exfiltration prevention and apply a `ProjectNetworkPolicy` egress policy to the project, such as preventing access to an external resource, use the following required policy to allow intra-project outbound traffic:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-intra-project-outbound-traffic
    spec:
      policyType: Egress
      egress:
      - to:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of your project.



To verify the policy is ready, see Verify policy readiness.

## Create a workload-level intra-project policy

Workload-level network policies offer granular control over communication between individual workloads within a project. This granularity allows stricter control of network access, improving security and resource use.

### Create an ingress workload-level intra-project policy

When you create a project, you implicitly create a default base `ProjectNetworkPolicy` resource that allows intra-project communication between all workloads. This policy allows inbound traffic from other workloads in the same project.

To create an ingress workload-level intra-project policy, the default base policy must first be deleted. Otherwise, unexpected behavior may occur.

  1. To delete the default base policy, run the following command:
         
         kubectl --kubeconfig GLOBAL_API_SERVER delete pnp base-policy-allow-intra-project-traffic -n PROJECT
         

  2. To create an ingress workload-level intra-project policy, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT
           name: allow-workload-level-intra-project-inbound-traffic
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 workloads:
                   matchLabels:
                     SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
           ingress:
           - from:
             - projectSelector:
                 projects:
                   matchNames:
                   - PROJECT
                 workloadSelector:
                   labelSelector:
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `PROJECT`: the name of your project.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.

To verify the policy is ready, see Verify policy readiness.




### Create an egress workload-level intra-project policy

  * To create an egress workload-level intra-project policy, create and apply the following custom resource:
        
        kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
        apiVersion: networking.global.gdc.goog/v1
        kind: ProjectNetworkPolicy
        metadata:
          namespace: PROJECT
          name: allow-workload-level-intra-project-outbound-traffic
        spec:
          policyType: Egress
          subject:
            subjectType: UserWorkload
            userWorkloadSelector:
              labelSelector:
                workloads
                  matchLabels:
                    SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          egress:
          - to:
            - projectSelector:
                projects:
                  matchNames:
                  - PROJECT
                workloadSelector:
                  labelSelector:
                    workloads:
                      matchLabels:
                        PEER_LABEL_KEY: PEER_LABEL_VALUE
        EOF
        

Replace the following:

    * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `PROJECT`: the name of your project.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
    * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.

To verify the policy is ready, see Verify policy readiness.




## Create a single zone workload-level intra-project policy

Workload-level network policies can enforce PNP along a single zone. Specific labels can be added to workloads within a single zone, allowing you to control communication between individual workloads within a project or in different projects for that zone.

### Create a single zone ingress workload-level intra-project policy

When you create a project, you implicitly create a default base `ProjectNetworkPolicy` resource that allows intra-project communication between all workloads. This policy allows inbound traffic from other workloads in the same project.

To create a single zone ingress workload-level intra-project policy, the default base policy must first be deleted. Otherwise, unexpected behavior may occur.

  1. To delete the default base policy, run the following command:
         
         kubectl --kubeconfig GLOBAL_API_SERVER delete pnp base-policy-allow-intra-project-traffic -n PROJECT
         

  2. To create a single zone ingress workload-level intra-project traffic network policy, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT
           name: allow-single-zone-intra-project-inbound-traffic
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 workloads:
                   matchLabels:
                     SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
                     ZONE_SUBJECT_LABEL_KEY: ZONE_SUBJECT_LABEL_VALUE
           ingress:
           - from:
             - projectSelector:
                 projects:
                   matchNames:
                   - PROJECT
                 workloadSelector:
                   labelSelector:
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
                         ZONE_PEER_LABEL_KEY: ZONE_PEER_LABEL_VALUE
         EOF
         

**Note:** Resources must have exact matching labels. To ensure this policy is enforced within a single zone, the subject and peer workloads must have the same zone label.

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `PROJECT`: the name of your project.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
     * `ZONE_SUBJECT_LABEL_KEY`: the key of the label used to select the subject zone. For example, `zone`, or `region`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `ZONE_SUBJECT_LABEL_VALUE`: the value associated with the `ZONE_SUBJECT_LABEL_KEY`. For example, if `ZONE_SUBJECT_LABEL_KEY` is `zone`, and `ZONE_SUBJECT_LABEL_VALUE` is `us-central1-a`, then workloads with the label `zone: us-central1-a` are receiving the traffic.
     * `ZONE_PEER_LABEL_KEY`: the key of the label used to select the zone associated with the peer. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `ZONE_PEER_LABEL_VALUE`: the value associated with the `ZONE_PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.

To verify the policy is ready, see Verify policy readiness.




### Create a single zone egress workload-level intra-project policy

  * To create a single zone egress workload-level intra-project policy, create and apply the following custom resource:
        
        kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
        apiVersion: networking.global.gdc.goog/v1
        kind: ProjectNetworkPolicy
        metadata:
          namespace: PROJECT
          name: allow-single-zone-intra-project-outbound-traffic
        spec:
          policyType: Egress
          subject:
            subjectType: UserWorkload
            userWorkloadSelector:
              labelSelector:
                workloads:
                  matchLabels:
                    SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
                    ZONE_SUBJECT_LABEL_KEY: ZONE_SUBJECT_LABEL_VALUE
          egress:
          - to:
            - projectSelector:
                projects:
                  matchNames:
                  - PROJECT
                workloadSelector:
                  labelSelector:
                    workloads:
                      matchLabels:
                        PEER_LABEL_KEY: PEER_LABEL_VALUE
                        ZONE_PEER_LABEL_KEY: ZONE_PEER_LABEL_VALUE
        EOF
        

**Note:** Resources must have exact matching labels. To ensure this policy is enforced within a single zone, the subject and peer workloads must have the same zone label.

Replace the following:

    * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `PROJECT`: the name of your project.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
    * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
    * `ZONE_SUBJECT_LABEL_KEY`: the key of the label used to select the subject zone. For example, `zone`, or `region`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `ZONE_SUBJECT_LABEL_VALUE`: the value associated with the `ZONE_SUBJECT_LABEL_KEY`. For example, if `ZONE_SUBJECT_LABEL_KEY` is `zone`, and `ZONE_SUBJECT_LABEL_VALUE` is `us-central1-a`, then workloads with the label `zone: us-central1-a` are receiving the traffic.
    * `ZONE_PEER_LABEL_KEY`: the key of the label used to select the zone associated with the peer. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `ZONE_PEER_LABEL_VALUE`: the value associated with the `ZONE_PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.

To verify the policy is ready, see Verify policy readiness.




## Create an intra-project policy for standard clusters

Standard Clusters are project-scoped Kubernetes clusters that provide greater control, flexibility, and cluster-admin permissions. When you create an intra-project policy, it is inherited by standard clusters by default. This policy allows all communication within the standard clusters that reside in the same project.

### Create an ingress intra-project policy for standard clusters

When you create a project, you implicitly create a default base `ProjectNetworkPolicy` resource that allows intra-project communication between all workloads. This policy allows inbound traffic from other workloads in the same project and also allows intra-cluster communication between all workloads in the standard clusters within the project.

To create an ingress intra-project policy for standard clusters, the default base policy must first be deleted. Otherwise, unexpected behavior may occur.

  1. To delete the default base policy, run the following command:
         
         kubectl --kubeconfig GLOBAL_API_SERVER delete pnp base-policy-allow-intra-project-traffic -n PROJECT
         

You can add the default policy back by applying the following manifest:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT
           name: base-policy-allow-intra-project-traffic
         spec:
           policyType: Ingress
           ingress:
           - from:
             - projectSelector:
                 projects:
                   matchNames:
                   - PROJECT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `PROJECT`: the name of your project.

To verify the policy is ready, see Verify policy readiness.

  2. To create an ingress intra-cluster pod-to-pod policy in standard clusters, create and apply the following custom resource
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-ingress-from-intra-cluster-traffic
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 clusters:
                   matchLabels:
                     kubernetes.io/metadata.name: STANDARD_CLUSTER_NAME
                 namespaces:
                   matchLabels:
                     kubernetes.io/metadata.name: SUBJECT_NAMESPACE
                 workloads:
                   matchLabels:
                     SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
           ingress:
           - from:
             - projectSelector:
                 projects:
                   matchNames:
                   - STANDARD_CLUSTER_PROJECT
                 workloadSelector:
                   labelSelector:
                     clusters:
                       matchLabels:
                         kubernetes.io/metadata.name: STANDARD_CLUSTER_NAME
                     namespaces:
                       matchLabels:
                         kubernetes.io/metadata.name: PEER_NAMESPACE
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.

To verify the policy is ready, see Verify policy readiness.

  3. Controlling traffic between pods and specific cluster nodes using the `ipBlocks` field is a [Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview) feature. For details and scale considerations, see [Target cluster nodes using IP blocks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#node-selection-considerations). To create an ingress intra-cluster node-to-pod policy in standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-ingress-from-node-to-pod-traffic
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 clusters:
                   matchLabels:
                     kubernetes.io/metadata.name: STANDARD_CLUSTER_NAME
                 namespaces:
                   matchLabels:
                     kubernetes.io/metadata.name: SUBJECT_NAMESPACE
                 workloads:
                   matchLabels:
                     SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
           ingress:
           - from:
             - ipBlocks:
               - cidr: NODE_IP
             ports:
             - protocol: TCP
               port: PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `webhook`, then workloads with the label `app: webhook` receive the traffic.
     * `NODE_IP`: the IP address (in `/32` notation) or CIDR range of the source cluster node from which traffic is allowed.
     * `PORT`: the port on the subject workload where traffic is allowed (for example, `8443` or `443`).

To verify the policy is ready, see Verify policy readiness.




### Create an egress intra-project policy for standard clusters

  1. To create an egress intra-cluster pod-to-pod policy in standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-egress-to-intra-cluster-traffic
         spec:
           policyType: Egress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 clusters:
                   matchLabels:
                     kubernetes.io/metadata.name: STANDARD_CLUSTER_NAME
                 namespaces:
                   matchLabels:
                     kubernetes.io/metadata.name: SUBJECT_NAMESPACE
                 workloads:
                   matchLabels:
                     SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
           egress:
           - to:
             - projectSelector:
                 projects:
                   matchNames:
                   - STANDARD_CLUSTER_PROJECT
                 workloadSelector:
                   labelSelector:
                     clusters:
                       matchLabels:
                         kubernetes.io/metadata.name: STANDARD_CLUSTER_NAME
                     namespaces:
                       matchLabels:
                         kubernetes.io/metadata.name: PEER_NAMESPACE
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.

To verify the policy is ready, see Verify policy readiness.

  2. Controlling traffic between pods and specific cluster nodes using the `ipBlocks` field is a [Preview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview) feature. For details and scale considerations, see [Target cluster nodes using IP blocks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#node-selection-considerations). To create an egress intra-cluster pod-to-node policy in standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-egress-from-pod-to-node-traffic
         spec:
           policyType: Egress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 clusters:
                   matchLabels:
                     kubernetes.io/metadata.name: STANDARD_CLUSTER_NAME
                 namespaces:
                   matchLabels:
                     kubernetes.io/metadata.name: SUBJECT_NAMESPACE
                 workloads:
                   matchLabels:
                     SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
           egress:
           - to:
             - ipBlocks:
               - cidr: NODE_IP
             ports:
             - protocol: TCP
               port: PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `controller`, then workloads with the label `app: controller` send the traffic.
     * `NODE_IP`: the IP address (in `/32` notation) or CIDR range of the destination cluster node to which traffic is allowed.
     * `PORT`: the port on the destination node to which traffic is allowed (for example, `6444` or `443`).

To verify the policy is ready, see Verify policy readiness.




## Verify policy readiness

To verify that the project network policy is ready, run the following command:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER get pnp POLICY_NAME -n PROJECT -oyaml
    

Replace `POLICY_NAME` with the name of the policy you want to verify, and `PROJECT` with the project name where the policy was created.

Look for `status: "True"` in the `Ready` condition of the output:
    
    
    ...
    status:
      ...
      conditions:
      - lastTransitionTime: "2026-03-24T10:55:25Z"
        message: ProjectNetworkPolicy propagated to remote clusters
        observedGeneration: 1
        reason: Propagated
        status: "True"
        type: Ready
    ...
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
