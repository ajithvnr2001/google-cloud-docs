---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:04.485777+00:00
---

# Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/pnp-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of project network policies in Google Distributed Cloud (GDC) air-gapped.

Project network policies define either ingress or egress rules. Unlike Kubernetes network policies, you can only specify one policy type for a policy. Each rule in a policy can be configured with an action of either Allow (the default) or Deny.

For traffic within a project, GDC applies a predefined project network policy, the default intra-project policy, to each project.

Services and workloads in a project are isolated from external services and workloads by default. However, services and workloads from different project namespaces and within the same organization can communicate with each other by applying cross-project traffic network policies.

Similarly, connecting services and workloads to a destination outside of your project in a different organization requires explicit approval. You must disable data exfiltration protection to allow organization-external traffic.

Ingress and egress firewall rules are the main components of project network policies and determine which types of traffic are allowed or denied in and out of your network. To set firewall rules for your project namespace in GDC, use the GDC console.

## Security and connectivity

By default, services and workloads in a project are isolated within that project. They cannot communicate with external services and workloads without configuring a network policy.

To set a network policy for your project namespace in GDC, use the `ProjectNetworkPolicy` resource. This resource lets you define policies, which allow communication within projects, between projects, to external IP addresses, and from external IP addresses. Also, you can transfer workloads out from a project only if you [disable data exfiltration protection for the project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#prevent-data-exfiltration).

GDC project network policies are additive. The resulting enforcement for a workload is an _any_ match for the traffic flow against the union of all policies applied to that workload. When multiple policies are present, the rules for each policy are additively combined, allowing traffic if it matches at least one of the rules.

Explicit `Deny` rules take absolute precedence over `Allow` rules. If a traffic flow matches a `Deny` rule, it is dropped, even if it is allowed by another rule or default platform policies.

Furthermore, after you apply a single policy that selects a workload, all traffic you don't specify is denied (default-deny mode). Therefore, when you apply one or more policies that select a workload as the subject, only the traffic that is explicitly allowed (and not explicitly denied) is permitted.

When you use a well-known IP address you allocate for the project, it performs a source network address translation (NAT) on the outbound traffic from the organization.

## Default intra-project policy

When you create a project, GDC automatically creates a global project network policy named `base-policy-allow-intra-project-traffic` in the project namespace. This default policy does the following:

  * Selects all user workloads in the project as its subject.
  * Allows inbound traffic to those workloads from all workloads in the same project, on all ports.
  * Doesn't allow inbound traffic from other projects or from outside the organization.



GDC creates the default policy only once, when it creates the project. If you change or delete the policy, GDC doesn't restore it. GDC propagates the policy to each cluster in the project as a network policy named `g-base-policy-allow-intra-project-traffic`. The `status.zones[].replicaStatus.propagatedName` field of the policy shows this name.

To view the default policy, run the following command:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER get projectnetworkpolicy \
        base-policy-allow-intra-project-traffic -n PROJECT -o yaml
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path. For more information, see [Global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers).
  * `PROJECT`: the name of your project.



If the command returns a `NotFound` error, the default policy was deleted. To add it back, see [Create an ingress intra-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#ingress-intra-project).

The default policy combines with the policies that you create as follows:

  * **Ingress** : Workloads are isolated from other projects and from outside the organization by default, whether or not the default policy exists. Ingress policies that you create add allowed sources, such as other projects or external CIDR blocks. While the default policy exists, you don't need to repeat the intra-project rule in your own ingress policies.
  * **Workload-level intra-project ingress** : While the default policy exists, all workloads in the project can reach each other on all ports. A workload-level intra-project ingress policy that uses the `Allow` action doesn't restrict this traffic until you delete or change the default policy. To avoid an interruption, apply your workload-level policies and [verify that they're ready](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#verify-policy-readiness) before you delete the default policy. To block specific intra-project traffic while you keep the default policy, you can use an explicit deny rule, which is a Preview feature. For more information, see [Create an ingress workload-level intra-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#ingress-workload-level-intra-project).
  * **Egress** : A project has no egress policy by default. Outbound traffic is unrestricted within the organization, but [data exfiltration protection](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#allow-egress-traffic) (enabled by default) blocks traffic that leaves the organization. Egress policies take effect only after you disable data exfiltration protection for the project. While data exfiltration protection is enabled, zonal API servers reject egress policies, and global egress policies don't become ready.

**Caution:** When an egress policy is enforced, the selected workloads can send traffic _only_ to the destinations explicitly allowed by your egress policies (DNS is exempt). This blocks outbound traffic to other workloads and `ClusterIP` Services in the same project. To avoid unexpected outages, always apply an [egress intra-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#egress-intra-project) before you disable data exfiltration protection or apply a restrictive egress policy.

## Global project network policies

You can create global project network policies. The scope of global project network policies span across a GDC universe. Each GDC universe can consist of multiple GDC zones organized into regions that are interconnected and share a control plane. For example, a universe consisting two regions with three zones each might look like: `us-virginia1-a`, `us-virginia1-b`, `us-virginia1-c` and `eu-ams1-a`, `eu-ams1-b`, `eu-ams1-c`.

The scope of zonal project network policies is limited to the zones specified at the time of creation. Each zone is an independent disaster domain. A zone manages infrastructure, services, APIs, and tooling that use a local control plane.

For more information on global resources in a GDC universe, see [Multi-zone overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).

You can create global project network policies using the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/networking-v1). Use the API version `networking.global.gdc.goog` to create global resources.

You can create zonal project network policies using the KRM API or the GDC console. Use the API version `networking.gdc.goog` to create zonal resources.

## Allow-all network policies

You can create allow-all network policies to establish broad, default access rules for a project.

You can configure the following types of allow-all network policies:

  * Allow-all Network Policy: Allows traffic to and from any source, which includes other projects and external IPs.
  * Allow-all-external Network Policy: Allows traffic to and from IP addresses external to the organization.
  * Allow-all-projects Network Policy: Allows traffic to and from all projects within the organization.



For more information, see [Create allow-all traffic network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/allow-all-traffic).

## Explicit deny network policies

**Preview:** Configuring explicit deny project network policies is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service Level Agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview).

You can configure explicit deny rules in project network policies to restrict connectivity between specified projects or CIDR blocks.

Key features and constraints of deny rules:

  * **Precedence** : Deny rules take absolute precedence over allow rules (including base platform policies).
  * **Egress safety rules** : To prevent accidentally blocking critical infrastructure traffic, egress deny rules automatically exclude system and non-project namespaces.
  * **Peer restriction** : To ensure safe configuration, ingress deny rules must explicitly specify a source peer in the `from` field, and egress deny rules must explicitly specify a destination peer in the `to` field. You cannot select all sources or destinations by leaving the peer field empty. Leaving the peer field empty is disallowed, and the policy will be rejected.
  * **No egress deny with DEP** : You cannot configure egress deny rules when data exfiltration protection (DEP) is enabled for the project.



For more information, see [Create explicit deny network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/deny-traffic).

## Workload-level network policies

You can create workload-level network policies to define fine-grained access control for individual VMs and pods within a project. These policies act like firewalls for your workloads, controlling traffic flow based on labels to enhance security and isolate applications. This granularity allows stricter control over which workloads can communicate with each other within and across projects.

Workload-level network policies also provide the capability to enforce PNP along a single zone.

For more information, see [Create a workload-level intra-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#create-workload-level-intra) and [Create a workload-level cross-project policy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic#create-workload-level-cross).

## Policy structure and validation

In a `ProjectNetworkPolicy` resource, workload label selectors are nested several levels deep. The following ingress policy shows the correct location of each selector:
    
    
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-frontend-to-backend
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
        userWorkloadSelector:
          labelSelector:
            workloads:
              matchLabels:
                app: backend
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PEER_PROJECT
            workloadSelector:
              labelSelector:
                workloads:
                  matchLabels:
                    app: frontend
        ports:
        - protocol: TCP
          port: 8080
    

Replace the following:

  * `PROJECT`: the name of your project.
  * `PEER_PROJECT`: the name of the project that contains the client workloads.



This policy allows workloads labeled `app: frontend` in `PEER_PROJECT` to connect to workloads labeled `app: backend` in your project on TCP port `8080`.

When you write a policy, follow these rules:

  * Always set `spec.policyType` explicitly to `Ingress` or `Egress`. An `Ingress` policy can contain only `ingress` rules with `from` peers, and an `Egress` policy can contain only `egress` rules with `to` peers. If you omit `policyType`, the policy defaults to `Ingress`, and the API server rejects a policy that contains only `egress` rules.
  * To select subject workloads by label, use `spec.subject.userWorkloadSelector.labelSelector.workloads`. If you omit `userWorkloadSelector`, the policy applies to all user workloads in the project.
  * Don't put label selectors directly under `spec.subject`. By default, `kubectl` rejects fields such as `spec.subject.matchLabels` with a `strict decoding error: unknown field` message.
  * To select peer workloads by label, use `projectSelector.workloadSelector.labelSelector.workloads` in a `from` or `to` entry.
  * If the subject or peer workloads are VMs, prefix their label keys with `user-label.gpc.gke.io/`. For example, use `user-label.gpc.gke.io/app: backend`.
  * The automatically created default intra-project policy and some existing policies use the deprecated `spec.subject.workloadSelector` field, which takes a label selector directly. Use `userWorkloadSelector` in new policies.

**Warning:** Don't apply policies with `--validate=false`, `--validate=ignore`, or `--validate=warn`. With these settings, the API server drops unknown fields instead of rejecting them. The `warn` setting only prints a warning. A misplaced subject selector then makes the policy apply to all user workloads in the project, which can allow more traffic than you intended.

To validate a policy against the global API server without applying it, run a server-side dry run:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER apply --dry-run=server \
        --validate=strict -f POLICY_FILE
    

The dry run reports the same schema and validation errors as a real `kubectl apply` command, such as an unknown field or an `egress` rule in an `Ingress` policy, but doesn't create or change the policy. The dry run requires the same permissions as applying the policy. A successful dry run doesn't confirm that the policy is enforced. After you apply the policy, [verify that it's ready](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#verify-policy-readiness).

To list the fields that your global API server accepts, run the following command:
    
    
    kubectl --kubeconfig GLOBAL_API_SERVER explain projectnetworkpolicy.spec \
        --api-version=networking.global.gdc.goog/v1 --recursive
    

Replace the following:

  * `GLOBAL_API_SERVER`: the global API server's kubeconfig path.
  * `POLICY_FILE`: the path to your `ProjectNetworkPolicy` manifest.



## Prepare predefined roles and access

To configure project network policies, you must have the necessary identity and access roles:

  * Project Network Policy Admin: has write permissions on all multi-zone PNP resources in the global project namespace. Ask your IAM Org Admin to grant you the `global-project-networkpolicy-admin` role. For more information, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/role-descriptions).



## Target cluster nodes using IP blocks

**Preview:** Targeting specific cluster nodes using the `ipBlocks` field is a Preview feature that is available as-is and is not recommended for production environments. Google provides no Service Level Agreements (SLA) or technical support commitments for Preview features. For more information, see [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview).

You can use the `ipBlocks` field in a `ProjectNetworkPolicy` resource to specify individual node IP addresses or node CIDR ranges and control traffic between pods and specific cluster nodes (for example, allowing ingress from control plane nodes to a custom webhook pod, or restricting pod egress to control plane nodes). For instructions, see [Create an intra-project policy for standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic#create-standard-cluster-intra).

### Scale considerations

When configuring project network policies to target specific nodes or using broad CIDR ranges, your policy configuration choices might affect scalability and performance:

  * **Behavior of`0.0.0.0/0`**: Using a broad CIDR range such as `0.0.0.0/0` in an `ipBlocks` rule matches all nodes in the cluster, in addition to external IP addresses.
  * **Scale** : Each node in the cluster is assigned a unique CIDR identity. Each workload endpoint (VM or pod) has an internal policy table that stores its network rules. In large clusters, broad `ipBlocks` rules such as `0.0.0.0/0` increase policy table usage in proportion to the number of nodes because the system must create entries for every unique node CIDR identity.
  * **Warning** : Avoid using overly broad CIDR ranges in `ipBlocks` rules if you have a high node count or many complex policies, because you risk hitting the policy table limit for an endpoint. If an endpoint hits this limit, new network policies fail to apply, which can disrupt network connectivity or prevent policy enforcement for that workload.



## What's next

  * [Create intra-project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/intra-project-traffic)
  * [Create cross-project network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/cross-project-traffic)
  * [Create organization-external network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/organization-external-traffic)
  * [Create allow-all network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/allow-all-traffic)
  * [Create explicit deny network policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/deny-traffic)
  * [Create network policies for managed services](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pnp/policy-managed-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
