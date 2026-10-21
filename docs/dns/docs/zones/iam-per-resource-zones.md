---
url: https://docs.cloud.google.com/dns/docs/zones/iam-per-resource-zones/
title: Set and manage IAM policies for managed zones \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.018747+00:00
---

# Set and manage IAM policies for managed zones  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/iam-per-resource-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Set and manage IAM policies for managed zones Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions about how to set up specific read, write, or administrator Identity and Access Management (IAM) permissions for different managed zones under the same project.

For detailed information about IAM policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/policies). For information about the IAM policy API, see [`Policy`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy). To learn how to create IAM custom roles that you can use on your managed zones, see [Understanding IAM custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.managedZones.setIamPolicy` for the `setIamPolicy` method
  * `dns.managedZones.getIamPolicy` for the `getIamPolicy` method
  * `dns.managedZones.list` for the `testIamPermission` method



**Roles**

  * `roles/iam.securityAdmin`
  * `roles/dns.admin`



This procedure assumes that you have created a managed zone in a project. For instructions about how to create a managed zone, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).

## Set IAM policy for a managed zone

To set the IAM policy on a specific managed zone, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/zones)

  2. Select one or more zones for which you want to add access control permissions.

  3. On the **Permissions to resources** page, click **Add principal**.

  4. On the **Grant access to resource** page, under **New principals** , add the email address of the user, group, domain, or service account that you want to add as the new principal.

  5. From the **Assign roles** list, select the role that you want to assign to the principal.

  6. To assign additional roles, click **Add another role**.

  7. Click **Save**.




###  gcloud 

Run the [`gcloud dns managed-zones set-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy):
    
    
    gcloud dns managed-zones set-iam-policy NAME \
      --policy-file=POLICY-FILE
    

Replace the following:

  * `NAME`: the name of the managed zone for which you want to set the IAM permission
  * `POLICY-FILE`: the file that contains the IAM policy that you want to specify for the managed zone. For an example policy file, see [Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy)



If this command runs successfully, it returns the IAM policy. Otherwise it returns an error message specifying the error.

###  API 

Send a `POST` request by using the [`managedZone.setIamPolicy`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/setiampolicy) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/MANAGED_ZONE:setIamPolicy
    

Replace the following:

  * `PROJECT_ID`: the name or ID of the project
  * `MANAGED_ZONE`: the name of the managed zone for which you want to set the IAM permission



For detailed information on this API call, see [Binding](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#binding) on the IAM `Policy` API page.

### Grant access to specific resource record sets

Cloud DNS supports using [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to provide granular access control for specific resource record sets (RRsets) within a managed zone.

You can configure granular access control using one of the following methods:

  * **Standard Role (Recommended):** Use the standard `roles/dns.admin` role with a specific IAM condition that allows necessary non-record-set operations. This is the simplest approach as it doesn't require creating custom roles.
  * **Custom Roles:** Create two custom roles to separate record set management from other administrative tasks.



#### Method 1: Standard Role (Recommended)

To use the standard `roles/dns.admin` role, you must include additional resources in your IAM condition. This is because to successfully modify DNS records, the principal must have permission to perform both the record modification itself and the associated operations on Change resources.

Depending on your security requirements, you can choose one of the following condition structures:

  * **Permissive:** Allows all other DNS administrative actions. This is equivalent to the Custom Roles approach if the complementary role contains all other standard administrative permissions. `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && <RRSET_CONDITION>) || (resource.type != 'dns.googleapis.com/ResourceRecordSet')`
  * **Restrictive:** Only allows record set modifications and operations on Change resources. Other administrative actions, including listing record sets (`dns.resourceRecordSets.list`) and describing the managed zone, are blocked. `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && <RRSET_CONDITION>) || (resource.type == 'dns.googleapis.com/Change')`



Replace `<RRSET_CONDITION>` with your specific access requirements (see Example conditions).

To grant permissions: 1\. Assign the `roles/dns.admin` role to the principal on the managed zone.

  1. Add the condition (Permissive or Restrictive) to the binding.



#### Method 2: Custom Roles

If you prefer not to use complex conditions, you can create custom roles to separate permissions.

##### Prerequisite: Create custom roles

  1. Create a record set management role (for example, `DnsRecordSetAdmin`) that contains the following permissions:

     * `dns.resourceRecordSets.create`
     * `dns.resourceRecordSets.delete`
     * `dns.resourceRecordSets.get`
     * `dns.resourceRecordSets.update`
  2. Create a complementary role (for example, `DnsNonRecordSetAdmin`) that contains **all remaining permissions** from the standard `roles/dns.admin` role. These additional permissions (such as `dns.changes.create` and `dns.managedZones.get`) are necessary for the overall administration of the zone and to satisfy prerequisite checks when modifying records.




##### Grant permissions

To ensure that your conditional policies work as expected, you must grant these roles to the principal as follows:

  1. Grant the complementary role unconditionally: Assign the role that contains the remaining administrative permissions (for example, `DnsNonRecordSetAdmin`) to the principal **unconditionally** on the managed zone.
  2. **Grant the record set management role conditionally:** Assign the role that contains the record set permissions (for example, `DnsRecordSetAdmin`) to the principal **conditionally** based on your specific access requirements.



#### Example conditions

The following examples show how to restrict access using the `resource.name` and `resource.type` attributes.

**Note:** Cloud DNS resource names in IAM conditions use the **numeric managed zone ID** , not the human-readable zone name.

If you are using **Method 1 (Standard Role)** , you must append the appropriate non-record-set clause (for example, `|| (resource.type != 'dns.googleapis.com/ResourceRecordSet')`) to these expressions.

  * **Exact Record Match:** Grant permission to manage only the A record for `api.example.com.`.

    * **Custom Roles / Raw Condition:** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.endsWith('/rrsets/api.example.com./A'))`
    * **Standard Role (Permissive):** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.endsWith('/rrsets/api.example.com./A')) || (resource.type != 'dns.googleapis.com/ResourceRecordSet')`
    * **Standard Role (Restrictive):** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.endsWith('/rrsets/api.example.com./A')) || (resource.type == 'dns.googleapis.com/Change')`
  * **Subdomain Delegation:** Grant permission to manage all records within the `p.example.com.` subdomain.

    * **Custom Roles / Raw Condition:** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.extract('/rrsets/{name}/').endsWith('.p.example.com.'))`
    * **Standard Role (Permissive):** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.extract('/rrsets/{name}/').endsWith('.p.example.com.')) || (resource.type != 'dns.googleapis.com/ResourceRecordSet')`
  * **Manage All Records of a Specific Type:** Grant permission to manage all `A` records in the zone.

    * **Custom Roles / Raw Condition:** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.endsWith('/A'))`
    * **Standard Role (Permissive):** `none (resource.type == 'dns.googleapis.com/ResourceRecordSet' && resource.name.endsWith('/A')) || (resource.type != 'dns.googleapis.com/ResourceRecordSet')`

**Note:** When a principal with conditional access to specific record sets uses [transactions](https://docs.cloud.google.com/dns/docs/records#add-transaction) to modify those records, they must use the `--skip-soa-update` flag. By default, transactions attempt to update the SOA record, which the principal might not be authorized to modify (depending on the condition). 

## Get IAM policy for a managed zone

To get the IAM policy for a specific managed zone, follow these steps.

###  gcloud 

Run the [`gcloud dns managed-zones get-iam-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/get-iam-policy):
    
    
    gcloud dns managed-zones get-iam-policy NAME
    

Replace `NAME` with the name of the managed zone for which you want to get the IAM policy.

If this command runs successfully, it returns the IAM policy. Otherwise it returns an error message specifying the error.

###  API 

Send a `POST` request by using the [`managedZone.getIamPolicy`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/getiampolicy) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/ManagedZone:getIamPolicy
    

Replace the following:

  * `PROJECT_ID`: the name or ID of the project
  * `MANAGED_ZONE`: the name of the managed zone for which you want to set the IAM permission



## Check IAM permissions for a managed zone

Send a `POST` request by using the [`managedZone.testIamPermissions`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/testiampermissions) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/ManagedZone:testIamPermissions
    

Replace the following:

  * `PROJECT_ID`: the name or ID of the project
  * `MANAGED_ZONE`: the name of the managed zone for which you want to check the IAM permission



## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
