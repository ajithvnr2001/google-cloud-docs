---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2/
title: Migrate nodes to containerd 2 \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:35.956523+00:00
---

# Migrate nodes to containerd 2  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Migrate nodes to containerd 2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) clusters use containerd [node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#available_node_images) with all worker nodes that run version 1.24 and later. The worker nodes use a specific version of containerd, based on the operating system and GKE minor version:

  * **Container-Optimized OS and Ubuntu nodes (Linux)** : 
    * Linux nodes that run GKE 1.32 or earlier, with containerd node images, use containerd 1.7 or earlier versions.
    * Linux nodes that run GKE 1.33 use containerd 2.0.
  * **Windows Server nodes** : 
    * Windows Server nodes that run GKE 1.34 or earlier, with containerd node images, use containerd 1.7 or earlier versions.
    * Windows Server nodes that run GKE 1.35 use containerd 2.0.



When GKE nodes are upgraded to the respective GKE minor version, the nodes migrate from using containerd 1.7 to the new major version, containerd 2.0. You can't change which containerd version a GKE version uses.

You can skip reading this page if you know that your workloads run as expected on containerd 2.

## How GKE is transitioning to containerd 2

Review the following timeline to understand how GKE is transitioning existing clusters to use containerd 2:

  * For Linux nodes with 1.32 and Windows Server nodes with 1.34, GKE uses containerd 1.7. containerd 1.7 deprecated both Docker Schema 1 images and the Container Runtime Interface (CRI) v1alpha2 API. To learn about other features deprecated in earlier versions, see [Deprecated config properties](https://containerd.io/releases/#deprecated-features).
  * For Linux nodes with 1.33 and Windows Server nodes with 1.35, GKE uses containerd 2.0, which removes support for Docker Schema 1 images and the CRI v1alpha2 API.
  * The following containerd config properties in the CRI plugin are deprecated and will be removed in containerd 2.4 or later, with a GKE version yet to be announced: `registry.auths`, `registry.configs`, `registry.mirrors`. `registry.configs.tls`, however, was already removed in containerd 2.0.



For approximate timing of automatic upgrades to later minor versions, see the [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

## Impact of the transition to containerd 2

Read the following section to understand the impact of this transition to containerd 2.

### Paused automatic upgrades

GKE pauses automatic upgrades in the following ways, depending on the cluster's current minor version and if the nodes in the cluster are Linux nodes or Windows Server nodes.

#### Paused automatic upgrades for Linux nodes

GKE [pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with) to 1.33 for clusters with Linux nodes when it detects that the cluster uses the deprecated features. However, if your cluster nodes use these features, we recommend creating a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) to prevent cluster upgrades. The maintenance exclusion ensures that your cluster isn't upgraded if GKE doesn't detect usage.

After you migrate from using these features, GKE resumes automatic minor upgrades to 1.33 if the following are true:

  * GKE hasn't detected usage of deprecated features in 14 days, or 3 days for deprecated CRI `registry.configs` properties.
  * 1.33 is an automatic upgrade target for your cluster.
  * There are no other blocking factors. For more information, see [The timing of automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#the_timing_of_automatic_upgrades).



You can also [manually upgrade the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

#### Paused automatic upgrades for Windows Server nodes

GKE pauses automatic upgrades to 1.35 for any clusters with Windows Server nodes, regardless of whether the cluster uses the deprecated features. GKE can't detect whether Windows Server nodes are using the deprecated features.

To upgrade your cluster with Windows Server nodes to 1.35, first follow the instructions to Migrate from deprecated features. After you've followed these instructions, you can [manually upgrade the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) to 1.35.

### End of support and the impact of failing to prepare for migration

GKE pauses automatic upgrades until the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support). If your cluster is enrolled in the [Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended), your nodes can remain on a version until the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support). For more details about automatic node upgrades at the end of support, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).

If you don't migrate from these features, when 1.32 (for Linux nodes) or 1.34 (for Windows Server nodes) reaches the end of support, and your cluster nodes are automatically upgraded to 1.33 or 1.35, you could experience the following issues with your clusters:

  * Workloads using Docker Schema 1 images fail.
  * Applications calling the CRI v1alpha2 API experience failures calling the API.



## Identify affected clusters

GKE monitors your clusters and uses the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview) to deliver guidance through insights and recommendations for identifying Linux nodes in your cluster that use these deprecated features. GKE doesn't detect usage from Windows Server nodes.

### Version requirements

Clusters receive these insights and recommendations if they're running the following versions or later:

  * 1.28.15-gke.1159000
  * 1.29.9-gke.1541000
  * 1.30.5-gke.1355000
  * 1.31.1-gke.1621000



### Get insights and recommendations

Follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations#view-insights-recs). You can get insights using the Google Cloud console. You can also use the Google Cloud CLI or the Recommender API, by filtering with the following subtypes:

  * `DEPRECATION_CONTAINERD_V1_SCHEMA_IMAGES:` Docker Schema 1 images
  * `DEPRECATION_CONTAINERD_V1ALPHA2_CRI_API:` CRI v1alpha2 API
  * `DEPRECATION_CONTAINERD_V2_CONFIG_REGISTRY_CONFIGS`: Deprecated CRI `registry.configs` properties, including `registry.configs.auth` and `registry.configs.tls`



## Migrate from deprecated features

Review the following content to understand how to migrate from features deprecated with containerd 2.

### Migrate from Docker Schema 1 images

Identify workloads using images that must be migrated, then migrate those workloads.

A Google-provided image affected by this issue is `gcr.io/google-containers/startup-script`.

  * `gcr.io/google-containers/startup-script:v1`: uses the deprecated Schema 1 format and can't be pulled on GKE 1.33 and later for Linux nodes.
  * `gcr.io/google-containers/startup-script:v2`: uses the supported Schema 2 format and can be pulled successfully.



If you are using `gcr.io/google-containers/startup-script:v1` in any of your workloads (such as DaemonSets or Deployments), you must update the image reference to `gcr.io/google-containers/startup-script:v2`.

#### Find images to be migrated

You can use different tools to find images that must be migrated.

##### Use insights and recommendations or Cloud Logging

As explained in the Identify affected clusters section, you can use insights and recommendations to find clusters with Linux nodes that use Docker Schema 1 images if your cluster is running a minimum version or later. Additionally, you can use the following query in Cloud Logging to check containerd logs to find Docker Schema 1 images in your cluster:
    
    
    jsonPayload.SYSLOG_IDENTIFIER="containerd"
    "conversion from schema 1 images is deprecated"
    

If more than 30 days have passed since the image was pulled, you might not see logs for an image.

##### Use the `ctr` command directly on a node

To query a specific node to return all non-deleted images that were pulled as Schema 1, run the following command on a node:
    
    
      ctr --namespace k8s.io images list 'labels."io.containerd.image/converted-docker-schema1"'
    

This command can be useful if, for example, you're troubleshooting a specific node and you don't see log entries in Cloud Logging because it's been more than 30 days since the image was pulled.

##### Use the `crane` open-source tool

You can also use open-source tools such as [crane](https://github.com/google/go-containerregistry/blob/v0.20.2/cmd/crane/README.md) to check for images.

Run the following `crane` command to check the schema version for an image:
    
    
    crane manifest $tagged_image | jq .schemaVersion
    

#### Prepare workloads

To prepare workloads that run Docker Schema 1 images, you must migrate those workloads to Schema 2 Docker images, or Open Container Initiative (OCI) images. Consider the following options for migrating:

  * **Find a replacement image:** you might be able to find a publicly available open-source or vendor-provided image.
  * **Convert the existing image:** if you can't find a replacement image, you can convert existing Docker Schema 1 images to OCI images with the following steps: 
    1. Pull the Docker image into containerd, which automatically converts it to an OCI image.
    2. Push the new OCI image to your registry.



### Migrate from the CRI v1alpha2 API

The CRI v1alpha2 API was [removed in Kubernetes 1.26](https://github.com/kubernetes/kubernetes/pull/110618). You must identify workloads that access the containerd socket and update these applications to use the v1 API.

#### Identify potentially affected workloads

You can use different techniques to identify workloads that might need to be migrated. These techniques might generate false positives which you must further investigate to determine that no action is needed.

##### Use insights and recommendations

You can use insights and recommendations to find clusters with Linux nodes that use the v1alpha2 API if your cluster is running a minimum version or later. For more details, see Identify affected clusters.

When viewing insights in the Google Cloud console, see the sidebar panel **Migrate your workloads off deprecated CRI v1alpha2 API**. The **Workloads to Verify** table in this panel lists workloads that _might_ be affected. This list includes any workloads that are not managed by GKE that have `hostPath` volumes containing the containerd socket path (for example, `/var/run/containerd/containerd.sock` or `/run/containerd/containerd.sock`).

It's important to understand the following:

  * **The list of workloads to verify can contain false positives. Use it only for investigation.** A workload appearing in this list does not definitively mean it is using the deprecated API, and the presence of a false positive will _not_ pause auto-upgrades. Pausing is based only on the _actually observed_ usage of the deprecated API.
  * **This list might be empty or incomplete.** An empty or incomplete list can happen if workloads that use the deprecated API were short-lived and not running when GKE performed its periodic check. The presence of the recommendation itself means that CRI v1alpha2 API usage was detected on at least one node in your cluster. Auto-upgrades resume after the deprecated API usage has not been detected for 14 days.



Therefore, we recommend further investigation by using the following methods to confirm actual API usage.

##### Check for affected third-party workloads

For third-party software deployed to your clusters, verify that these workloads don't use the CRI v1alpha2 API. You might need to contact the respective vendors to verify which versions of their software are compatible.

##### Use kubectl

The following command helps you find potentially affected workloads by looking for those that access the containerd socket. It uses similar logic to the one used for the **Workloads to Verify** table in the Google Cloud console recommendation. It returns workloads not managed by GKE that have `hostPath` volumes including the socket's path. Like the recommendation, this query might return false positives or miss short-lived workloads.

Run the following command:
    
    
    kubectl get pods --all-namespaces -o json | \
    jq -r '
      [
        "/", "/var", "/var/","/var/run", "/var/run/",
        "/var/run/containerd", "/var/run/containerd/", "/var/run/containerd/containerd.sock",
        "/run", "/run/", "/run/containerd", "/run/containerd/",
        "/run/containerd/containerd.sock"
      ] as $socket_paths |
      [
        "kube-system", "kube-node-lease", "istio-system", "asm-system",
        "gatekeeper-system", "config-management-system", "config-management-monitoring",
        "cnrm-system", "hnc-system", "gke-managed-system", "gke-gmp-system",
        "gmp-system", "gke-managed-cim"
      ] as $excluded_namespaces |
      .items[] |
      select(
        (.spec.volumes[]?.hostPath.path as $p | $socket_paths | index($p))
        and
        ([.metadata.namespace] | inside($excluded_namespaces) | not)
      ) |
      .metadata.namespace + "/" + .metadata.name
    '
    

##### Use eBPF tracing to identify API callers

For a more definitive way to identify which workloads running on Linux nodes call the CRI v1alpha2 API, you can deploy two specialized DaemonSets:

  * The `containerd-socket-tracer` logs any process opening a connection to the `containerd` socket, along with the Pod and container details.
  * The `cri-v1alpha2-api-deprecation-reporter` logs the last time the CRI v1alpha2 API was called.



These tools use [Extended Berkeley Packet Filter (eBPF)](https://en.wikipedia.org/wiki/EBPF) to trace connections to the `containerd` socket and correlate the connections with actual deprecated API calls.

You can't deploy these DaemonSets on Windows Server nodes.

By correlating the timestamps from these two tools, you can pinpoint the exact workload making the deprecated API call. This method provides a higher degree of confidence than checking for `hostPath` volumes alone, because it observes actual socket connections and API usage.

For detailed instructions about how to deploy and use these tools, and how to interpret their logs, see [Tracing containerd Socket Connections](https://github.com/GoogleCloudPlatform/k8s-node-tools/tree/master/containerd/socket-tracer).

If, after using these tools, you are still unable to identify the source of the deprecated API calls but the recommendation remains active, see Get support.

After you identify a workload that is using the CRI v1alpha2 API, either through the preceding methods or by inspecting your codebase, you must update its code to use the v1 API.

#### Update application code

To update your application, remove where the application imports the `k8s.io/cri-api/pkg/apis/runtime/v1alpha2` client library and modify the code to use the `v1` version of the API. This step involves changing the import path and updating how your code calls the API.

For example, see the following golang code, which uses the deprecated library:
    
    
      package main
    
      import (
        ...
    
        runtimeapi "k8s.io/cri-api/pkg/apis/runtime/v1alpha2"
      )
    
      func foo() {
        ...
    
        client := runtimeapi.NewRuntimeServiceClient(conn)
        version, err := client.Version(ctx, &runtimeapi.VersionRequest{})
    
        ...
      }
    

Here, the application imports the v1alpha2 library and uses it to issue RPCs. If the RPCs use the connection to the containerd socket, then this application is causing GKE to pause auto-upgrades for the cluster.

Do the following steps to search and update your application code:

  1. Identify problematic golang applications by running the following command to search for the v1alpha2 import path:
         
         grep -r "k8s.io/cri-api/pkg/apis/runtime/v1alpha2"
         

If the output of this command shows that the v1alpha2 library is used in the file, you must update the file.

For example, replace the following application code:
         
         runtimeapi "k8s.io/cri-api/pkg/apis/runtime/v1alpha2"
         

  2. Update the code to use v1:
         
         runtimeapi "k8s.io/cri-api/pkg/apis/runtime/v1"
         




### Migrate from deprecated containerd config properties

The `registry.auths`, `registry.configs`, and `registry.mirrors` containerd config properties in the CRI plugin are deprecated and will be removed in containerd 2.4 or later, with a GKE version yet to be announced. `registry.configs.tls`, however, was already removed in containerd 2.0.

#### Identify workloads

You can use different techniques to identify workloads that must be migrated.

##### Use insights and recommendations

As an initial approach, you can use insights and recommendations to find clusters with Linux nodes that use the deprecated containerd config properties. This requires a minimum GKE version. For more information about this approach, see Identify affected clusters.

When viewing insights in the Google Cloud console, see the sidebar panel **Migrate your containerd configuration off deprecated CRI registry auths field** or **Migrate your containerd configuration off deprecated CRI registry mirrors field**. To find workloads that might access the containerd configuration, check the **Workloads to Verify** section.

##### Use kubectl

Alternatively, you can use kubectl to identify workloads.

Locate workloads that modify the containerd configuration by checking for workloads with the following attributes:

  * Workloads that contain a `hostPath` volume that includes the containerd config
  * Workloads that have a container with privileged access (`spec.containers.securityContext.privileged: true`) and use the host process ID (PID) namespace (`spec.hostPID: true`)



This command might return false positives because the workload might access other files in these directories that aren't the containerd configuration. Or, this command might not return workloads which access the containerd configuration file in other, less common, ways.

Run the following command to check for the DaemonSets:
    
    
    kubectl get daemonsets --all-namespaces -o json | \
    jq -r '
      [
        "/", "/etc", "/etc/",
        "/etc/containerd", "/etc/containerd/",
        "/etc/containerd/config.toml"
      ] as $host_paths |
      [
        "kube-system", "kube-node-lease", "istio-system", "asm-system",
        "gatekeeper-system", "config-management-system", "config-management-monitoring",
        "cnrm-system", "hnc-system", "gke-managed-system", "gke-gmp-system",
        "gmp-system", "gke-managed-cim"
      ] as $excluded_namespaces |
      .items[] |
      select(
        ([.metadata.namespace] | inside($excluded_namespaces) | not)
        and
        (
          (any(.spec.template.spec.volumes[]?.hostPath.path; IN($host_paths[])))
          or
          (
            .spec.template.spec.hostPID == true and
            any(.spec.template.spec.containers[]; .securityContext?.privileged == true)
          )
        )
      ) |
      .metadata.namespace + "/" + .metadata.name
    '
    

#### Migrate from the CRI registry `auths` or `configs.auth` properties

If your workloads use the `auths` or `configs.auth` properties in the containerd config to authenticate to a private registry for pulling container images, you must migrate the workloads using those images to the `imagePullSecrets` field instead. For more information, see [Pull an Image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

To identify and migrate workloads that use the deprecated `auths` or `configs.auth` properties, review the following instructions.

##### Locate the authentication details for your registry

You can locate the authentication details for your registry in one of the following ways:

  * Review the CRI registry `auths` and `configs.auth` sections in the `/etc/containerd/config.toml` file by connecting to a GKE node.
  * Find the workload that modifies your containerd configuration file and see what authentication details are included using the previously described methods for identifying workloads. GKE doesn't use these settings for its system workloads.



If you use the `registry.configs.auth` property, the authentication details might look like the following:
    
    
      [plugins."io.containerd.grpc.v1.cri".registry.configs."$REGISTRY_DOMAIN".auth]
        username = "example-user"
        password = "example-password"
    

Collect these authentication details for each registry domain that's specified in your configuration.

##### Update your workload to use the `imagePullSecrets` field

  1. Create a Secret with your authentication details from the previous section by following the instructions to [pull an image from a Private Registry](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).
  2. Identify which workloads need to be migrated to the `imagePullSecrets` field by running the following command:
         
         kubectl get pods -A -o json |
         jq -r ".items[] |
           select(.spec.containers[] |
                 .image | startswith(\"$REGISTRY_DOMAIN\")) |
           .metadata.namespace + \"/\" + .metadata.name"
         

You must create a Secret for each namespace that's used by workloads with images from this registry domain.

  3. Update your workloads to use the `imagePullSecrets` field with the Secrets that you created in the previous step.

Alternatively, if you need to migrate a large number of workloads, you can implement a [MutatingAdmissionWebhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook) to add the `imagePullSecrets` field.




##### Update your containerd config to stop setting registry auths

After your migrate your workloads to use the `imagePullSecrets` field, you must update your workloads that modify your containerd configuration to stop setting registry auths. For any workloads that you identified as modifying the configuration, modify the workloads to stop setting registry auths.

##### Test with a new node pool and migrate workloads to the new node pool

To mitigate the risk of causing issues with your workloads, do the following:

  1. Create a new node pool.
  2. Schedule the updated workload that modifies your containerd configuration to nodes in the new node pool.
  3. Migrate your remaining workloads to the new node pool by following the instructions to [migrate workloads between node pools](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-pools#migrate-node-pools).



#### Migrate from the CRI registry `configs.tls` property

If your workloads use the `registry.configs.tls` property, you must migrate those workloads to access private registries with private CA certificates.

Follow the instructions to [migrate from configuration DaemonSets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates#migrate-config-daemonsets). This process is done with the following steps:

  1. Update your workloads that modify the containerd config to stop setting TLS details.
  2. Store the certificates in Secret Manager.
  3. Create a runtime configuration file that points to your certificates.
  4. Create a new node pool and test that your workloads that use images hosted from the private registry work as expected.
  5. Apply the configuration to a new cluster and start running the workloads on that cluster, or apply the configuration to the existing cluster. Applying the configuration to the existing cluster could potentially disrupt other existing workloads. For more information about these two approaches, see [Create a runtime configuration file](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates#create-config-file).



After you migrate, ensure that you stop applying any changes to your `registry.configs` field or you might experience issues with containerd.

## Get support

If you still can't determine the source of the deprecated API calls, and the recommendations remain active, consider the following next step:

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
