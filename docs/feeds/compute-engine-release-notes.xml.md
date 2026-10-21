---
url: https://docs.cloud.google.com/feeds/compute-engine-release-notes.xml
title: Compute Engine - Release Notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:15.859773+00:00
---

# Compute Engine - Release Notes

> Source: https://docs.cloud.google.com/feeds/compute-engine-release-notes.xml

tag:google.com,2016:compute-engine-release-notesCompute Engine - Release NotesGoogle Cloud2020-04-23T21:59:06.719027+00:00April 20, 2020tag:google.com,2016:compute-engine-release-notes#april2020202020-04-20T00:00:00+00:00
* The `us-west4` Las Vegas, Nevada region is now available to all projects and users. The zones in the `us-west4` region have [N1 and E2 machine types](https://cloud.google.com/compute/docs/machine-types). See [Regions and zones](https://cloud.google.com/compute/docs/regions-zones) for more information.
]]> April 16, 2020tag:google.com,2016:compute-engine-release-notes#april1620202020-04-16T00:00:00+00:00
* Committed use discount shared billing is now available in **beta**. You can share committed use discounts among all your projects that fall under the same billing account. For more information, see [Signing up committed use discounts](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).
]]> April 15, 2020tag:google.com,2016:compute-engine-release-notes#april1520202020-04-15T00:00:00+00:00
* You can identify VM instances that are not being used with [idle VM recommendations](https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations). Use these recommendations to reduce unused resources and reduce your compute bill. This feature is **Generally available**.
* You can manage, maintain, and view patch compliance for your VM instances using the OS patch management feature. For more information, see [OS patch management](https://cloud.google.com/compute/docs/os-patch-management). This feature is now **Generally available**.

The latest stable version of the OS Config agent is [`20200402.01`](https://github.com/GoogleCloudPlatform/osconfig/releases/tag/20200402.01). If you were using OS patch management in Beta, you can update the agent on your existing VMs, see [Updating the OS Config agent](https://cloud.google.com/compute/docs/manage-os#update-agent).

]]> April 09, 2020tag:google.com,2016:compute-engine-release-notes#april0920202020-04-09T00:00:00+00:00
* **GA:** [Compute Engine enables Shielded VM features by default](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm).
]]> April 08, 2020tag:google.com,2016:compute-engine-release-notes#april0820202020-04-08T00:00:00+00:00
* You can identify idle persistent disk resources by using [idle persistent disk recommendations](https://cloud.google.com/compute/docs/disks/viewing-and-applying-idle-pd-recommendations). Following these recommendations will help reduce unused resources and reduce your compute bill. This feature is in **Beta**.
]]> April 06, 2020tag:google.com,2016:compute-engine-release-notes#april0620202020-04-06T00:00:00+00:00
* C2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Ashburn, Northern Virginia, USA `us-east4-b,c`


* N2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * The Dalles, Oregon, USA `us-west1-b`
  * Ashburn, Northern Virginia, USA `us-east4-a`
  * St. Ghislain, Belgium `europe-west1-d`


* [N2D machine types](https://cloud.google.com/compute/docs/machine-types#n2d_machine_types) are now **Generally Available**.

]]> April 01, 2020tag:google.com,2016:compute-engine-release-notes#april0120202020-04-01T00:00:00+00:00
* You can now define where your VM instances are located relative to each other on the underlying host systems in a Google datacenter. Create a placement policy to locate VM instances close to each other for low latency, or create a policy to spread VM instances out so that they do not share the same infrastructure. See [Defining instance location within a zone](https://cloud.google.com/compute/docs/instances/define-instance-placement) to learn more.

* NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

  * Frankfurt, Germany: `europe-west3-b`



For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://cloud.google.com/compute/docs/gpus).

]]> March 31, 2020tag:google.com,2016:compute-engine-release-notes#march3120202020-03-31T00:00:00+00:00
* **Beta:** [Collect diagnostic information from Windows VMs](https://cloud.google.com/compute/docs/instances/collecting-diagnostic-information).

* C2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Frankfurt, Germany `europe-west3-a,b`
  * Ashburn, Northern Virginia, USA `us-east4-a`


* N2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * The Dalles, Oregon, USA `us-west1-a`
  * Changua County, Taiwan `asia-east1-c`


* M1 megamem machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Eemshaven, Netherlands `europe-west4-b`


* M1 ultramem machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Ashburn, Northern Virginia, USA `us-east4-a`


* M2 ultramem machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Los Angeles, California, USA `us-west2-a,c`


]]> March 24, 2020tag:google.com,2016:compute-engine-release-notes#march2420202020-03-24T00:00:00+00:00
* Committed use discounts no longer require specific ratios for cores and memory. Now you can create separate committed use discount contracts for either cores or memory. Separating cores and memory provides more flexibility and improved cost optimization. Learn more at [Purchasing commitments for machine types](https://cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#purchasecommitment).

* You can [preserve the names](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#preserving_instance_names) of your VM instances when rolling out updates in a managed instance group. This is **Generally available**.

* You can [update selected VM instances in a managed instance group](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances), with minimal disruption and in a controlled way. This is **Generally available**.

]]> March 19, 2020tag:google.com,2016:compute-engine-release-notes#march1920202020-03-19T00:00:00+00:00
* [E2 machine types](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) are **Generally available**.
]]> March 16, 2020tag:google.com,2016:compute-engine-release-notes#march1620202020-03-16T00:00:00+00:00
* N2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * London, England UK `europe-west2-b`


* C2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * St. Ghislain, Belgium `europe-west1-c,d`


]]> March 11, 2020tag:google.com,2016:compute-engine-release-notes#march1120202020-03-11T00:00:00+00:00
* You can identify VM instances that are not being used with [idle VM recommendations](https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations). Use these recommendations to reduce unused resources and reduce your compute bill. This feature is **Beta**.

* In **beta** , you can create an instance with 16 or 24 local SSD partitions for 6 TB and 9 TB of local SSD space, respectively. With 24 local SSD partitions, performance can reach a combined total of 2.4 million read IOPS. For more information, see [9 TB Local SSD maximum capacity beta](https://cloud.google.com/compute/docs/disks/local-ssd#capacity_9tb).

]]> March 09, 2020tag:google.com,2016:compute-engine-release-notes#march_09_20202020-03-09T00:00:00+00:00
* [Machine image](https://cloud.google.com/compute/docs/machine-images) is now available in **beta**. You can use machine images to store configuration, metadata, permission, and data required to create a VM instance in a single resource.
]]> March 05, 2020tag:google.com,2016:compute-engine-release-notes#march0520202020-03-05T00:00:00+00:00
* CoreOS Container Linux images will reach their end of life on May 26, 2020. For more information, see [CoreOS End-Of-Life (EOL)](https://cloud.google.com/compute/docs/eol/coreOS).
]]> March 3, 2020tag:google.com,2016:compute-engine-release-notes#march320202020-03-03T00:00:00+00:00
* You can now create [E2 machine types](https://cloud.google.com/compute/docs/machine-types#e2_machine_types) in all [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available).
]]> March 2, 2020tag:google.com,2016:compute-engine-release-notes#march220202020-03-02T00:00:00+00:00
* You can now [use the Google Cloud Console to export images to Cloud Storage](https://cloud.google.com/compute/docs/images/export-image#exporting_an_image_with_a_single_command). This is **Generally Available**.
]]> February 27, 2020tag:google.com,2016:compute-engine-release-notes#february2720202020-02-27T00:00:00+00:00
* E2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Los Angeles, USA `us-west2-a,b,c`
  * London, England, UK `europe-west2-a,b,c`
  * Frankfurt, Germany `europe-west3-b,c`
  * Tokyo, Japan `asia-northeast1-a,b,c`


* N2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Frankfurt, Germany `europe-west3 a,b`


* C2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Council Bluffs, Iowa, US `us-central1-a`


* M2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Mumbai, India `asia-south1-a`


* You can now manage, maintain, and view patch compliance for your VM instances using the OS patch management feature. For more information, see [OS patch management](https://cloud.google.com/compute/docs/os-patch-management). This feature is available in **beta**.

]]> February 24, 2020tag:google.com,2016:compute-engine-release-notes#february2420202020-02-24T00:00:00+00:00
* The `us-west3` Salt Lake City, UT region is now available to all projects and users. The zones in the `us-west3` region have the [Skylake CPU platform](https://cloud.google.com/compute/docs/cpu-platforms). See [Regions and zones](https://cloud.google.com/compute/docs/regions-zones) for more information.
]]> February 21, 2020tag:google.com,2016:compute-engine-release-notes#february2120202020-02-21T00:00:00+00:00
* NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

  * Changhua County, Taiwan: `asia-east1-a`
  * London, England, UK: `europe-west2-b`



For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://cloud.google.com/compute/docs/gpus).

]]> February 19, 2020tag:google.com,2016:compute-engine-release-notes#february1920202020-02-19T00:00:00+00:00
* M2 machine types are now available in the following [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available):

  * Northern Virginia `us-east4-a,b`


* If you have configured autohealing for your managed instance group, you can [review the health state](https://cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#checking_whether_instances_are_healthy) of each VM in the group. This is **Generally Available**.

]]> February 18, 2020tag:google.com,2016:compute-engine-release-notes#february1820202020-02-18T00:00:00+00:00
* N2D machine types are available in beta. N2D machine types are built on top of second generation AMD EPYC Rome processors. They are a great fit for general purpose workloads and for workloads that require high memory bandwidth. Learn more about these [general purpose machine types](https://cloud.google.com/compute/docs/machine-types#n2d_machine_types_beta).
]]> February 13, 2020tag:google.com,2016:compute-engine-release-notes#february1320202020-02-13T00:00:00+00:00
* NVIDIA® Tesla® T4 GPUs are now available in the following additional regions and zones:

  * London, England, UK: `europe-west2-a`
  * Seoul, South Korea: `asia-northeast3-b,c`



For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://cloud.google.com/compute/docs/gpus).

]]> February 12, 2020tag:google.com,2016:compute-engine-release-notes#february1220202020-02-12T00:00:00+00:00
* You can now maintain consistent software configurations across VM instances using guest policies. For more information, see [OS configuration management](https://cloud.google.com/compute/docs/os-config-management). This feature is available in **beta**.
]]> February 11, 2020tag:google.com,2016:compute-engine-release-notes#february1120202020-02-11T00:00:00+00:00
* To support a wide variety of BYOL scenarios, you can now [configure VMs to live migrate within a sole-tenant node group during host maintenance events](https://cloud.google.com/compute/docs/instances/windows/bring-your-own-license). This is available in **Beta**.
]]> February 07, 2020tag:google.com,2016:compute-engine-release-notes#february0720202020-02-07T00:00:00+00:00
* G Suite administrators can now choose whether to include the domain suffix in usernames generated by the OS Login API. For more information, see [Managing the OS Login API](https://cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#manage-oslogin-api). This feature is **Generally Available**.
]]> February 5, 2020tag:google.com,2016:compute-engine-release-notes#february520202020-02-05T00:00:00+00:00
* Read an [FAQ](https://cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq) that can help you evaluate whether to classify [sole-tenant node](https://cloud.google.com/compute/docs/nodes) payments as capital expenditures (CAPEX) or operational expenditures (OPEX).
]]> February 3, 2020tag:google.com,2016:compute-engine-release-notes#february320202020-02-03T00:00:00+00:00
* You can build highly available deployments of stateful workloads on VM instances using [stateful managed instance groups (stateful MIGs)](https://cloud.google.com/compute/docs/instance-groups/stateful-migs). A stateful MIG preserves the unique state of each instance (instance name, attached persistent disks, and/or metadata) on machine restart, recreation, autohealing, or update. Stateful MIGs are available in **beta**.
]]> January 31, 2020tag:google.com,2016:compute-engine-release-notes#january3120202020-01-31T00:00:00+00:00
* You can now [reschedule VMs on, off, or between sole-tenant nodes](https://cloud.google.com/compute/docs/nodes/vm-tenancy). This is **Generally Available**.

* You can now enable an [autoscaler](https://cloud.google.com/compute/docs/nodes/node-group-autoscaler) on your sole-tenant node groups. This is available in **Beta**.

]]> January 24, 2020tag:google.com,2016:compute-engine-release-notes#january2420202020-01-24T00:00:00+00:00
* The `asia-northeast3` Seoul region is now available to all projects and users. The zones in the `asia-northeast3` region have the [Skylake CPU platform](https://cloud.google.com/compute/docs/cpu-platforms). See [Regions and zones](https://cloud.google.com/compute/docs/regions-zones) for more information.
]]> January 21, 2020tag:google.com,2016:compute-engine-release-notes#january2120202020-01-21T00:00:00+00:00
* NVIDIA® Tesla® T4 GPUs are now available in the following additional zones:

  * Tokyo: `asia-northeast1-c`
  * Singapore: `asia-southeast1-c`
  * Iowa: `us-central1-f`
  * Mumbai: `asia-south1-a`



For information about using T4 GPUs on Compute Engine, see [GPUs on Compute Engine](https://cloud.google.com/compute/docs/gpus).

* You can temporarily turn off or restrict managed instance group autoscaling. The autoscaler's configuration remains intact, and all autoscaling activities resume when you turn it on again or lift the restriction. [Turning off or restricting autoscaling](https://cloud.google.com/compute/docs/autoscaler/managing-autoscalers#disable_or_restrict_an_autoscaler) for managed instance groups is now **Generally available**.

]]>
