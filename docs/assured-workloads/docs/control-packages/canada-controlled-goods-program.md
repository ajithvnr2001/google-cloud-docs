---
url: https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-controlled-goods-program/
title: Data Boundary for Canada Controlled Goods Program (CGP) \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:46.617814+00:00
---

# Data Boundary for Canada Controlled Goods Program (CGP)  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-controlled-goods-program/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Boundary for Canada Controlled Goods Program (CGP)

**Important:** Before following the guidance on this page, you should seek independent legal advice relating to your responsibilities under CGP. Nothing in this document is intended to provide you with or should be used as a substitute for legal advice. Additionally, review [CGP guidance on using cloud solutions for controlled goods data](https://www.canada.ca/en/public-services-procurement/services/industrial-security/controlled-goods/program-requirements/guidance-using-providing-cloud-solutions.html) and contact the Controlled Goods Directorate if you have any questions.

This page describes the set of controls that are applied on Canada Controlled Goods Program (CGP) workloads in Assured Workloads. It provides detailed information about [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency), supported Google Cloud products and their API endpoints, and any applicable restrictions or limitations on those products. The following additional information applies to CGP:

  * **Data residency** : The CGP control package sets data location controls to support [Canada-only regions](https://docs.cloud.google.com/assured-workloads/docs/locations#americas). See the Google Cloud-wide organization policy constraints section for more information.
  * **Customer-managed encryption keys (CMEK)** : You must use CMEK in CGP workloads for products or services that support it. During folder creation, Assured Workloads creates a key management project and a key ring for you to store your keys. See [Supporting compliance with key management](https://docs.cloud.google.com/assured-workloads/docs/key-management) for more information.
  * **Support** : Technical support services for CGP workloads are available with Enhanced or Premium [Cloud Customer Care](https://docs.cloud.google.com/support) subscriptions. CGP workloads support cases are routed to Canadian support personnel who have completed Canada Controlled Goods Program screenings. See [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support#ca-controlled-goods) for more information. 
  * **Pricing** : The CGP control package is included in Assured Workloads' _Premium tier_ , which incurs a 5% additional charge. See [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing) for more information.



## Prerequisites

To remain compliant as a user of the CGP control package, verify that you satisfy and adhere to the following prerequisites:

  * Create a CGP folder using Assured Workloads and deploy your CGP workloads only in that folder.
  * Only enable and use in-scope CGP services for CGP workloads.
  * Don't use [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) unless otherwise noted. CGP doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM page](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page.
  * Don't change the default organization policy constraint values unless you understand and are willing to accept the data residency risks that may occur.
  * When accessing the Google Cloud console for CGP workloads, you must use one of the following [Jurisdictional Google Cloud console](https://docs.cloud.google.com/assured-workloads/docs/jurisdictional-console) URLs: 
    * [console.ca.cloud.google.com](https://console.ca.cloud.google.com)
    * [console.ca.cloud.google](https://console.ca.cloud.google) for federated identity users
  * For all services used in a CGP folder, don't store controlled goods data in the following user-defined or security configuration information types: 
    * Error messages
    * Console output
    * Attribute data
    * Service configuration data
    * Network packet headers
    * Resource identifiers
    * Data labels
  * Don't enter or access controlled goods data through the Google Cloud console.
  * Consider adopting the general security best practices provided in the [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).



## Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through [organization policy constraint settings](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table.

If a product is not listed, that product is unsupported and has not met the control requirements for CGP. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the [shared responsibility model](https://docs.cloud.google.com/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users.**Important** : [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) aren't supported for any CGP products unless otherwise noted. CGP doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any CGP products. To block unwanted Google Cloud MCP servers access, see the [Control Google Cloud MCP servers use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam) page. 

Supported product | API endpoints | Restrictions or limitations  
---|---|---  
[Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) |  `dns.googleapis.com`  
|  Affected features  
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) |  `compute.googleapis.com`  
|  None   
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) |  `cloudkms.googleapis.com`  
|  None   
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) |  `logging.googleapis.com`  
|  Affected features  
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) |  `monitoring.googleapis.com`  
|  Affected features  
[Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) |  `compute.googleapis.com`  
|  Affected features  
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) |  `sqladmin.googleapis.com`  
|  Organization policy constraints  
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) |  `storage.googleapis.com`  
|  None   
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview) |  `compute.googleapis.com`  
|  Affected features and organization policy constraints  
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) |  `dataflow.googleapis.com`  
`datapipelines.googleapis.com`  
|  None   
[Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) |  `essentialcontacts.googleapis.com`  
|  None   
[External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs) |  `netapp.googleapis.com`  
|  Affected features  
[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) |  `iam.googleapis.com`  
|  None   
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) |  `compute.googleapis.com`  
|  None   
[Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) |  `compute.googleapis.com`  
|  None   
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) |  `pubsub.googleapis.com`  
|  Organization policy constraints  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#regional-td) |  `compute.googleapis.com`  
|  None   
[Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-external-proxy-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  `compute.googleapis.com`  
|  None   
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp#regional-internal-proxy-network-load-balancer) |  `compute.googleapis.com`  
|  None   
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview) |  `cloudresourcemanager.googleapis.com`  
|  None   
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) |  `secretmanager.googleapis.com`  
|  None   
[Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) |  `compute.googleapis.com`  
|  Affected features  
  
## Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on CGP folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources.

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding.   
  
Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally.

### Google Cloud-wide

#### Affected Google Cloud-wide features

Feature | Description  
---|---  
Google Cloud console | To access the Google Cloud console when using the CGP control package, you must use one of the following URLs:  


  * [console.ca.cloud.google.com](https://console.ca.cloud.google.com)
  * [console.ca.cloud.google](https://console.ca.cloud.google) for federated identity users

  
  
#### Google Cloud-wide organization policy constraints

The following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) apply across Google Cloud. 

Organization policy constraint | Description  
---|---  
[`gcp.resourceLocations`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) | Set to the following locations in the `allowedValues` list: 

  * `ca`
  * `northamerica-northeast1`
  * `northamerica-northeast2`

This value restricts creation of new resources to the selected values. When set, no resources can be created in any other regions, multi-regions, or locations outside of the selection. See [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services) for a list of resources that can be restricted by the Resource Locations organization policy constraint, as some resources may be out of scope and cannot be restricted.  
  
Changing this value by making it less restrictive potentially undermines data residency by allowing data to be created or stored outside of a compliant data boundary.   
`gcp.restrictCmekCryptoKeyProjects` | Set to `under:organizations/your-organization-name`, which is your Assured Workloads organization. You can further restrict this value by specifying a project or folder.  
  
Limits the scope of approved folders or projects that can provide [Cloud KMS keys](https://docs.cloud.google.com/kms/docs/algorithms) for encrypting at-rest data using CMEK. This constraint prevents unapproved folders or projects from providing encryption keys, thus helping to guarantee data sovereignty for in-scope services' at-rest data.   
[`gcp.restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek) | Set to a list of all in-scope [API service names](https://docs.cloud.google.com/iam/docs/full-resource-names), including: 

  * `bigquerydatatransfer.googleapis.com`
  * `compute.googleapis.com`
  * `logging.googleapis.com`
  * `pubsub.googleapis.com`
  * `sqladmin.googleapis.com`
  * `storage.googleapis.com`

Some features may be affected for each of the services listed above.   
  
Each listed service requires [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek). CMEK encrypts at-rest data with a key managed by you, not Google's default encryption mechanisms.   
  
Changing this value by removing one or more in-scope services from the list may undermine data sovereignty, because new at-rest data will be automatically encrypted using Google's own keys instead of yours. Existing at-rest data will remain encrypted by the key you provided.   
[`gcp.restrictServiceUsage`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources) | Set to allow all supported products and API endpoints.  
  
Determines which services can be used by restricting runtime access to their resources. For more information, see [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources).   
[`gcp.restrictTLSVersion`](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions) | Set to deny the following TLS versions:  


  * `TLS_1_0`
  * `TLS_1_1`

For more information, see [Restrict TLS versions](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions).   
  
### Cloud DNS

#### Affected Cloud DNS features

Feature | Description  
---|---  
Google Cloud console | Cloud DNS features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/dns/docs/apis) instead.  
  
### Cloud Logging

#### Affected Cloud Logging features

To use Cloud Logging with Customer-managed encryption keys (CMEK), you must complete the steps in the [Enable CMEK for an organization](https://docs.cloud.google.com/logging/docs/routing/managed-encryption#enable) page in the Cloud Logging documentation. Feature | Description  
---|---  
[Log sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) | Filters shouldn't contain Customer Data.  
  
Log sinks include filters which are stored as configuration. Don't create filters that contain Customer Data.   
[Live tailing log entries](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) | Filters shouldn't contain Customer Data.  
  
A live tailing session includes a filter which is stored as configuration. Tailing logs doesn't store any log entry data itself, but can query and transmit data across regions. Don't create filters that contain Customer Data.   
[Log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) | This feature is disabled.  
  
You cannot create log-based alerts in the Google Cloud console.   
[Shortened URLs for Logs Explorer queries](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#action-bar) | This feature is disabled.  
  
You cannot create shortened URLs of queries in the Google Cloud console.   
[Saving queries in Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries#saved-queries) | This feature is disabled.  
  
You cannot save any queries in the Google Cloud console.   
[SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting) | This feature is disabled.  
  
You cannot use the SQL-based alerting policies feature.   
  
### Cloud Monitoring

#### Affected Cloud Monitoring features

Feature | Description  
---|---  
[Synthetic Monitor](https://docs.cloud.google.com/monitoring/uptime-checks/introduction#about-sm) | This feature is disabled.  
[Uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/introduction#about-uptime) | This feature is disabled.  
  
### Cloud Router

#### Affected Cloud Router features

Feature | Description  
---|---  
Google Cloud console | Cloud Router features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/network-connectivity/docs/router/reference/apis) instead.   
  
### Cloud SQL

#### Affected Cloud SQL features

Feature | Description  
---|---  
Exporting to CSV | Don't use the [Exporting to CSV](https://docs.cloud.google.com/sql/docs/mysql/import-export/import-export-csv#export_data_to_a_csv_file_from) feature as it's not compliant with CGP. This feature is disabled in the Google Cloud console.   
`executeSql` | Don't use the `executeSql` method of the Cloud SQL API as it's not compliant with CGP.  
  
### Compute Engine

#### Affected Compute Engine features

Feature | Description  
---|---  
[ Suspending and resuming a VM instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) | This feature is disabled.  
  
Suspending and resuming a VM instance requires persistent disk storage, and persistent disk storage used for storing the suspended VM state cannot currently be encrypted by using CMEK. See the `gcp.restrictNonCmekServices` organization policy constraint in the section above to understand the data sovereignty and data residency implications of enabling this feature.   
[ Local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) | This feature is disabled.  
  
You will be unable to create an instance with Local SSDs because they cannot be encrypted by using CMEK. See the `gcp.restrictNonCmekServices` organization policy constraint in the section above to understand the data sovereignty and data residency implications of enabling this feature.   
Google Cloud console | The following Compute Engine features are not available in the Google Cloud console. Use the API or Google Cloud CLI instead:

  * [Health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#gcloud)
  * [Network endpoint groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups)

  
[VM metadata security considerations](https://docs.cloud.google.com/compute/docs/metadata/overview#security-considerations) | It's your responsibility not to write sensitive data to the VM metadata server.   
[Bare Metal Solution VMs](https://docs.cloud.google.com/bare-metal/docs/bms-overview) | You cannot use Bare Metal Solution VMs (o2 VMs) because Bare Metal Solution VMs are not compliant with CGP.   
  
  
[Google Cloud VMware Engine VMs](https://docs.cloud.google.com/vmware-engine/docs/overview) | You cannot use Google Cloud VMware Engine VMs, as Google Cloud VMware Engine VMs are not compliant with CGP.   
  
  
[Creating a C3 VM instance](https://cloud.google.com/blog/products/compute/introducing-c3-machines-with-googles-custom-intel-ipu) | This feature is disabled.  
  
  
[Using persistent disks or their snapshots without CMEK](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) | You cannot use persistent disks or their snapshots unless they have been encrypted using CMEK.  
  
  
[Sharing an SSD persistent disk in multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms) | You cannot share an SSD persistent disk in multi-writer mode between VM instances.   
[Adding an instance group to a global load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#global-regional) | You cannot add an instance group to a global load balancer.  
  
This feature is disabled by the `compute.disableGlobalLoadBalancing` organization policy constraint.   
[ Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) | It is possible for scripts, daemons, and binaries that are included with the guest environment to access unencrypted at-rest and in-use data. Depending on your VM configuration, updates to this software may be installed by default. See [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) for specific information about each package's contents, source code, and more.  
  
These components help you meet data sovereignty through internal security controls and processes. However, if you want additional control, you can also curate your own images or agents and optionally use the `compute.trustedImageProjects` organization policy constraint.   
  
For more information, see [Building a custom image](https://docs.cloud.google.com/compute/docs/images/building-custom-os).   
[ OS policies in VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies) |  Inline scripts and binary output files within the OS policy files are not encrypted using customer-managed encryption keys (CMEK). Don't include any sensitive information in these files. Consider storing these scripts and output files in Cloud Storage buckets. For more information, see [Example OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy).  
  
If you want to restrict the creation or modification of OS policy resources that use inline scripts or binary output files, enable the `constraints/osconfig.restrictInlineScriptAndOutputFileUsage` organization policy constraint.  
  
For more information, see [Constraints for OS Config](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).   
`[instances.getSerialPortOutput()](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getSerialPortOutput)` | This API is disabled. You will be unable to get serial port output from the specified instance using this API.  
  
Change the `compute.disableInstanceDataAccessApis` organization policy constraint value to **False** to enable this API. You can also enable and use the interactive serial port by following the instructions in [Enabling access for a project](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enable_project_access).   
`[instances.getScreenshot()](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getScreenshot)` | This API is disabled. You will be unable to get a screenshot from the specified instance using this API.  
  
Change the `compute.disableInstanceDataAccessApis` organization policy constraint value to **False** to enable this API. You can also enable and use the interactive serial port by following the instructions in [Enabling access for a project](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enable_project_access).   
  
#### Compute Engine organization policy constraints

Organization policy constraint | Description  
---|---  
`compute.enableComplianceMemoryProtection` | Set to **True**.  
  
Disables some internal diagnostic features to provide additional protection of memory contents when an infrastructure fault occurs.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
`compute.disableGlobalCloudArmorPolicy` | Set to **True**.  
  
Disables the creation of new global [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) and the addition or modification of rules to existing global Google Cloud Armor security policies. This constraint doesn't restrict the removal of rules or the ability to remove or change the description and listing of global Google Cloud Armor security policies. Regional Google Cloud Armor security policies are unaffected by this constraint. All global and regional security policies that exist prior to the enforcement of this constraint remain in effect.  
  
  
`compute.disableGlobalLoadBalancing` | Set to **True**.  
  
Disables creation of global load balancing products.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
`compute.disableGlobalSelfManagedSslCertificate` | Set to **True**.  
  
Disables creation of global self-managed SSL certificates.  
  
Changing this value may affect your workload's data residency or data sovereignty.   
`compute.disableInstanceDataAccessApis` | Set to **True**.  
  
Globally disables the `instances.getSerialPortOutput()` and `instances.getScreenshot()` APIs.  
  
Enabling this constraint prevents you from [generating credentials on Windows Server VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials#generate_credentials).   
  
If you need to manage a username and password on a Windows VM, do the following: 

  1. [Enable SSH for Windows VMs](https://docs.cloud.google.com/compute/docs/connect/windows-ssh#enable).
  2. Run the following command to change the VM's password: 
         
         gcloud compute ssh
           VM_NAME --command "net user USERNAME PASSWORD"
           

Replace the following: 
     * VM_NAME: The name of the VM you're setting the password for.
     * USERNAME: The username of the user who you're setting the password for.
     * PASSWORD: The new password.

  
`compute.disableNonFIPSMachineTypes` | Set to **True**.  
  
Disables creation of VM instance types that do not comply with FIPS requirements.  
  
  
`compute.restrictNonConfidentialComputing`  
  
| (Optional) Value is not set. Set this value to provide additional defense-in-depth. For more information, see the [Confidential VM documentation](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm).   
`compute.trustedImageProjects`  
  
| (Optional) Value is not set. Set this value to provide additional defense-in-depth.   
  
Setting this value constrains image storage and disk instantiation to the specified list of projects. This value affects data sovereignty by preventing use of any unauthorized images or agents.   
  
### Google Cloud NetApp Volumes

#### Affected Google Cloud NetApp Volumes features

Feature | Description  
---|---  
[Supported service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels) | CGP supports the following service levels:  


  * Standard
  * Premium
  * Extreme

  
  
### Pub/Sub

#### Pub/Sub organization policy constraints

Organization policy constraint | Description  
---|---  
`pubsub.enforceInTransitRegions` | Set to **True**.  
  
Ensures that Customer Data transits only within the allowed regions specified in the message storage policy for the Pub/Sub topic.  
  
Changing this value might affect your workload's data residency or data sovereignty.   
`pubsub.managed.disableSubscriptionMessageTransforms` | Set to **True**.  
  
Disables Pub/Sub subscriptions from being set with [Single Message Transforms (SMTs)](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).  
  
Changing this value might affect your workload's data residency or data sovereignty.   
`pubsub.managed.disableTopicMessageTransforms` | Set to **True**.  
  
Disables Pub/Sub topics from being set with [Single Message Transforms (SMTs)](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).  
  
Changing this value may affect your workload's data residency or data sovereignty.   
  
### Virtual Private Cloud (VPC)

#### Affected VPC features

Feature | Description  
---|---  
Google Cloud console | VPC networking features are not available in the Google Cloud console. Use the [API or Google Cloud CLI](https://docs.cloud.google.com/vpc/docs/apis) instead.  
  
## What's next

  * Learn how to [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder)
  * Understand [Assured Workloads pricing](https://cloud.google.com/assured-workloads/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
