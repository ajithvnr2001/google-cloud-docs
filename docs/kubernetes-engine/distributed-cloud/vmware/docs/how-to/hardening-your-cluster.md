---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/hardening-your-cluster/
title: Hardening your cluster's security \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:06.113317+00:00
---

# Hardening your cluster's security  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/hardening-your-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Hardening your cluster's security Stay organized with collections  Save and categorize content based on your preferences. 

With the speed of development in Kubernetes, there are often new security features for you to use. This document describes how to harden your Google Distributed Cloud clusters.

This document prioritizes high-value security mitigations that require your action at cluster creation time. Less critical features, secure-by-default settings, and those that can be enabled after cluster creation are mentioned later in the document. For a general overview of security topics, review [Security](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/security).

## Checklist

The following deployment checklist highlights best practices for hardening your GKE clusters platform deployment. For more information about each practice, see the sections in this document.

Deployment checklist | Description  
---|---  
**Identity and access control** | **Use vSphere account privileges:**  
Use a vSphere administrator account with minimal privileges. **Secure Google Cloud service accounts:**  
Minimize Google Cloud service account privileges. **Configure OpenID Connect (OIDC):**  
Configure OpenID Connect for user authentication. **Use Kubernetes namespaces and RBAC to restrict access:**  
Use namespaces with RBAC for administrative isolation and least privilege roles and entitlements.  
**Data protection** | **Encrypt vSphere virtual machines:**  
Set vSphere to encrypt the volumes used by Google Distributed Cloud. **Manage secrets:**  
Encrypt secrets at rest.  
**Network protection** | **Restrict network access to the control plane and nodes:**  
Set up controls to isolate and protect the control plane networks and nodes. **Use network policies to restrict traffic:**  
Implement network policies to restrict intra-cluster traffic.  
**Declarative security** | **Use Policy Controller:**  
Install Policy Controller for declarative security policy within your clusters.  
**Maintenance** | **Upgrades:**  
Make sure that you're running the latest version of Google Distributed Cloud. **Monitor security bulletins:**  
Check GKE security bulletins for the latest advice and guidance on versioning.  
**Monitoring and logging** | **Set options for logging:**  
Ensure logging is enabled and integrated into a SIEM solution.  
  
## Identity and access control

This section provides information on controlling access to your clusters.

### Use vSphere account privileges

The vCenter user account that you use to install Google Distributed Cloud must have sufficient privileges. For example, a user account that is assigned the vCenter's Administrator role has privileges for complete access to all vCenter objects and provides a Google Distributed Cloud cluster administrator with full access.

The [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) is recommended, granting only the necessary privileges to successfully install {product_name}}. We have [predefined the minimum set of privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#vcenter-user-account-privileges) needed to perform the installation, as well as the commands needed to grant these permissions.

### Secure Google Cloud service accounts

Google Distributed Cloud requires several [Google Cloud service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts). During installation, you bind Identity and Access Management roles to these service accounts. Those roles grant the service accounts specific privileges within your project. Some of the service accounts can be generated for you during installation.

### Configure authentication for cluster users

To configure user authentication for your cluster, you can use [OpenID Connect (OIDC)](https://openid.net/connect/) or [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/).

For more information, See [GKE Identity Service](https://docs.cloud.google.com/anthos/identity).

### Use Kubernetes namespaces and RBAC to restrict access

To give teams least-privilege access to Kubernetes, create Kubernetes [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) or environment-specific clusters. Assign cost centers and appropriate labels to each namespace for [accountability and chargeback](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering). Only give developers the level of access to their Namespaces that they need to deploy and manage their applications, especially in production.

Map the tasks that users need to complete against the cluster and define the permissions required to complete each task. To grant cluster- and namespace-level permissions, use Kubernetes [RBAC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/security#authentication_and_authorization).

Beyond the permissions for [Google Cloud service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts) used to install Google Distributed Cloud, IAM does not apply to Google Distributed Cloud clusters.

For more information, see the following documentation:

  * [Service accounts and keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts)
  * [Overview of the installation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview)
  * [vCenter user account privileges](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vsphere-requirements#vcenter-user-account-privileges)



## Data protection

This section provides information on protecting your data.

### Encrypt vSphere virtual machines

Google Distributed Cloud cluster nodes run on virtual machines (VMs) in your vSphere cluster. Google strongly recommends that you encrypt all data at rest. To do so on vSphere, follow the [VMware vSphere Hardening and Compliance page](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security/understanding-vsphere-hardening-and-compliance.html) and best practice guidance for [encrypting VMs](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-security/virtual-machine-encryption/virtual-machine-encryption-best-practices.html).

This must be done prior to the installation of Google Distributed Cloud.

### Manage secrets

To provide an extra layer of protection for sensitive data, such as Kubernetes Secrets stored in [etcd](https://kubernetes.io/docs/concepts/overview/components/#etcd), configure a secrets manager that is integrated with Google Distributed Cloud clusters.

If you are running workloads across multiple environments, you might prefer a solution that works for both Google Kubernetes Engine and Google Distributed Cloud. If you choose to use an external secrets manager, such as [HashiCorp Vault](https://www.hashicorp.com/products/vault/secrets-management), set it up prior to integrating your Google Distributed Cloud clusters.

You have several options for secrets management:

  * You can use Kubernetes Secrets natively in Google Distributed Cloud. We expect clusters to be using vSphere encryption for VMs as described earlier, which provides basic encryption-at-rest protection for secrets. Secrets are not further encrypted by default.
  * You can use an external secrets manager, such as HashiCorp Vault. You can authenticate to HashiCorp using either a Kubernetes service account or a Google Cloud service account.



## Network protection

This section provides information on protecting your network.

### Restrict network access to the control plane and nodes

Limit exposure of your cluster control plane and nodes to the internet. These choices cannot be changed after cluster creation. By default, Google Distributed Cloud cluster nodes are created using [RFC 1918](https://tools.ietf.org/html/rfc1918) addresses, and it is best practice to not change this. Implement firewall rules in your on-premises network to restrict access to the control plane.

### Use network policies to restrict traffic

By default, all Services in a Google Distributed Cloud cluster can communicate with each other. For information about controlling Service-to-Service communication as needed for your workloads, see the following sections.

Restricting network access to services makes it much more difficult for attackers to move laterally within your cluster and offers services some protection against accidental or deliberate denial of service. There are two recommended ways to control traffic:

  * To control L7 traffic to your applications' endpoints, use [Istio](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-install). Choose this if you're interested in load balancing, service authorization, throttling, quota, and metrics.
  * To control L4 traffic between Pods, use Kubernetes [network policies](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/). Choose this if you're looking for the basic access control capabilities managed by Kubernetes.



You can enable both Istio and Kubernetes network policy after you create your Google Distributed Cloud clusters. You can use them together if you need to.

For more information, see the following documentation:

  * [vSphere network](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/network)
  * [Proxy and firewall rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/firewall-rules)



## Declarative security

This section provide recommendations for securing your clusters.

### Use Policy Controller

Kubernetes [admission controllers](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/) are plugins that govern and enforce how a Kubernetes cluster is used. Admission controllers are an important part of the defence-in-depth approach to hardening your cluster.

The best practice is to use [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller). Policy Controller uses the [OPA Constraint Framework](https://github.com/open-policy-agent/frameworks/tree/master/constraint) to describe and enforce policy as CRDs. The constraints that you apply to your cluster are defined in constraint templates, which are deployed in your clusters.

For information about how to use Policy Controller constraints to achieve many of the same protections as [PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies), with the added ability to test your policies before enforcing them, see [Using constraints to enforce Pod security](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-constraints-to-enforce-pod-security).

For more information, see the following documentation:

  * [Using constraints to enforce pod security](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-constraints-to-enforce-pod-security)



### Restrict the ability for workloads to self-modify

Certain Kubernetes workloads, especially system workloads, have permission to self-modify. For example, some workloads vertically autoscale themselves. While convenient, this can allow an attacker who has already compromised a node to escalate further in the cluster. For example, an attacker could have a workload on the node change itself to run as a more privileged service account that exists in the same namespace.

Ideally, workloads shouldn't be granted the permission to modify themselves in the first place. When self-modification is necessary, you can limit permissions by applying Gatekeeper or Policy Controller constraints, such as [NoUpdateServiceAccount](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/general/noupdateserviceaccount) from the open source Gatekeeper library, which provides several useful security policies.

When you deploy policies, it is usually necessary to allow the controllers that manage the cluster lifecycle to bypass the policies and the logging and monitoring pipelines. This is necessary so that the controllers can make changes to the cluster, such as applying cluster upgrades. For example, if you deploy the `NoUpdateServiceAccount` policy on Google Distributed Cloud, you must set the following parameters in the `Constraint`:
    
    
    parameters:
      allowedGroups:
      - system:masters
      allowedUsers:
      - system:serviceaccount:kube-system:monitoring-operator
      - system:serviceaccount:kube-system:stackdriver-operator
      - system:serviceaccount:kube-system:metrics-server-operator
      - system:serviceaccount:kube-system:logmon-operator
    

## Maintenance

This section provides information on maintaining your clusters.

### Upgrade Google Distributed Cloud

Kubernetes regularly introduces new security features and provides security patches.

You are responsible for keeping your Google Distributed Cloud clusters up to date. For each release, review the [release notes](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/release-notes). Additionally, plan to update to new patch releases every month and minor versions every three months. Learn how to [upgrade your clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

You are also responsible for upgrading and securing the vSphere infrastructure:

  * Establish a process to [undertake timely patching and upgrades](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new.html) of your VMs
  * Keep up to date with the latest [VMware security advisories](https://www.vmware.com/security/advisories.html)
  * Follow the guidance on [applying patches to hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/managing-host-and-cluster-lifecycle/about-vsphere-lifecycle-manager-new.html)



### Monitor security bulletins

The GKE security team publishes [security bulletins](https://docs.cloud.google.com/kubernetes-engine/security-bulletins) for high and critical severity vulnerabilities.

These bulletins follow a common Google Cloud vulnerability numbering scheme and are linked from the main Google Cloud bulletins page and the Google Distributed Cloud release notes. Each security bulletin page has an RSS feed where users can subscribe to updates.

When customer action is required to address these high and critical vulnerabilities, Google contacts customers by email. In addition, Google might also contact customers with support contracts through support channels.

For more information, see the following documentation:

  * [Upgrading Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading)



## Monitoring and logging

Google Distributed Cloud includes multiple options for cluster logging and monitoring, including cloud-based managed services, open source tools, and validated compatibility with third-party commercial solutions:

  * Cloud Logging and Cloud Monitoring, enabled by in-cluster agents deployed with Google Distributed Cloud
  * Validated configurations with third-party solutions



Whichever logging solution you choose based on business requirements, we strongly advise logging forward-relevant events and alerts to a centralized security information and event management (SIEM) service for management of security incidents.

For more information, see the following documentation:

  * [Logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring)
  * [Using logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring)
  * [Application logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/application-logging-monitoring)
  * [Monitoring Google Distributed Cloud with the Elastic Stack](https://docs.cloud.google.com/solutions/partners/monitoring-gke-on-prem-with-the-elastic-stack)
  * [Stream logs from Google Cloud to Splunk](https://docs.cloud.google.com/solutions/logging-anthos-with-splunk-connect)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
