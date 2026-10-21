---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic/
title: Create organization-external network policies \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:27:51.222042+00:00
---

# Create organization-external network policies  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create organization-external network policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure organization-external traffic network policies in Google Distributed Cloud (GDC) air-gapped.

Organization-external traffic refers to the communication between services and workloads from different organizations and external endpoints.

## Before you begin

To configure organization-external traffic network policies, you must have the following:

  * The necessary identity and access roles. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-a-project).
  * [Disable data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#disable-data-exfiltration-protection).
  * One of following network configurations: 
    * Organizations using a common [Interconnect AttachmentGroup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview).
    * Organizations using connectivity through their respective external peered networks.

**Note:** When configuring project network policies to target specific nodes or using broad CIDR ranges, your policy configuration choices may have an impact on scalability and performance. For more information, see [Node selection and scale considerations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview#node-selection-considerations).

## Create an organization-external policy

You can define ingress or egress organization-external traffic policies to manage the communication between services and workloads from different organizations and external endpoints.

You can create global organization-external traffic project network policies that apply to traffic across all zones in your organization. For more information on global resources in a GDC universe, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

Connecting services and workloads to a destination outside of your project in a different organization requires explicit approval. You must [disable data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#disable-data-exfiltration-protection) to allow organization-external traffic.

### Create a global ingress firewall rule for organization-external traffic

When exposing workloads in your project using an external load balancer, you must also create a `ProjectNetworkPolicy` ingress policy to allow external client IP addresses to access the workloads.

This global ingress policy applies to all zones in your organization.

Work through the following steps to create a new firewall rule and allow inbound traffic from workloads in a project of a different organization:

###  Console 

  1. Within the GDC console of the project you are configuring, go to **Networking** > **Firewall** in the navigation menu to open the **Firewall** page.
  2. Click **Create** in the action bar to begin creating a new firewall rule.
  3. On the **Firewall rule details** page, fill out the following information:

     1. In the **Name** field, enter a valid name for your firewall rule.
     2. In the **Direction of traffic** section, select **Ingress** to allow inbound traffic from workloads in other organizations.
     3. In the **Target** section, select one of the following options: 
        * **All user workloads:** allow connections to the workloads of the project you are configuring.
        * **Service:** indicate that this firewall rule targets a specific service within the project you are configuring.
     4. If your target is a project service, select the name of the service from the list of available services on the **Service** drop-down menu.
     5. In the **From** section, select **Outside the organization** and enter the CIDR block of another organization in the **CIDR** field to allow connections from that organization's network.
     6. If your target is all user workloads, select one of the following options in the **Protocols and ports** section: 
        * **Allow all:** allow connections using any protocol or port.
        * **Specified protocols and ports:** allow connections using only the protocols and ports that you specify in the corresponding fields for the ingress firewall rule.
  4. On the **Firewall rule details** page, click **Create**.




You've now permitted connections from project workloads of a different organization. After creating the firewall rule, the rule is visible in a table on the **Firewall** page.

###  API 

Configure and apply your own customized `ProjectNetworkPolicy` ingress policy:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-inbound-traffic-from-external
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - ipBlock:
            cidr: CIDR
    EOF
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of the GDC project.
  * `CIDR`: the CIDR block of another organization.



This policy is required as the external load balancer uses Direct Server Return (DSR), which preserves the source external IP address and bypasses the load balancer on the return path.

### Create a global egress firewall rule for organization-external traffic

To transfer data to services outside of the organization, you must first disable data exfiltration protection. Then, you must configure an egress firewall rule to allow outbound traffic from your project workloads or services.

This section describes the process to enable outbound traffic at the project level. For information about managing egress connectivity at the workload level, see [NAT overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-overview).

This global egress firewall rules applies to all zones in your organization.

Work through the following steps to create a new firewall rule and allow outbound traffic from project workloads or services to workloads in another organization:

###  Console 

  1. Within the GDC console of the project you are configuring, go to **Networking** > **Firewall** in the navigation menu to open the **Firewall** page.
  2. Click **Create** in the action bar to begin creating a new firewall rule.
  3. On the **Firewall rule details** page, fill out the following information:

     1. In the **Name** field, enter a valid name for your firewall rule.
     2. In the **Direction of traffic** section, select **Egress** to indicate that this firewall rule is controlling outbound traffic.
     3. In the **Target** section, select one of the following options: 
        * **All user workloads:** allow connections from the workloads of the project you are configuring.
        * **Service:** indicate that this firewall rule targets a specific service within the project you are configuring.
     4. If your target is a project service, select the name of the service from the list of available services on the **Service** drop-down menu.
     5. In the **To** section, select **Outside the organization** and enter the CIDR block of another organization in the **CIDR** field to allow connections to that organization's network.
     6. If your target is all user workloads, select one of the following options in the **Protocols and ports** section: 
        * **Allow all:** allow connections using any protocol or port.
        * **Specified protocols and ports:** allow connections using only the protocols and ports that you specify in the corresponding fields for the egress firewall rule.
  4. On the **Firewall rule details** page, click **Create**.




You've now permitted connections to another organization. After creating the firewall rule, the rule is visible in a table on the **Firewall** page.

###  API 

To enable outbound traffic to services outside of the organization, customize your `ProjectNetworkPolicy` resource. However, because data exfiltration prevention is enabled by default, your customized `ProjectNetworkPolicy` egress policy shows a validation error in the status field, and the dataplane ignores it. This behavior happens by design.

You can transfer workloads from a given project when you allow data exfiltration for that project. The outbound traffic that you allow is a source network address translation (NAT) using a well-known IP address allocated for the project.

To enable your customized egress policy, follow these steps:

  1. Configure and apply your own customized `ProjectNetworkPolicy` egress policy on all user workloads in a project.

Use the following example:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: PROJECT
           name: allow-outbound-traffic-to-external
         spec:
           subject:
             subjectType: UserWorkload
           egress:
           - to:
             - ipBlock:
                 cidr: CIDR
         EOF
         

The policy allows outbound traffic to all hosts in the CIDR block, which reside outside the organization. Your first attempt must cause an intended and necessary status error.

  2. Confirm that you see a validation error in your status.

**Important:** Only the outbound traffic to destinations outside your project's organization that you explicitly allow in your `ProjectNetworkPolicy` egress policy configuration is granted. Any other outbound traffic is denied. Therefore, only apply a customized `ProjectNetworkPolicy` egress policy when requirements mandate such a policy.
  3. Ask the Organization IAM Admin to disable data exfiltration prevention. This action enables your configuration, while preventing all other outbound traffic.

**Important:** Disabling data exfiltration prevention without defining one or more valid `ProjectNetworkPolicy` resources permits all outbound traffic to destinations outside your project's organization. Never disable this setting without configuring your customized `ProjectNetworkPolicy` egress policy.
  4. Check the `ProjectNetworkPolicy` that you created and verify that the error in the validation status field is gone, and the status `Ready` is `True`, indicating that your policy is in effect:
         
         kubectl --kubeconfig GLOBAL_API_SERVER \
             get projectnetworkpolicy allow-outbound-traffic-to-external \
             -n PROJECT -o yaml
         

Replace the following:

     * `GLOBAL_API_SERVER`: The global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.

     * `PROJECT`: the name of the GDC project.




After you have applied this policy, and provided that you have not defined other egress policies, all other outbound traffic is denied for `PROJECT`.

## Create an organization-external policy for standard clusters

Standard clusters are project-scoped Kubernetes clusters that provide greater control, flexibility, and cluster-admin permissions.

### Create an ingress organization-external policy for standard clusters

  1. To create an ingress organization-external policy for standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-ingress-from-external-endpoint-to-standard-cluster-pod
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
               - cidr: EXTERNAL_IP
             ports:
             - protocol: TCP
               port: PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are receiving the traffic.
     * `EXTERNAL_IP`: the IP address of the external endpoint.
     * `PORT`: the port on the subject workload where traffic is allowed.



### Create an egress organization-external policy for standard clusters

  1. To create an egress organization-external policy for standard clusters, create and apply the following custom resource:
         
         kubectl --kubeconfig GLOBAL_API_SERVER apply -f - <<EOF
         apiVersion: networking.global.gdc.goog/v1
         kind: ProjectNetworkPolicy
         metadata:
           namespace: STANDARD_CLUSTER_PROJECT
           name: allow-egress-from-standard-cluster-pod-to-external-endpoint
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
               - cidr: EXTERNAL_IP
             ports:
             - protocol: TCP
               port: PORT
         EOF
         

Replace the following:

     * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers). If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli) for details.
     * `STANDARD_CLUSTER_PROJECT`: the name of the standard cluster project.
     * `STANDARD_CLUSTER_NAME`: the name of the standard cluster.
     * `SUBJECT_LABEL_KEY`: the key of the label used to select the subject workloads. For example, `app`, `tier`, or `role`.
     * `SUBJECT_LABEL_VALUE`: the value associated with the `SUBJECT_LABEL_KEY`. For example, if `SUBJECT_LABEL_KEY` is `app`, and `SUBJECT_LABEL_VALUE` is `backend`, then workloads with the label `app: backend` are sending the traffic.
     * `EXTERNAL_IP`: the IP address of the external endpoint.
     * `PORT`: the port on the external endpoint to which traffic is allowed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
