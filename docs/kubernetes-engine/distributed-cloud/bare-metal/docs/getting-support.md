---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support/
title: Get support \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:03.984620+00:00
---

# Get support  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Get support Stay organized with collections  Save and categorize content based on your preferences. 

Google's primary support objective is to resolve production incidents as quickly as possible. We do this by understanding your configuration, analyzing logs and metrics, and collaborating with partners to solve incidents quickly.

[Cloud Customer Care](https://docs.cloud.google.com/support) offers various support packages to accommodate your support needs. All Cloud Customer Care packages include support for GKE and Google Distributed Cloud. If you have an existing Cloud Customer Care support package, then you already have support for GKE and Google Distributed Cloud.

For more information, see the [Cloud Customer Care hub](https://cloud.google.com/support-hub).

## Requirements for Google Distributed Cloud support

To effectively troubleshoot business-critical incidents, you must do the following:

  * Check that your environment is current and within the published end-of-support timeframes. For more information, see the Version Support Policy section.
  * Enable [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring) for system components. For more information, see the following Support tools section.



## Support tools

To troubleshoot a Google Distributed Cloud incident, Cloud Customer Care relies on three pieces of information:

  * Your environment configuration
  * Logs from your clusters
  * Metrics from your clusters



### Your environment configuration

When you open a support case, provide key information about your cluster setup by running the following commands:

  * For all your cluster types, capture information about Kubernetes and your nodes by running the `bmctl check cluster --snapshot` command. Attach the resulting tar file to the support case.

  * For admin, hybrid, and standalone clusters, check the health status of the cluster and nodes by running the `bmctl check cluster` command. Attach the resulting logs to the support case. The logs should exist under the `bmctl-workspace/[CLUSTER_NAME]/log/check-cluster-[TIMESTAMP]` directory.

  * For user clusters, first create a health check YAML file with the cluster name and namespace, and then apply the file in the appropriate admin cluster:

    1. Create a YAML file with the following `healthcheck` properties. The following is sample content for a cluster named `user1` in the `cluster-user1` namespace:
           
           apiVersion: baremetal.cluster.gke.io/v1
           kind: HealthCheck
           metadata:
             generateName: healthcheck-
             namespace: cluster-user1
           spec:
             clusterName: user1
           

    2. After you create the YAML file, apply the custom resource in the admin cluster that's managing the user cluster by using the `kubectl` command. The following is a sample command that uses the YAML file created in the previous step. In the sample, the `ADMIN_KUBECONFIG` variable specifies the path to the admin cluster's kubeconfig file:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG create -f healthcheck-user1.yaml
           

The command returns the following response:
           
           healthcheck.baremetal.cluster.gke.io/healthcheck-7c4qf created
           

    3. Wait until the health check job is completed. To do so, test to see if the health check job finished reconciling. In the previous example case, the health check job name is `healthcheck.baremetal.cluster.gke.io/healthcheck-7c4qf`. The following is a sample test that uses the `kubectl` command, and it waits 30 minutes for the health check job to complete:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG wait healthcheck healthcheck-7c4qf \
               -n cluster-user1 --for=condition=Reconciling=False --timeout=30m
           

When the health check job is complete, the preceding `kubectl` command returns:
           
           healthcheck.baremetal.cluster.gke.io/healthcheck-7c4qf condition met
           

You can see the health check job results with the following command:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG get healthcheck healthcheck-7c4qf \
               -n cluster-user1
           

The command returns the following result:
           
           NAME                PASS   AGE
           healthcheck-7c4qf   true   17m
           

    4. Gather all the logs for the health check job Pod into a local file by using the `kubectl` command. The following is an example that uses the previous sample health check job:
           
           kubectl --kubeconfig ADMIN_KUBECONFIG logs -n cluster-user1 \
               -l baremetal.cluster.gke.io/check-name=healthcheck-7c4qf --tail=-1 > \
               healthcheck-7c4qf.log
           




### Cluster logs

When you create a new Google Distributed Cloud cluster, Cloud Logging agents are enabled by default and scoped only to system-level components. This replicates system-level logs into the Google Cloud project associated with the cluster. System-level logs are from Kubernetes Pods in the following namespaces:

  * `kube-system`
  * `gke-system`
  * `gke-connect`
  * `istio-system`
  * `config-management-system`
  * `gatekeeper-system`
  * `cnrm-system`
  * `knative-serving`



You can query logs from the [Logs Explorer](https://console.cloud.google.com/logs/query).

**Note:** If Cloud Logging is disabled, support is offered on a best-effort basis only, and could require significant additional effort from your on-site engineering team.

For more details, see [Configure logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring).

### Google Cloud CLI and remote cluster access

If you open a support case, Cloud Customer Care might ask you for remote read-only access to your clusters to help diagnose and resolve issues more effectively. For Cloud Customer Care to have sufficient access to troubleshoot your cluster issue remotely, ensure that you've installed and updated to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). The Google Cloud CLI must be at version 401.0.0 or higher to give Cloud Customer Care the needed permissions. We recommend that you update Google Cloud CLI regularly to pick up added permissions and other enhancements.

To install the latest components of the gcloud CLI, use the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command. For more information about giving Cloud Customer Care remote read-only access to your clusters, see [Remote GKE Cluster Support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-access).

## Cluster metrics

In addition to logs, the Cloud Monitoring agent also captures metrics. This replicates system-level metrics into the Google Cloud project associated with the cluster. System-level metrics are from Kubernetes Pods that run in the same namespaces that are listed in the Cluster logs section.

**Note:** If Cloud Monitoring is disabled, support is offered on a best-effort basis only, and could require significant additional effort from your on-site engineering team.

For more details, see [Configure logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring).

## How we troubleshoot your environment

Here is an example of a typical support incident:

  1. The cluster administrator opens a support case in Google Cloud console with [Cloud Customer Care](https://cloud.google.com/support-hub). They then select GKE and Google Distributed Cloud as **Category** and **Component** , respectively. They enter the required information and attach the output of relevant `bmctl` commands to the case.

  2. The support case is routed to a Technical Support Engineer who specializes in Google Distributed Cloud.

  3. The support engineer examines the contents of the snapshot to gain context of the environment.

  4. The support engineer examines the logs and metrics in the Google Cloud project. They enter the support case ID as the business justification, which is logged internally.

  5. The support engineer responds to the case with an assessment and recommendation. The support engineer and the user continue troubleshooting until they come to a resolution.




## What does Google support?

Generally, Cloud Customer Care supports all software components shipped as part of Google Distributed Cloud and Cloud Service Mesh, Policy Controller, Config Sync, and Config Controller. The following table provides a more complete list of what is and isn't supported:

Google Cloud supported | Not supported  
---|---  
Kubernetes and the container runtime | Customer choice of load balancer (manual load balancing)  
Connect and the Connect Agent | Customer code (see Developer Support)  
Google Cloud operations, Monitoring, Logging, and agents | Customer choice of operating system  
Bundled load balancer | Physical or virtual server, storage, and network  
Ingress controller | External DNS, DHCP, and identity systems  
GKE Identity Service |   
Cloud Service Mesh |   
Policy Controller |   
Config Sync |   
Config Controller |   
  
## Version Support Policy

The objective of this Version Support Policy is to give you the flexibility to schedule upgrades when it meets your business needs, while balancing the rapid evolution of both Kubernetes and Google Distributed Cloud.

Google Distributed Cloud software only follows the Kubernetes versioning scheme and release cycle. Minor releases happen approximately three times per year. Patches for each supported minor version occur approximately monthly. Like Kubernetes, Google Distributed Cloud supports the latest three minor versions concurrently.

Google supports each Google Distributed Cloud minor version for the later of:

  * 12 months after the initial release of the minor version.
  * The release of the third subsequent minor version.



For example, minor version 1.33 released on September 02, 2025. This minor version and all of its patches are supported until either September 02, 2026 or the release date of minor version 1.36, whichever date is later.

We encourage you to maintain your Google Distributed Cloud environment with the product's latest minor release and [recommended patch version](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support#google_cloud_distributed).

This version support policy includes:

  * Break-fix support from Cloud Customer Care.
  * CVE security vulnerabilities to Kubernetes and related components.
  * General patches to Kubernetes and related components. 



When your version reaches end-of-life, you can continue to open cases to receive support for the following:

  * Help with technical issues.
  * Assistance with billing issues.
  * Guidance on product usage, including help with troubleshooting and testing.



Extended support can be conditionally approved as a one-time event, with version-pinning, and future upgrade timeline requirements. For additional information, reach out to the lead customer engineer for your account or the account manager. Alternatively, you can [file a support case](https://console.cloud.google.com/support) through Google Cloud console. Such requests are routed to the customer engineering group for your account.

### Support period

The following table shows the supported minor releases for Google Distributed Cloud and the earliest end-of-life (EOL) dates:

Google Distributed Cloud version | Release date | End-of-life date*  
---|---|---  
1.35 | 2026-04-29 | 2027-04-29 or 1.38 release date  
1.34 | 2025-12-11 | 2026-12-11 or 1.37 release date  
1.33 | 2025-09-02 | 2026-09-02 or 1.36 release date  
1.32 | 2025-05-06 | 2026-05-06 or 1.35 release date  
  
* The EOL will be the later of these two dates.

To learn more version compatibility for Google Distributed Cloud and related Google Cloud products, see [Version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support).

### Versioning scheme

Google Distributed Cloud uses Kubernetes [semantic versioning](https://semver.org/) to refer to supported Kubernetes versions, but appends a GKE patch version. This results in a version number of the form: `x.y.z-gke.N`.

Kubernetes major version (x)
    Major versions are typically incremented if any backwards incompatible changes are introduced to the public API. A major version increments the Kubernetes version from `x.y` to `x+1.y`.
Kubernetes minor version (y)
    Kubernetes releases a new minor version [three times a year](https://github.com/kubernetes/kubernetes/releases). Each release cycle is approximately 15 weeks long. [Deprecated APIs](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) might be removed with a new minor version. A minor version increments the Kubernetes version from `1.y` to `1.y+1`; for example, Kubernetes 1. **29** is the minor release that follows Kubernetes 1.**28**.
Google Distributed Cloud patch release (z-gke.N)
    A patch release, such as 1.28.**300-gke.131** , increments the patch version (z) by 100 and includes a `-gke.N` suffix, which indicates the build. Patch releases include security updates and bug fixes. A Google Distributed Cloud patch release version doesn't correlate to a Kubernetes patch version.

## Shared responsibility model

Running a business-critical production application on Google Distributed Cloud requires multiple parties to carry different responsponsibilities. Although they aren't an exhaustive list, the following sections list the roles and responsibilities of different parties.

### Google responsibilities

  * Maintenance and distribution of the Google Distributed Cloud software package.
  * Notifying users of available upgrades for Google Distributed Cloud, and producing upgrade scripts for the previous version.

Google Distributed Cloud supports sequential cluster upgrades only (example: 1.34 → 1.35 → 1.36, but not 1.34 → 1.36). When you upgrade node pools, in some cases, you can skip a minor version. For more information about upgrade logic, see [Version rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-lifecycle#version_rules).

  * Operating the Connect and Cloud Operations services.

  * Troubleshooting, providing workarounds, and correcting the root cause of any issues related to Google-provided components.




### User responsibilities

  * Overall system administration for on-premises clusters.
  * Maintaining any application workload deployed on the cluster.
  * Running, maintaining, and patching the data center infrastructure, including networking, servers, operating system, storage, and connectivity to Google Cloud.
  * Running, maintaining, and patching network load balancers if manual load balancer option is chosen.
  * Upgrading Google Distributed Cloud versions regularly.
  * Monitoring of the cluster and applications, and responding to any incidents.
  * Ensuring Cloud Operations agents are deployed to clusters.
  * Providing Google with environmental details for troubleshooting purposes.



## Developer support

Google doesn't provide support specifically for your application workloads. However, we do provide _best-effort_ developer support to ensure your developers can run applications on Google Distributed Cloud. We believe that engaging earlier during development can prevent critical incidents later in the deployment.

This _best-effort_ developer support is available to customers with any paid support package and is treated as a P3 priority for an issue blocking a launch, or a P4 priority for general consultation. In this classification, priority level 0 is the highest priority.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
