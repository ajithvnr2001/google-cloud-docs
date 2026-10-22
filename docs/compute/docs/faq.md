---
url: https://docs.cloud.google.com/compute/docs/faq/
title: Google Compute Engine FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:16.498289+00:00
---

# Google Compute Engine FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Google Compute Engine FAQ Stay organized with collections  Save and categorize content based on your preferences. 

## About Compute Engine

This section answers general questions about Compute Engine.

### What is Compute Engine? What can it do?

Compute Engine is an Infrastructure-as-a-Service product offering flexible, self-managed virtual machines (VMs) hosted on Google's infrastructure. Compute Engine includes Linux- and Windows-based VMs running on KVM, local and durable storage options, and a REST-based API for configuration and control. The service integrates with Google Cloud technologies such as [Cloud Storage](https://docs.cloud.google.com/storage), [App Engine](https://docs.cloud.google.com/appengine), and [BigQuery](https://docs.cloud.google.com/bigquery) to extend beyond the basic computational capability to create more complex and sophisticated apps.

### What is a virtual CPU in Compute Engine?

On Compute Engine, each virtual CPU (vCPU) is implemented as a single hardware hyper-thread on one of the available [CPU Platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms). On Intel Xeon processors, [Intel Hyper-Threading Technology](https://www.intel.com/content/www/us/en/support/articles/000098959/processors/intel-xeon-processors.html) allows multiple application threads to run on each physical processor core. You configure your Compute Engine VMs with one or more of these hyper-threads as vCPUs. The [machine type](https://docs.cloud.google.com/compute/docs/machine-types) specifies the number of vCPUs that your instance has.

You can identify the specific CPU platform for your instance using one of the following options:

  * See what CPU platforms are available in each of the [available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * Use the [`compute.instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) to obtain the `cpuPlatform` property for one of your existing instances.
  * On Linux instances, run `cat /proc/cpuinfo`.



If you want to change the CPU platform for your instance, you can [specify a minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform).

### How do App Engine and Compute Engine relate to each other?

We see the two as being complementary. App Engine is Google's Platform-as-a-Service offering and Compute Engine is Google's Infrastructure-as-a-Service offering. App Engine is great for running web-based apps, line of business apps, and mobile backends. Compute Engine is great for when you need more control of the underlying infrastructure. For example, you might use Compute Engine when you have highly customized business logic or you want to run your own storage system.

### How do I get started?

[Try the Getting Started guides](https://docs.cloud.google.com/compute/docs/quickstart) for the service. After you have finished the quickstart, read the [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances) overview to start learning about Compute Engine.

You might be eligible for a [ free trial](https://console.cloud.google.com/freetrial). For information about how the free trial works, including information about quotas, see the [ Free cloud features and trial offer](https://docs.cloud.google.com/free/docs/free-cloud-features).

## Billing

This section answers questions about Compute Engine billing.

### How does pricing and purchasing work?

Compute Engine charges based on compute instance, storage, and network use. VMs are charged on a per-second basis with a 1 minute minimum. Storage cost is calculated based on the amount of data you store. Network cost is calculated based on the amount of data transferred between VMs that communicate with each other and with the Internet. For more information, [review our price sheet](https://cloud.google.com/products/compute/pricing).

### Do your prices include tax?

No, the price sheet does not include tax.

## Support and feedback

This section answers questions about Compute Engine support and feedback.

### Do you offer paid support?

Yes, we offer paid support for enterprise customers. For more information, contact our [sales organization](https://docs.cloud.google.com/contact).

### Do you offer a Service Level Agreement (SLA)?

Yes, we offer a [Compute Engine SLA](https://cloud.google.com/compute/sla).

### Where can I send feedback?

For billing-related questions, you can send questions to the appropriate [support channel](https://support.google.com/cloud/contactflow).

For feature requests and bug reports, submit an issue to our [issues tracker](https://issuetracker.google.com/issues/new?component=187134&template=0).

## Authentication

This section answers questions about authentication and authorization.

### How can I authenticate to the Compute Engine API?

How you authenticate to the Compute Engine API depends on the method used to access the API: client libraries, Google Cloud CLI, or REST. For more information, see [Authenticate to Compute Engine](https://docs.cloud.google.com/compute/docs/authentication).

To authenticate apps or workloads to Google Cloud APIs, see [Choose a workload authentication method](https://docs.cloud.google.com/compute/docs/access/app-authentication-methods).

### What are service accounts?

A _service account_ is an account that represents an application, as opposed to representing an end user. These accounts can be used to authorize Compute Engine to act on the behalf of the user to access non-sensitive information. A service account is never used to access user information. Service accounts simplify the process of authenticating from Compute Engine to other services by handling the authorization process for the user.

Compute Engine developers typically use Compute Engine service accounts in their applications. For more information about service accounts, see [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).

### How do I create a service account?

Compute Engine creates a service account automatically when you create a new instance and [specify a service account scope](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) for that instance.

## Projects

This section answers questions about projects in Compute Engine.

### What are projects?

A [project](https://docs.cloud.google.com/compute/docs/projects) is a container for all Compute Engine resources. Each project is a totally compartmentalized world; projects don't share resources, can have different owners and users, are billed separately, and are no more accessible to each other than your home computer is accessible to your neighbor's computer.

### How can I create a project?

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account. If you don't already have one, [ Sign up for a new account](https://accounts.google.com/SignUp). 
  2. Go to the [Google Cloud console](https://console.cloud.google.com/compute/instances). When prompted, select an existing project or create a new project. **Important:** The name you use must be between 4 and 30 characters. When you type the name, the form will suggest a project ID, which you can edit. The project ID you use must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character cannot be a dash. You should be aware that some resource identifiers (such as project IDs) might be retained beyond the life of your project. For this reason, avoid storing sensitive information in resource identifiers. ...see naming guidelines
  3. Follow the prompts to set up billing. If you are new to Google Cloud, then you have 90 days, $300 [ free trial](https://docs.cloud.google.com/free/docs/free-cloud-features) credit to pay for your instances. 



### What is the difference between a project number and a project ID?

Every project can be identified in two ways: the project number or the project ID. The project number is automatically created when you create the project, whereas the project ID is created by you, or whoever created the project. The project ID is optional for many services, but is required by Compute Engine. For more information, see [Google Cloud console Projects](https://docs.cloud.google.com/compute/docs/projects).

### Where can I find my project ID?

You can find your project ID on the [Google Cloud console](https://console.cloud.google.com/), which provides a list of your projects and their project IDs upon entry.

### Where can I request more quota for my project?

By default, all Compute Engine projects have [default quotas](https://docs.cloud.google.com/compute/docs/resource-quotas) for various resource types. However, these default quotas can be increased on a per-project basis. Check your quota limits and usage in the [quota page](https://console.cloud.google.com/iam-admin/quotas) on the Google Cloud console. If you reach the limit for your resources and need more quota, make a request to increase the quota for certain resources using the [IAM quotas page](https://console.cloud.google.com/iam-admin/quotas). You can make a request by clicking the **Edit Quotas** button on the top of the page.

## Instances

This section answers questions about compute instances.

### What kind of machine configuration (memory, RAM, CPU) can I choose for my instance?

Compute Engine offers several configurations for your instance. You can also create custom configurations that match your exact instance needs. See the full list of available options on the [Machine Types](https://docs.cloud.google.com/compute/docs/machine-types) page.

### If I accidentally delete my instance, can I retrieve it?

No, instances that have been [deleted](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) cannot be retrieved. However, if an instance is only [stopped](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance), then you can [ start](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance) it again.

### What operating systems can my instances run on?

Compute Engine supports several [operating system images](https://docs.cloud.google.com/compute/docs/images#os-compute-support) and third-party images. Additionally, you can [create a customized version of an image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) or [build your own image](https://docs.cloud.google.com/compute/docs/tutorials/building-images).

### What are the available zones I can create my instance in?

For a list of available regions and zones, see [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### How do I find out how much quota I have used or have left?

Check your quota limits and usage in the [quota page](https://console.cloud.google.com/iam-admin/quotas) on the Google Cloud console. If you reach the limit for your resources and need more quota, click the **Request increase** button on the [quota page](https://console.cloud.google.com/iam-admin/quotas) and complete the request form.

### What kind of virtual CPU do I have running on my instance?

Check the specific CPU platform for your instance using one of the following options:

  * See what CPU platforms are available in each of the [available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * Use the [`compute.instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) to obtain the `cpuPlatform` property for one of your existing instances.
  * On Linux instances, run `cat /proc/cpuinfo`.



### What are Preemptible VM instances, and how are Preemptible instances different from normal instances?

Preemptible instances are instances that you can create and run at a much lower price than normal instances, but might stop if Compute Engine needs to reclaim the compute capacity for allocation to other VMs. For more information, see [Create and use preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible).

### How can I send outbound emails from a Compute Engine instance?

Generally, Compute Engine blocks outbound traffic through these [blocked ports](https://docs.cloud.google.com/firewall/docs/firewalls#blockedtraffic). However, you can set up a mail gateway through Google using SMTP. For more information, read [Sending Email from an Instance](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail).

### There was a host error with my virtual machine and it was restarted. What happened?

A host error (`compute.instances.hostError`) means that there was a hardware or software issue on the physical machine or the data center infrastructure hosting your compute instance that caused your instance to crash. A host error involving a total hardware failure or other hardware issues might prevent the [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) of your instance. If your instance is set to automatically restart, which is the default setting, Compute Engine restarts your instance, typically within three minutes from the time the error was detected. Depending on the issue, the restart might take up to 5.5 minutes.

After a compute instance encounters a host error, or you report its host as faulty, the instance's host requires emergency, unplanned maintenance. By default, Compute Engine provides a few hours of advance notice when it schedules this type of maintenance.

Occasionally, a compute instance might become unresponsive before a host error is signaled. You can reduce the amount of time Compute Engine waits to restart or terminate the instance by setting the host error recovery timeout. For more information, see [Set the policy for an existing instance](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#updatingoption). 

Physical hardware and software failures can happen occasionally but are rare occurrences. To protect your applications and services from these potentially disruptive system events, review the following resources:

  * [Designing robust systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems)
  * [Patterns for scalable and resilient apps](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps)
  * [ Creating managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances)



Google also offers managed services such as [App Engine](https://docs.cloud.google.com/appengine) and the [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible).

To determine if a host error caused your VM to shut down, see [Diagnosing VM shutdowns and reboots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reboots#diagnosing_vm_shutdowns_and_reboots).

## Images

This section answers questions about the OS images that you can use for your instances.

### Do I need to enable the Cloud Storage service before I can store my images externally?

Yes, to store images externally, you need to enable the [Cloud Storage](https://docs.cloud.google.com/storage) service.

## Persistent Disk

This section answers questions about storage using Persistent Disk.

### How do I choose the right size for my Persistent Disk volume?

Persistent Disk performance scales with the size of the Persistent Disk volume. Use the [Persistent Disk performance chart](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) to help decide what size disk works for you. If you're not sure, read the documentation to [decide how big to make your Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).

### Do Persistent Disk volumes cache writes?

No, Persistent Disk volumes don't cache writes. Successful completion of a write command occurs only after the data has been transferred to stable media.

### LVM for Compute Engine

Logical Volume Manager (LVM) is only available for select Red Hat Enterprise Linux (RHEL) images provided by Google Cloud. If you require the flexibility of LVM on other Linux OS images, we recommend the following approaches to volume management on Compute Engine:

  * Use secondary disks. You can avoid the need for root disk resizing by using secondary disks without partitions. Depending on the scenario, using secondary disks can lower the risk of an outage due to error.
  * [Resize the file system and partitions](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) on a zonal persistent disk. Before you make any file system modifications, backup your disk by [taking a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots). In the event of failures during the file system resize, you can use the snapshot to recover the disk.
  * Use existing images that have LVM-based roots by [importing them](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) or [migrating your existing VMs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0) into Compute Engine.



### What steps does Google take to protect my data?

See [Disk Encryption](https://docs.cloud.google.com/compute/docs/disks#pd_encryption).

### Can I attach my Persistent Disk volume to more than one instance?

You can attach a Persistent Disk volume to multiple instances only if the disk is in read-only mode. An SSD Persistent Disk volume in multi-writer mode can be attached to two N2 virtual machine (VM) instances. You cannot attach a Persistent Disk volume in both read-write mode and read-only mode at the same time. For more information, see [Share Persistent Disk volumes between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

### When should I use Persistent Disk versus Cloud Storage?

Both Persistent Disk and Cloud Storage can both be used to store files but are very different offerings. Cloud Storage is a massive file container, designed to store extremely large amounts of relatively static data which can be accessed globally, including from Compute Engine virtual machine instances.

The following chart provides some information about the characteristic specialties of each offering and what they are best used for.

| Cloud Storage | Persistent Disk  
---|---|---  
Characteristics | 

  * Accessibility 
    * Global accessibility (including non-Compute Engine systems)
    * Accessible read/write from many systems
  * Scale 
    * Multi-PB scale buckets
  * How to use 
    * REST interface; higher latency than locally attached block storage
    * Write semantics at the file level only
    * Offers versioning
    * Files implicit in Cloud Storage

| 

  * Accessibility 
    * Regional accessibility and only by Compute Engine instances
    * Mounted read/write by one instance or read-only by many Compute Engine instances
  * Scale 
    * 64 TB volume limit
  * How to use 
    * SCSI interface; lower latency
    * Write semantics are transactional - random edits
    * No versioning; continuous edits
    * Must format a file system to make usable for files

  
Target Users | 

  * Content distribution for mobile, consumer, gaming, and SaaS
  * Rich media
  * Read-only input for parallelizable HPC work (e.g., rendering and genomics)
  * Backup and archival
  * Hadoop (via GHFS)

| 

  * Compute Engine boot devices
  * Raw block datastore to build 
    * SQL servers (e.g., MySQL)
    * NoSQL servers (e.g., Cassandra/Mongo)
    * Fileservers (e.g., Gluster)
    * Key value store persistence (e.g., Redis)

  
  
## Networking

This section answers questions about networking in Compute Engine.

### Where can I find Compute Engine IP ranges?

Google Cloud publishes a JSON-formatted list of customer-usable global and regional external IP address ranges in [cloud.json](https://www.gstatic.com/ipranges/cloud.json).

**Important:** In the past, Google Cloud instructed users to inspect the `_cloud-netblocks.googleusercontent.com` DNS TXT record (and the records it referenced). Update your scripts or software libraries so that they read from the _cloud.json_ file instead. The JSON file includes additional information, such as the region to which a regional external IP address is attached.

Other Google Cloud IP ranges:

  * [Health check IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges)

  * Cloud DNS source ranges for traffic sent to [forwarding targets](https://docs.cloud.google.com/dns/zones#firewall-rules) or [alternative name servers](https://docs.cloud.google.com/dns/docs/policies#firewall-rules)

  * Source ranges used by [TCP forwarding for Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#preparing_your_project_for_tcp_forwarding)

  * For information about how to determine source ranges for Google APIs and services, see [network configuration for Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config).




### Why is traceroute missing hops to internet-bound destinations?

Running `traceroute` on a Compute Engine VM instance either shows only the destination or some hops towards internet-bound destinations. For more information, see [Traceroute to internet-bound destinations](https://docs.cloud.google.com/vpc/docs/vpc#traceroute) in the VPC documentation.

## Zones

This section answers questions about the zones where you can use Compute Engine resources.

### Do I have the option of using a regional data center in selected countries?

Yes, Compute Engine offers data centers around the world. These data center options are designed to provide low latency connectivity options from those regions. For specific region information, including the geographic location of regions, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

### How can I tell if a zone is offline?

The [Compute Engine **Zones**](https://console.cloud.google.com/compute/zones) section in the Google Cloud console shows the status of each zone. You can also get the status of zones through the [command-line tool](https://docs.cloud.google.com/compute/docs/quickstart) by running `gcloud compute zones list`, or through the Compute Engine API with the [`compute.zones.list`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zones/list) method.

## Startup scripts

This section answers questions about startup scripts that you can use with your instances.

### When does my custom startup script run?

[Startup scripts](https://github.com/GoogleCloudPlatform/guest-agent/#metadata-scripts) run at the end of the boot process.

## Infrastructure maintenance events

This section answers questions about maintenance events for your instances.

### What are infrastructure maintenance events?

Compute Engine might periodically need to perform scheduled maintenance on zones that may affect your instances. By default, all instances are configured so that these maintenance events are transparent to your apps and workloads. This may cause some performance degradation but your instances will remain online through the maintenance event. For more information, see [Transparent maintenance](https://docs.cloud.google.com/compute/docs/regions-zones#maintenance).

### How often do scheduled infrastructure maintenance events happen?

Infrastructure maintenance events don't have a set interval between occurrences, but generally happen once every two weeks.

### How do I know if an instance will be undergoing an infrastructure maintenance event?

Shortly before a maintenance event, Compute Engine changes a special attribute in a virtual machine's metadata server before any attempts to live migrate or stop and restart the virtual machine as part of a pending infrastructure maintenance event. The `maintenance-event` attribute is updated before and after an event, letting you detect when these events are imminent. You can use this information to help automate any scripts or commands you want to run before or after a maintenance event. For more information, see [Host maintenance](https://docs.cloud.google.com/compute/docs/metadata/overview#host_maintenance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
