---
url: https://docs.cloud.google.com/kubernetes-engine/versioning/
title: GKE versioning and support \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:23.575317+00:00
---

# GKE versioning and support  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/versioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE versioning and support Stay organized with collections  Save and categorize content based on your preferences. 

This page explains versioning in Google Kubernetes Engine (GKE), and the policies for version support. Over time, GKE upgrades clusters to newer versions of Kubernetes. To learn more about how upgrades work, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades).

You can see the current versions rollout and support schedule in the [ GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

**Note:** The Kubernetes API is versioned separately from Kubernetes itself. Refer to the [Kubernetes API documentation](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-versioning) for information about Kubernetes API versioning.

## Minor version support

GKE support for Kubernetes minor versions is based on Kubernetes open source policies. To support available minor versions during their lifecycle, GKE provides patch versions and regularly performs automatic cluster upgrades to apply those newer patches. For information about how GKE supports patch versions, see Patch version support.

In addition to supporting available minor versions, GKE also provides alpha patch versions of the _next minor version_ in the Kubernetes release cycle up to four months before that minor version becomes available to all clusters in the Rapid channel. These alpha versions are available only to GKE alpha clusters in the Rapid channel and are intended for early adopters who want to experiment with upcoming features.

### How Kubernetes supports a minor version

The Kubernetes Open Source Software (OSS) community releases a minor version with new features and enhancements [three times a year](https://github.com/kubernetes/kubernetes/releases). Each release cycle is approximately 15 weeks long.

Kubernetes supports each minor version for 14 months. Major bugs and security vulnerabilities found in a supported minor version are fixed with the release of an ad hoc patch version. The Kubernetes community sometimes revises their version support calendar, as necessary. To learn more, see [Support period](https://kubernetes.io/releases/patch-releases/#support-period).

### How GKE supports a minor version

Before the release of a stable new minor version, the Kubernetes project releases experimental, unstable patch versions of that minor version. GKE introduces _alpha patch versions_ that are based on these experimental versions in the _Rapid_ channel to only GKE alpha clusters. Similarly to other patch versions in the Rapid channel, alpha versions are excluded from the [GKE SLA](https://cloud.google.com/kubernetes-engine/sla).

After Kubernetes releases the stable new minor version, GKE removes the alpha versions of that minor version and makes patch versions for that minor version available to any cluster that's in the Rapid channel. Because the Rapid channel provides the newest GKE patch versions, these versions are excluded from the [GKE SLA](https://cloud.google.com/kubernetes-engine/sla) and might contain issues without known workarounds.

After the initial availability in the Rapid channel, GKE promotes the new minor version to the Regular channel. GKE provides up to a total of _24 months of support_ for a minor version after the version has been made available for new cluster creation in the [_Regular_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) channel. This support includes around 14 months of _standard support_ and approximately an additional 10 months of _extended support_ available with the [_Extended_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended) channel. To see the availability of specific minor versions, review the [ GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

## GKE minor version lifecycle

The lifecycle of a GKE minor version includes the following key steps:

  1. Up to four months before the release date for a minor version, GKE makes alpha patch versions for that minor version available in the Rapid channel to only alpha clusters.
  2. Kubernetes releases the new minor version.
  3. GKE makes the new minor version available in the Rapid channel and removes any existing alpha patch versions for that minor version.
  4. GKE makes the new minor version available in the Regular channel (start of standard support period).
  5. During the standard support period, GKE provides patches for the minor version which include new features, security fixes, and bug fixes.
  6. The minor version reaches the end of standard support after approximately 14 months in total, entering the period of extended support. After this time, GKE provides security patches for clusters in the Extended channel.
  7. The minor version reaches the end of extended support, meaning that the minor version will receive no further security patches.



### Adjustments of version availability

GKE might revise the end of support for GKE versions, due to shifts in policy in the Kubernetes OSS community, the discovery of vulnerabilities, or other technical issues that cannot be reasonably resolved. GKE might also extend end of support dates around key business periods such as Black Friday and Cyber Monday.

GKE provides at least 14 months of standard support, and up to a total of 24 months of support with extended support.

To get the latest available versions, see the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). GKE regularly updates the release schedule to reflect the timing of auto-upgrades.

### Periods of availability in the minor version lifecycle

GKE provides the following periods of availability for a Kubernetes minor version:

![Periods of support. GKE supports a minor version for a total of 24 months.](https://docs.cloud.google.com/static/kubernetes-engine/images/periods-of-support.svg)

See the following table summarizing the periods of availability, described in detail in the next sections:

Period of availability | Approximate timespan from Regular channel availability | What support does GKE provide | Access to this period of availability  
---|---|---|---  
Alpha version availability period | Month -5 through Month -1 | GKE introduces new alpha patch versions in the Rapid channel until the start of the Rapid-only availability period. The alpha patch versions are available only to alpha clusters, have no technical support or SLA, and are highly likely to contain issues. When the minor version becomes available to all clusters in the Rapid channel at the end of the alpha-only availability period, GKE removes all alpha versions from the Rapid channel. | Rapid channel only (requires alpha clusters)  
Rapid-only availability period | Month -1 through Month 0 | GKE makes the minor version available to all clusters in the Rapid channel by providing patch versions with new features, security fixes, and bug fixes. However, these versions are excluded from the [GKE SLA](https://cloud.google.com/kubernetes-engine/sla) and may contain issues without known workarounds. GKE also removes any available alpha versions for that minor version from the Rapid channel. | Rapid Channel only  
Standard support period | Month 1 through Month 14 | GKE provides patch versions with new features, security fixes, and bug fixes. | Rapid, Regular, Stable, Extended, No Channel ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel))  
Extended support period | Month 15 through Month 24 | GKE provides patch versions with security fixes. | Extended Channel only (requires additional fee per cluster, see [Get long-term support with the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended))  
  
#### Period of alpha version availability

GKE releases alpha patch versions of an upcoming minor version in the Rapid channel up to four months before the release of that minor version. The alpha versions are available only for alpha clusters. GKE releases additional alpha patch versions in the weeks that follow and typically maintains between one and three active alpha versions.

This period lasts until GKE releases the stable minor version in the Rapid channel. After the stable release, GKE removes all of the alpha patch versions for that minor version from the Rapid channel because stable patch versions are available to install.

#### Period of Rapid-only availability

GKE first releases a new minor version in the Rapid channel. The version first accumulates usage and demonstrates stability across clusters in this channel before being promoted to the Regular channel. Only clusters enrolled in the Rapid channel can run a new minor version during this period of availability.

This period typically lasts around 1-2 months, however the exact timing depends on each minor version. For details, see [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

#### Period of standard support

The period of standard support for a GKE minor version begins when the version is released to the Regular channel. All GKE clusters, regardless of release channel enrollment, can run a minor version in standard support. During this period, GKE automatically upgrades clusters on a regular basis to new patch versions, which include new features, security fixes, and bug fixes.

GKE automatically upgrades clusters in the following way:

  * **Rapid, Regular, Stable, No Channel ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel))**: Automatic upgrades to other supported minor versions, or patch versions of the same minor version.
  * **Extended** : GKE only automatically upgrades to newer patch versions of the same minor version.



For clusters not enrolled in the Extended release channel, GKE eventually automatically upgrades clusters to the next supported minor version before the end of standard support, based on the schedule for the cluster's release channel. For details, see [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels). However, GKE doesn't upgrade clusters during this period if they use [deprecated features or APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with). You can use a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) to temporarily prevent GKE from upgrading your cluster to the next minor version.

##### End of standard support (formerly _end of life_)

**Note:** GKE previously used the term _end of life_ to refer to the end of standard support date. With the introduction of extended support, we updated this term to reflect the multiple periods of support for a GKE minor version.

After the standard support period, the minor version reaches the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) (formerly known as _end of life_) and becomes unsupported and unavailable for all clusters not enrolled in the Extended channel.

Customers running an end of support version are notified through an email to the project contact before the end of support of a version. GKE also begins to gradually auto-upgrade nodes (regardless of auto-upgrade enablement) running unsupported versions for security and compatibility purposes because no new security patches or bug fixes are provided for end of support versions. Before engaging with Cloud Customer Care for any issues with a cluster or nodes running an unsupported version, you must first upgrade your cluster and nodes to a supported version.

GKE minor versions that have reached the end of support no longer receive security patches or bug fixes. Patch versions of a minor version that has reached the end of support are unsupported and unavailable. GKE automatically upgrades all clusters not enrolled in the Extended channel. To learn more, see Automatic upgrades at the end of support.

#### Period of extended support

After the end of standard support, the minor version reaches the period of extended support (Month 15 through Month 24). During this period, GKE provides patches for security fixes, including the following types of fixes:

  * Medium, high, and critical security patches for core Kubernetes components, node operating system and Google-managed containers bundled with the GKE cluster version.
  * For Container-Optimized OS, the node operating system's end of support might come before the end of extended support for the GKE minor version, or introduce incompatible changes. To learn more about how GKE continues to provide support, see Container-Optimized OS updates during the extended support period.



Towards the end of extended support, GKE begins upgrading clusters to the next minor version. GKE won't upgrade clusters that use deprecated features or APIs. You can use a maintenance exclusion to temporarily prevent GKE from upgrading your cluster to the next minor version.

#### End of extended support

At the end of extended support, GKE doesn't provide any patches for security fixes, and the minor version is considered unsupported. GKE upgrades clusters still running the unsupported minor version to the next minor version, regardless of the cluster's use of deprecated features or APIs.

## Automatic upgrades at the end of support

GKE schedules automatic upgrades for clusters from one minor version to the next supported minor version before the minor version reaches the end of support. The timing of this upgrade depends on the schedule for the cluster's release channel. For details, see [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels). For example, clusters enrolled in the Stable channel are upgraded to the next minor version closer to the end of standard support than clusters enrolled in the Rapid channel.

During the standard support period, and extended support period for clusters enrolled in the Extended channel, you can prevent this minor version upgrade with maintenance exclusions at the cluster level, or by [choosing what types of upgrades GKE performs in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#what-type-of-upgrades-scope). Additionally, GKE won't upgrade clusters using deprecated features or APIs.

However, at the end of standard support, or at the end of extended support for clusters enrolled in the Extended channel, GKE automatically upgrades clusters to the next supported minor version to ensure that the cluster remains performant, available, and secure.

Each GKE minor version is supported for 14 months of standard support and for 24 months of total support, including extended support. You can't keep your cluster on a minor version indefinitely, because operating a cluster that uses an unsupported GKE minor version carries significant security, reliability, and compatibility risk as GKE doesn't provide security patches or bug fixes for end of support minor versions. GKE can't commit to providing patches or updates for minor versions at the end of support.

GKE upgrades the cluster in the following way:

  * **Control plane** : GKE automatically upgrades cluster control planes to supported versions when the control plane version is no longer available for new cluster creation.
  * **Nodes** : GKE automatically upgrades nodes that are running an unsupported minor version after the minor version has reached end of support to help to ensure cluster health and alignment with the GKE version skew policy. Nodes running unsupported minor versions are typically scheduled for an automated upgrade to a supported minor version within one month of the [end of support date](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule_for_static_no-channel_versions). Nodes running unsupported minor versions might not be upgraded immediately upon minor version end of life, and actual timing can vary at Google's discretion.



Similarly, GKE upgrades the cluster control planes that haven't been upgraded to a new version in 90 days. For more information, see Control plane 90-day patch policy.

### Temporary, emergency prevention of automatic upgrades at the end of support

As a temporary measure, to be used only in emergencies where no other options are available, you can delay the automatic upgrades at the end of support for up to 90 days after the end of support date by [configuring a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configure-maintenance-exclusion) with the default scope of "No upgrades". We don't recommend this practice because of the risks associated with running an unsupported version. After the maintenance exclusion expires, GKE upgrades the cluster.

### Identify clusters running a minor version past the end of standard support

GKE identifies clusters that meet both of the following conditions:

  * The control plane runs a minor version that has reached the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support).
  * The cluster isn't enrolled in the [Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended).



GKE recommends that you upgrade these clusters because of the risks associated with running an unsupported minor version. GKE upgrades clusters to the next supported minor version if the existing version isn't supported in the cluster's release channel.

GKE delivers this guidance with an insight and recommendation through the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview). This guidance doesn't apply to clusters that are enrolled in the Extended channel, which can continue to run a minor version until the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support). To learn more about how to manage insights and recommendations from Recommender, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

To find clusters where the control plane is running a version past the end of support, you can use one of the following ways:

  * Use the Google Cloud console.
  * Use the gcloud CLI or Recommender API, by specifying the `CLUSTER_VERSION_END_OF_LIFE` [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype).



For instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation, [upgrade your cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp) to a supported minor version. For supported minor versions and end of support dates, see the [ GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule). Or, [change your cluster to the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#change-to-extended) if you want to continue to use the existing minor version until the end of extended support.

## Container-Optimized OS updates during the extended support period

During the period of extended support for a GKE minor version, GKE provides patch upgrades for the cluster. These patch upgrades might include Container-Optimized OS updates to the existing Container-Optimized OS milestone used by the GKE minor version. GKE minor versions typically use one milestone during the period of standard support through the beginning of the period of extended support.

However, the Container-Optimized OS milestone used by the GKE minor version reaches its own end of support, typically during the extended support period for a GKE minor version. When this occurs, GKE builds all subsequent GKE patch versions with the next Container-Optimized OS milestone. To learn more about milestone lifecycles, see the [versioning scheme](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning) for Container-Optimized OS.

Review the following scenario to understand how automatic upgrades proceed, and what decisions cluster administrators must make when GKE can no longer introduce Container-Optimized OS updates in the same milestone for a GKE minor version.

### The Container-Optimized OS milestone reaches the end of support before the minor version end of extended support

The [Container-Optimized OS milestone](https://docs.cloud.google.com/container-optimized-os/docs/resources/support-policy) reaches its own end of support before the end of extended support for the minor version that uses the milestone. In this scenario, GKE uses the next available Container-Optimized OS milestone for future patch upgrades. GKE performs this update before the Container-Optimized OS milestone that's used by the minor version reaches the end of support.

Cluster administrators must evaluate whether to upgrade the cluster's worker nodes, because GKE won't automatically upgrade these nodes to the next patch version with the new milestone. You can manually upgrade the nodes to the next GKE patch version, which contains a new milestone. Or, you can keep the nodes running the same GKE patch version to not use the new milestone. However, the nodes won't receive security patches until upgrading to the next patch or minor version.

#### Automatic upgrades for the new Container-Optimized OS milestone

The next patch version for a GKE minor version in the extended support period uses a newer Container-Optimized OS milestone from previous patch versions. GKE automatically upgrades clusters in the following ways when the new patch version becomes an auto-upgrade target:

  * **Control plane upgrades** : 
    * GKE upgrades the control plane to the next patch version, as normal.
  * **Node upgrades** : 
    * GKE doesn't upgrade nodes to the next patch version.
    * GKE upgrades the nodes to the next minor version towards the end of extended support, as normal. To learn more, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).



Because the new milestone version might introduce changes that are incompatible with your workloads, GKE pauses automatic node upgrades to the next patch version. You can manually upgrade to the new patch version if you've determined that your workloads are compatible with the next Container-Optimized OS milestone. If you manually upgrade your nodes to a patch version which uses the new Container-Optimized OS milestone, GKE resumes automatic patch upgrades of the nodes because the nodes now run the new milestone.

#### Cluster notification when new patch versions use the new milestone

GKE sends a [cluster notification](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications) informing you when this situation occurs. This notification is sent when the first patch version that uses the new Container-Optimized OS milestone becomes available in the Extended channel.

When you receive this notification, evaluate whether you want to manually upgrade the nodes to the next patch or minor version, or receive no later patch versions for this minor version during the period of extended support. To learn more, see [New patch versions change to new Container-Optimized OS milestone during extended support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#extended-patch-new-cos-milestone).

## Versioning scheme

Kubernetes releases use the [Semantic Versioning standard](https://semver.org/) for version numbers (X.Y.Z). GKE appends a GKE patch version number to the Kubernetes version (X.Y.Z**-gke.N**).

Kubernetes major version (X)
    Major versions typically are incremented if any backwards incompatible changes are introduced to the public API. A major version increments the Kubernetes version from X.Y to X+1.Y.
Kubernetes minor version (Y)
    Kubernetes releases a new minor version [three times a year](https://github.com/kubernetes/kubernetes/releases). Each release cycle is approximately 15 weeks long. [Deprecated APIs](https://kubernetes.io/docs/reference/using-api/deprecation-guide/) might be removed with a new minor version, for example with [1.22](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22). A minor version release increments the Kubernetes version from 1.Y to 1.Y+1. For example, Kubernetes 1.32 is the minor release that follows Kubernetes 1.31.
Kubernetes patch version (Z)
    Kubernetes releases patch versions during the 12-month period that follows a minor version release. A patch version release increments the Kubernetes version from X.Y.Z to X.Y.Z+1. For example, 1.32.6 is the patch release that follows 1.32.5.
GKE patch version (-gke.N)
    

GKE releases patch versions that correspond to upstream Kubernetes patch versions. The GKE patch versions can include security updates, feature changes, and bug fixes for GKE alongside the open source Kubernetes software. These updates or fixes are required for compatibility and interoperability with Google Cloud.

GKE might release multiple GKE patch versions for each Kubernetes patch version. For example, Kubernetes patch version 1.35.6 has GKE patch versions like 1.35.6-gke.1638000, 1.35.6-gke.1641000, and 1.35.6-gke.1250000.

GKE patch versions typically become available each week. Patch releases are incrementally rolled out to each [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available).

GKE alpha patch version (X.Y+1.Z-gke.N+preview) - alpha clusters only
    

GKE releases _alpha patch versions_ for an upcoming Kubernetes minor version up to four months before the release date for that minor version. These pre-release patch versions are available for experimentation and testing in GKE alpha clusters that are enrolled in the Rapid release channel. Alpha patch versions always target the next minor version in the Kubernetes release cycle before that minor version release. For example, if minor version 1.36 is the most recent stable release and 1.37 hasn't yet been released, the alpha patch versions are for version 1.37.

### Checking available and default versions

For information about available versions, see the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

To check the default and available GKE versions, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page:

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the **Location type** section, choose a location type and the region or zone for your cluster control plane.

  3. In the **Target release channel** list, select a release channel.

  4. Open the **Target version** list. This list displays all of the available GKE patch versions for the release channel. The default patch version for the release channel is automatically selected. If you select the Rapid release channel, then you also see any available alpha patch versions for the upcoming minor version.


**Note:** If you use the Google Cloud console to create a cluster before a version rollout has completed, the lists of available versions might not be accurate for your zone.

###  gcloud 

To check the available and default versions for a specific release channel, run one of the following commands:

  * Check the available versions:
        
        gcloud container get-server-config \
            --flatten="channels" \
            --filter="channels.channel=RELEASE_CHANNEL" \
            --format="yaml(channels.channel,channels.validVersions)" \
            --location=COMPUTE_LOCATION
        

Replace the following:

    * `RELEASE_CHANNEL`: the name of the release channel. Specify one of the following values:

      * `RAPID`
      * `REGULAR`
      * `STABLE`
      * `EXTENDED`
    * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) that you want to check.

The output is similar to the following:
    
    channels:
      channel: RAPID
      validVersions:
      - 1.36.2-gke.2064000
      - 1.36.2-gke.1498000
      - 1.35.6-gke.1641000
      - 1.35.6-gke.1638000
      - 1.35.6-gke.1258000
      - 1.34.9-gke.1610000
      - 1.34.9-gke.1322000
      - 1.33.13-gke.1269000
      - 1.33.13-gke.1109000
    

In the Rapid channel, the `previewVersions` field indicates the GKE alpha patch versions for the upcoming Kubernetes minor version. These versions are available only to [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

  * Check the default version:
        
        gcloud container get-server-config \
            --flatten="channels" \
            --filter="channels.channel=RELEASE_CHANNEL" \
            --format="yaml(channels.channel,channels.defaultVersion)" \
            --location=COMPUTE_LOCATION
        

The output is similar to the following:
        
        channels:
          channel: RAPID
          defaultVersion: 1.36.2-gke.1498000
        

  * Check the available alpha patch versions in the Rapid channel:
        
        gcloud container get-server-config \
            --flatten="channels" \
            --filter="channels.channel=RAPID" \
            --format="yaml(channels.channel,channels.previewVersions)" \
            --location=COMPUTE_LOCATION
        

The output is similar to the following:
        
        channels:
          channel: RAPID
          previewVersions:
          - 1.37.0-gke.2064000+preview
        




To check the available and default versions for clusters that use no channel ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)), run one of the following commands:

  * Check the default version:
        
        gcloud container get-server-config \
            --format="value(defaultClusterVersion)" \
            --location=COMPUTE_LOCATION
        

Replace `COMPUTE_LOCATION` with the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) that you want to check.

The output is similar to `1.35.6-gke.1127000`.

  * Check the available control plane versions:
        
        gcloud container get-server-config \
          --format="yaml(validMasterVersions)" \
          --location=COMPUTE_LOCATION
        

The output is similar to the following:
        
        validMasterVersions:
        - 1.36.2-gke.2064000
        - 1.36.2-gke.1498000
        - 1.36.2-gke.1346000
        - 1.36.0-gke.4681000
        - 1.36.0-gke.4447000
        - 1.35.6-gke.1641000
        - 1.35.6-gke.1638000
        - 1.35.6-gke.1258000
        - 1.35.6-gke.1250000
        - 1.35.6-gke.1127000
        - 1.35.6-gke.1049000
        

  * Check the available node versions:
        
        gcloud container get-server-config \
          --format="yaml(validNodeVersions)" \
          --location=COMPUTE_LOCATION
        

The output is similar to the following:
        
        validNodeVersions:
        - 1.36.2-gke.2064000
        - 1.36.2-gke.1498000
        - 1.36.2-gke.1346000
        - 1.36.0-gke.4681000
        - 1.36.0-gke.4447000
        - 1.35.6-gke.1641000
        - 1.35.6-gke.1638000
        - 1.35.6-gke.1258000
        - 1.35.6-gke.1250000
        - 1.35.6-gke.1127000
        - 1.35.6-gke.1049000
        # Multiple lines are omitted here
        


**Note:** For advanced `get-server-config` output manipulation, see the gcloud CLI documentation about [filtering](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) and [formatting](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats).

### Specifying cluster version

When you create or upgrade a cluster using the gcloud CLI, you can use the `--cluster-version` flag to specify either a cluster version or an alias.

For **both Autopilot and Standard clusters** , you can use the following alias when you create a cluster:

  * `upgrade-target` ([Preview](https://cloud.google.com/products#product-launch-stages)): For clusters enrolled in a [rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing), this alias resolves to the target version of a cluster's [stage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#concepts). Otherwise, GKE uses the release channel's [auto-upgrade target version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target). You can only use this alias during cluster creation. It can't be used during cluster upgrades.



For **Standard clusters only** , you can specify an available version (such as `1.30.2-gke.1500`) or use one of the following aliases:

  * `latest`: The highest supported Kubernetes version available in the cluster's zone or region. Specifying `latest` doesn't provide automatic upgrades. Enable [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) to ensure that the nodes in your cluster are up-to-date with the latest stable version.
  * `1.X`: The highest valid patch release in the specified minor version.
  * `1.X.Y`: The highest valid `gke.N` patch in the specified patch release.
  * `-`: The default Kubernetes version for control planes. For node upgrades, this specifies the version that the cluster control plane is running.

You can use these aliases for both cluster creation and cluster upgrades.




### Specifying node version

_This section applies only to clusters created in the Standard mode. In Autopilot clusters, nodes are upgraded automatically to the control plane version, and you can't specify a version._

When you [create or upgrade a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools), you can specify its version. By default, nodes run the same version of GKE as the control plane. Nodes can be no more than two minor versions older than control planes.

With rare exceptions, node versions remain available even if the cluster version is no longer available.

## Control plane 90-day patch policy

To help ensure that a GKE cluster receives critical security patches and other fixes in a timely manner, GKE requires that a cluster's control plane is upgraded to a new patch (or minor) version at least every 90 days. GKE, by default, automatically upgrades the control plane of clusters more frequently than every 90 days. But, you can delay these control plane upgrades by configuring [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) or [choosing what types of upgrades GKE performs in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#what-type-of-upgrades-scope). However, similar to automatic upgrades at the end of support, if you have a GKE cluster that hasn't been upgraded as required, GKE automatically upgrades your cluster to a later patch version regardless of any policies that you configured.

## GKE version skew policy

The GKE version skew policy ensures that a GKE cluster maintains compatibility between the control plane and nodes. In a GKE cluster, nodes can match the control plane version or run up to two minor versions earlier than the control plane.

The nodes can't run versions newer than the control plane version. For example, if the cluster's control plane runs version 1.31, the nodes can run the following versions: 1.31, 1.30, or 1.29, but not 1.28 or earlier. The version of the nodes can't be newer than the control plane version due to the [Kubernetes OSS version skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).

To ensure supportability and reliability, nodes should use a supported version regardless of following a valid version skew.

### Identify clusters with an unsupported version skew

GKE identifies clusters in which the nodes are running a version that is incompatible with the control plane due to version skew. GKE recommends that you upgrade the nodes running this unsupported version, delivering this guidance with an insight and recommendation through the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview). To learn more about how to manage insights and recommendations from Recommender, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

To find clusters with an unsupported version skew, you can use one of the following ways:

  * Use the Google Cloud console.
  * Use the gcloud CLI or Recommender API, by specifying the `CLUSTER_VERSION_SKEW_UNSUPPORTED` [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype).



For instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation, [upgrade any nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) that are running a minor version that is more than two minor versions earlier than the control plane version.

## Support for skipping minor versions

GKE does not allow skipping minor versions for the cluster control plane, however you can skip patch versions. Worker nodes can skip minor versions. For example, a node pool can be upgraded from version 1.32 to 1.34 while skipping version 1.33.

To upgrade a cluster across multiple minor versions, upgrade your control plane one minor version at a time and upgrade your worker nodes to the same version each time. For example, to upgrade your control plane from version 1.32 to 1.34, upgrade it from version 1.32 to 1.33 first, then upgrade your worker nodes to match the control plane version, and then repeat the process to upgrade from version 1.33 to 1.34.

Upgrading your worker nodes to match versions helps you to avoid unsupported version skew. We recommend that you avoid version skipping when possible. Skipping worker node versions usually implies a larger testing scope that, although manageable, requires more consideration.

Alternatively, you can create a new cluster with the version you want and redeploy your workloads.

## Patch version support

GKE first introduces a patch version to the Rapid channel, and then gradually promotes this patch version through other release channels. When GKE makes a patch version available in a release channel, you can create, upgrade, or—in [specific cases](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading-limitations)—downgrade your cluster to this version. While a minor version is supported, GKE continues to introduce new patch versions of the minor version in a release channel.

Earlier patch versions remain available in the release channel for nodes until the minor version reaches its end of support, but are removed and made unavailable for use with the control plane before that date. When GKE removes a patch version for use with the control plane, you can't create, upgrade, or downgrade your cluster's control plane to the removed patch version. If your cluster's control plane runs a removed patch version, we recommend that you upgrade the control plane to the latest auto-upgrade target.

### Deprecation of patch versions for the control plane

The following information applies to any patch version where the minor version has already been introduced to the Regular channel.

Before GKE removes patch versions from a release channel for use with a cluster control plane, GKE deprecates the patch version. Although deprecated patch versions are no longer listed as available for the control plane, you can still use them to create, upgrade, or downgrade your control plane.

We recommend upgrading to a newer patch version as soon as possible; use deprecated versions only if your environment's rollout process strictly prevents you from upgrading sooner. GKE deprecates a patch version for 90 days, or until the minor version reaches the end of standard support (Regular, Stable, No channel) or the end of extended support (Extended channel).

## Alpha version support

**Caution:** Alpha versions are unstable versions of Kubernetes that are intended for experimentation. These versions have the same expectations of technical support and stability as the [Preview](https://cloud.google.com/products#product-launch-stages) launch stage.

_Alpha versions_ are GKE patch versions of an upcoming Kubernetes minor version that GKE releases up to four months before the minor version is available to all clusters in the Rapid channel. These alpha versions are available only in GKE [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) and are intended for early adopters who want to experiment with upcoming features with no expectation of stability or support.

The Rapid channel has between one and three alpha patch versions available for the upcoming minor version. In the months before GKE makes the minor version available to all clusters in the Rapid channel, GKE introduces new alpha patch versions and removes existing versions. Because alpha patch versions are available only in alpha clusters, the following considerations apply:

  * You can't upgrade the alpha clusters to new versions. To test a new alpha version, create an alpha cluster that runs that version.
  * Alpha clusters that run a removed alpha version continue to exist until the clusters expire 30 days after creation or until you delete the clusters.
  * Fixes for CVEs and bugs in specific system components aren't retroactively applied to existing alpha patch versions. To get these fixes, you must create an alpha cluster that runs a more recent alpha patch version.



After GKE releases a stable minor version in the Rapid channel, GKE removes the alpha patch versions for that minor version. Alpha versions of the _next_ minor version in the release cycle become available in the Rapid channel up to four months before the release date for that minor version.

### Alpha version lifecycle

The alpha version lifecycle has the following milestones:

  1. Kubernetes releases the first development version for the upcoming minor version (`X.Y+1.0-alpha.0`).
  2. Up to four months before the upcoming minor version release date, GKE introduces alpha patch versions for that minor version in the Rapid channel (`X.Y+1.0-gke.N+preview`).
  3. Kubernetes releases the stable minor version (`X.Y.0`).
  4. GKE makes the stable minor version available in the Rapid channel (`X.Y.0-gke.N`). GKE removes the alpha versions for that minor version from the Rapid channel.



The lifecycle of an alpha version doesn't affect the GKE minor version lifecycle.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
