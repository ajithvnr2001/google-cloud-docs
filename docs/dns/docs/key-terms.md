---
url: https://docs.cloud.google.com/dns/docs/key-terms/
title: Key terms \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:56.787610+00:00
---

# Key terms  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Key terms Stay organized with collections  Save and categorize content based on your preferences. 

This document provides key terminology that applies to Cloud DNS. Review these terms to better understand how Cloud DNS works and the concepts on which it is built.

The Cloud DNS API is built around projects, managed zones, record sets, and changes to record sets.

delegated subzone
    

DNS lets the owner of a zone delegate a subdomain to a different name server by using NS (name server) records. Resolvers follow these records and send queries for the subdomain to the target name server specified in the delegation.

    **Note:** Private zones don't support delegation of subdomains to different name servers by using NS records.
DNS server policy
    

A DNS server policy lets you access name resolution services provided by Google Cloud in a VPC network with inbound forwarding, or supersede the VPC [name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order) with an outbound server policy. For more information, see [DNS server policies](https://docs.cloud.google.com/dns/docs/server-policies-overview).

DNSKEYs collection
    

The DNSKEYs collection holds the current state of the DNSKEY records used to sign a DNSSEC-enabled managed zone. You can only read this collection; all changes to the DNSKEYs are made by Cloud DNS. The DNSKEYs collection has all the information that domain registrars require to [activate DNSSEC](https://docs.cloud.google.com/dns/docs/registrars#add-ds).

DNSSEC
    

The [Domain Name System Security Extensions (DNSSEC)](https://docs.cloud.google.com/dns/docs/dnssec) is a suite of Internet Engineering Task Force (IETF) extensions to DNS which authenticate responses to domain name lookups. DNSSEC does not provide privacy protections for those lookups, but prevents attackers from manipulating or poisoning the responses to DNS requests.

domain, subdomain, and delegation
    

Most subdomains are only records in the managed zone for the parent domain. Subdomains that are _delegated_ by creating NS (name server) records in their parent domain's zone need to have their own zones as well. 

    

Create managed public zones for parent domains in Cloud DNS _before_ creating any public zones for their delegated subdomains. Do this even if you are hosting the parent domain on another DNS service. If you have several subdomain zones but don't create the parent zone, it can be complicated to create the parent zone later if you decide to move it to Cloud DNS. For more information, see [Name server limits](https://docs.cloud.google.com/dns/quotas#name-server-limits). 

forwarding zone
    

A forwarding zone is a type of Cloud DNS managed private zone that forwards requests for that zone to the IP addresses of its forwarding targets. For more information, see [DNS forwarding methods](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods).

    

When you [create a forwarding zone](https://docs.cloud.google.com/dns/docs/zones#creating-forwarding-zones), you cannot add records to the forwarding zone directly; the data comes from one or more configured target name servers or resolvers.

internal DNS
    

Google Cloud creates internal DNS names for VMs automatically, even if you do not use Cloud DNS. For more information about internal DNS, see the [internal DNS documentation](https://docs.cloud.google.com/compute/docs/internal-dns).

Internationalized Domain Name (IDN)
    

An [Internationalized Domain Name (IDN)](https://www.icann.org/resources/pages/idn-2012-02-25-en) is an internet domain name that allows people all over the world to use a language-specific script or alphabet, such as Arabic, Chinese, Cyrillic, Devanagari, Hebrew, or the Latin alphabet-based special characters in domain names. This conversion is implemented by using [Punycode](https://wikipedia.org/wiki/Punycode), which is a representation of Unicode characters that use ASCII. For example, an IDN representation of `.ελ` is `.xn--qxam`. Some browsers, email clients, and applications might recognize it and render it as `.ελ` on your behalf. The [Internationalizing Domain Names in Applications (IDNA)](https://tools.ietf.org/html/rfc3490) standard only allows for Unicode strings that are short enough to be represented as a valid DNS label. For information about how you can use IDN with Cloud DNS, see [Creating zones with Internationalized Domain Names](https://docs.cloud.google.com/dns/docs/zones/international-domains).

managed zone
    

The managed zone holds Domain Name System (DNS) records for the same DNS name suffix (such as `example.com`). A project can have multiple managed zones, but they must each have a unique name. In Cloud DNS, the managed zone is the resource that models a [DNS zone](http://wikipedia.org/wiki/DNS_zone).

    

All records in a managed zone are hosted on the same Google-operated name servers. These name servers respond to DNS queries against your managed zone according to how you configure the zone. A project can contain multiple managed zones. [Charges accrue](https://cloud.google.com/dns/pricing) for each zone for each day that the managed zone exists. Managed zones support [labels](https://cloudplatform.googleblog.com/2015/10/using-labels-to-organize-Google-Cloud-Platform-resources.html) that you can use to help organize your billing.

peering zone
    

A peering zone is a type of Cloud DNS managed private zone that follows the name resolution order of another VPC network. You can use it to resolve the names that are defined in the other VPC network.

    

When you [create a DNS peering zone](https://docs.cloud.google.com/dns/docs/zones/peering-zones), you cannot add records to the zone directly; the data comes from the producer VPC network according to its [Name resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order).

private zone
    

Private zones enable you to manage custom domain names for your virtual machine (VM) instances, load balancers, and other Google Cloud resources without exposing the underlying DNS data to the public internet. A private zone is a container of DNS records that can only be queried by one or more Virtual Private Cloud (VPC) networks that you authorize.

    

You must specify the list of authorized VPC networks that can query your private zone when you create or update it. Only authorized networks are allowed to query your private zone; if you do not specify any authorized networks, you cannot query the private zone at all.

    

You can use private zones with [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). For important information about using private zones with Shared VPC, see [Shared VPC considerations](https://docs.cloud.google.com/dns/docs/overview#shared-vpc).

    

Private zones do not support DNS security extensions (DNSSEC) or custom resource record sets of type NS. Requests for DNS records in private zones must be submitted through the metadata server `169.254.169.254`, which is the default internal name server for VMs created from [Google-supplied images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

    

You can submit queries to this name server from any VM that uses an authorized VPC network. For example, you can create a private zone for `dev.gcp.example.com` to host internal DNS records for experimental applications. The following table shows example records in that zone. Database clients can connect to the database server `db-01.dev.gcp.example.com` by using its internal DNS name instead of its IP address. Database clients resolve this internal DNS name by using the host resolver on the VM, which submits the DNS query to the metadata server `169.254.169.254`. The metadata server acts as a recursive resolver to query your private zone.

DNS name | Type | TTL (seconds) | Data  
---|---|---|---  
`db-01.dev.gcp.example.com` | A | 5 | 10.128.1.35  
`instance-01.dev.gcp.example.com` | A | 50 | 10.128.1.10  
    

Private zones enable you to create [split horizon](https://docs.cloud.google.com/dns/docs/zones/zones-overview#split-horizon) DNS configurations. This is because you can create a private zone with a different set of records, which overrides the entire set of records in a public zone. You can then control which VPC networks query the records in the private zone. For example, see [overlapping zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#overlapping-zones).

project
    

A Google Cloud console project is a container for resources, a domain for access control, and the place where [billing](https://cloud.google.com/dns/pricing) is configured and aggregated. For more details, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

public zone
    

A public zone is visible to the internet. Cloud DNS has public authoritative name servers that respond to queries about public zones regardless of where the queries originate. You can create DNS records in a public zone to publish your service on the internet. For example, you might create the following record in a public zone `example.com` for your public website `www.example.com`.

DNS name | Type | TTL (seconds) | Data  
---|---|---|---  
www.example.com | A | 300 | 198.51.100.0  
    

Cloud DNS assigns a set of name servers when a public zone is created. For the DNS records in a public zone to be resolvable over the internet, you must [update the name server setting](https://docs.cloud.google.com/dns/docs/update-name-servers) of your domain registration at your registrar.

    **Note:** Cloud DNS public zones are authoritative, and NS (name server) and SOA resource records are at the zone apex. You cannot delete these types of records. For details, see [RFC 1034](https://tools.ietf.org/html/rfc1034).
    

For more information about how to register and set up your domain, see [Setting up a domain using Cloud DNS](https://docs.cloud.google.com/dns/docs/tutorials/create-domain-tutorial).

registrar
    A [domain name registrar](https://wikipedia.org/wiki/Domain_name_registrar) is an organization that manages the reservation of internet domain names. A registrar must be accredited by a generic top-level domain (gTLD) registry or a country code top-level domain (ccTLD) registry.
resource record set change
    

To make a change to a resource record set, submit a `Change` or a `ResourceRecordSets` request containing additions or deletions. Additions and deletions can be done in bulk or in a single atomic transaction, and take effect at the same time in each authoritative DNS server.

    

For example, if you have an A record that looks like this:

    
    
    
    www  A  203.0.113.1 203.0.113.2
    

    

And you run a command that looks like this:

    
    
    
    DEL  www  A  203.0.113.2
    ADD  www  A  203.0.113.3
    

    

Your record looks like this after the bulk change:

    
    
    
    www  A  203.0.113.1 203.0.113.3
    

    

The ADD and DEL happen simultaneously.

resource record sets
    

A resource record set is a collection of DNS records with the same label, class, and type, but with different data. Resource record sets hold the current state of the DNS records that make up a managed zone. You can read a resource record set, but you do not modify it directly. Rather, you edit the resource record set in a managed zone by creating a `Change` request in the [changes collection](https://docs.cloud.google.com/dns/docs/reference/v1/changes). You can also edit the resource record sets by using the [`ResourceRecordSets` API](https://docs.cloud.google.com/dns/docs/reference/v1/resourceRecordSets). The resource record set reflects all your changes immediately. However, there is a delay between when changes are made in the API and the time that they take effect at your authoritative DNS servers. For information about how to manage records, see [Add, update, and delete records](https://docs.cloud.google.com/dns/docs/records).

    **Note:** Consistent with DNS industry practices, Cloud DNS name servers now randomize the order of the resource record sets when multiple records exist in a set. This is normal DNS behavior and applies to both public _and_ private Cloud DNS zones. Caching resolvers in the path might still return record sets as originally cached, and not re-randomize the order on subsequent responses.
response policy
    

A response policy is a Cloud DNS private zone concept that contains rules instead of records. These rules can be used to achieve effects similar to the DNS [response policy zone](https://wikipedia.org/wiki/Response_policy_zone) (RPZ) draft concept ([IETF](https://datatracker.ietf.org/doc/draft-ietf-dnsop-dns-rpz/)). The response policy feature lets you introduce customized rules in DNS servers within your network that the DNS resolver consults during lookups. If a rule in the response policy affects the incoming query, it is processed. Otherwise, the lookup proceeds normally. For more information, see [Managing response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).

    

A response policy is different from an RPZ, which is an otherwise normal DNS zone with specially formatted data that causes compatible resolvers to do special things. Response policies are not DNS zones and are managed separately in the API.

Service Directory
    

Service Directory is a managed service registry for Google Cloud that lets you register and discover services by using HTTP or gRPC (using its Lookup API) in addition to using conventional DNS. You can use Service Directory to register both Google Cloud and non-Google Cloud services.

    

Cloud DNS lets you create Service Directory-backed zones, which are a type of private zone containing information about your services and endpoints. You don't add record sets to the zone; rather, they're inferred automatically based on the configuration of the Service Directory namespace associated with the zone. For more information about Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).

    

When you [create a Service Directory-backed zone](https://docs.cloud.google.com/dns/docs/zones#create-service-directory-zone), you cannot add records to the zone directly; the data comes from the Service Directory service registry.

SOA serial number format
    

The serial numbers of SOA records created in Cloud DNS managed zones monotonically increase with each transactional change to a zone's record sets made by using the `gcloud dns record-sets transaction` command. However, you are free to manually change the serial number of an SOA record to an arbitrary number, including an ISO 8601-formatted date as recommended in [RFC 1912](https://datatracker.ietf.org/doc/html/rfc1912).

    

For example, in the following SOA record, you can change the serial number directly from the Google Cloud console by entering the selected value into the third space-delimited field of the record:

    
    
    
    ns-gcp-private.googledomains.com. cloud-dns-hostmaster.google.com.
    [serial number] 21600 3600 259200 300`
    

zone operations
    

Any changes that you make to managed zones in Cloud DNS are recorded in the [operations collection](https://docs.cloud.google.com/dns/docs/zones/operations), which lists managed zone updates (modifying descriptions or DNSSEC state or configuration). Changes to record sets inside a zone are stored separately in resource record sets, described later in this document.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
