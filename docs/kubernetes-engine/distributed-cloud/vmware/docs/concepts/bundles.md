---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/bundles/
title: About Distributed Cloud bundles \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:49.701355+00:00
---

# About Distributed Cloud bundles  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/bundles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  About Distributed Cloud bundles Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (software only) for VMware uses bundles to mitigate issues with slow proxy connections during image downloads. This page describes the different bundle types, bundle contents, naming conventions, and use cases.

## Bundle types

Distributed Cloud for VMware offers two types of bundles: regular bundles and full bundles. These bundles contain the necessary components for your cluster.

A regular bundle contains metadata and manifests only. A full bundle includes metadata, OS image OVAs, and container image tarballs.

The following table compares the contents of regular and full bundles.

Bundle Type | Contents  
---|---  
Regular | Metadata and manifests only  
Full | Metadata, OS image OVAs, and container image tarballs  
  
## Bundle naming conventions

Bundles follow specific naming conventions. You can identify a full bundle by the `-full.tgz` suffix in its filename.

For example, a full bundle might have a name similar to `gke-onprem-vsphere-[VERSION]-full.tgz`.

## Bundle use cases

Choose a bundle type based on your environment and network conditions.

### Regular bundle use cases

Use a regular bundle for standard installations. These installations typically have high-bandwidth access to Google Cloud.

### Full bundle use cases

Use a full bundle in air-gapped environments or production workstations with slow proxy connections to Google Cloud.

Full bundles offer several benefits:

  * Avoid proxy downtime.
  * Eliminate the need to enable or disable a proxy for different production environments.
  * Distribute full bundle tarballs to workstations.



You can download a full bundle in an environment without a proxy. Since the full bundle contains all system images, you can run `gkectl prepare` with the full bundle in your production workstation without connecting to Google Cloud.

## Version differences and limitations

Bundle contents and compatibility differ by Google Distributed Cloud version:

  * Versions 1.33 and higher: The full bundle includes cgroup v2 images and excludes cgroup v1 images, aligning with the default runtime requirements of newer clusters.
  * Versions 1.32 and lower: Full bundles don't contain cgroup v2 images. If you require cgroup v2 on an older version, you must use a regular bundle.



## How bundles work with private registries

You can configure a private registry in your cluster configuration files. If you configure a private registry in the admin cluster file, all user clusters pull their workload images from that private registry.

If you don't configure a private registry, system images are pulled from `gcr.io/gke-on-prem-release` using the component access service account, `component-access-sa`. For more information about private registries in Google Distributed Cloud software only for VMware, see [Configure a private container registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry).

When you have a proxy and the network speed to connect to Google Cloud is slow, you can run `gkectl prepare` without a proxy by using a full bundle. After preparation, you re-enable the proxy and expect minimum connection to external networks. This method highly improves security.

## What's next

  * To download a bundle, see [Downloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#bundle).
  * To configure the bundle path, see the [Admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field).
  * To learn more about bypassing external networks, see [Configure a private container registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
