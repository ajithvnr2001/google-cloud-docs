---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/safe-rollouts-with-config-sync/
title: Safe rollouts with Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:12.746139+00:00
---

# Safe rollouts with Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/safe-rollouts-with-config-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Safe rollouts with Config Sync Stay organized with collections  Save and categorize content based on your preferences. 

This document shows cluster operators and platform administrators how to safely roll out changes across multiple environments using [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview). This approach can help you avoid errors that affect all of your environments simultaneously.

Config Sync lets you manage single clusters, multi-tenant clusters, and multi-cluster Kubernetes configurations by using files stored in a [Git](https://git-scm.com/) repository.

Configurations can represent several things, including the following:

  * Standard GKE objects, such as [NetworkPolicies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) resources, [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) resources, or [RoleBindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#rolebinding-example) resources.
  * Google Cloud resources, such as [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) or [Cloud SQL](https://docs.cloud.google.com/sql/docs) databases, through Config Connector.
  * Constraints on the configuration themselves, through Policy Controller.



Config Sync is especially suited to deploy configurations, policies, and workloads needed to run the platform that you build on top of Google Kubernetes Engine—for example, security agents, monitoring agents, and certificate managers.

Although you can deploy user-facing applications with Config Sync, we don't recommend linking their release lifecycle to the release lifecycle of the administrative workloads mentioned earlier. Instead, we recommend that you use a tool dedicated to application deployment, such as a [continuous deployment](https://docs.cloud.google.com/architecture/devops/devops-tech-deployment-automation) tool, so that application teams can be in charge of their release schedule.

Config Sync is a powerful product that can manage many elements, so you need guardrails to avoid errors that have a major impact. This document describes several methods to create guardrails. The first section covers staged rollouts and the second section focuses on tests and validations. The third section shows how to monitor your deployments.

**Note:** This tutorial uses a Git repository to explain how to implement rollouts. OCI images and Helm charts are also supported.

## Implementing staged rollouts with Config Sync

In a multi-cluster environment, we don't recommend applying a configuration change across all the clusters at the same time. A staged rollout, cluster per cluster, is much safer because it reduces the potential impact of any error.

There are several ways to implement staged rollouts with Config Sync:

  * Use Git commits or tags to manually apply the changes that you want to the clusters.
  * Use Git branches to automatically apply the changes when the changes are merged. You can use different branches for different groups of clusters.
  * Use `ClusterSelector` and `NamespaceSelector` objects to selectively apply changes to subgroups of clusters or namespaces.



All methods for staged rollouts have advantages and disadvantages. The following table shows which of these methods you can use at the same time:

Compatibility | Git commits or tags | Git branches | Cluster selectors | Namespace selectors  
---|---|---|---|---  
Git commits or tags |  | Not compatible | Compatible | Compatible  
Git branches | Not compatible |  | Compatible | Compatible  
Cluster selectors | Compatible | Compatible |  | Compatible  
Namespace selectors | Compatible | Compatible | Compatible |   
  
The following decision tree can help you decide when to use one of the staged rollout methods.

![Decision tree for rollout methods.](https://docs.cloud.google.com/static/architecture/images/safe-rollouts-acm1.svg)

**Note:** Config Sync lets you synchronize configs from [multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories): one repository for the cluster-scoped configs, and one optional repository per namespace. While the usage of namespace selectors is different when using multiple repositories, you can still apply all the other methods described in this section to the repositories that you synchronize configs from.

### Use Git commits or tags

Compared to the other staged rollout methods, using Git commits or tags provides the most control and is the safest. You can use the [Config Sync page in the Google Cloud console](https://console.cloud.google.com/kubernetes/config_management) in the console to update multiple clusters at the same time. Use this method if you want to apply changes to your clusters one by one, and to control exactly when this happens.

In this method, you "pin" each cluster to a specific version (either a commit or a tag) of your repository. This method is similar to using the Git commit as a container image tag. You implement this method by specifying the commit, tag, or hash in the `spec.git.revision` field of the `RootSync` or `RepoSync` [custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

If you manage your `RootSync` or `RepoSync` custom resources with a tool like Kustomize, you can reduce the amount of manual work required for rollouts. With such a tool, you only need to change the `revision` parameter in one place, and then selectively apply the new `RootSync` or `RepoSync` custom resource to your clusters in the order, and at the pace, that you choose.

Additionally, you can use the Google Cloud console to update the `revision` parameter for multiple clusters belonging to the same [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts) at the same time. However, if you have an automated system to update your configurations, we don't recommend using the Google Cloud console to make configuration changes.

For example, the following RootSync definition configures Config Sync to use the `1.2.3` tag:
    
    
    apiVersion: configsync.gke.io/v1
    kind: RootSync
    metadata:
      name: root-sync
      namespace: config-sync-system
    spec:
      sourceType: git
      sourceFormat: unstructured
      git:
        repo: git@example.com:gke/config-sync.git
        revision: 1.2.3
        auth: ssh
    

If you apply this configuration to your cluster, Config Sync will use the `1.2.3` tag of the `example.com:gke/config-sync.git` repository.

To update a cluster, change the `spec.git.revision` field to the new value for the cluster. This lets you define which clusters get updated and when. If you need to roll back a change, change the `spec.git.revision` field back to its former value.

With this rollout method, you first commit changes to the Config Sync repository, and then you update the RootSync definitions on all the clusters.

We recommend the following actions:

  * Use Git commit IDs rather than tags. Because of the way that Git functions, you have a [guarantee](https://git-scm.com/about/info-assurance) that they will never change. For example, a `git push --force` can't change the commit that Config Sync is using. This approach is useful for auditing purposes and to track which commit you are using in logs. Additionally, unlike with tags, there's no extra step to commit IDs.
  * If you prefer using Git tags instead of Git commit IDs, you can protect your tags if you're using a Git solution that supports protection.
  * If you want to update multiple clusters at the same time, you can do that in the [Google Cloud console](https://console.cloud.google.com/kubernetes/config_management). To update multiple clusters at once, they must be part of the same [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts) (and be in the same [project](https://docs.cloud.google.com/docs/overview#projects)).



### Use Git branches

If you want changes to be applied to clusters as soon as they are merged in your Git repository, configure Config Sync to use Git branches instead of commits or tags. In this method, you create multiple long-lived branches in your Git repository, and configure Config Sync in different clusters to read its configuration from different branches.

For example, a simple pattern has two branches:

  * A `staging` branch for non-production clusters.
  * A `main` branch for production clusters.

**Warning:** If you are dealing with a large number of clusters and environments, you may need a large number of branches. This can quickly become cumbersome to manage. This is why we recommend using Git commits over branches.

For non-production clusters, create the `RootSync` or `RepoSync` object with the `spec.git.branch` field set to `staging`. For production clusters, create the `RootSync` or `RepoSync` object with the `spec.git.branch` parameter set to `main`.

For example, the following RootSync definition configures Config Sync to use the `main` branch:
    
    
    apiVersion: configsync.gke.io/v1
    kind: RootSync
    metadata:
      name: root-sync
      namespace: config-sync-system
    spec:
      git:
        repo: git@example.com:gke/config-sync.git
        branch: main
        auth: ssh
    

The following diagram illustrates the rollout process for this method:

![Rollout process for Git branches.](https://docs.cloud.google.com/static/architecture/images/safe-rollouts-acm3.svg)

You can adapt this pattern to specific needs, using more than two branches, or using branches that are mapped to something other than environments. If you need to roll back a change, use the [`git revert` command](https://git-scm.com/docs/git-revert) to create a new commit on the same branch that reverts the changes from the previous commit.

We recommend the following actions:

  * When dealing with multiple clusters, use at least two Git branches to help to distinguish between production and non-production clusters.
  * Most Git solutions let you use the protected branches feature to prevent deletions or unreviewed changes of those branches. For more information, see the documentation for [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches), [GitLab](https://docs.gitlab.com/ee/user/project/protected_branches.html), and [Bitbucket](https://confluence.atlassian.com/bitbucketserver/using-branch-permissions-776639807.html).



### Use ClusterSelector and NamespaceSelector objects

Git branches are a good way of doing a staged rollout of changes across multiple clusters that will eventually all have the same policies. However, if you want to rollout a change only to a subset of clusters or of namespaces, then use the `ClusterSelector` and `NamespaceSelector` objects. These objects have a similar goal: they let you apply objects only to clusters or namespaces that have specific labels.

For example:

  * By using `ClusterSelector` objects, you can apply different policies to clusters, depending on which country they are located in, for various compliance regimes.
  * By using `NamespaceSelector` objects, you can apply different policies to namespaces used by an internal team and by an external contractor.



`ClusterSelector` and `NamespaceSelector` objects also let you implement advanced testing and release methodologies, such as the following:

  * Canary releases of policies, where you deploy a new policy to a small subset of clusters and namespaces for a long time to study the policy's impact.
  * A/B testing, where you deploy different versions of the same policy to different clusters to study the difference of the policy versions' impact and then choose the best one to deploy everywhere.



For example, imagine an organization with several production clusters. The platform team has already created two categories of production clusters, called `canary-prod` and `prod`, using `Cluster`, and `ClusterSelector` objects (see [Use ClusterSelectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#configure_a_subset_of_clusters)).

The platform team wants to rollout a policy with Policy Controller to enforce the presence of a team label on namespaces in order to identify which team each namespace belongs to. They have already rolled out a version of this policy in _dry run_ mode, and now they want to enforce it on a small number of clusters. Using `ClusterSelector` objects, they create two different `K8sRequiredLabels` resources that are applied to different clusters.

  * The `K8sRequiredLabels` resource is applied to clusters of type `prod`, with an `enforcementAction` parameter set to `dryrun`:
        
        apiVersion: constraints.gatekeeper.sh/v1beta1
        kind: K8sRequiredLabels
        metadata:
          name: ns-must-have-team
          annotations:
            configmanagement.gke.io/cluster-selector: prod
        Spec:
          enforcementAction: dryrun
          match:
            kinds:
              - apiGroups: [""]
                kinds: ["Namespace"]
          parameters:
            labels:
              - key: "team"
        

  * The `K8sRequiredLabels` resource is applied to clusters of type `canary-prod`, without the `enforcementAction` parameter, meaning that the policy is actually enforced:
        
        apiVersion: constraints.gatekeeper.sh/v1beta1
        kind: K8sRequiredLabels
        metadata:
          name: ns-must-have-team
          annotations:
            configmanagement.gke.io/cluster-selector: canary-prod
        spec:
          match:
            kinds:
              - apiGroups: [""]
            kinds: ["Namespace"]
          parameters:
            labels:
              - key: "team"
        




The `configmanagement.gke.io/cluster-selector` annotation allows the team to enforce the policy only in clusters of type `canary-prod`, preventing any unintended side-effects from spreading to the whole production fleet. For more information about the dry run feature of Policy Controller, see [creating constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).

We recommend the following actions:

  * Use `ClusterSelector` and `NamespaceSelector` objects if you need to apply a configuration change to only a subset of clusters or namespaces indefinitely or for a long time.
  * If you roll out a change by using selectors, be very careful. If you use Git commits, any error affects only one cluster at a time, because you're rolling out cluster by cluster. But if you use Git branches, any error can affect all the clusters that use that branch. If you use selectors, error can affect all clusters at once.



## Implementing reviews, tests, and validations

One advantage of Config Sync is that it manages everything declaratively—Kubernetes resources, cloud resources, and policies. This means that files in a source control management system represent the resources (Git files, in the case of Config Sync). This characteristic lets you implement development workflows that you already use for an application's source code: reviews and automated testing.

### Implement reviews

Because Config Sync is based on Git, you can use your preferred Git solution to host the Config Sync repository. Your Git solution probably has a code review feature, which you can use to review changes made to the Config Sync repository.

The best practices for reviewing changes to the your repository are the same as with a normal code review, as follows:

  * Practice [trunk-based development](https://docs.cloud.google.com/architecture/devops/devops-tech-trunk-based-development).
  * Work in [small batches](https://docs.cloud.google.com/architecture/devops/devops-process-working-in-small-batches).
  * Ensure that [code review is done synchronously or at least promptly](https://docs.cloud.google.com/architecture/devops/devops-tech-trunk-based-development#common_pitfalls).
  * The person who reviews and approves the change should not be the same person who suggested the change.



Because of the sensitivity of the Config Sync codebase, we also recommend that, if possible with your Git solution, you make the following configurations:

  * Protect the branches that are directly used by clusters. See the documentation for [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches), [GitLab](https://docs.gitlab.com/ee/user/project/protected_branches.html), and [Bitbucket](https://confluence.atlassian.com/bitbucketserver/using-branch-permissions-776639807.html). GitLab also lets you [protect tags](https://docs.gitlab.com/ee/user/project/protected_tags.html).
  * After the branches are protected, you can refine the approvals that are needed to merge a change: 
    * On GitHub, [enable required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews).
    * For GitLab, use [Code Owners](https://docs.gitlab.com/ee/user/project/codeowners/) to delegate approval permissions on a file or directory basis. You can use [merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals) to require different people from different teams to approve a request before it's merged.
    * On Bitbucket, combine [default reviewers](https://confluence.atlassian.com/bitbucketserver/add-default-reviewers-to-pull-requests-834221295.html) with [default merge checks](https://confluence.atlassian.com/bitbucketserver/checks-for-merging-pull-requests-776640039.html). Optionally, use a Code Owners plugin for Bitbucket Server is available on the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1218598/code-owners-for-bitbucket-server?hosting=server&tab=overview) to control who can approve changes for subsections of the repository.



By using these different features, you can enforce approvals for each change request to your codebase. For example, you can ensure that each change is approved at least by a member of the platform team (who operates the fleet of clusters), and by a member of the security team (who is in charge of defining and implementing security policies).

We recommend the following action:

  * Enforce peer reviews on your repository and protect the Git branches that are used by your clusters.



### Implement automated tests

A common best practice when working on a codebase is to implement [continuous integration](https://docs.cloud.google.com/architecture/devops/devops-tech-continuous-integration). This means that you configure automated tests to run when a change request is created or updated. Automated tests can catch many errors before a human reviews the change request. This tightens the feedback loop for the developer. You can implement the same idea, using the same tools, for the Config Sync repository.

For example, a good place to start is to run the [`nomos vet` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#vet) automatically on new changes. This command validates that your Config Sync repository's syntax is valid. You can implement this test by using [Cloud Build](https://docs.cloud.google.com/build/docs) by following the [validating configs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/validating-configs) tutorial. You can integrate Cloud Build with the following options:

  * Bitbucket, by using [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * GitHub, by using the Google Cloud Build GitHub application. Build triggers are also available for GitHub, but the GitHub application is the preferred method of integration.



As you can see in the [validating configs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/validating-configs) tutorial, the test is done by using a container image. You can therefore implement the test in any continuous integration solution that runs containers, not only Cloud Build.

To tighten the feedback loop even more, you can ask that users run the `nomos vet` command as a [Git pre-commit hook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#automatically_checking_for_syntax_errors_when_committing). One caveat is that some users might not have access to the Kubernetes clusters managed by Config Sync, and they might not be able to run the full validation from their workstation. Run the `nomos vet --clusters ""` command to restrict the validation to semantic and syntactic checks.

We recommend the following action:

  * Implement tests in a continuous integration pipeline.
  * Run at least the `nomos vet` command on all suggested changes.



## Monitoring rollouts

Even if you implement all the guardrails that this document covers, errors can still occur. Following are two common types of errors:

  * Errors that pose no problem to Config Sync itself, but prevent your workloads from working properly, such as an overly restrictive NetworkPolicy that prevents components of your workload from communicating.
  * Errors that make it impossible for Config Sync to apply changes to a cluster, such as an invalid Kubernetes manifest, or an object rejected by an [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/). The methods explained earlier should catch most of these errors.



Detecting the errors described in the first preceding bullet is almost impossible at the level of Config Sync because this requires understanding the state of each of your workloads. For this reason, detecting these errors is best done by your existing monitoring system that alerts you when an application is misbehaving.

Detecting the errors described in the second preceding bullet—which should be rare if you have implemented all the guardrails—requires a specific setup. By default, Config Sync writes errors to its logs (which you will find, by default, in [Cloud Logging](https://docs.cloud.google.com/logging)). Errors are also displayed in the [Config Sync Google Cloud console page](https://console.cloud.google.com/kubernetes/config_management). Neither logs nor the console are usually enough to detect errors, because you probably don't monitor them at all times. The simplest way to automate error detection is to run the `nomos status` [command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install), which tells you if there's an error in a cluster.

You can also set up a more advanced solution with automatic alerts for errors. Config Sync exposes metrics in the [Prometheus format](https://prometheus.io/docs/concepts/data_model/). For more information, see [monitoring Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync).

After you have the Config Sync metrics in your monitoring system, create an alert to notify you when the `gkeconfig_monitor_errors` metric is greater than 0. For more information, see [managing alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) for Cloud Monitoring, or [alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) for Prometheus.

## Summary of mechanisms for safe rollouts with Config Sync

The following table summarizes the various mechanisms described earlier in this document. None of these mechanisms is exclusive. You can choose to use some of them or all of them, for different purposes.

Mechanism | What it's good for | What it's not good for | Example use case  
---|---|---|---  
Git commit IDs and tags | Use specific Git commit IDs or tags to precisely control which cluster changes are applied on. | Don't use Git commit IDs or tags for long-lived differences between clusters. Use cluster selectors. | All your clusters are configured to apply the `12345` Git commit. You make a change with a new commit, `abcdef`, that you want to test. You change the configuration of a single cluster to use this new commit to validate the change.  
Git branches | Use multiple Git branches when you want to roll out the same change to multiple environments, one after the other. | Don't use multiple Git branches for long-lived differences between clusters. The branches will significantly diverge and will be hard to merge back together. | First merge the change in the staging branch, where it will be picked up by staging clusters.  
Then merge the change in the master branch, where it will be picked up by production clusters.  
Cluster selectors and namespace selectors | Use selectors for long-lived differences between clusters and namespaces. | Don't use selectors for a staged rollout across multiple environments. If you want to test a modification first in staging, and then deploy it in production, use separate Git branches. | If the application teams need full access to development clusters, but read-only access to production clusters, use the `ClusterSelector` object to apply the correct RBAC policies only to the relevant clusters.  
Peer reviews | Use peer reviews to ensure that the relevant teams approve the changes. | Human reviewers don't catch all errors, especially items like syntax errors. | Your organization mandates that the security team must review configuration changes that affect multiple systems. Have a security team member review the changes.  
Automated tests in continuous integration pipeline | Use automated tests to catch errors in suggested changes. | Automated tests can't fully replace a human reviewer. Use both. | Running a `nomos vet` command on all suggested changes confirms that the repository is a valid Config Sync configuration.  
Monitor syncing errors | Be sure that Config Sync actually applies changes to your clusters. | Syncing errors occur only if Config Sync tries to apply an invalid repository or if the Kubernetes API server rejects some of the objects. | A user bypasses all your tests and reviews and commits an invalid change to the Config Sync repository. This change can't be applied to your clusters. If you're monitoring syncing errors, you'll be alerted if an error is made.  
  
## Rollout strategy example

This section uses the concepts introduced in the rest of this article to help you create an end-to-end rollout strategy across all the clusters in your organization. This strategy assumes that you have separate fleets for development, staging, and production (as shown in [Fleet Example 1 - Approach 1](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts/examples)).

**Warning:** This rollout strategy is complex. It only makes sense to implement if you have a complex infrastructure with at least 2 fleets, and at least 3 clusters per fleet. If you have a large number of fleets, but with a single cluster in each one, then you can adapt this strategy by having "canary fleets" instead of "canary clusters".

In this scenario, you configure each cluster to synchronize with your Git repository using a specific Git commit. Deploying a change to a given fleet is a 4-step process:

  1. You update a single (the "canary") cluster in the fleet to use the new commit first.
  2. You validate that everything works as expected by running tests and monitoring the rollout.
  3. You update the rest of the clusters in the fleet.
  4. You validate again that everything works as expected.



To deploy a change across all your clusters, you repeat this process for each fleet. You can technically apply this method with any Git commit, from any branch. However, we suggest that you adopt the following process to identify problems early in the review process:

  1. When someone opens a change request in the Config Sync Git repository, deploy that change to one of the development clusters.
  2. If the change request is accepted and merged in your main branch, run the full deployment across all fleets as described earlier.



While some changes might target only a specific fleet, we recommend that you deploy all changes to all fleets eventually. This strategy eliminates the problem of tracking which fleet should sync with which commit. Pay special attention to the changes that target only the production fleet because proper testing will not have been possible in previous fleets. For example, this means waiting longer for issues to surface between deploying to the canary clusters and to the rest of the clusters.

To summarize, a full end-to-end deployment looks like this:

  1. Someone opens a change request.
  2. Automated tests and validations run, and a manual review is done.
  3. You trigger a job manually to deploy the change to the canary cluster in the development fleet. Automated end-to-end tests run in this cluster.
  4. If everything is OK, you merge the change request on the main branch.
  5. The merge triggers an automated job to deploy the new main branch tip commit to the canary cluster in the development fleet. Automated end-to-end tests run in this cluster (to detect potential incompatibilities between two change requests that have been created and merged approximately at the same time).
  6. The following jobs run one after the other (you trigger them manually, or after a predefined time to allow for user reports of regressions): 
     1. Deploy to all the clusters of the development fleet.
     2. Run tests and validations in the clusters of the development fleet.
     3. Deploy to the canary cluster of the staging fleet.
     4. Run tests and validations in the canary cluster of the staging fleet.
     5. Deploy to all the clusters of the staging fleet.
     6. Run tests and validations in the clusters of the staging fleet.
     7. Deploy to the canary cluster of the production fleet.
     8. Run tests and validations in the canary cluster of the production fleet.
     9. Deploy to all the clusters of the production fleet.
     10. Run tests and validations in the clusters of the production fleet.



## What's next

  * Read about [monitoring Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitoring-config-sync).
  * Read about [fleets](https://docs.cloud.google.com/anthos/fleet-management/docs/fleet-concepts).
  * Learn how to [validate your app against company policies in a continuous integration pipeline](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
