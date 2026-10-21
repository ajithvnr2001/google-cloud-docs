---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/troubleshooting-dns/
title: Troubleshooting Cloud DNS \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:47.616114+00:00
---

# Troubleshooting Cloud DNS  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/troubleshooting-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Troubleshooting Cloud DNS Stay organized with collections  Save and categorize content based on your preferences. 

This document provides guidance on troubleshooting issues with Cloud DNS in Google Distributed Cloud (GDC) air-gapped. It covers potential errors and problems that you might encounter when performing management operations on DNS configurations, and provides tips and suggestions for debugging issues with DNS resolution. The intended audience for this document is platform administrators and application operators responsible for managing DNS records within a project.

## Troubleshoot Cloud DNS management operations

This section provides troubleshooting information for common issues encountered when performing Create, Read, Update, and Delete (CRUD) operations on Cloud DNS zones and record sets.

### Basic troubleshooting

  * Ensure that you have the correct IAM roles, as described in [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/dns-permissions).
  * If using `gdcloud`, you can refresh your authentication token by running `gdcloud auth login`.



### Resource naming and validation (RFC 1123)

**Issue:** Creation or update fails with invalid argument or validation errors.

**Details:**

  * **Resource Names:** Names for DNS zones and record sets must conform to RFC 
    1. They must contain only lowercase alphanumeric characters or `-`, and must start and end with an alphanumeric character.
  * **DNS Names:** Values for domain names and Fully Qualified Domain Names (FQDNs) must be valid domain names.
  * **Enum Values:** Values like visibility (`PUBLIC` or `PRIVATE`) and record types (e.g., `A`, `CNAME`) are case-sensitive and must match the exact expected string.



### Unable to delete non-empty zones

**Issue:** Cannot delete a managed zone; the operation is rejected.

**Details:** A Managed DNS Zone must be empty of resource record sets before it can be deleted. You must delete all records within the zone first.

### Naming and domain conflicts

**Issue:** Failing to create a resource with an error indicating the name or domain is already in use.

**Details:**

  * **Kubernetes Resource Name:** The name of the object (e.g., the name in `metadata.name`) must be unique within the specific project namespace.
  * **DNS Name (FQDN):** The actual domain name (e.g., `dnsName` for zones or records) must be unique within a given **visibility** (PUBLIC or PRIVATE). You cannot create two zones or two records with the identical domain name in the same visibility tier.



## Troubleshoot DNS resolution issues

This section helps platform administrators and application operators troubleshoot DNS resolution issues when accessing services hosted on Google Distributed Cloud.

### Wait for propagation and clear DNS cache

When DNS records are created or updated, the changes might not be visible instantly. This delay is usually caused by:

  1. **Reconciliation Time:** The system needs time to process the request and update the DNS server configuration. This usually takes a few minutes.
  2. **DNS Propagation Delay (Caching):** DNS resolvers and clients cache records to speed up lookups. Clients might continue to use the old record until the Time to live (TTL) period has passed.



**Recommendations:**

  * **Wait:** Allow sufficient time for reconciliation and cache expiration.
  * **Flush Cache:** Clear your local DNS cache to force a fresh lookup.



### Verify local resolver configuration

Ensure that your client is using the correct DNS servers. If you don't know the correct IP address, contact your Infrastructure Operations (IO) team to find the correct DNS server IP.

  * **Linux/macOS:** Check the contents of `/etc/resolv.conf`.
  * **Windows:** Run `ipconfig /all` and check the DNS Servers listed.



### Test resolution using standard tools

Use standard command-line tools to test resolution and identify where the failure occurs.

  * **Basic Lookup:**
        
        dig <domain_name>
        

or
        
        nslookup <domain_name>
        

  * **Query a Specific DNS Server:** If you know the IP of the public ManagedDNS server, query it directly to bypass local resolvers:
        
        dig @<public_dns_server_ip> <domain_name>
        

  * **Query a Public Nameserver:** To rule out local resolver issues, try querying a public resolver like Google DNS:
        
        dig @8.8.8.8 <domain_name>
        

**Note:** This step will only work if your system has internet connectivity. In air-gapped or restricted network environments typical of GDC air-gapped deployments, this command may time out.



### Analyze DNS response codes

When using `dig` or `nslookup`, check the status code in the response:

  * **NXDOMAIN** : The domain name was not found. Check for typos or verify if the record exists.
  * **SERVFAIL** : The server failed to process the query. This often indicates an issue on the server side or communication failure between DNS servers.
  * **NOERROR** : The query was successful, but there might be no answers. Verify if the requested record type (e.g., A, CNAME) exists.
  * **REFUSED** : The server refused to answer the query, likely due to policy or access control settings.



### Check network connectivity

Ensure that network traffic to the DNS server is not blocked.

  * DNS uses port 53 for both UDP and TCP.
  * Test connectivity using `nc` (netcat):
        
        nc -zv <dns_server_ip> 53
        

  * Verify that firewall rules allow traffic on port 53.




### Flush DNS cache

Flushing the DNS cache removes all entries from your local DNS cache. This forces your operating system to query the DNS servers again for the domain name, ensuring you get the most up-to-date record rather than a stale cached one.

  * **Windows:** `ipconfig /flushdns`
    * _What it does:_ Clears the DNS resolver cache maintained by the DNS Client service.
  * **macOS:** `sudo killall -HUP mDNSResponder`
    * _What it does:_ Sends a hangup signal (`HUP`) to the `mDNSResponder` process, forcing it to reload and clear its cache.
  * **Linux (systemd-resolved):** `sudo systemd-resolve --flush-caches` or `sudo resolvectl flush-caches`
    * _What it does:_ Tells the `systemd-resolved` service to discard its internal DNS cache.



### Check resource status with API or `gdcloud`

If you are a tenant or have access to the GDC API, you can check the status of the resources directly:

  * **Check a DNS zone:**
        
        kubectl describe manageddnszone <zone_name> -n <project_namespace>
        

  * **Check a Resource Record Set:**
        
        kubectl describe resourcerecordset <record_name> -n <project_namespace>
        

Look for conditions and events that might indicate failures in the reconciliation process.




If you have access to the `gdcloud` command line, you can use the `describe` sub-command as documented in [List DNS records](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-records#list-dns-records) or [List DNS zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/dns/list-dns-zones#list-dns-zones). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
