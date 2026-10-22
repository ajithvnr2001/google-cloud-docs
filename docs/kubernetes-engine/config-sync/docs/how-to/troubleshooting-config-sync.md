---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync/
title: Introduction to troubleshooting \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:05.648986+00:00
---

# Introduction to troubleshooting  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Introduction to troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

If you're encountering difficulties with Config Sync, this page introduces you to some common tools and procedures that can help you identify and resolve problems that you experience.

## Upgrade to a supported version

Consider [upgrading Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/upgrade-config-sync) to a [supported version](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync#version_support_policy). Upgrading often resolves common problems and gives you access to the most current functionalities.

## Use the `nomos` command-line tool

The [`nomos` command-line tool](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command) provides essential insights into your Config Sync setup. The commands described in the following sections are particularly helpful when you're trying to determine the source of your problem or when you need to work with Cloud Customer Care.

### View Config Sync status

The [`nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) command provides you with aggregated data and errors to help you understand what's happening with your Config Sync installation. The following information is available with `nomos status`:

  * Installation status per cluster
  * Syncing errors (both reading from Git as well as reconciling the changes)



### Create a bug report

If you have a problem with Config Sync that requires help from [Cloud Customer Care](https://docs.cloud.google.com/support), you can provide them with valuable debugging information by using the [`nomos bugreport`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#bug) command.

This command generates a timestamped zip file with information on the Kubernetes cluster set in your `kubectl` context. The file also contains logs from Config Sync Pods. It doesn't contain information from the resources synced with Config Sync.

## View the overview dashboard

The [Config Sync dashboard](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/use-config-sync-dashboard) provides you with an overview of the status of the packages that Config Sync manages and the status of the resources in these packages. Exploring this dashboard can help you to get a quick overview of the status of your Config Sync installation and discover any packages that have issues.

  * To access the dashboard, in the Google Cloud console go to the **Config** page in the **Features** section:

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)




## Use monitoring and log analysis

Monitoring Config Sync and exploring its logs can help you determine the source of bugs and to better understand any unexpected behavior.

### Understand Config Sync metrics

Use [Config Sync metrics](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync) to gain visibility into the health of Config Sync.

### Monitor RootSync and RepoSync objects

When you install Config Sync using the Google Cloud console or Google Cloud CLI, Config Sync automatically creates a _RootSync_ object for you. When you [Configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories), you can create _RepoSync_ objects that contain configuration information about your namespace repositories.

Monitoring these objects can reveal valuable information about the state of Config Sync. To learn more, see [Monitor RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).

### Use service level indicators (SLIs)

To receive notifications when Config Sync isn't working as intended, [use Config Sync SLIs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/config-sync-slis).

### Query logs

You can use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to retrieve, view, and analyze log data for Config Sync. These logs can contain valuable historical data that isn't captured by `nomos bugreport` when the operator or reconciler Pods are restarted. For examples of queries that might help you diagnose your issue, see [Query Config Sync logs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/query-logs).

## Examine resources with the `kubectl` command-line tool

Config Sync is composed of multiple custom resources that you can query by using `kubectl` commands. These commands help you understand the status of each of Config Sync's objects.

You should know the following information about the Kubernetes resources that Config Sync manages:

  * `config-management-system` is the namespace we use to run all core system components of Config Sync.
  * `configmanagement.gke.io` and `configsync.gke.io` are the API groups we use for all custom resources.



### Examples

The following sections show you how you might use `kubectl` commands to examine Config Sync.

#### List custom resources

  * You can get a full list of the custom resources by running the following command:
        
        kubectl api-resources | grep -E "configmanagement.gke.io|configsync.gke.io"
        

  * Individual custom resources can be consumed by running the following command:
        
        kubectl get RESOURCE -o yaml.
        

Replace `RESOURCE` with the name of the resource that you want to query.

For example, the output of the following command lets you check the status of a RootSync object:
        
        kubectl get rootsync -n config-management-system -o yaml
        




#### Check an object's token annotation

You might want to know when a managed Kubernetes object was last updated by Config Sync. Each managed object is annotated with the hash of the Git commit when it was last modified, and the path to the config that contained the modification.

For example, to get the annotation of a ClusterRoleBinding named `namespace-readers`, run the following command:
    
    
    kubectl get clusterrolebinding namespace-readers
    

The output is similar to the following:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      annotations:
        configmanagement.gke.io/source-path: cluster/namespace-reader-clusterrolebinding.yaml
        **configmanagement.gke.io/token: bbb6a1e2f3db692b17201da028daff0d38797771**
      name: namespace-readers
    ...
    

For more information, see [labels and annotations](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/labels-and-annotations).

## Accelerate diagnosis with Gemini Cloud Assist

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Sometimes, the cause of your issue isn't immediately obvious, even after using the tools discussed in the preceding sections. Investigating complex cases can be time-consuming and requires deep expertise. For scenarios like this, Gemini Cloud Assist can help. It can automatically detect hidden patterns, surface anomalies, and provide summaries to help you quickly pinpoint a likely cause.

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

### Access Gemini Cloud Assist

To access Gemini Cloud Assist, complete the following steps:

  1. In the Google Cloud console, go to any page.
  2. In the Google Cloud console toolbar, click **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens. You can click example prompts if they are displayed, or you can enter a prompt in the **Enter a prompt** field.




### Explore example prompts

To help you understand how Gemini Cloud Assist can help you, here are some example prompts:

Theme | Scenario | Example prompt | How Gemini Cloud Assist can help  
---|---|---|---  
**Initial setup** | A platform engineer is setting up Config Sync for the first time so that they can manage GKE clusters from a Git repository. | How do I set up Config Sync to sync manifests from my GitHub repository to my GKE cluster? | Gemini Cloud Assist provides a step-by-step guide to setting up Config Sync, covering fleet registration and enabling the feature, and explaining details like repository URL, branch, path, and authentication methods (for example, `public`, `token`, or `ssh`).  
**Troubleshooting sync errors** | A developer commits a new manifest, but the resource fails to apply to the cluster, and the sync status shows an error code. | My Config Sync `RootSync` object shows "`KNV2009: the server could not find the requested resource`". What does this mean and how do I fix it? | Gemini Cloud Assist analyzes the error code, explaining that it generally indicates Config Sync cannot locate or interact with an expected Kubernetes resource. It then details common causes, including missing RBAC permissions, exceeding resource object size limits, incorrect directory paths, external inventory conflicts, and issues with unmanaged resources, providing specific troubleshooting steps for each cause.  
**Managing multiple teams** | An organization needs to allow application teams to manage their own configurations in specific namespaces without giving them access to the central platform repository. | What's the difference between a `RootSync` and a `RepoSync` object in Config Sync? When should I use `RepoSync`? | Gemini Cloud Assist explains the core difference between `RootSync` and `RepoSync` objects: `RootSync` objects are cluster-scoped and typically used by administrators for cluster-wide configurations, while `RepoSync` objects are namespace-scoped and designed for application teams to manage resources within a specific namespace, promoting delegation and multi-tenancy.Gemini Cloud Assist also details scenarios where `RepoSync` objects should be used, emphasizing its benefits for multi-tenancy and reducing the affected area of misconfigurations.  
**Proactive validation** | A developer wants to ensure their new manifest is valid before committing it to the repository to avoid breaking the sync in production. | How can I check my Kubernetes manifests for Config Sync errors on my local machine before I push them to the Git repository? | Gemini Cloud Assist explains how to check Kubernetes manifests for Config Sync errors by using the `nomos` command-line tool. It details how to use the `nomos vet` command for syntax validation and the `nomos hydrate` command for previewing rendered configurations from Kustomize or Helm. Gemini Cloud Assist also outlines a recommended workflow to integrate these checks before pushing to Git.  
  
For more information, see the following resources:

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Read the [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



### Use Gemini Cloud Assist Investigations

In addition to interactive chat, Gemini Cloud Assist can perform more automated, in-depth analysis through Gemini Cloud Assist Investigations. This feature is integrated directly into workflows like Logs Explorer, and is a powerful root-cause analysis tool.

When you initiate an investigation from an error or a specific resource, Gemini Cloud Assist analyzes logs, configurations, and metrics. It uses this data to produce ranked observations and hypotheses about probable root causes, and then provides you with recommended next steps. You can also transfer these results to a Google Cloud support case to provide valuable context that can help you resolve your issue faster.

For more information, see [Gemini Cloud Assist Investigations](https://docs.cloud.google.com/cloud-assist/investigations) in the Gemini documentation.

## Read additional troubleshooting documentation

If you're still experiencing problems, the following resources might be helpful:

  * If you've received an error message, see the [error reference](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors) page for advice on resolving the error.

  * Check to see if the problem you're having is caused by a [known issue](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/known-issues).

  * If you're having difficulties with a specific area, one of the targeted troubleshooting guides listed in the **Troubleshoot by issue type** section of the table of contents might help.




## What's next

If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync) for further help, including advice on the following topics: 

  * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
  * Getting support from the community by [asking questions on Stack Overflow](http://stackoverflow.com/questions). If you use kpt or Kustomize, use the `kpt` or `kustomize` tag to search for similar issues.
  * Opening bugs or feature requests by using the [public issue tracker](https://github.com/GoogleContainerTools/config-sync/issues) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
