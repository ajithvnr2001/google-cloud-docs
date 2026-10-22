---
url: https://docs.cloud.google.com/dns/docs/error-messages/
title: Error messages \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:40.797338+00:00
---

# Error messages  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

This page describes common error messages that you might receive when using Cloud DNS, what the messages mean, and recommended actions for resolving the errors.

## General errors

This section describes general errors.

### `alreadyExists`

> The specified resource already exists; you cannot create a duplicate.

**Recommended action:** When creating a resource, use the appropriate `get/list` API to discover what resources already exist.

If you get this error when adding records, it is because an individual record is treated as a record set, which means each entry (if you have multiple entries) acts as a different record. You can add two values or strings to the record set for the same Domain Name System (DNS) name by adding a space between the first value and the second value.

### `accessNotConfigured`

> Access not configured

To resolve this error, you must [enable the Cloud DNS API](https://console.cloud.google.com/start/api?id=dns) for your project.

### `inactiveBillingState`

> Project `example_project` cannot accept requests while in an inactive billing state. Billing state might take several minutes to update.

**Recommended action:** Enable billing for your project. To enable billing for a new project, or to re-enable billing for an existing project, follow the appropriate steps in [Enable billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).

### `preconditionFailed`

This is a generic error that means that something about the request is not compatible with the current state of the server resource. The client must do something to fix it and then try again. This can happen if you send a `create` change request that tries to delete a resource record set that doesn't match the one that already exists (same name and type).

Read the current state of the zone and decide what you want to delete. It might have changed since you last looked at it.

The error message includes the path to the problematic part of your request. For example, `entity.change.deletions[6]` refers to the seventh element in the `deletions` array of the change object in the POST body of your request.

**Recommended action:** Fix the part of the request that is flagged as problematic.

### `required`

This is a generic error that means that some required part of the request is missing. For example, the request to create a managed zone requires a name, a DNS name, and a description. If any of these fields is missing, the request fails with this error.

**Recommended action:** Fill in the required parameter and try again.

### `notFound`

The specified resource does not exist.

**Recommended action:** Make sure that you are using the name of an existing resource.

### `quotaExceeded`

You get this error when an impending change would exceed your current quota. The quota is associated with the project. For example, you are only allowed a certain number of resource record sets in each zone. If you need a quota increase, contact your Google Cloud sales team. New projects have a default quota as specified in [Cloud DNS resource quotas and limits](https://docs.cloud.google.com/dns/quotas#resource_limits). For all the different dimensions that DNS limits, see the [`Projects.get`](https://docs.cloud.google.com/dns/docs/reference/v1/projects/get) operation.

**Recommended action:** Check your project to understand why you are already using so much of that resource. You can request increased quota for a project on the [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas) of the Google Cloud console for the project. You can also refer to [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## Errors relating to managed zones

This section lists errors relating to managed zones.

### `invalidFieldValue`

> Invalid value for `entity.managedZone.name`.

The operation to create a managed zone can fail with this error if the managed zone name does not begin with a letter, end with a letter or digit, and contain only lowercase letters, digits, or dashes.

### `managedZoneDnsNameNotAvailable`

> The specified managed zone is not available and thus, cannot be created.

The operation to create a managed zone can fail with this error for the following reasons:

  * The DNS name of the proposed zone is reserved, for example, dot (`.`), `.com`, or `.co.uk`.
  * There are no more name servers available to host the DNS name of the zone. Cloud DNS uses a pool of name servers, and that pool is finite. A DNS query to any name server must map unambiguously to one managed zone. For more details, see [nameserver limits](https://docs.cloud.google.com/dns/quotas#name-server-limits).



**Recommended action:** If you are the registered owner of the DNS name in question, check for overlapping zones. To set up DNS for a domain and its subdomains, we recommend creating a single parent zone first and adding records for each subdomain in that zone.

### `verifyManagedZoneDnsNameOwnership`

> Verify ownership of the `example.com` domain (or a parent), and then try again.

**Recommended action:** When you receive this error, you must [verify domain ownership](http://www.google.com/webmasters/verification/), and then try again.

## Errors relating to managed records

The errors in this section relate to records.

### `containerNotEmpty`

> The specified resource cannot be deleted because it is not empty.

**Recommended action:** If you want to delete the resource, you must empty it first.

### `invalidZoneApex`

> The specified resource record set is invalid because a zone must contain exactly one resource record set of a certain type at the apex.

`Apex` in the DNS context means the DNS name with the fewest number of labels that are allowed in the zone. It is also the top of the zone hierarchy. The apex of a zone is the DNS name equal to [`ManagedZone.dnsName`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones).

This error means that you tried to make a change that would violate the DNS rule that a zone must contain exactly one resource record set of a certain type at the apex. The following actions can cause this error:

  * You tried to delete the required `NS` resource record set at the apex.
  * You tried to delete the required `SOA` resource record set at the apex.
  * You tried to create a resource record set of type `SOA` _not_ at the apex.



**Recommended action:** If you get this error, you are trying to do something that isn't allowed under the rules of DNS. Check your request for mistakes. There is no need to delete the required resource record sets.

### `invalidRecordCount`

> The resource record set `entity.change.additions[XX]` is only permitted to have one record because it is of type `<SOA_OR_CNAME>`.

The rules of DNS say that `SOA` and `CNAME` resource record sets can only have one resource record. You get this error if you try to create a change that would break those rules. For example:
    
    
      {
        kind: "dns#rrset"
        name: "blog.example.com.",
        type: "CNAME",
        rrdata: [ "www.example.com.", "www2.example.com." ],
        ...
      }
    

**Recommended action:** If you get this error, check your request. You are trying to do something that isn't allowed.

### `cnameResourceRecordSetConflict`

> The resource record set `entity.change.additions[XX]` is invalid because the DNS name `example.com` might have either one CNAME resource record set or resource record sets of other types, but not both.

This error occurs when you create two types of resource record sets, such as both an A record and a CNAME record for the same DNS name. A common cause of this error is trying to create a CNAME record at the zone apex. This is not possible because it would conflict with the required `SOA` and `NS` records of the same name.

**Recommended action:** Pick one or the other.

### `wildcardNotAllowed`

> The specified resource record set has the wrong type to be a wildcard.

In DNS, a [wildcard](https://wikipedia.org/wiki/Wildcard_DNS_record) is a special type of resource record set that matches requests for non-existent domain names. One limitation of Cloud DNS is that you cannot create a wildcard resource record set of type `NS`.

**Recommended action:** Wildcard `NS` resource record sets are not supported at this time. Contact [Cloud DNS Support](https://docs.cloud.google.com/dns/docs/getting-support) or join [cloud-dns-discuss](https://groups.google.com/forum/#!forum/cloud-dns-discuss) and share what you are trying to accomplish.

### `recordTypeDisallowedAtZoneApex`

> The specified resource record cannot exist alongside any other record type, including the `SOA` record that is required at the zone apex.

You cannot place a `CNAME` resource record at the apex because it cannot exist alongside any other resource record type, including the `SOA` resource record that is required at the zone apex.

**Recommended action:** Use an `ALIAS` resource record. An `ALIAS` resource record is a Cloud DNS custom record type that behaves like a `CNAME` resource record but can only be used at the zone apex and only responds to address record (A or AAAA) queries. For more information, see [Alias records](https://docs.cloud.google.com/dns/docs/records-overview#alias-records).

### `invalidValue`

This is a generic error that means something about your request was invalid, independent of the server's state. The error message includes the path to the problematic part of the request, as well as the invalid value. This error could be triggered by many different things, such as:

  * You specified a resource record set with an invalid name. For example, `cymbal...group` is not a valid DNS name (empty middle label).
  * You specified a resource record set with an invalid type. For example A and CNAME are valid types, but _group_ is not a valid type.
  * You specified a resource record set with no records in it.
  * You specified resource record data that is invalid. For example `1.1.1.1` is valid resource record data for type A. _X.X.X.X_ is invalid resource record data for type A.
  * You specified a resource record set with an invalid TTL. The TTL must be a non-negative integer.
  * You specified a resource name that is too long.



**Recommended action:** Fix your request.

## Errors related to threat detection

This section describes common errors when enabling threat detection.

### Privileged access only allowed from ThreatDetectorAdmin

You must have the `Threat Detector Admin` role to enable DNS threat detection.

**Recommended action:** You must be granted the `roles/networksecurity.dnsThreatDetectorAdmin` role.

### `FAILED_PRECONDITION`

> Another DNS threat detector already exists under the supplied parent.

**Recommended action** Inspect your current configuration state, and either use the existing DNS threat detector or remove it and create a new one.

### gcloud
    
    
    gcloud network-security dns-threat-detectors describe --location=global  RESOURCE_REPORTED_IN_ERROR_MESSAGE
    

Replace `RESOURCE_REPORTED_IN_ERROR_MESSAGE` with the other DNS threat detector that already exists under the supplied parent in the error message. 

## What's next

  * To learn more about features, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get additional help, see [Support](https://docs.cloud.google.com/dns/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
