---
url: https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option/
title: Choose a Compute Engine deployment strategy for your workload \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:41.932115+00:00
---

# Choose a Compute Engine deployment strategy for your workload  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Choose a Compute Engine deployment strategy for your workload Stay organized with collections  Save and categorize content based on your preferences. 

As a cloud architect or IT administrator, when you plan to run an application in Compute Engine, you need to design a VM topology that you can provision and operate efficiently.

Compute Engine offers a range of deployment options: for example, you could deploy a group of VMs that you manage as a single entity, or you could provision and manage the VMs as individual resources. Each approach has distinct merits and limitations. How do you choose an optimal deployment strategy?

  1. Start by assessing the key requirements of your application.
  2. Review the available deployment options and their relative merits.
  3. Select a strategy that meets your requirements and makes optimal use of the capabilities of Compute Engine.

**Note:** Compute Engine provides robust and flexible cloud infrastructure for hosting commercial off-the-shelf applications and for migrating workloads from your on-premises data centers. To learn about the hosting options in Google Cloud for other use cases, such as deploying serverless functions and running containerized applications in a Kubernetes cluster, see [App Hosting on Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/where-should-i-run-my-stuff-choosing-google-cloud-compute-option).

## Assess your workload

Use the following questions to analyze the key requirements of the workload that you want to deploy. Your answers will help you map the capabilities of each deployment option (listed in the next section) to the requirements of your workload. For an interactive, AI-powered alternative to this decision flow, you can prompt Gemini in the Google Cloud console with your project goals to get tailored deployment recommendations. For more information, see [Design compute infrastructure with Compute Advisor](https://docs.cloud.google.com/compute/docs/design-with-gemini).

**Important** : When migrating an on-premises workload to the cloud, consider any special requirements for the cloud version of the application. For example, the on-premises deployment might run in a single data center, whereas you might need the cloud topology to span more than one Google Cloud zone for higher availability. 

  * **Application state**

    * Is the application stateful?

      * A _stateful_ application stores certain data, such as the client or session ID, until that data is no longer necessary. For example, in an online shopping app, the shopping cart service might store details of items that are added or removed as the user continues shopping, and persist the final cart state when the user starts the check-out process.
      * A _stateless_ application does not need to store any client, transaction, or session data. For example, a web server might close a session after serving the content that the client requested.

To learn more about stateful and stateless applications, see [How stateful workloads are different from stateless workloads](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#how_stateful_workloads_are_different_from_stateless_workloads).

    * Should any instance-specific metadata be preserved when your VMs reboot or when Compute Engine recreates (autoheals) the VMs?

  * **Provisioning**

    * Should the VMs use a mix of machine types or images? For example, do some VMs need memory-optimized machine types while the others use general-purpose machine types?
    * Should the infrastructure scale automatically in tune with changes in load, so that you maintain an optimal balance between cost and response time?
    * Can all the VMs run within a single zone, VPC network, and subnet?
    * Should the application run in the same zone as certain other resources? For example, does the application require a low-latency connection with a database?
  * **Operations**

    * Do you want to manage the VMs as a single group? For example, would you like to automate rolling out application updates across all the VMs?
    * Do you need to use a custom or third-party tool to manage the VMs?
    * Do you need control over handling failed VMs? For example, if a VM fails, would you like it to remain stopped while you determine the root cause for the failure?
    * Do you need control over the start-stop-suspend-resume sequence or schedule of your VMs? For example, to save cost, do you plan to stop the VMs during weekends or for certain hours of the day?
  * **Resilience**

    * Does the application need protection against zonal failures? In other words, if a zone is down, would you like the application to continue serving requests from VMs in other zones in the region?
    * If a VM stops or crashes for any reason, or if the application doesn't respond to requests, should Compute Engine recreate the VM automatically?
    * Does the application need fixed internal or external IP addresses for the host VMs?



Now that you've assessed your requirements, learn about the deployment options that Compute Engine offers.

## Review the available deployment options

Review and understand the features and relative advantages of the options that you can consider for deploying your workloads to Compute Engine.

**Standalone VMs**
    With this option, you choose the machine type, image, disks, and other attributes individually for each VM that you provision. And you manage the VMs as separate resources.
**Unmanaged instance group**
    You can provision standalone VMs and add them to an instance group. You can then use the unmanaged instance group as a backend to a load balancer.
**Managed instance group (MIG)**
    

A MIG is a group of identical or similarly configured instances that you provision by using an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates).

  * You can make a MIG _stateful_ , so that specific disks or metadata are preserved.

  * For a _stateless_ MIG, you can enable autoscaling and configure a scaling policy.

  * While creating a MIG, you can choose to deploy the VMs within a single zone, or distribute them across more than one zone in a region for high availability.




The following table summarizes the key features of each deployment option.

Capability | Standalone VMs | Unmanaged instance group | Stateful MIG | Stateless MIG  
---|---|---|---|---  
[ Template-based provisioning of a group of VMs ](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) |  |  |  |   
Mix of [machine types](https://docs.cloud.google.com/compute/docs/machine-resource) and [images](https://docs.cloud.google.com/compute/docs/images) |  |  |  |   
Fixed [ internal](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address) or [ external](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) IP addresses  |  |  |  |   
[ Automatic healing of failed VMs](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) |  |  |  |   
Control over VM [start-stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) and [suspend-resume](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) operations  |  |  |  |   
[ Setting a group of VMs as a load-balancer backend](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer) |  |  |  |   
[ Disk and metadata preservation, for stateful workloads ](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) |  |  |  |   
[ Controlled update of specific VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#selective_updates) |  |  |  |   
[ Automatic rolling update of all the VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#automated_proactive_updates) |  |  |  |   
[ Automatic (and predictive) horizontal scaling](https://docs.cloud.google.com/compute/docs/autoscaler) |  |  |  |   
  
The following diagrams show sample deployments side-by-side to help you understand the key differences.

Standalone VMs | Stateful MIG | Stateless MIG  
---|---|---  
This example shows three VMs created individually.  |  This example shows a MIG containing three similarly configured VMs, provisioned by using an instance template.  |  This example shows a MIG containing three identical VMs, provisioned by using an instance template.   
![Three standalone VMs](https://docs.cloud.google.com/static/compute/images/standalone-vms.svg) |  ![A stateful MIG
                          with three VMs created by using an instance template](https://docs.cloud.google.com/static/compute/images/stateful-mig.svg) |  ![A stateless MIG with three VMs created by using an
                          instance template](https://docs.cloud.google.com/static/compute/images/stateless-mig.svg)  
  
  * Each VM in this example uses a distinct machine type, image, disks, and other attributes. 
  * The VMs were added individually to an unmanaged instance group. 

| 

  * The VMs in this example use a machine type and image defined in an instance template. 
  * A stateful policy ensures that the boot disks attached to all the VMs are stateful. 
  * Per-instance configurations add the required stateful data disks. 

| 

  * In this example, the VMs inherit the machine type and image from an instance template. 
  * The disks are recreated when the VM is updated or recreated. 
  * The MIG creates and deletes VMs automatically based on an autoscaling configuration. 

  
  
You've now assessed your workload, reviewed the deployment options that Compute Engine offers, and are ready to choose a deployment approach.

## Select a deployment strategy

The recommendations discussed here are based on a mapping of specific workload characteristics to the capabilities of each Compute Engine deployment option.

Use the following decision-making flow. If you prefer a visual guide, see the decision tree later in this document.

  1. Choose between standalone VMs and instance groups.

Requirements | Recommended deployment strategy  
---|---  
At least one of the following requirements is _essential_ for your workload. 
     * The application must run on VMs that use a mix of machine types or images. 
     * The application needs fixed internal or external IP addresses for the host VMs. 
     * You need control over handling failed VMs. 
     * You need control over your VMs' start-stop or suspend-resume operations. 
     * You need to use a custom script or third-party tool to provision and remove VMs. 
|  Choose standalone VMs.  If all the standalone VMs can run in a single zone, VPC network, and subnet, consider adding the VMs to an unmanaged instance group. You can then use the unmanaged instance group as a backend to a load balancer.  Skip the remainder of this decision-making flow.   
None of the above requirements is essential for your use case.  |  Use a MIG to set up a Compute Engine topology that is easy to manage, highly available, and scalable.  Proceed to the next step.   
  2. Choose between a stateful and stateless MIG.

Requirements | Recommended MIG type  
---|---  
The application requires disk and metadata preservation; that is, the application is stateful.  |  Choose a stateful MIG, and configure the disks that Compute Engine should preserve during disruptive events like VM recreation, autohealing, and updates.  Proceed to the next step.   
The application is not stateful.  |  Choose a stateless MIG, and take advantage of the autoscaling capability. During disruptive operations, Compute Engine recreates disks according to the instance template.  Proceed to the next step.   
  3. Choose between a zonal and regional MIG.

Requirements | Recommended MIG type  
---|---  
The application must run in a single zone, or protection against zonal failures is not essential.  |  Choose a zonal MIG.   
The application must continue to run even when a zonal failure occurs.  |  Choose a regional MIG.   

**Important** : Do review and consider the [ limitations ](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations) of each MIG type. 

### Decision tree

The following diagram guides you through the factors to consider when deciding your Compute Engine deployment strategy:

![Decision tree to choose a Compute Engine deployment strategy](https://docs.cloud.google.com/static/compute/images/migs-decision-tree.svg)

## What's next

  * Learn more about [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates).
  * Learn [how stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).
  * Learn more about [regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * [Create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
  * [Autoscale groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).
  * [Migrate an existing workload to a stateful MIG](https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
