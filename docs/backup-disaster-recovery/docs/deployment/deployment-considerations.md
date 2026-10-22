---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-considerations/
title: Backup/recovery appliance deployment considerations \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:45.850005+00:00
---

# Backup/recovery appliance deployment considerations  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup/recovery appliance deployment considerations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Following are some important considerations that affect how you deploy Backup and DR backup/recovery appliances:

  * What are your organization's Recovery Time Objective (RTO) requirements? The RTO is the maximum amount of time that you can afford to be without your data. For example, if your RTO is 4 hours,then you need to be able to access your data within 4 hours of a failure.

  * Do you need to centralize your backup management? You need to decide whether you want to manage your backups centrally or not.

    * Centralized backup management means that you have a single appliance management console to manage backups for all your workloads across all lines of business. This can be a more efficient way to manage backups, as you only need to manage a single appliance management console.
    * Decentralized backup management means that you have a separate appliance management console for each line of business. The mode of operation varies from organization to organization.
  * What is your backup use case? Do you need remote backups for disaster recovery in the event of a disaster in a production region, or is it enough to protect your data locally? If you need disaster recovery capability, you must consider cross-region backups. This means storing your backups in multiple locations, so that if one location is affected by a disaster, your data will still be accessible.




## Workloads are in a single region

Your best backup strategy within a region depends upon your needs.

### If you don't need disaster recovery (DR)

For fastest performance and lower cost, deploy the appliance management console and the backup/recovery appliances in the same region where your workloads are running. Store your backup images in the same region as your workloads.

If you also want to have backup copies off-site, then you can either store backups in a different region or use dual-region or multi-region storage. Storing backups in a different region incurs network and storage charges.

### If you need both backup and DR

For fastest performance and lower cost, deploy an appliance management console in the same region as the production workload region and a second appliance management console in a region that you can use for disaster recovery.

Deploy backup/recovery appliances in both the production workload region and the DR region to minimize recovery time objective (RTO). This makes sure that a DR environment is fully pre-provisioned and available in the event of a disaster.

**Note:** To optimize DR cost, you can wait to deploy the DR backup/recovery appliances until you actually perform DR.

Store backup images in the production region and a copy in the disaster recovery DR region, or use dual-region or multi-region storage. The production region backup copy can meet routine backup needs with faster performance. Data copied to your DR region can be used to recover your workloads in case the production region is down.

## Workloads are in multiple regions

Your best backup strategy across regions depends upon your needs.

### If you don't need disaster recovery (DR)

**Note:** A regional outage where the appliance management console is deployed affects backup operations in other regions. This is an extremely rare event. If this is undesirable, then use the strategy in If you need both backup and DR.

For fastest performance and lower cost, deploy the appliance management console in one of the regions where your workloads are running. This allows centralized management across all the workloads and regions.

Deploy one or more backup/recovery appliances in each region where the workloads are running. Store your backups in the same region as your workloads.

If you also want to have backup copies off-site, then you can either store backups in a different region or use dual-region or multi-region storage. Storing backups in a different region or multi-region incurs network and storage charges.

### If you need both backup and DR

Deploy an appliance management console in each of the production workload regions and another appliance management console in the DR region.

**Note:** If the production and DR regions overlap (for example, region A is production for some workloads and DR for others), you can use the same appliance management console for both production backups and DR recoveries in that region.

Deploy backup/recovery appliances in both the production workload regions and the DR region to minimize recovery time objective (RTO). This ensures that a DR environment is fully pre-provisioned and available in the event of a disaster.

**Note:** To reduce DR cost, you can choose to deploy the backup/recovery appliances later, when you actually perform DR.

Store backups in the production workload region and a copy in the DR region, or use dual-region or multi-region storage. The production region backup copy can be used to meet backup needs.

A backup image in the DR can be used to recover workloads if the production region is down.

## Recommended network topology for Backup and DR

Google Cloud recommends the use of Shared VPC while deploying Backup and DR. Shared VPC allows an [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) to connect resources from multiple projects to a common [VPC](https://docs.cloud.google.com/vpc/docs/vpc) (VPC) network, so that they can communicate with each other securely and efficiently using internal IPs from that network. When you use Shared VPC, you designate a project as a host project and attach one or more other service projects to it. The VPC networks in the host project are called Shared VPC networks. [Eligible resources](https://docs.cloud.google.com/vpc/docs/shared-vpc#resources_that_can_be_attached_to_shared_vpc_networks_from_a_service_project) from service projects can use subnets in the Shared VPC network.

Shared VPC lets [organization administrators](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) delegate administrative responsibilities, such as creating and managing instances, to [service project administrators](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc) while maintaining centralized control over network resources like subnets, routes, and firewalls.

The appliance management console is activated into a [service producer VPC network](https://docs.cloud.google.com/vpc/docs/private-services-access) VPC. This service producer VPC communicates with your project using [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). The primary purpose of this connection is for the appliance management console and the backup/recovery appliances to exchange metadata. Backup traffic doesn't traverse this link. However, an appliance management console needs to communicate with all of the backup/recovery appliances deployed in any network.

### Shared VPC best practices

The following best practices are recommended:

  * **Connecting to the appliance management console** : It's best to connect the service provider network to a Shared VPC within your network. All traffic from the appliance management console flows through this VPC, and therefore, through the host project. Provisioning the connectivity to the Backup and DR through a Shared VPC also enables a seamless connection between projects where the workloads are running (service projects) and the Backup and DR.

  * **Backup/recovery appliance appliance location** : The backup/recovery appliances must be deployed in a subnet that has Private Google Access enabled for connectivity to the appliance management console. There are two recommended strategies for selecting the projects for the backup/recovery appliances:

    * **In the central host project** : In this strategy, Backup and DR is treated as a central service from IT. The central backup team governs provisioning of the service. As such, all backup/recovery appliances are provisioned in the host project enabling central admins to consolidate all backup resources into a central project. This approach has the benefit of consolidating all backup-related resources and their billing into a single project.

    * **In service projects** : This strategy is suitable for more decentralized teams where service projects are created and their management is delegated to distributed teams. In this scenario, the recommended best practice is to provision VPC for downstream service projects. Backup/recovery appliance are installed in the service projects within these VPCs. This enables colocation of the workload and the backup/recovery appliance within a single project.

    * **Private Google Access** : It is a best practice to enable Private Google Access for each subnet where you install a backup/recovery appliance. This ensures the backup/recovery appliance can communicate with APIs, such as Compute Engine, Cloud Storage, and Cloud Logging, which is important for monitoring and alerting to work. To simplify and enhance connections to Google Cloud APIs, consider configuring DNS resolution for `private.googleapis.com` as documented in the [Summary of configuration options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-options) section. For Private Google Access, configure the firewall rules from the backup/recovery appliances to allow connections to the CIDR range `199.36.153.8/30` on TCP port 443.




## What's next

  * [Set up and plan a backup/recovery appliance deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
