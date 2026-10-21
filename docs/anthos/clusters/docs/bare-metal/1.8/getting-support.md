---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/getting-support/
title: Get support \u00a0|\u00a0 Anthos on bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:45.356899+00:00
---

# Get support  |  Anthos on bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/getting-support/

**Version 1.8**. This version is no longer supported. For information about how to upgrade to version 1.9, see [ Upgrading Anthos on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/how-to/upgrade) in the 1.9 documentation. For more information about supported and unsupported versions, see the [Version history](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on bare metal 1.8 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8)
  * [ Support ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/support)



Send feedback 

#  Get support Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.8 (unsupported)keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/getting-support)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/getting-support#version-support)



Google's primary support objective is to resolve production incidents as quickly as possible. We do this by understanding your configuration, analyzing logs and metrics, and collaborating with partners to solve incidents quickly.

Google Cloud offers a variety of support packages to accommodate your support needs. All Google Cloud Support packages include support for GKE Enterprise and Google Distributed Cloud. If you have an existing Google Cloud Support package, then you already have support for GKE Enterprise and Google Distributed Cloud.

For more information, see the [Cloud Customer Care](https://docs.cloud.google.com/support) documentation.

## Requirements for Google Distributed Cloud support

To troubleshoot business-critical incidents effectively:

  * Check that your environment is current and within the published end-of-support timeframes. See the Version Support Policy section for more information.
  * Enable [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) for system components. For details, see the following Support tools section.



## Support tools

To troubleshoot an Google Distributed Cloud incident, Google Cloud Support relies on three pieces of information:

  * Your environment configuration
  * Logs from your clusters
  * Metrics from your clusters



### Your environment configuration

When you open a support case, running the following commands provides key information about your cluster setup:

  * For all your cluster types, run `bmctl check cluster --snapshot` command to capture information about Kubernetes and your nodes. Attach the resulting tarball to the support case.

  * For admin, hybrid, and standalone clusters, run the `bmctl check cluster` command to check the health status of the cluster and nodes. Attach the resulting logs to the support case. They should exist under the `bmctl-workspace/[CLUSTER_NAME]/log/check-cluster-[TIMESTAMP]` directory.

  * For user clusters, first create a health check YAML file with the cluster name and namespace, and then apply the file in the appropriate admin cluster:

    1. Create a YAML file with the following `healthcheck` properties. Here is sample content for a cluster named `user1` in the `cluster-user1` namespace:
           
           apiVersion: baremetal.cluster.gke.io/v1
           kind: HealthCheck
           metadata:
             generateName: healthcheck-
             namespace: cluster-user1
           spec:
             clusterName: user1
           

    2. After you create the YAML file, apply the custom resource in the admin cluster that is managing the user cluster with the `kubectl` command. Here is a sample command using the YAML file created in the previous step. In the sample, the `ADMIN_KUBECONFIG` variable specifies the path to the admin cluster's kubeconfig file:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG create -f healthcheck-user1.yaml

The command returns the following response:
           
           healthcheck.baremetal.cluster.gke.io/healthcheck-7c4qf created
           

    3. Wait until the health check job is completed by testing to see if the health check job has finished reconciling. In the previous example case, the health check job name is `healthcheck.baremetal.cluster.gke.io/healthcheck-7c4qf`. Here is a sample test with the `kubectl` command that waits 30 minutes for the health check job to complete:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG wait healthcheck healthcheck-7c4qf \
               -n cluster-user1 --for=condition=Reconciling=False --timeout=30m

When completed, this command returns:
           
           healthcheck.baremetal.cluster.gke.io/healthcheck-7c4qf condition met
           

You can see the health check job results with the following command:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG get healthcheck healthcheck-7c4qf \
               -n cluster-user1

The command returns the following result:
           
           NAME                PASS   AGE
           healthcheck-7c4qf   true   17m
           

    4. Gather all the health check job pods's logs into a local file with the `kubectl` command. Here's an example using the previous sample health check job:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG logs -n cluster-user1 \
               -l baremetal.cluster.gke.io/check-name=healthcheck-7c4qf --tail=-1 > \
               healthcheck-7c4qf.log




### Cluster logs

When you create a new Google Distributed Cloud cluster, Cloud Logging agents are enabled by default and scoped only to system-level components. This replicates system-level logs into the Google Cloud project associated with the cluster. System-level logs are from Kubernetes pods in the following namespaces:

  * `kube-system`
  * `gke-system`
  * `gke-connect`
  * `istio-system`
  * `config-management-system`
  * `gatekeeper-system`
  * `cnrm-system`
  * `knative-serving`



Logs can be queried from the [Cloud Logging console](https://console.cloud.google.com/logs/query).

**Note:** If Cloud Logging is disabled, support is offered on a best-effort basis only, and could require significant additional effort from your on-site engineering team.

For more details, see [Logging and Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/log-monitoring).

## Cluster metrics

In addition to logs, metrics are also captured by the Cloud Monitoring agent. This replicates system-level metrics into the Google Cloud project associated with the cluster. System-level metrics are from Kubernetes pods running in the same namespaces listed in Logs.

**Note:** If Cloud Monitoring is disabled, support is offered on a best-effort basis only, and could require significant additional effort from your on-site engineering team.

For more details, see [Logging and Monitoring](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/how-to/log-monitoring).

## How we troubleshoot your environment

Here is an example of a typical support incident:

  1. Someone—-for example, the cluster administrator—-opens a support case via Google Cloud console or the Google Cloud Support Center, and selects GKE Enterprise and Google Distributed Cloud as Category and Component, respectively. They enter the information required and attach the output of relevant `bmctl` commands to the case.
  2. The support case is routed to a Technical Support Engineer specializing in Google Distributed Cloud.
  3. The support engineer examines the contents of the snapshot to gain context of the environment.
  4. The support engineer examines the logs and metrics in the Google Cloud project, entering the support case ID as the business justification, which is logged internally.
  5. The support engineer responds to the case with an assessment and recommendation. The support engineer and the user continue troubleshooting until they come to a resolution.



## What does Google support?

Generally, the Cloud Support team supports all software components shipped as part of Google Distributed Cloud as well as Anthos Service Mesh and Anthos Config Management. The table below details this further:

Google Cloud supported | Not supported  
---|---  
Kubernetes and the container runtime | Customer choice of load balancer (manual load balancing)  
Connect and the Connect Agent | Customer code (see Developer Support below)  
Google Cloud operations, Monitoring, Logging, and agents | Customer choice of operating system  
Bundled load balancer | Physical or virtual server, storage, and network  
Ingress controller | External DNS, DHCP, and identity systems  
GKE Identity Service |   
Cloud Service Mesh |   
Config Management |   
  
## Version Support Policy

Support for Google Distributed Cloud follows the [Anthos Version Support Policy](https://docs.cloud.google.com/anthos/docs/support/getting-support#version_support_policy). Google supports the current version and the previous two (n-2) minor versions of Google Distributed Cloud.

The following table shows the supported and unsupported versions of this product.

**Minor version** | **Release date** | **Earliest end of life date** | **Available patches** | **Kubernetes version**  
---|---|---|---|---  
[1.28 (latest)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver) | December 15, 2023 | December 15, 2024 | 1.28.400-gke.77 | v1.28.7-gke.1700  
1.28.300-gke.131 | v1.28.7-gke.1700  
1.28.200-gke.118 | v1.28.5-gke.1200  
1.28.100-gke.146 | v1.28.5-gke.1200  
1.28.0-gke.435 | v1.28.3-gke.700  
[1.16](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver) | August 25, 2023 | August 25, 2024 | 1.16.8 | v1.27.12-gke.800  
1.16.7 | v1.27.10-gke.500  
1.16.6 | v1.27.9-gke.1200  
1.16.5 | v1.27.8-gke.1500  
1.16.4 | v1.27.7-gke.1400  
1.16.3 | v1.27.6-gke.2500  
1.16.2 | v1.27.4-gke.1600  
1.16.1 | v1.27.4-gke.1600  
1.16.0 | v1.27.4-gke.1600  
[1.15](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver) | April 27, 2023 | April 27, 2024 | 1.15.11 | v1.26.13-gke.1100  
1.15.10 | v1.26.13-gke.400  
1.15.9 | v1.26.12-gke.1200  
1.15.8 | v1.26.10-gke.1400  
1.15.7 | v1.26.9-gke.2400  
1.15.6 | v1.26.8-gke.200  
1.15.5 | v1.26.8-gke.200  
1.15.4 | v1.26.5-gke.2100  
1.15.3 | v1.26.5-gke.2100  
1.15.2 | v1.26.5-gke.1200  
1.15.1 | v1.26.2-gke.1001  
1.15.0 | v1.26.2-gke.1001  
[1.14 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver) | December 8, 2022 | December 8, 2023 | 1.14.11 | v1.25.14-gke.2400  
1.14.10 | v1.25.14-gke.2400  
1.14.9 | v1.25.13-gke.200  
1.14.8 | v1.25.10-gke.2100  
1.14.7 | v1.25.10-gke.2100  
1.14.6 | v1.25.10-gke.1200  
1.14.5 | v1.25.7-gke.1000  
1.14.4 | v1.25.7-gke.1000  
1.14.3 | v1.25.6-gke.1000  
1.14.2 | v1.25.5-gke.1001  
1.14.1 | v1.25.5-gke.1001  
1.14.0 | v1.25.3-gke.1400  
[1.13 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes-ver) | September 29, 2022 | August 17, 2023 | 1.13.10 | v1.24.14-gke.2100  
1.13.9 | v1.24.14-gke.1200  
1.13.8 | v1.24.11-gke.1000  
1.13.7 | v1.24.11-gke.1000  
1.13.6 | v1.24.9-gke.2500  
1.13.5 | v1.24.9-gke.2500  
1.13.4 | v1.24.9-gke.2500  
1.13.3 | v1.24.7-gke.1700  
1.13.2 | v1.24.7-gke.300  
1.13.1 | v1.24.5-gke.400  
1.13.0 | v1.24.2-gke.1900  
[1.12 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12/release-notes-ver) | June 29, 2022 | March 29, 2023 | 1.12.9 | v1.23.17-gke.300  
1.12.8 | v1.23.16-gke.100  
1.12.7 | v1.23.15-gke.2400  
1.12.6 | v1.23.13-gke.1700  
1.12.5 | v1.23.13-gke.1700  
1.12.4 | v1.23.11-gke.500  
1.12.3 | v1.23.10-gke.1000  
1.12.2 | v1.23.5-gke.1505  
1.12.1 | v1.23.5-gke.1505  
1.12.0 | v1.23.5-gke.1504  
[1.11 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.11/release-notes-ver) | March 21, 2022 | December 21, 2022 | 1.11.8 | v1.22.15-gke.3300  
1.11.7 | v1.22.14-gke.500  
1.11.6 | v1.22.8-gke.204  
1.11.5 | v1.22.8-gke.204  
1.11.4 | v1.22.8-gke.204  
1.11.3 | v1.22.8-gke.203  
1.11.2 | v1.22.8-gke.200  
1.11.1 | v1.22.8-gke.200  
1.11.0 | v1.22.8-gke.200  
[1.10 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.10/release-notes-ver) | December 10, 2021 | September 10, 2022 | 1.10.8 | v1.21.13-gke.202  
1.10.7 | v1.21.13-gke.202  
1.10.6 | v1.21.13-gke.201  
1.10.5 | v1.21.6-gke.1503  
1.10.4 | v1.21.6-gke.1503  
1.10.3 | v1.21.5-gke.1300  
1.10.2 | v1.21.5-gke.1300  
1.10.1 | v1.21.5-gke.1200  
1.10.0 | v1.21.5-gke.1200  
[1.9 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.9/release-notes-ver) | September 23, 2021 | June 23, 2022 | 1.9.8 | v1.21.13-gke.200  
1.9.7 | v1.21.6-gke.1503  
1.9.6 | v1.21.5-gke.1300  
1.9.5 | v1.21.5-gke.1300  
1.9.4 | v1.21.5-gke.1200  
1.9.3 | v1.21.5-gke.1200  
1.9.2 | v1.21.4-gke.201  
1.9.1 | v1.21.4-gke.201  
1.9.0 | v1.21.4-gke.200  
[1.8 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.8/release-notes-ver) | June 21, 2021 | March 21, 2022 | 1.8.9 | v1.20.9-gke.102  
1.8.8 | v1.20.9-gke.102  
1.8.7 | v1.20.9-gke.102  
1.8.6 | v1.20.9-gke.102  
1.8.5 | v1.20.9-gke.102  
1.8.4 | v1.20.9-gke.101  
1.8.3 | v1.20.9-gke.101  
1.8.2 | v1.20.8-gke.1500  
1.8.1 | v1.20.5-gke.1301  
1.8.0 | v1.20.5-gke.1301  
[1.7 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.7/release-notes-ver) | March 25, 2021 | December 25, 2021 | 1.7.7 | v1.19.14-gke.2201  
1.7.6 | v1.19.14-gke.2201  
1.7.5 | v1.19.14-gke.2201  
1.7.4 | v1.19.14-gke.400  
1.7.3 | v1.19.13-gke.100  
1.7.2 | v1.19.10-gke.1602  
1.7.1 | v1.19.7-gke.1200  
1.7.0 | v1.19.7-gke.1200  
[1.6 (unsupported)](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.6/release-notes-ver) | November 30, 2020 | August 30, 2021 | 1.6.4 | v1.18.20-gke.3000  
1.6.3 | v1.18.18-gke.100  
1.6.2 | v1.18.6-gke.6600  
1.6.1 | v1.18.6-gke.6600  
1.6.0 | v1.18.6-gke.6600  
  
To get added features and performance, upgrade to Anthos clusters on bare metal release 1.9. For information about how to upgrade, see [Upgrading Anthos on bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade).

## Supported features

This document lists the availability of features and capabilities for Google Distributed Cloud for supported releases. The table is not intended to be an exhaustive list, but it highlights some of the benefits of upgrading your clusters to the latest supported version.

Features listed as Preview are covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA products and features might have limited support, and changes to pre-GA products and features might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Preview offerings are intended for use in test environments only.

Features listed as [General Availability (GA)](https://cloud.google.com/products#general-availability) are fully supported, open to all customers, and ready for production use.

**Note:** For information about supported GKE Enterprise components and their compatibility, see [Anthos version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support).

Feature/capability | 1.15 (unsupported) | 1.16 | 1.28 | 1.29 (latest)  
---|---|---|---|---  
Admin cluster support for multiple user cluster versions | - | - | - | [Preview](https://cloud.google.com/products#product-launch-stages)  
Alerting policies | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages)  
VM Runtime on Google Distributed Cloud | GA | GA | GA | GA  
Azure Active Directory (AD) groups | GA | GA | GA | GA  
BGP-based Load Balancer support for IPv6 | GA | GA | GA | GA  
Binary Authorization | [Preview](https://cloud.google.com/products#product-launch-stages) | GA | GA | GA  
Bundled load balancing with BGP | GA | GA | GA | GA  
Cloud Audit Logging | GA | GA | GA | GA  
Cluster backup and restore CLI support | GA | GA | GA | GA  
Cluster Certificate Authorities (CAs) rotation | GA | GA | GA | GA  
Cluster node reset CLI support | GA | GA | GA | GA  
Cluster upgrade pause and resume | - | - | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages)  
containerd container runtime | GA | GA | GA | GA  
Control group v2 | GA | GA | GA | GA  
Custom Certificate Authorities | - | [Preview](https://cloud.google.com/products#product-launch-stages) | GA | GA  
Dataplane V2 Direct Server Return (DSR) load balancing forwarding mode | - | [Preview](https://cloud.google.com/products#product-launch-stages) | GA | GA  
Dynamic Flat IP with Border Gateway Protocol (BGP) | GA | GA | GA | GA  
Egress NAT gateway | GA | GA | GA | GA  
Flat IPv4 mode (static) | GA | GA | GA | GA  
Flat IPv6 support (BGP mode) | GA | GA | GA | GA  
GKE Identity Service v2 | - | - | [Preview](https://cloud.google.com/products#product-launch-stages) | GA  
IPv4/IPv6 Dual Stack | GA | GA | GA | GA  
KSA support | GA | GA | GA | GA  
Managed Collector for Google Cloud Managed Service for Prometheus | GA | GA | GA | GA  
Multi-Cluster Connectivity | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages)  
Multi-NIC for Pods | GA | GA | GA | GA  
Network Gateway for GDC | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages)  
Node problem detector | GA | GA | GA | GA  
Parallel node upgrades | GA | GA | GA | GA  
Parallel node pool upgrades | [Preview](https://cloud.google.com/products#product-launch-stages) | GA | GA | GA  
Performance Tuning Operator | - | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages) | [Preview](https://cloud.google.com/products#product-launch-stages)  
Private registry support for nodes | - | - | - | [Preview](https://cloud.google.com/products#product-launch-stages)  
Registry mirror support | GA | GA | GA | GA  
Secure computing mode (seccomp) | GA | GA | GA | GA  
Skip node pool version upgrade | - | - | [Preview](https://cloud.google.com/products#product-launch-stages) | GA  
SR-IOV networking | GA | GA | GA | GA  
Summary API metrics | GA | GA | GA | GA  
VPC Service Controls | [Preview](https://cloud.google.com/products#product-launch-stages) | GA | GA | GA  
Worker node pool upgrade rollback | - | - | - | [Preview](https://cloud.google.com/products#product-launch-stages)  
Workload identity | GA | GA | GA | GA  
  
## Shared Responsibility Model

Running a business-critical production application on Google Distributed Cloud requires multiple parties to carry different responsponsibilities. While not an exhaustive list, the sections below list the roles and responsibilities.

### Google responsibilities

  * Maintenance and distribution of the Google Distributed Cloud software package.
  * Notifying users of available upgrades for Google Distributed Cloud, and producing upgrade scripts for the previous version; Google Distributed Cloud supports sequential upgrades only (example: 1.2 → 1.3 → 1.4 and not 1.2 → 1.4).
  * Operating the Connect and Cloud Operations services.
  * Troubleshooting, providing workarounds, and correcting the root cause of any issues related to Google-provided components



### User responsibilities

  * Overall system administration for on-premises clusters.
  * Maintaining any application workload deployed on the cluster.
  * Running, maintaining, and patching the data center infrastructure, including networking, servers, operating system, storage, and connectivity to Google Cloud.
  * Running, maintaining, and patching network load balancers if manual load balancer option is chosen.
  * Upgrading Google Distributed Cloud versions regularly.
  * Monitoring of the cluster and applications, and responding to any incidents.
  * Ensuring Cloud Operations agents are deployed to clusters.
  * Providing Google with environmental details for troubleshooting purposes.



## Developer Support

Google does not provide support for application workloads running on Google Distributed Cloud. However, we do provide best-effort developer support to ensure your developers can easily run applications on Google Distributed Cloud. We believe that engaging earlier during development can prevent critical incidents later in the deployment.

This Developer Support is available to customers with a paid support package and is treated as a P3 priority for an issue blocking a launch, or a P4 priority for general consultation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
