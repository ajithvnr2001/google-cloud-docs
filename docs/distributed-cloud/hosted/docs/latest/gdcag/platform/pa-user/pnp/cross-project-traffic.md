---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic/
title: Create cross-project network policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:29.304622+00:00
---

# Create cross-project network policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create cross-project network policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure cross-project traffic network policies in Google Distributed Cloud (GDC) air-gapped.

Cross-project traffic refers to the communication between services and workloads from different project namespaces but within the same organization.

Services and workloads in a project are isolated from external services and workloads by default. However, services and workloads from different project namespaces and within the same organization can communicate with each other by applying cross-project traffic network policies.

By default, these policies apply globally across all zones. For more information on global resources in a GDC universe, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

To enforce cross-project traffic within a single zone, see [Create a single zone workload-level cross-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic#single-zone-workload-level-cross-project).

## Before you begin

To configure cross-project traffic network policies, you must have the following:

  * The necessary identity and access roles. To manage traffic network policies, you need the **Project Network Policy Admin** (`global-project-networkpolicy-admin`) role. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * For egress network policies, you must also disable [data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration) for the project.



## Create a cross-project policy

You can define ingress or egress cross-project traffic policies to manage the communication between projects.

**Note:** The policies defined in this section apply to both shared and standard clusters.

### Create an ingress cross-project policy

To allow connections to your project's workloads or services from workloads in another project within your organization, you must configure an ingress firewall rule.

This policy applies to all zones in your organization.

Work through the following steps to create a new firewall rule and allow inbound traffic from workloads in another project:

###  Console 

  1. Within the GDC console of the project you are configuring, go to **Networking** > **Firewall** in the navigation menu to open the **Firewall** page.
  2. Click **Create** in the action bar to begin creating a new firewall rule.
  3. On the **Firewall rule details** page, fill out the following information:

     1. In the **Name** field, enter a valid name for your firewall rule.
     2. In the **Direction of traffic** section, select **Ingress** to allow inbound traffic from workloads in other projects.
     3. In the **Target** section, select one of the following options: 
        * **All user workloads:** allow connections to the workloads of the project you are configuring.
        * **Service:** indicate that this firewall rule targets a specific service within the project you are configuring.
     4. If your target is a project service, select the name of the service from the list of available services on the **Service** drop-down menu.
     5. In the **From** section, select one of the following two options: 
        * **All projects:** allow connections from workloads in all the projects of the same organization.
        * **Another project** and **All user workloads:** allow connections from workloads in another project of the same organization.
     6. If you want to transfer workloads only from another project, select a project that you can access from the list of projects on the **Project ID** drop-down menu.
     7. If your target is all user workloads, select one of the following options in the **Protocols and ports** section: 
        * **Allow all:** allow connections using any protocol or port.
        * **Specified protocols and ports:** allow connections using only the protocols and ports that you specify in the corresponding fields for the ingress firewall rule.
  4. On the **Firewall rule details** page, click **Create**.




You've now permitted connections from other project workloads within the same organization. After creating the firewall rule, the rule is visible in a table on the **Firewall** page.

To create a reciprocal ingress policy in the other direction, visit the GDC console of the other project and repeat the process.

###  API 

The following policy enables workloads in the `PROJECT_1` project to permit connections from workloads in the `PROJECT_2` project, as well as the return traffic for the same flows. Apply the policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: allow-inbound-traffic-from-PROJECT_2
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_2
    EOF
    

Replace `GLOBAL_API_SERVER` with the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.

The preceding command allows `PROJECT_2` to go to `PROJECT_1`, but doesn't allow connections initiated from `PROJECT_1` to `PROJECT_2`. For the latter, you require a reciprocal policy in the `PROJECT_2` project. Apply the reciprocal policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_2
      name: allow-inbound-traffic-from-PROJECT_1
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_1
    EOF
    

Connections are now permitted to and from `PROJECT_1` and `PROJECT_2`.

### Create an egress cross-project policy

When you grant an ingress cross-project traffic policy to let workloads in one project to allow connections from workloads in another project, this action also grants the return traffic for the same flows. Therefore, you don't need an egress cross-project traffic network policy in the original project.

Work through the following steps to create a new firewall rule and allow outbound traffic from workloads in a project:

###  Console 

  1. Within the GDC console of the project you are configuring, go to **Networking** > **Firewall** in the navigation menu to open the **Firewall** page.
  2. In the action bar, click **Create** to create a new firewall rule.
  3. On the **Firewall rule details** page, fill out the following information:

     1. In the **Name** field, enter a valid name for your firewall rule.
     2. In the **Direction of traffic** section, select **Egress** to indicate that this firewall rule is controlling outbound traffic.
     3. In the **Target** section, select one of the following options: 
        * **All user workloads:** allow connections from the workloads of the project you are configuring.
        * **Service:** indicate that this firewall rule targets a specific service within the project you are configuring.
     4. If your target is a project service, select the name of the service from the list of available services on the **Service** drop-down menu.
     5. In the **To** section, select one of the following two options: 
        * **All projects:** allow connections to workloads in all the projects of the same organization.
        * **Another project** and **All user workloads:** allow connections to workloads in another project of the same organization.
     6. If you want to transfer workloads only to another project, select a project that you can access from the list of projects on the **Project ID** drop-down menu.
     7. If your target is all user workloads, select one of the following options in the **Protocols and ports** section: 
        * **Allow all:** allow connections using any protocol or port.
        * **Specified protocols and ports:** allow connections using only the protocols and ports that you specify in the corresponding fields for the egress firewall rule.
  4. On the **Firewall rule details** page, click **Create**.




You've now permitted connections to other project workloads within the same organization. After creating the firewall rule, the rule is visible in a table on the **Firewall** page.

To create a reciprocal egress policy in the other direction, visit the GDC console of the other project and repeat the process.

###  API 

The following policy enables workloads in the `PROJECT_1` project to permit connections to workloads in the `PROJECT_2` project. Apply the policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: allow-outbound-traffic-to-PROJECT_2
    spec:
      policyType: Egress
      subject:
        subjectType: UserWorkload
      egress:
      - to:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_2
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT_1`: The name of the project that is receiving the traffic.
  * `PROJECT_2`: The name of the project that the traffic is coming from.



The preceding command allows outgoing connections from `PROJECT_1` to `PROJECT_2`, but doesn't allow connections from `PROJECT_2` to `PROJECT_1`. For the latter, you require a reciprocal policy in the `PROJECT_2` project. Apply the reciprocal policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_2
      name: allow-outbound-traffic-to-PROJECT_1
    spec:
      policyType: Egress
      subject:
        subjectType: UserWorkload
      egress:
      - to:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_1
    EOF
    

### Create an egress workload-level cross-project policy

  * To create an egress workload-level cross-project policy, create and apply the following custom resource:
        
        kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
        apiVersion: networking.global.gdc.goog/v1
        kind: ProjectNetworkPolicy
        metadata:
          namespace: PROJECT_2
          name: allow-cross-project-outbound-traffic-from-project-2-to-project-1
        spec:
          policyType: Egress
          subject:
            subjectType: UserWorkload
            userWorkloadSelector:
              labelSelector:
                workloads:
                  matchLabels:
                    SUBJECT_LABEL_KEY: SUBJECT_LABEL_VALUE
          egress:
          - to:
            - projectSelector:
                projects:
                  matchNames:
                  - PROJECT_1
                workloadSelector:
                  labelSelector:
                    workloads:
                      matchLabels:
                        PEER_LABEL_KEY: PEER_LABEL_VALUE
        EOF
        

Replace the following:

    * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
    * `PROJECT_1`: The name of the project that is receiving the traffic.
    * `PROJECT_2`: The name of the project that the traffic is coming from.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
    * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.



## Create a single zone workload-level cross-project policy

Workload-level network policies can enforce PNP along a single zone. Specific labels can be added to workloads within a single zone, allowing you to control communication between individual workloads within a project or in different projects for that zone.

### Create a single zone ingress workload-level cross-project policy

  1. To create a single zone ingress workload-level cross-project policy, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT_1
           name: allow-single-zone-cross-project-inbound-traffic-from-project-2-to-project-1
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
                   - PROJECT_2
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
     * `PROJECT_1`: The name of the project that is receiving the traffic.
     * `PROJECT_2`: The name of the project that the traffic is coming from.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
     * `ZONE_SUBJECT_LABEL_KEY`: the key of the label used to select the subject zone. For example, `zone`, or `region`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `ZONE_SUBJECT_LABEL_VALUE`: the value associated with the `ZONE_SUBJECT_LABEL_KEY`. It specifies which zone is receiving the traffic. For example, if `ZONE_SUBJECT_LABEL_KEY` is `zone`, and `ZONE_SUBJECT_LABEL_VALUE` is `us-central1-a`, then workloads with the label `zone: us-central1-a` are receiving the traffic.
     * `ZONE_PEER_LABEL_KEY`: the key of the label used to select the zone associated with the peer. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `ZONE_PEER_LABEL_VALUE`: the value associated with the `ZONE_PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.



### Create a single zone egress workload-level cross-project policy

  * To create a single zone egress workload-level cross-project policy, create and apply the following custom resource:
        
        kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
        apiVersion: networking.global.gdc.goog/v1
        kind: ProjectNetworkPolicy
        metadata:
          namespace: PROJECT_2
          name: allow-single-zone-cross-project-outbound-traffic-from-project-2-to-project-1
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
                  - PROJECT_1
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
    * `PROJECT_1`: The name of the project that is receiving the traffic.
    * `PROJECT_2`: The name of the project that the traffic is coming from.
    * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
    * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
    * `ZONE_SUBJECT_LABEL_KEY`: the key of the label used to select the subject zone. For example, `zone`, or `region`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `ZONE_SUBJECT_LABEL_VALUE`: the value associated with the `ZONE_SUBJECT_LABEL_KEY`. For example, if `ZONE_SUBJECT_LABEL_KEY` is `zone`, and `ZONE_SUBJECT_LABEL_VALUE` is `us-central1-a`, then workloads with the label `zone: us-central1-a` are sending the traffic.
    * `ZONE_PEER_LABEL_KEY`: the key of the label used to select the zone associated with the peer. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
    * `ZONE_PEER_LABEL_VALUE`: the value associated with the `ZONE_PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.



## Create a cross-project policy for standard clusters

Standard clusters are project-scoped Kubernetes clusters that provide greater control, flexibility, and cluster-admin permissions.

### Create an ingress cross-project policy for standard clusters

  1. To create an ingress intercluster policy between standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_1_PROJECT
           name: allow-ingress-from-standard-cluster-2-to-standard-cluster-1
         spec:
           policyType: Ingress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 clusters:
                   matchLabels:
                     kubernetes.io/metadata.name: STANDARD_CLUSTER_1_NAME
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
                   - STANDARD_CLUSTER_2_PROJECT
                 workloadSelector:
                   labelSelector:
                     clusters:
                       matchLabels:
                         kubernetes.io/metadata.name: STANDARD_CLUSTER_2_NAME
                     namespaces:
                       matchLabels:
                         kubernetes.io/metadata.name: PEER_NAMESPACE
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_1_PROJECT`: the name of the standard cluster project that is receiving the traffic.
     * `STANDARD_CLUSTER_2_PROJECT`: the name of the standard cluster project that the traffic is coming from.
     * `STANDARD_CLUSTER_1_NAME`: the name of the standard cluster that is receiving the traffic.
     * `STANDARD_CLUSTER_2_NAME`: the name of the standard cluster that the traffic is coming from.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.
  2. To create an ingress intercluster policy between standard and shared clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: SHARED_CLUSTER_PROJECT
           name: allow-ingress-from-standard-cluster-to-shared-cluster
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
     * `SHARED_CLUSTER_PROJECT`: the name of the shared cluster project.
     * `STANDARD_CLUSTER_NAME`: The name of the standard cluster.
     * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.



### Create an egress cross-project policy for standard clusters

  1. To create an egress intercluster policy between standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_2_PROJECT
           name: allow-egress-from-standard-cluster-2-to-standard-cluster-1
         spec:
           policyType: Egress
           subject:
             subjectType: UserWorkload
             userWorkloadSelector:
               labelSelector:
                 clusters:
                   matchLabels:
                     kubernetes.io/metadata.name: STANDARD_CLUSTER_2_NAME
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
                   - STANDARD_CLUSTER_1_PROJECT
                 workloadSelector:
                   labelSelector:
                     clusters:
                       matchLabels:
                         kubernetes.io/metadata.name: STANDARD_CLUSTER_1_NAME
                     namespaces:
                       matchLabels:
                         kubernetes.io/metadata.name: PEER_NAMESPACE
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_1_PROJECT`: the name of the standard cluster project that is receiving the traffic.
     * `STANDARD_CLUSTER_2_PROJECT`: the name of the standard cluster project that the traffic is coming from.
     * `STANDARD_CLUSTER_1_NAME`: the name of the standard cluster that is receiving the traffic.
     * `STANDARD_CLUSTER_2_NAME`: the name of the standard cluster that the traffic is coming from.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `PEER_NAMESPACE`: the peer namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.
  2. To create an egress intercluster policy between standard and shared clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-egress-from-standard-cluster-to-shared-cluster
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
                   - SHARED_CLUSTER_PROJECT
                 workloadSelector:
                   labelSelector:
                     workloads:
                       matchLabels:
                         PEER_LABEL_KEY: PEER_LABEL_VALUE
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `SHARED_CLUSTER_PROJECT`: the name of the shared cluster project.
     * `STANDARD_CLUSTER_NAME`: The name of the standard cluster.
     * `SUBJECT_NAMESPACE`: the subject namespace in the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
     * `PEER_LABEL_KEY`: the key of the label used to select the peer workloads. If you are referencing VM labels, you must add a prefix to this key; see the warning that follows this list.
     * `PEER_LABEL_VALUE`: the value associated with the `PEER_LABEL_KEY`.
**Warning:** When referencing VM labels in the `workloadSelector` or `workloads` fields, you must prepend the prefix `user-label.gpc.gke.io/` to the label key. For example, if you assign the label `app: backend` to a VM, you must specify it as `user-label.gpc.gke.io/app: backend` to successfully match the workload. This prefix is specific to VMs and does not apply to any other workloads.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
