---
url: https://docs.cloud.google.com/vpc/docs/troubleshooting-policy-and-access-problems/
title: Troubleshoot policy and access problems \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:18.340858+00:00
---

# Troubleshoot policy and access problems  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/troubleshooting-policy-and-access-problems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot policy and access problems

This document provides an overview of Google Cloud access policy enforcement controls and the tools that are available to help troubleshoot access problems. This document is for support teams who want to help customers in their organization to resolve issues related to accessing their Google Cloud resources.

## Google Cloud access policy enforcement controls

This section describes the policies that you or your organization administrator can implement that affect access to your Google Cloud resources. You implement access policies by using all or some of the following products and tools.

### Labels, tags, and network tags

Google Cloud offers several [ways to label and group resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources). You can use labels, tags, and network tags to help enforce policies.

[Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) are key-value pairs that help you organize your Google Cloud resources. [Many Google Cloud services](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#label_support) support labels. You can also use labels to filter and group resources for other use cases, for example, to identify all the resources that are in a test environment as opposed to resources that are in production. In the context of policy enforcement, labels can identify where resources should be located. For example, the access policies that you apply to resources that are labeled as test are different from the access policies that you apply to resources that are labeled as production resources.

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are key-value pairs that provide a mechanism for identifying resources and applying policy. You can attach tags to an organization, folder, or project. A tag applies to all resources at the hierarchy level that the tag is applied to. You can use tags to conditionally allow or deny access policies based on whether a resource has a specific tag. You can also [use tags with firewall policies](https://docs.cloud.google.com/vpc/docs/tags-firewalls-overview) to control traffic in a Virtual Private Cloud (VPC) network. Understanding how tags are inherited and combined with access and firewall policies is important in troubleshooting.

[Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) are different from the preceding resource manager tags. Network tags apply to VM instances, and they are another way that you can control network traffic to and from a VM. On Google Cloud networks, network tags identify which VMs are subject to firewall rules and network routes. You can use network tags as source and destination values in firewall rules. You can also use network tags to identify which VMs a certain route applies to. Understanding network tags can help you to troubleshoot access problems because network tags are used to define network and routing rules.

### VPC firewall rules

You can configure [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to allow or deny traffic to and from your virtual machine (VM) instances and products built on VMs. Every VPC network functions as a distributed firewall. Although VPC firewall rules are defined at the network level, connections are allowed or denied on a per-instance basis. You can apply VPC firewall rules to the VPC network, VMs grouped by tags, and VMs grouped by service accounts.

### VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) provides a perimeter security solution that helps mitigate data exfiltration from Google Cloud services such as Cloud Storage and BigQuery. You create a service perimeter that creates a security boundary around Google Cloud resources, and you can manage what is allowed in and out of the perimeter. VPC Service Controls also provides context-aware access controls by implementing policies based on contextual attributes such as IP address and identity.

### Resource Manager

You use [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) to set up an [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) resource. Resource Manager provides tools that let you map your organization and the way you develop applications to a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Along with helping you to group resources logically, Resource Manager provides attach points and inheritance for access control and organization policies.

### Identity and Access Management

[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) lets you define _who_ (identity) has what _access_ (role) for _which resource_. An [IAM policy](https://docs.cloud.google.com/iam/docs/overview#cloud-iam-policy) is a collection of statements that defines who has what type of access, such as read or write access. The IAM policy is attached to a resource and the policy enforces access control whenever a user attempts to access the resource.

A feature of IAM is [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). When you implement IAM Conditions as part of your policy definition, you can choose to grant resource access to identities (principals) only if configured conditions are met. For example, you can use IAM Conditions to limit access to resources only for employees making requests from your corporate office.

### Organization Policy Service

The [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) lets you enforce constraints on [supported resources](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) across your organization hierarchy. Each resource that the Organization Policy supports has a set of constraints that describes the ways that the resource can be restricted. You define a policy that defines specific rules that restrict resource configuration.

The Organization Policy Service lets you as an authorized administrator override the default organization policies at the folder or project level as required. Organization policies focus on how you configure resources, while IAM policies focus on what permissions your identities have been granted to those resources.

### Quotas

[Google Cloud enforces quotas](https://docs.cloud.google.com/docs/quotas/overview) on resources, which sets a limit on how much of a particular Google Cloud resource your project can use. The number of projects that you have is also subject to a quota. The following types of resource usage are limited by quotas:

  * **Rate quota** , such as API requests per day. This quota resets after a specified time, such as a minute or a day.
  * **Allocation quota** _,_ such as the number of virtual machines or load balancers used by your project. This quota doesn't reset over time. An allocation quota must be explicitly released when you no longer want to use the resource, for example, by deleting a Google Kubernetes Engine (GKE) cluster.



If you reach an allocation quota limit, you can't start new resources. If you reach a rate quota, you can't complete API requests. Both of these issues can look like an access-related issue.

### Chrome Enterprise Premium

[Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) uses various Google Cloud products to enforce granular access control based on a user's identity and context of the request. You can configure Chrome Enterprise Premium to [restrict access to the Google Cloud console and to Google Cloud APIs](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis).

[Chrome Enterprise Premium access protection](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-protection) works by using the following Google Cloud services:

  * [**Identity-Aware Proxy (IAP)**](https://docs.cloud.google.com/iap/docs/concepts-overview): A service that verifies user identity and uses context to determine whether a user should be granted access to a resource.
  * [**IAM**](https://docs.cloud.google.com/iam/docs/overview): The identity management and authorization service for Google Cloud.
  * [**Access Context Manager**](https://docs.cloud.google.com/access-context-manager/docs/overview): A rules engine that enables fine-grained access control.
  * [**Endpoint Verification**](https://docs.cloud.google.com/endpoint-verification/docs/overview): A Google Chrome extension that collects user device details.



### IAM Recommender

IAM includes [Policy Intelligence](https://docs.cloud.google.com/policy-intelligence) tools that provide you with a comprehensive set of proactive guidance to help you to be more efficient and secure when using Google Cloud. Recommended actions are provided to you through notifications in the console, which you can apply directly or by using an event sent to a Pub/Sub topic.

[IAM Recommender](https://docs.cloud.google.com/iam/docs/recommender-overview) is part of the Policy Intelligence suite, and you can use it to help apply the principle of least privilege. Recommender compares project-level role grants with the permissions that each principal used during the past 90 days. If you grant a project-level role to a principal, and the principal doesn't use all of that role's permissions, then Recommender might recommend that you revoke the role. If necessary, Recommender also recommends less permissive roles as a replacement.

If you automatically apply a recommendation, you can inadvertently cause a user or service account to be denied access to a resource. If you decide to use automations, use the [IAM Recommender best practices](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-best-practices#automation-best-practices) to help you decide how much automation you are comfortable with.

### Kubernetes namespaces and RBAC

Kubernetes is operated as a managed service on Google Cloud as Google Kubernetes Engine (GKE). GKE can enforce policies that are consistent no matter where your GKE cluster is running. The policies that affect access to resources are a combination of built-in Kubernetes controls and Google Cloud specific controls.

In addition to VPC firewalls and VPC Service Controls, GKE uses namespaces, [role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control), and workload identities to manage policies that affect access to resources.

#### Namespaces

[Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) are virtual clusters that are backed by the same physical cluster, and they provide a scope for names. Names of resources must be unique within a namespace, but you can use the same name in different namespaces. Namespaces let you use [resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) to divide cluster resources between multiple users.

#### RBAC

RBAC includes the following features:

  * Fine-grained control over how users access the API resources that are running on your cluster. 
    * Lets you create detailed policies that define which operations and resources you allow users and service accounts to access.
    * Can control access for Google Accounts, Google Cloud service accounts, and Kubernetes service accounts.
  * Lets you create RBAC permissions that apply to your entire cluster or to specific namespaces within your cluster. 
    * **Cluster-wide permissions** are useful for limiting access to specific API resources for certain users. These API resources include security policies and secrets.
    * **Namespace-specific permissions** are useful if, for example, you have multiple groups of users who operate within their own respective namespaces. RBAC can help you ensure that users only have access to cluster resources within their own namespace.
  * A role that can only be used to grant access to resources within a single namespace.
  * A role that contains rules that represent a set of permissions. Permissions are purely additive, and there are no deny rules.



IAM and Kubernetes RBAC are integrated so that users are authorized to perform actions if they have sufficient permissions according to _either_ tool.

Figure 1 shows how to use IAM with RBAC and namespaces to implement policies.

[ ![](https://docs.cloud.google.com/static/vpc/images/troubleshooting-policy-and-access-problems-iam-gke.svg)](https://docs.cloud.google.com/static/vpc/images/troubleshooting-policy-and-access-problems-iam-gke.svg) IAM and Google Kubernetes Engine RBAC work together to control access to a GKE cluster (click to enlarge). 

Figure 1 shows the following policy implementations:

  1. At the project level, IAM defines roles for cluster administrators to manage clusters and to let container developers access APIs within clusters.
  2. At the cluster level, RBAC defines permissions on individual clusters.
  3. At the namespace level, RBAC defines permissions on namespaces.



#### Workload identity

In addition to RBAC and IAM, you also need to understand the impact of workload identities. [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) lets you configure a [Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) to act as a [Google service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts). Any application that runs as the Kubernetes service account automatically authenticates as the Google service account when accessing Google Cloud APIs. This authentication lets you assign fine-grained identity and authorization for applications in your cluster.

Workload Identity Federation for GKE relies on IAM permissions to control what Google Cloud APIs your GKE application can access. For example, if IAM permissions change, a GKE application might become unable to write to Cloud Storage.

## Troubleshooting tools

This section describes the tools that are available to help you troubleshoot your policies. You can use different products and features to apply a combination of policies. For example, you can use firewalls and subnets to manage communication between resources within your environment and within any security zones that you have defined. You can also use IAM to restrict who can access what within the security zone and any VPC Service Controls zones that you have defined.

### Logs

When a problem occurs, typically the first place to start troubleshooting is to look at logs. The Google Cloud logs that provide insight into access-related issues are Cloud Audit Logs, Firewall Rules Logging, and VPC Flow Logs.

#### Cloud Audit Logs

[Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) consists of the following audit log streams for each project, folder, and organization: Admin Activity, Data Access, and System Event. Google Cloud services write audit log entries to these logs to help you identify which user performed an action within your Google Cloud projects, where they did it, and when.

  * **Admin Activity logs** contain log entries for API calls or other administrative actions that modify the configuration or metadata of resources. Admin Activity logs are always enabled. For information about Admin Activity logs pricing and quotas, see the [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit#admin-activity).
  * **Data Access logs** record API calls that create, modify, or read user-provided data. Data Access audit logs are disabled by default, except for BigQuery. The Data Access logs can grow to be large, and can incur costs. For information about Data Access logs usage limits, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas). For information about potential costs, see [Pricing](https://cloud.google.com/stackdriver/pricing).
  * **System Event logs** contain log entries for when Compute Engine performs a system event. For example, each [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration) is recorded as a system event. For information about System Event logs pricing and quotas, see the [Cloud Audit Logs overview.](https://docs.cloud.google.com/logging/docs/audit#admin-activity)



In [Cloud Logging](https://docs.cloud.google.com/logging), the `protoPayload` field contains an [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) object that stores the audit logging data. For an example of an audit log entry, see the [sample audit log entry](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#sample).

To view [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity), you must have either the Logs Viewer role (`roles/logging.viewer`) or the basic Viewer role (`roles/viewer`). Where possible, select the role with the least privileges required to complete the task.

Individual audit log entries are stored for a [specified length of time](https://docs.cloud.google.com/logging/docs/audit#audit_log_retention). For longer retention, you can export the log entries to Cloud Storage, BigQuery, or Pub/Sub. To export log entries from all the projects, folders, and billing accounts of your organization, you can use [aggregated exports](https://docs.cloud.google.com/logging/docs/export/aggregated_exports). Aggregated exports provide you with a centralized way to review logs across the organization.

To use your audit logs to help with troubleshooting, do the following:

  * Ensure that you have the required IAM roles to view the logs. If you export the logs, you also need permissions to [view the exported logs](https://docs.cloud.google.com/logging/docs/export/using_exported_logs) in the sink.
  * Follow the [best practices for using audit logs](https://docs.cloud.google.com/logging/docs/audit/best-practices) to meet your audit strategy.
  * Select a team strategy to view logs. There are [several ways to view logs](https://docs.cloud.google.com/monitoring/audit-logging#viewing_logs) in Cloud Audit Logs, and everyone on your troubleshooting team should use the same method.
  * Use the [Google Cloud console Activity page](https://console.cloud.google.com/logs) to get a high-level view of your activity logs.
  * View exported logs from the sink that they were exported to. Logs that are outside the retention period are only visible in the sink. You can also use exported logs to do a comparison investigation, for example, to a time when everything worked as expected.



#### Firewall Rules Logging

[Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) lets you audit, verify, and analyze the effects of your firewall rules. For example, you can determine if a firewall rule that is designed to deny traffic is functioning as intended.

You enable Firewall Rules Logging individually for each firewall rule whose connections you need to log. Firewall Rules Logging is an option for any firewall rule, regardless of the action (allow or deny) or direction (ingress or egress) of the rule. Firewall Rules Logging can generate a lot of data. [Firewall Rules Logging has a charge](https://cloud.google.com/compute/pricing#network_telemetry) associated with it, so you need to carefully plan what connections you want to log.

Determine where you want to store your firewall logs. If you want an organization-wide view of your logs, export the firewall logs to the same sink as your audit logs. Use [filters](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging#viewing_logs) to search for specific firewall events.

### Firewall Insights

[Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview) provides reports that contain information about firewall usage and the impact of various firewall rules on your VPC network. You can use Firewall Insights to verify that firewall rules allow or block their intended connections.

You can also use Firewall Insights to detect firewall rules that are shadowed by other rules. A _shadowed rule_ is a firewall rule that has all of its relevant attributes, such as IP address range and ports, overlapped by attributes from one or more other firewall rules that have higher or equal priority. Shadowed rules are calculated within 24 hours after you enable Firewall Rules Logging.

When you enable Firewall Rules Logging, Firewall Insights analyzes logs to suggest insights for any deny rule that is used in the observation period that you specify (by default, the last 24 hours). The deny rule insights provide you with firewall packet-drop signals. You can use the packet-drop signals to verify that the dropped packets are expected due to security protections, or that dropped packets are unexpected due to issues such as network misconfigurations.

#### VPC Flow Logs

[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) records a sample of network flows sent from and received by VM instances. VPC Flow Logs covers traffic that affects a VM. All egress (outgoing) traffic is logged, even if an egress deny firewall rule blocks the traffic. Ingress (incoming) traffic is logged if an ingress allow firewall rule permits the traffic. Ingress traffic isn't logged if an ingress deny firewall rule blocks the traffic.

Flow logs are collected for each VM connection at specific intervals. All the [sampled packets](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling) collected for a given interval for a given connection—an aggregation interval—are aggregated into a single flow log entry. The log flow entry is then sent to Cloud Logging.

VPC Flow Logs is enabled or disabled for each VPC subnet. When you enable VPC Flow Logs, it generates a lot of data. We recommend that you carefully manage the subnets that you enable VPC Flow Logs on. For example, we recommend that you don't enable flow logs for a sustained period on subnets that are used by development projects. You can [query VPC Flow Logs ](https://docs.cloud.google.com/vpc/docs/using-flow-logs#accessing_logs_via_logging) directly by using Cloud Logging or the exported sink. When you troubleshoot perceived traffic-related issues, you can use VPC Flow Logs to see whether traffic is leaving or entering a VM through the expected port.

### Alerting

Alerts let you get timely notification of any out-of-policy events that might affect access to your Google Cloud resources.

### Real-time notifications

[Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) keeps a five-week history of Google Cloud [asset](https://docs.cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview#asset) metadata. An asset is a [supported Google Cloud resource](https://docs.cloud.google.com/resource-manager/docs/cloud-asset-inventory/overview#supported_resource_types). Supported resources include IAM, Compute Engine with associated network features such as firewall rules and GKE namespaces, and role and cluster role bindings. All the preceding resources affect access to Google Cloud resources.

To monitor deviations from your resource configurations, such as firewall rules and forwarding rules, you can subscribe to [real-time notifications](https://docs.cloud.google.com/resource-manager/docs/cloud-asset-inventory/real-time-notifications). If your resource configurations change, real-time notifications immediately send a notification through [Pub/Sub](https://docs.cloud.google.com/pubsub/docs). Notifications can alert you to any issues early, preempting a support call.

### Cloud Audit Logs and Cloud Run functions

To complement the use of real-time notifications, you can monitor Cloud Logging and alert on calls to sensitive actions. For example, you can create a [Cloud Logging sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-create) that [filters](https://docs.cloud.google.com/logging/docs/view/advanced-filters) calls to the `SetIamPolicy` at the organization level. The sink sends logs to a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic-console#create_a_topic) that you can use to trigger [Cloud Run function](https://docs.cloud.google.com/functions/docs/calling/logging#functions_log_stackdriver-python).

### Connectivity Tests

To determine if an access problem is network-related or permission-related, use the Network Intelligence Center [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) tool. Connectivity Tests is a static configuration analyzer and diagnostics tool that lets you check connectivity between a source and destination endpoint. Connectivity Tests helps you identify the root cause for network-related access problems that are associated with your Google Cloud network configuration.

Connectivity Tests performs tests that include your VPC network, VPC Network Peering, and VPN tunnels to your on-premises network. For example, Connectivity Tests might identify that a firewall rule is blocking connectivity. For more information, see [Common use cases](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/common-use-cases).

### Policy Troubleshooter

Many tasks in Google Cloud require an IAM role and associated permissions. We recommend that you check what permissions are contained within a role and check for each permission that's required to complete a task. For example, to use Compute Engine images to create an instance, a user needs the [`compute.imageUser`](https://docs.cloud.google.com/compute/docs/access/iam#compute.imageUser) role, which includes nine permissions. Therefore, the user must have a combination of roles and permissions that include all nine permissions.

[Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access) is a Google Cloud console tool that helps you debug why a user or service account doesn't have permission to access a resource. To troubleshoot access problems, you use the IAM part of the Policy Troubleshooter.

For example, you might want to check why a particular user can create objects in buckets in a project while another user can't. The Policy Troubleshooter can help you see what permissions the first user has that the second user doesn't have.

The Policy Troubleshooter requires the following inputs:

  * Principal (individual user, service account, or groups)
  * Permission (note that these are the underlying permissions, not the IAM roles)
  * Resource



### IAM Recommender

Although IAM Recommender is a policy enforcement control as described in the previous Recommender section, you can also use it as a troubleshooting tool. Recommender runs a daily job that analyzes IAM access log data and the permissions granted from the previous 60 days. You can use Recommender to check whether a recommendation was approved and applied recently that could have affected a user's access to a previously allowed resource. In this case, you can grant the permissions that were removed.

## Escalating to Customer Care

When you troubleshoot access-related problems, it's important to have a good internal support process and a well-defined process for escalating to [Cloud Customer Care](https://docs.cloud.google.com/support). This section describes an example support setup and how you can communicate with Customer Care to help them resolve your issues quickly.

If you're unable to resolve a problem by using the tools described in this document, a clearly defined support process helps Customer Care to troubleshoot your issues. We recommend that you have a systematic approach to troubleshooting, as described in the [effective troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) chapter of Google's _Site Reliability Engineering (SRE)_ book.

We recommend that your internal support process does the following:

  * Detail the procedures to be followed if there is a problem.
  * Have a clearly defined escalation path.
  * Set up an on-call process.
  * Create an incident response plan.
  * Set up a bug tracking or help desk system.
  * Ensure that your support personnel have been authorized to communicate with Customer Care and are named contacts.
  * Communicate support processes to internal staff, including how to contact Google Cloud named contacts.
  * Regularly analyze support issues, iterate, and improve based on things that you learned.
  * Include a standardized retrospective form.



If you need to escalate to Customer Care, have the following information available to share with Customer Care when troubleshooting access issues:

  * The identity (user or service account email) that is requesting access. 
    * Whether this issue impacts all identities or only some.
    * If only some identities are impacted, provide an example identity that works and an example identity that fails.
  * Whether the identity was recently recreated.
  * The resource that the user is attempting to access (include project ID).
  * The request or method that is being called. 
    * Provide a copy of the request and response.
  * The permissions that were granted to the identity for this access. 
    * Provide a copy of the IAM policy.
  * The source (location) from which the identity is attempting to access resources. For example, if they are attempting access from a Google Cloud resource (such as a Compute Engine instance), the Google Cloud console, the Google Cloud CLI, Cloud Shell, or from an external source such as on-premises or internet. 
    * If the source is from another project, provide the source project ID.
  * The time (timestamp) when the error first occurred and whether it's still an issue.
  * The last known time that the identity successfully accessed the resource (include timestamps).
  * Any changes that were made before the issue started (include timestamps).
  * Any errors that are recorded in Cloud Logging. Before you share with Customer Care, make sure that you redact sensitive data such as access tokens, credentials, credit card numbers.



## What's next

For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
