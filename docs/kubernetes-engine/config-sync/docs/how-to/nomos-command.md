---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command/
title: Use the nomos command-line tool \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:34.803509+00:00
---

# Use the nomos command-line tool  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Use the nomos command-line tool Stay organized with collections  Save and categorize content based on your preferences. 

The `nomos` command-line tool is an optional tool for Config Sync that you can use to get the status of Config Sync and the sync status of your source of truth. The `nomos` tool provides you with the following commands:

Command | Usage  
---|---  
`nomos status` | Check Config Sync status  
`nomos vet` | Check for errors in the source of truth  
`nomos hydrate` | View all configs in the source of truth  
`nomos bugreport` | Create a bug report  
`nomos migrate` | Migrate from ConfigManagement object to RootSync  
`nomos init` | Initialize a hierarchical source of truth  
  
## Prerequisites

Before you can use the `nomos` tool to interact with a cluster, Config Sync must already be installed on the target cluster. You must also [install and configure the `kubectl` command-line tool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl). If you're interacting with Google Kubernetes Engine clusters, ensure that you also install the [`gke-gcloud-auth-plugin`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin).

The `nomos` tool supports previewing and validating Kustomize configurations and Helm charts. Before you can use this feature, install [Kustomize](https://kubectl.docs.kubernetes.io/installation/kustomize/) and [Helm](https://helm.sh/docs/intro/install/) in your local workstation. If your source of truth only contains fully rendered configurations, Kustomize and Helm are optional.

## Install the `nomos` tool

The `nomos` tool is a binary compiled from Go code and you can install it locally, for example, on a workstation or laptop.

The `nomos` tool is not included when you install Config Sync. You can install the `nomos` tool by installing the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works), the Google Cloud CLI comes pre-installed.

If you do not have the Google Cloud CLI, we recommend that you use [`gcloud components install nomos`](https://docs.cloud.google.com/sdk/gcloud/reference/components/install) to install the `nomos` tool. Installing the `nomos` tool with the Google Cloud CLI lets you use [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) to update the `nomos` tool to the latest version.

For information on alternate ways to install the `nomos` tool, see [Downloads](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/downloads#nomos_command).

## Basic usage

For basic command syntax, use the `--help` argument:
    
    
    nomos --help
    

The `nomos` tool reads from the local clone of your source of truth. Use the `--path` flag to specify the location of the top level of the source of truth. By default, `--path` is set to `.`, or the current directory. For example:
    
    
    nomos vet --path=PATH_TO_SOURCE --source-format unstructured
    

## Check Config Sync status

You can monitor the status of Config Sync on all enrolled clusters by using the `nomos status` command. For each cluster, `nomos status` reports the hash of the commit that was last applied to the cluster and any errors that occurred while trying to apply any recent changes.

You can also use `nomos status` to check if the resources managed by Config Sync are ready. `nomos status` reports the status for each individual resource in the `STATUS` column of the `Managed resources` section of the output.

The following example shows you some of the different conditions that the `nomos status` command might report:
    
    
    nomos status

Example output:
    
    
    MANAGED_CLUSTER_1
      --------------------
      <root>   git@github.com:foo-corp/acme@main
      SYNCED   f52a11e4
      Managed resources:
       NAMESPACE   NAME                                                                   STATUS
                   k8snoexternalservices.constraints.gatekeeper.sh/no-internet-services   Current
                   namespace/hello                                                        Current
    
    MANAGED_CLUSTER_2
      --------------------
      <root>   git@github.com:foo-corp/acme@main
      PENDING  9edf8444
    
    MANAGED_CLUSTER_3
      --------------------
      <root>   git@github.com:foo-corp/acme@main
      ERROR    f52a11e4
      Error:   KNV1021: No CustomResourceDefinition is defined for the resource in the cluster.
    
    MANGED_CLUSTER_4
      --------------------
      NOT INSTALLED
    
    MANAGED_CLUSTER_5
      --------------------
      <root>   git@github.com:foo-corp/acme/admin@main
      SYNCED   f52a11e4
      Managed resources:
       NAMESPACE   NAME                                                                   STATUS
                    namespace/gamestore                                                   Current
                    namespace/monitoring                                                  Current
       gamestore    reposync.configsync.gke.io/repo-sync                                  Current
       gamestore    rolebinding.rbac.authorization.k8s.io/gamestore-admin                 Current
       gamestore    rolebinding.rbac.authorization.k8s.io/gamestore-webstore-admin        Current
       monitoring   deployment.apps/prometheus-operator                                   Current
       monitoring   prometheus.monitoring.coreos.com/acm                                  Current
       monitoring   service/prometheus-acm                                                Current
       monitoring   service/prometheus-operator                                           Current
       monitoring   serviceaccount/prometheus-acm                                         Current
       monitoring   serviceaccount/prometheus-operator                                    Current
       monitoring   servicemonitor.monitoring.coreos.com/acm-service                      Current
      --------------------
      bookstore  git@github.com:foo-corp/acme/bookstore@v1
      SYNCED     34d1a8c8
      Managed resources:
       NAMESPACE   NAME                                 STATUS
       gamestore   configmap/store-inventory            Current
       gamestore   webstore.marketplace.com/gameplace   Current
    

In this output:

  * `MANAGED_CLUSTER_1` has synced the most recent change to the source of truth and all managed resources have a status of `Current`. A status of `Current` means that the state of the resource matches the state that you want.
  * `MANAGED_CLUSTER_2` is still syncing.
  * `MANAGED_CLUSTER_3` has an error that has prevented the change from being applied. In this example, `MANAGED_CLUSTER_3` has error [KNV1021](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors#knv1021) since it's missing a CustomResourceDefinition (CRD) that the other clusters have installed.
  * `MANAGED_CLUSTER_4` does not have Config Sync installed.
  * `MANAGED_CLUSTER_5` is syncing from two Git repositories. The `<root>` source of truth belongs to the cluster admin and the `bookstore` source of truth might belong to an application development team.



### Managed resource statuses

The status of your managed resources can be one of the following values:

  * `InProgress`: The actual state of the resource has not yet reached the state that you specified in the resource manifest. This status means that the resource reconciliation is not complete yet. Newly created resources usually start with this status, although some resources like ConfigMaps are `Current` immediately.

  * `Failed`: The process of reconciling the actual state with the state that you want has encountered an error or it has made insufficient progress.

  * `Current`: The actual state of the resource matches the state that you want. The reconciliation process is considered complete until there are changes to either the wanted or the actual state.

  * `Terminating`: The resource is in the process of being deleted.

  * `NotFound`: The resource does not exist in the cluster.

  * `Unknown`: Config Sync is unable to determine the status of the resource.




To turn off showing the resource level status, add `--resources=false` to the `nomos status` command.

### About last synced commit

The `nomos status` command displays the most recent commit hash that was applied to the cluster in its output under `status.sync.commit`. To obtain this value, query the `RootSync` or `RepoSync` object and look at the `status.sync` field.

For example, to query a `RootSync` object, run the following command:
    
    
    kubectl get rootsyncs.configsync.gke.io -n config-management-system root-sync -o yaml
    

Example output:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    status:
      sync:
        commit: f1739af550912034139aca51e382dc50c4036ae0
        lastUpdate: "2021-04-20T00:25:01Z"
    

To query a `RepoSync` object, run the following command:
    
    
    kubectl get reposync.configsync.gke.io -n NAMESPACE repo-sync -o yaml
    

Replace `NAMESPACE` with the namespace that you created your namespace source of truth in.

Example output:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    status:
      sync:
        commit: ed95b50dd918cf65d8908f7561cb8d8d1f179c2f
        lastUpdate: "2021-04-20T00:25:20Z"
    

This commit represents the most recent commit against the cluster. However, not every resource in the cluster is affected by each commit; to see the most recent commit for a specific resource, query the specific resource and look at `metadata.annotations.configmanagement.gke.io/token`. For example:
    
    
    kubectl get clusterroles CLUSTER_ROLE_NAME -o yaml

Replace `CLUSTER_ROLE_NAME` with the name of the cluster role you want to query.
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        configmanagement.gke.io/token: ed95b50dd918cf65d8908f7561cb8d8d1f179c2f
    

### nomos status flags

To customize the `nomos status` command, add the following flags:

Flag | Description  
---|---  
`--contexts` | Accepts a comma-separated list of contexts to use in multi-cluster commands. Defaults to all contexts. Use "" for no contexts.  
`-h` or `--help` | Help for the `nomos status` command.  
`--name` | Accepts a string. Use this flag to filter Root and Repo Sync with the provided name. This flag can be used alongside the `namespace` flag.  
`--namespace` | Accepts a string. Use the `namespace` flag to limit the command to a specific namespace source of truth. Leave unset to get all sources. This flag is only available if you enabled syncing from more than one source of truth.  
`--poll` | Use the `poll` flag to run `nomos status` continuously and have it reprint the status table at a regular interval. For example `3s`. Leave this flag unset to run `nomos status` once  
`--resources` | Accepts `true` or `false`. If `true`, `nomos status` shows the resource level status for your root or namespace source of truth when syncing from more than one source of truth. The default value is `true`.  
`--timeout` | Timeout for connecting to each cluster. The default value is `3s`.  
  
### Required permissions

If you are a project owner, you have the `cluster-admin` RBAC role and you can use the `nomos status` command for any clusters in your project without adding any further permissions. If you don't have the `cluster-admin` role, you can use `nomos status` by creating the following ClusterRole:

  1. Create a file named `nomos-status-reader.yaml` and copy the following ClusterRole into it. The rules that you need differ depending on whether you are using [RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### Using RootSync and RepoSync objects
         
         # nomos-status-reader.yaml
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: nomos-status-reader
         rules:
         - apiGroups: ["configsync.gke.io"]
           resources: ["reposyncs", "rootsyncs"]
           verbs: ["get"]
         - nonResourceURLs: ["/"]
           verbs: ["get"]
         

### Not using RootSync and RepoSync objects
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: nomos-status-reader
         rules:
         - apiGroups: ["configmanagement.gke.io"]
           resources: ["configmanagements", "repos"]
           verbs: ["get", "list"]
         - nonResourceURLs: ["/"]
           verbs: ["get"]
         

  2. Apply the `nomos-status-reader.yaml` file:
         
         kubectl apply -f nomos-status-reader.yaml
         




## Check for errors in the source of truth

Before you commit a config to the source of truth, use the `nomos vet` command to check the syntax and validity of the configs in your source of truth:
    
    
    nomos vet --source-format unstructured

If syntax errors are found, the `nomos vet` command exits with a non-zero status and logs error messages to `STDERR`.

### nomos vet flags

To customize the `nomos vet` command, add the following flags:

Flag | Description  
---|---  
`--api-server-timeout` | Accepts a duration string. Sets the client-side timeout for talking to the Kubernetes API server. Defaults to `15s`.  
`--clusters` | Accepts a comma-separated list of cluster names to use in multi-cluster commands. Defaults to all clusters. Use `""` for no clusters.  
`--format` | Accepts `yaml` or `json`. The format of the output. The default value is `yaml`.  
`-h` or `--help` | Help for the `nomos vet` command.  
`--keep-output` | Accepts a Boolean. If `true`, the rendered output is saved to the location that you can specify with the `--output` flag.  
`--namespace` | Accepts a string. If set, validates the source of truth as a namespace source of truth with the provided name. Automatically sets `--source-format=unstructured`.  
`--no-api-server-check` | Accepts a Boolean. If `true`, disables talking to the Kubernetes API server for discovery. For more information on this flag, see the Server-side validation section.  
`--output` | Accepts a string. The path to the rendered output. Defaults to the `compiled` directory. If `--keep-output ` is set to `false`, this flag is ignored.  
`--path` | Accepts a string. The path to the root directory of your Config Sync source of truth. The default is "`.`"  
`--source-format` | Accepts `hierarchy` or `unstructured`. If `hierarchy` or unset, validates the source of truth as a [hierarchical source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo). If `unstructured`, validates the source of truth as an [ unstructured source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo). This flag is required if you are using an unstructured source of truth.  
`--threshold` | Optionally accepts an integer. Sets the maximum objects allowed per repository; errors if exceeded. Omit the flag or use `--threshold=0` to disable the maximum objects validation. Provide the flag without a value to use the default `1000`, or use `--threshold=N` to set a specific limit.  
  
### Server-side validation

If the `nomos vet` command can't determine if the type is namespaced, the `nomos` tool connects to the API Server of the current `kubectl` context. Because the `nomos` tool by default understands core Kubernetes types and Config Sync CRDs, it only tries to connect to the API Server if CRs don't have a corresponding declared CRD. In this case, if the API Server does not have the CRD applied, the `nomos vet` command returns [error KNV1021](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors#knv1021). To disable this check and suppress errors from missing CRDs, pass the `--no-api-server-check` flag.

#### Caching API server metadata

Instead of suppressing API server checks, you can cache the data on the API server for the `nomos vet` command. To cache your `api-resources`, complete the following steps:

  1. Connect to a cluster which has all CRDs that you need for your source of truth. The cluster does not need to have Config Sync enabled.
  2. Go to the policyDir of your source of truth. This is the same directory specified in your ConfigManagement or RootSync resource.
  3. Run the following command: `kubectl api-resources > api-resources.txt` This command creates a file called api-resources.txt that contains the exact output of kubectl api-resources.



From now on, runs of `nomos vet` within the source of truth are aware of those type definitions. If the `api-resources.txt` file is removed or renamed, `nomos vet` cannot find the file. `nomos vet` will still attempt to connect to the cluster if it finds manifests for types not declared in api-resources.txt (unless `--no-api-server-check` is passed).

The `api-resources.txt` file only affects how the `nomos` tool works. It does not modify the behavior of Config Sync in any way.

It's okay to have extra entries in the api-resources.txt file which are for types that are not in the source of truth being validated. `nomos vet` imports the definitions, but does nothing with them.

**Caution:** Custom types in a source of truth must either be namespaced or not-namespaced. The `nomos vet` command does not support types which are namespace-scoped in some clusters and cluster-scoped in others.

##### Update api-resources.txt

After ensuring all the CRDs that you want are on the cluster, run the following command:
    
    
    kubectl api-resources > api-resources.txt
    

**Caution:** Avoid directly editing `api-resources.txt` as it is easy to format incorrectly and cause errors.

### Automatically check for syntax errors when committing

If you commit a file with JSON or YAML errors, Config Sync does not apply the change. However, you can prevent these types of errors from ever getting into the source of truth by using client-side or server-side hooks.

#### Use `nomos vet` in a pre-commit hook

You can configure a pre-commit hook that runs the `nomos vet` command to check for syntax errors when you commit a change to the local Git clone of your repo. If a pre-commit hook exits with a non-zero status, the `git commit` operation fails.

**Note:** Pre-commit hooks run on the client, not the server. They must be added manually to each client, and the user can bypass or disable them at any time.

To run the `nomos vet` command as a pre-commit hook, edit the `.git/hooks/pre-commit` file in your source of truth (notice that `.git` starts with a `.` character). You may need to create the file manually. Add the `nomos vet` command to a new line in the script. The `--path` argument is optional. Set the `--source-format` argument to the source format of the repository.
    
    
    nomos vet --path=/path/to/repo --source-format unstructured
    

Ensure that the `pre-commit` file is executable:
    
    
    chmod +x .git/hooks/pre-commit
    

Now, when you run a `git commit` command in the clone of your source of truth, `nomos vet` runs automatically.

The contents of the `.git/` directory are not tracked by the source of truth itself, and cannot be committed to the source of truth in the same location. You can create a directory in the source of truth for Git hooks, and people who use the source of truth can copy the hooks into the appropriate place in their local clone.

#### Use `nomos vet` in a server-side hook

Git provides a mechanism for running checks at the server, rather than the client, during a `git push` operation. If the check fails, the `git push` also fails. These server-side hooks cannot be bypassed by the client. The method for configuring server-side hooks depends on how your Git server is hosted. See one of the following links for more information, or check the documentation for your Git hosting service.

  * [GitHub](https://help.github.com/articles/about-required-status-checks/)
  * [Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/integrating-with-cloud-build#create_a_build_trigger)
  * [Bitbucket](https://confluence.atlassian.com/bitbucket/manage-webhooks-735643732.html)
  * [GitLab](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
  * [Self-hosted Git server](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)



### Enforce the maximum number of objects to sync

Config Sync stores a reference to each object it syncs in a ResourceGroup inventory object, along with the object's current status. Because Kubernetes has a byte size limit for resource objects, this limits the maximum number of objects that Config Sync can sync with a single RootSync or RepoSync.

By default, the server-side etcd size limit is 1.5 MiB. For more details, see [the etcd documentation](https://etcd.io/docs/v3.5/dev-guide/limit/#request-size-limit). Applying an object larger than this limit causes one of the following errors, depending on object size:

  * `etcdserver: request is too large`
  * `rpc error: code = ResourceExhausted desc = trying to send message larger than max`
  * `Request entity too large: limit is 3145728`



To protect against ResourceGroup objects exceeding the Kubernetes size limit, you can use the `nomos vet --threshold` to validate the number of objects in your source repository.

By default, when you use the `nomos vet` command, the threshold is not enforced. Passing the `--threshold` flag will cause the `vet` command to error if the number of objects in your source repository exceeds the threshold.

The ResourceGroup inventory contains both object references and current object status. It can grow especially large when the objects fail to sync or reconcile. To avoid exceeding the Kubernetes object size limit, choose a threshold that will leave enough capacity for object errors to be recorded. The default value of `1000` should work for almost all cases, but you can raise or lower the threshold as needed.

This threshold is only validated by the `nomos vet` command, not by Config Sync itself. To enforce the threshold, use the `nomos vet --threshold` command in a source repository presubmit check or git pre-commit hook.

## View all configs in the source of truth

You can use the `nomos hydrate` command to view the combined contents of your source of truth on each enrolled cluster.

If you run `nomos hydrate` with no options, it creates a `compiled/` directory in the current working directory. Within that directory, a subdirectory is created for each enrolled cluster, with the fully resolved configs the Operator would apply to the cluster.

This command can also convert a [hierarchical source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo) to one or more [unstructured sources of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo), using the content in the `compiled/` directory.

### nomos hydrate flags

To customize the `nomos hydrate` command, add the following flags:

Flag | Description  
---|---  
`--api-server-timeout` | Accepts a duration string. Sets the client-side timeout for talking to the Kubernetes API server. Defaults to `15s`.  
`--clusters` | Accepts a comma-separated list of cluster names. Use this flag to limit the output to a single cluster or a list of clusters. Defaults to all clusters. Use `""` for no clusters.  
`--flat` | If enabled, print all output to a single file. Use this flag if you want to emulate the behavior of `nomos view`.  
`--format` | Accepts a `yaml` or `json`. The format of the output. The default value is `yaml`.  
`-h` or `--help` | Help for the `nomos hydrate` command.  
`--no-api-server-check` | Accepts a Boolean. If `true`, disables talking to the API server for discovery. For more information on this flag, see the Server-side validation section.  
`--output` | Accepts a string. The location to write hydrated configuration to. The default is the `compiled` directory. If `--flat` is not enabled, writes each resource manifest as a separate file. If `--flat` is enabled, writes to the, writes a single file holding all resource manifests.   
`--path` | Accepts a string. The path to the root directory of your Config Sync source of truth. The default is "`.`"  
`--source-format` | Accepts `hierarchy` or `unstructured`. If `hierarchy` or unset, validates the source of truth as a [hierarchical source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo). If `unstructured`, validates the source of truth as an [ unstructured source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo). This flag is required if you are using an unstructured source of truth.  
  
## Create a bug report

If you have a problem with Config Sync that requires help from [Google Cloud support](https://docs.cloud.google.com/support), you can get valuable debugging information by using the `nomos bugreport` command. You can use this command for a single source of truth and multiple repositories.
    
    
    nomos bugreport
    

This command generates a timestamped zip file with information on the Kubernetes cluster set in your `kubectl` context. The file also contains logs from Config Sync Pods. It does not contain information from the resources synced with Config Sync. For more information about the contents of the zip file, see [nomos bugreport reference](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/nomos-bugreport).

### Limitations

The `nomos bugreport` command fails and produces an incomplete zip file if any individual file exceeds 1GiB. This often occurs due to large log files.

The following table includes the most common causes of large log files and how you can resolve them:

Cause | Recommended action  
---|---  
Increased log verbosity | Reduce log verbosity with [log level overrides](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#override-log-level)  
Very large objects | [Unmanage](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects#stop-managing) the large object or reduce their size  
Many objects | [Split your repository into multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/breaking-up-repo)  
Controller fights | [Resolve the fighting](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/controller-fights)  
  
## Migrate from a ConfigManagement object to a RootSync object

You can run the `nomos migrate` command to migrate from your ConfigManagement object to a RootSync object to enable the `RootSync` and `RepoSync` APIs.

`nomos migrate` supports dry-run for previewing the migration process.

`nomos migrate` modifies your ConfigManagement object on the cluster directly. To avoid changes made through `nomos migrate` being reverted, ensure the ConfigManagement object isn't checked into your source of truth.

**Note:** Passing the `--contexts` flag specifies the contexts to migrate. This is only necessary if you want to migrate clusters beyond the current context.
    
    
    nomos migrate --contexts=KUBECONFIG_CONTEXTS --dry-run
    

If the dry-run result looks good, you can migrate your ConfigManagement object by using `nomos migrate`:
    
    
    nomos migrate --contexts=KUBECONFIG_CONTEXTS
    

The output is similar to the following:
    
    
    --------------------
    Enabling the multi-repo mode on cluster "my_managed_cluster-1" ...
    - A RootSync object is generated and saved in "/tmp/nomos-migrate/my_managed_cluster-1/root-sync.yaml".
    - The original ConfigManagement object is saved in "/tmp/nomos-migrate/my_managed_cluster-1/cm-original.yaml".
    - The ConfigManagement object is updated and saved in "/tmp/nomos-migrate/my_managed_cluster-1/cm-multi.yaml".
    - Resources for the multi-repo mode have been saved in a temp folder. If the migration process is terminated, it can be recovered manually by running the following commands:
      kubectl apply -f /tmp/nomos-migrate/my_managed_cluster-1/cm-multi.yaml && \
      kubectl wait --for condition=established crd rootsyncs.configsync.gke.io && \
      kubectl apply -f /tmp/nomos-migrate/my_managed_cluster-1/root-sync.yaml.
    - Updating the ConfigManagement object ....
    - Waiting for the RootSync CRD to be established ....
    - The RootSync CRD has been established.
    - Creating the RootSync object ....
    - Waiting for the reconciler-manager Pod to be ready ....
    -   Haven't detected running Pods with the label selector "app=reconciler-manager".
    -   Haven't detected running Pods with the label selector "app=reconciler-manager".
    -   Haven't detected running Pods with the label selector "app=reconciler-manager".
    - The reconciler-manager Pod is running.
    - Waiting for the root-reconciler Pod to be ready ....
    -   Haven't detected running Pods with the label selector "configsync.gke.io/reconciler=root-reconciler".
    -   Haven't detected running Pods with the label selector "configsync.gke.io/reconciler=root-reconciler".
    -   Haven't detected running Pods with the label selector "configsync.gke.io/reconciler=root-reconciler".
    - The root-reconciler Pod is running.
    - The migration process is done. Please check the sync status with `nomos status`.
    
    Finished migration on all the contexts. Please check the sync status with `nomos status`.
    

**Note:** `nomos migrate` saves the original ConfigManagement object, the updated ConfigManagement object, and the converted RootSync object to a temporary directory. If `nomos migrate` fails or is terminated unexpectedly, you can manually recover the migration by running the commands provided in `nomos migrate` output.

### Roll back to the previous configuration

If you need to roll back after performing the migration with `nomos migrate`, apply the original ConfigManagement object. `nomos migrate` saves the original ConfigManagement object to a file and prints the name to the terminal. The name of the file is of the form `/tmp/nomos-migrate/CURRENT_CONTEXT/cm-original.yaml`.

To roll back to the previous configuration, copy the file path for `cm-original.yaml` and apply the file to your cluster:
    
    
    kubectl apply -f CM_ORIGINAL_PATH
    

### nomos migrate flags

To customize the `nomos migrate` command, add the following flags:

Flag | Description  
---|---  
`--connect-timeout` | Accepts a duration. Timeout duration for connecting to each cluster. Default to `3s`.  
`--contexts` | Accepts a comma-separated list of contexts to use in multi-cluster environments. Defaults to the current context. Use `"all"` for all contexts.  
`--dry-run` | Accepts a boolean. If `true`, only prints the migration output.  
`-h` or `--help` | Help for the `nomos migrate` command.  
`--remove-configmanagement` | Accepts a boolean. If `true`, migrates to OSS Config Sync by removing the ConfigManagement Operator and the ConfigManagement CRD.  
`--wait-timeout` | Accepts a duration. Timeout duration for waiting for Kubernetes resources' conditions to be true. Defaults to `10m`.  
  
## Initialize a hierarchical source of truth

You can organize your source of truth arbitrarily if you are using an [unstructured source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo). If you are using a [hierarchical source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo), you need to run the `nomos init` command to initialize a hierarchical directory:
    
    
    nomos init
    

This creates the basic directory structure of a hierarchical source of truth, including the `system/`, `cluster/`, and `namespaces/` directories.

### nomos init flags

To customize `nomos init`, add the following flags:

Flag | Description  
---|---  
`--force` | Write to directory even if nonempty, overwriting conflicting files  
`-h` or `--help` | Help for the `nomos init` command.  
`--path` | Accepts a string. The root directory to use for your source of truth. The default value is `"."`  
  
## Troubleshooting

On Linux, you might see the following error when executing a `nomos` command:
    
    
    failed to create client configs: while getting config path: failed to get current user: user: Current not implemented on linux/amd64
    

To fix this problem, create a `USER` environment variable:
    
    
    export USER=$(whoami)
    

## What's next

  * [Get started with Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
