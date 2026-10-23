---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting/
title: Troubleshoot Managed Microsoft AD \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:52.996399+00:00
---

# Troubleshoot Managed Microsoft AD  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Troubleshoot Managed Microsoft AD Stay organized with collections  Save and categorize content based on your preferences. 

This page provides tips and approaches to troubleshoot and resolve common issues with Managed Service for Microsoft Active Directory.

## Unable to create a Managed Microsoft AD domain

If you are unable to create a Managed Microsoft AD domain, verifying the following configurations can help.

### Required APIs

Managed Microsoft AD requires that you enable a group of APIs before you can create a domain.

To verify that the required APIs are enabled, complete the following steps:

###  Console 

  1. Go to the [**APIs & Services**](https://console.cloud.google.com/apis/dashboard) page in the Google Cloud console.   
[Go to APIs & Services](https://console.cloud.google.com/apis/dashboard)
  2. On the **Dashboard** page, verify that the following APIs are listed:

     * Managed Service for Microsoft Active Directory API
     * Compute Engine API
     * Cloud DNS API



###  gcloud 

  1. Run the following gcloud CLI command:
         
         gcloud services list --available
         

  2. The command returns the list of enabled APIs. Verify that the following APIs are listed:

     * Managed Service for Microsoft Active Directory API
     * Compute Engine API
     * Cloud DNS API



If any of these APIs are missing, complete the following steps to enable them:

###  Console 

  1. Go to the [**API Library**](https://console.cloud.google.com/apis/library) page in the Google Cloud console.   
[Go to API Library](https://console.cloud.google.com/apis/library)
  2. On the **API Library** page, in the search field, enter the name of the missing API.
  3. On the API information page, click **Enable**.



###  gcloud 

Run the following gcloud CLI command:
    
    
      gcloud services enable API_NAME
      

Replace `API_NAME` with the name of the missing API.

Repeat this process until all of the required APIs are enabled.

### Billing

Managed Microsoft AD requires that you enable billing before you can create a domain.

To verify that billing is enabled, complete the following steps:

###  Console 

  1. Go to the [**Billing**](https://console.cloud.google.com/billing) page in the Google Cloud console.   
[Go to Billing](https://console.cloud.google.com/billing/)
  2. Verify that there is a billing account set up for your organization.
  3. Click the **My projects** tab and then verify that the project where you are trying to create a Managed Microsoft AD domain is listed.



###  gcloud 

Run the following gcloud CLI command:
    
    
      gcloud billing projects describe PROJECT_ID
      

If you do not see a valid billing account linked to the project, you should [enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).

### IP address range

If you receive an `IP range overlap` error when you try to create a domain, it means that the reserved IP address range that you provided in the domain creation request overlaps with the IP address range of the authorized network. To resolve this issue, you should choose a different IP address range or a different authorized network. For more information, see [Select IP address ranges](https://docs.cloud.google.com/managed-microsoft-ad/docs/selecting-ip-address-ranges).

### Permissions

If you receive a `Permission denied` error when you try to create a domain, you should verify that the calling identity is allowed to call the Managed Microsoft AD API. Learn more about [Managed Microsoft AD roles and permissions](https://docs.cloud.google.com/managed-microsoft-ad/docs/access-control).

### Organization policy

The domain creation can fail because of an organization policy configuration. For example, you can configure an organization policy to allow access to only specific services, such as GKE or Compute Engine. Learn more about [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

Ask your administrator who has the organization policy administrator ([`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy)) IAM role on the organization to update the required organization policies.

#### `Resource Location Restriction` organization policy

This list constraint defines the set of locations where location-based Google Cloud resources can be created. Denying the `global` location can impact Managed Microsoft AD.

To view and update the `Resource Location Restriction` organization policy:

###  Console 

  1. Go to the **Organization policies** page in the Google Cloud console.   
[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)
  2. On the **Organization policies** page, in the **Name** column, select the **Resource Location Restriction** policy to open the **Policy summary** panel.
  3. In the **Policy summary** panel, verify that the `global` location is allowed.
  4. If you need to make a change, select **Edit** , update the policy, and then click **Save**.



Learn about [restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

###  gcloud 

  1. To view the details for the `Resource Location Restriction` organization policy, run the following gcloud CLI command. Learn about the [`gcloud resource-manager org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe) command.
         
         gcloud resource-manager org-policies describe constraints/gcp.resourceLocations \
             --organization=ORGANIZATION_ID
         

  2. If the `describe` command shows that `global` is not allowed, run the following command to allow it. Learn about the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command.
         
         gcloud resource-manager org-policies allow constraints/gcp.resourceLocations global \
             --organization=ORGANIZATION_ID
         




Learn about [restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

#### `Restrict VPC peering usage` organization policy

This list constraint defines the set of VPC networks that are allowed to be peered with the VPC networks belonging to a given resource. When you specify an authorized network for a Managed Microsoft AD domain, a VPC peering is created between the authorized network and the isolated network containing the AD domain controllers. If the organization policy for the project denies peerings, Managed Microsoft AD cannot create any peerings to the authorized network so domain creation fails. You receive an error like this:
    
    
    GCE_PRECONDITION_FAILED: Constraint constraints /compute.restrictVpcPeering
    violated for project PROJECT_ID. Peering the network projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME
    is not allowed.
    

To view and update the `Restrict VPC peering usage` organization policy:

###  Console 

  1. Go to the **Organization policies** page in the Google Cloud console.   
[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)
  2. On the **Organization policies** page, in the **Name** column, select the **Restrict VPC peering usage** policy to open the **Policy summary** panel.
  3. In the **Policy summary** panel, verify that the project allows peerings.
  4. If you need to make a change, select **Edit** , update the policy, and then click **Save**.



###  gcloud 

  1. To view the details for the `Restrict VPC peering usage` organization policy, run the following gcloud CLI command. Learn about the [`gcloud resource-manager org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe) command.
         
         gcloud resource-manager org-policies describe constraints/compute.restrictVpcPeering \
             --organization=ORGANIZATION_ID
         

  2. If the `describe` command shows that peerings are not allowed, run the following command to allow it. Learn about the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command.
         
         gcloud resource-manager org-policies allow constraints/compute.restrictVpcPeering under:projects/PROJECT_ID \
             --organization=ORGANIZATION_ID
         

Replace the following:

     * `PROJECT_ID`: the name of the project that contains the Managed Microsoft AD resource.
     * `ORGANIZATION_ID`: the ID of the organization that hosts that project.



## Unable to join a Windows VM automatically to a domain

Here are some issues with error codes that you might run into when trying to join a [Windows VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce) or [ GKE Windows Server nodes](https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke) automatically to a domain:

Error code | Description | Potential solution  
---|---|---  
`CONFLICT (409)` | Indicates that the VM instance account already exists in the Managed Microsoft AD domain. | Remove the account manually from Managed Microsoft AD using RSAT tools and try again. For more information about managing AD objects in Managed Microsoft AD, see [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).  
`BAD_REQUEST (412)` | Indicates that the domain join request contains invalid information such as incorrect domain name and incorrect organizational unit (OU) hierarchy structure. | Review the information, update the details if required, and try again.  
`INTERNAL (500)` | Indicates that the server encountered an unknown internal error. | [Contact Google Cloud Support](https://cloud.google.com/support-hub) to resolve this issue.  
`FORBIDDEN (403)` | Indicates that the specified service account doesn't have the required privileges. | Check if you have the [required privileges on the service account](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#before_you_begin) and try again.  
`UNAUTHORIZED (401)` | Indicates that the VM lacks valid authorization to join the domain. | Check if you have the [required access scope on the VM](https://docs.cloud.google.com/managed-microsoft-ad/docs/seamless-domain-join-gce#before_you_begin) and try again.  
  
## Unable to join a VM manually to a domain

If you're unable to join a machine manually from an on-premises environment to your Managed Microsoft AD domain, verify the following requirements:

  * The machine that you're trying to join is discoverable from Managed Microsoft AD. To verify this connectivity, perform a DNS lookup from the on-premises environment to the Managed Microsoft AD domain using the [`nslookup` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup).

  * The on-premises network that the machine is in must be peered with VPC network of your Managed Microsoft AD domain. For information about troubleshooting a VPC Network Peering connection, see [Troubleshooting](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#troubleshooting).




## Unable to use Shared VPC as authorized network

In order to access a Managed Microsoft AD domain from a Shared VPC network, the domain must be created in the same project that hosts the Shared VPC network.

## Unable to access Managed Microsoft AD domain

If your Managed Microsoft AD domain seems to be unavailable, you can get more information about its status by completing the following steps:

###  Console 

Go to the [**Managed Service for Microsoft Active Directory**](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.   
[Go to Managed Service for Microsoft Active Directory](https://console.cloud.google.com/security/cloud-ad)

On the **Managed Service for Microsoft Active Directory** page, in the **Status** column, you can view the statuses for your domains.

###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory domains list
    

This command returns the statuses for your domains.

If your domain status is `DOWN`, this indicates that your account may have been suspended. [Contact Google Cloud Support](https://cloud.google.com/support-hub) to resolve this issue.

If your domain status is `PERFORMING_MAINTENANCE`, Managed Microsoft AD should still be available for use, but may not allow operations such as extending schema, adding or removing regions. This status is rare and only happens when the OS is patched.

## Unable to create trust

If you follow the steps for [creating a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-manage-trusts#creating_a_trust), but cannot complete the process, verifying the following configurations can help.

### On-premises domain is reachable

To verify that the on-premises domain is reachable from the Managed Microsoft AD domain, you can use `ping` or `Test-NetConnection`. Run these commands from a VM hosted on Google Cloud and on an authorized network. Verify that the VM can reach an on-premises domain controller. Learn more about [`Test-NetConnection`](https://docs.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection?view=win10-ps).

### IP address

To verify that the IP address that was supplied during the trust setup is able to resolve the on-premises domain, run the following command:
    
    
    nslookup ON_PREMISES_DOMAIN_NAME CONDITIONAL_FORWARDER_ADDRESS
    

Replace the following:

  * `ON_PREMISES_DOMAIN_NAME`: the name of your on-premises domain.
  * `CONDITIONAL_FORWARDER_ADDRESS`: the IP address of your DNS conditional forwarder.



If there are multiple conditional forwarder addresses, you can test against any of them.

Learn more about [`nslookup`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup).

### On-premises trust relationship

To verify that the on-premises trust relationship is established, you should check that the following information matches.

  * The trust type and direction on the Managed Microsoft AD domain complements the trust created on the on-premises domain.
  * The trust secret provided while creating the trust on the Managed Microsoft AD domain matches the one entered on the on-premises domain.



The on-premises trust direction complements the trust direction configured on Managed Microsoft AD. That is, if the on-premises domain expects an inbound trust, the trust direction for the Managed Microsoft AD domain is outbound. Learn more about [trust directions](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731404\(v=ws.11\)?redirectedfrom=MSDN).

## Trust no longer works

If you previously created a trust, but it no longer works, you should verify the same configurations as you would for [troubleshooting creating a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#create-trust).

Additionally, if a trust is not used for 60 days or more, the trust password expires. To refresh the password, change the password for the trust on the on-premises domain, and then update the password on the Managed Microsoft AD domain.

## Active Directory authentication is failing (Managed Microsoft AD-hosted accounts)

If it appears that the Active Directory authentication is failing when using Managed Microsoft AD-hosted accounts, verifying the following configurations can help.

### VM is on an authorized network

To verify that the VM used to access the domain is on an authorized network, complete the following steps.

  1. Go to the [**Managed Service for Microsoft Active Directory**](https://console.cloud.google.com/security/cloud-ad) page in the Google Cloud console.   
[Go to Managed Service for Microsoft Active Directory](https://console.cloud.google.com/security/cloud-ad)

  2. Select the name of your domain.

  3. On the **Domain** page, under **Networks** , check that the authorized network is listed.




### Username and password are correct

Verify that the username and password provided to log in are correct.

### Firewall rules

A `deny` firewall rule for egress to the domain controllers' IP address range can cause authentication to fail.

To check your firewall rules, complete the following steps:

###  Console 

  1. Go to the [**Firewall rules**](https://console.cloud.google.com/networking/firewalls/list) page in the Google Cloud console.   
[Go to Firewall rules](https://console.cloud.google.com/networking/firewalls/list)

  2. On this page, check that there is not a `deny` for egress configured for the domain controllers' IP address range.




###  gcloud 

  1. Run the following gcloud CLI command:
         
         gcloud compute firewall-rules list
         

  2. This command returns a list of the configured firewall rules. Check that there is not a `deny` for egress configured for the domain controllers' IP address range.




Learn more about [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).

### IP address

Authentication can fail if the IP address is not in the reserved CIDR range.

To check the IP address, run the following command.
    
    
    nslookup DOMAIN_NAME
    

If `nslookup` fails or returns an IP address that is not in CIDR range, you should verify that the DNS zone exists.

To validate that the DNS zone exists, complete the following steps:

###  Console 

  1. Go to the [**Cloud DNS**](https://console.cloud.google.com/net-services/dns/zones) page in the Google Cloud console.   
[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/zones)

  2. On the **Cloud DNS** page, on the **Zones** tab, check the **In use by** column for the authorized network.




###  gcloud 

  1. Run the following gcloud CLI command:
         
         gcloud dns managed-zones list --filter=FQDN
         

Replace `FQDN` with the fully qualified domain name of your Managed Microsoft AD domain.




If none of the listed zones are in use by the authorized network, you should remove and re-add the authorized network.

### Network peering

Authentication can fail if VPC network peering is not properly configured.

To verify peering is set up, complete the following steps:

###  Console 

  1. Go to the **VPC network peering** page in the Google Cloud console.   
[Go to VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. On the **VPC network peering** page, in the **Name** column, look for a peering called `peering-VPC_NETWORK_NAME`.




###  gcloud 

  1. Run the following gcloud CLI command:
         
         gcloud compute networks peerings list --network=VPC_NETWORK_NAME
         

  2. This command returns a list of peerings. In the list, look for one called `peering-VPC_NETWORK_NAME`.




If `peering-VPC_NETWORK_NAME` is not in the list, you should remove and re-add the authorized network.

## Active Directory authentication is failing (via trust)

If it appears that the Active Directory authentication is failing when using managed on-premises hosted accounts via trust, you should verify the same configurations as you would for [troubleshooting creating a trust](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#create-trust).

Additionally, verify that the account is in the `Cloud Service Computer Remote Desktop Users` delegated group. Learn more about [delegated groups](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#groups)

## Unable to access the domain from a manageability VM

If you are unable to access the Managed Microsoft AD domain from the VM used for [managing AD objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects), you should verify the same configurations as you would for [troubleshooting Active Directory authentication for Managed Microsoft AD-hosted accounts](https://docs.cloud.google.com/managed-microsoft-ad/docs/troubleshooting#active-directory-authentication).

## `Org policy` error when creating, updating, or deleting

If you encounter an `org policy` error when creating, updating, or deleting resources, you may need to change an organization policy. Learn about [Organization Policy Constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

Ask your administrator who has the organization policy administrator ([`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy)) IAM role on the organization to update the required organization policies.

### `Define allowed APIs and services` organization policy

This list constraint defines the set of services and APIs that can be enabled on a given resource. Its descendants in the resource hierarchy also inherit the constraint. If this constraint does not allow the APIs that are required for Managed Microsoft AD, you receive an error when you try to create, update, or delete resources.

To view and update the `Define allowed APIs and services` organization policy:

###  Console 

  1. Go to the **Organization policies** page in the Google Cloud console.   
[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)
  2. On the **Organization policies** page, in the **Name** column, select the **Define allowed APIs and services** policy to open the **Policy summary** panel.
  3. In the **Policy summary** panel, verify that the following APIs are not denied: 
     * `dns.googleapis.com`
     * `compute.googleapis.com`
  4. If you need to make a change, select **Edit** , update the policy, and then click **Save**.



###  gcloud 

  1. Run the following gcloud CLI command. Learn about the [`gcloud resource-manager org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe) command.
         
         gcloud resource-manager org-policies describe constraints/serviceuser.services \
             --organization=ORGANIZATION_ID
         

  2. If the `describe` command shows that `dns.googleapis.com` or `compute.googleapis.com` is not allowed, run the following command to allow it. Learn about the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command.
         
         gcloud resource-manager org-policies allow constraints/serviceuser.services API_NAME \
             --organization=ORGANIZATION_ID
         




### `Restrict VPC peering usage` organization policy

This list constraint defines the set of VPC networks that are allowed to be peered with the VPC networks belonging to a given resource. If peerings are denied, you receive an error when you try to create, update, or delete resources. Learn how to view and update the `Restrict VPC peering usage` organization policy.

## Unable to resolve on-premises resources from Google Cloud

If you are unable to resolve on-premises resources from Google Cloud, you may need to change your DNS configuration. Learn [how to configure DNS forwarding to resolve queries for non-Managed Microsoft AD objects in VPC networks](https://docs.cloud.google.com/managed-microsoft-ad/docs/resolve-non-managed-objects-vpc).

## Intermittent DNS lookup failures

If you are experiencing intermittent DNS lookup failures when using a highly available scheme for Cloud Interconnect or multiple VPNs, you should verify the following configurations:

  * A route for 35.199.192.0/19 exists.
  * The on-premises network allows traffic from 35.199.192.0/19 for all Cloud Interconnect connections or VPN tunnels.



## Delegated administrator account password expires

If the password for the delegated administrator account has expired, you can [reset the password](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin#reset-password). Make sure that you have the required permissions to reset the password for the delegated administrator account. If you want, you can also [disable the password expiration](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin#disable-password-expiration) for the account.

## Unable to view Managed Microsoft AD audit logs

If you are unable to view any Managed Microsoft AD audit logs in the Logs Viewer or Logs Explorer, you should verify the following configurations.

  * [Logging is enabled for the domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs#verifying-logs).
  * You have the `roles/logging.viewer` IAM role on the project where the domain is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
