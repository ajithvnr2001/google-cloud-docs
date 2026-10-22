---
url: https://docs.cloud.google.com/dns/docs/dnssec-migrate/
title: Migrate or transfer DNSSEC-enabled zones \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:40.865144+00:00
---

# Migrate or transfer DNSSEC-enabled zones  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/dnssec-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Migrate or transfer DNSSEC-enabled zones Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate a DNSSEC-enabled zone that is activated at the domain registrar between Cloud DNS and other DNS hosting providers while maintaining the DNSSEC chain of trust. This process helps to prevent common validation errors and helps safeguard your domain's security throughout the transfer.

For a conceptual overview of DNSSEC, see [DNSSEC overview](https://docs.cloud.google.com/dns/docs/dnssec).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.dnsKeys.create` to create DNSKEYS
  * `dns.dnsKeys.delete` to delete DNSKEYS
  * `dns.dnsKeys.list` to list DNSKEYS
  * `dns.dnsKeys.update` to update DNSKEYS



**Roles**

  * `roles/dns.admin`



## Before you begin

DNSSEC migration is complex and requires coordination to migrate a zone between operators without incurring outages. Read this guide in full before you transfer or migrate a zone. We recommend that you test the migration process on a less critical zone before attempting migration of critical production zones.

### Coordinate with DNS operators and domain registrar

To prevent validating resolvers from treating the domain as invalid, you must coordinate the migration with both the DNS operators and the domain registrar. This step ensures that you can establish and maintain a valid chain of trust from the parent zone to keys managed by both DNS operators during the transition.

If your domain registrar also provides DNS hosting, you must coordinate with your domain registrar to migrate the DNSSEC chain of trust. If the registrar does not support this operation, you cannot migrate the name servers while maintaining the DNSSEC chain of trust.

### Wait for resolver caches to expire

During migration, after you make critical record updates, wait for resolver caches to expire. This step prevents validation errors caused by old cached records inconsistent with the updated zone after migrating to the new name servers.

## Limitations

Migrating a DNSSEC zone has the following limitations:

  * You can only migrate a zone while maintaining the DNSSEC chain of trust if the new operator and registrar support DNSSEC migration, including importing DNSKEY records, setting multiple DS records, and preventing automatic key rotation during migration.

  * You must use the same [algorithm](https://docs.cloud.google.com/dns/docs/dnssec-advanced#advanced-signing-options) at both operators since zones must be signed with all algorithms in use. For details, see [RFC 4035 section 2.2](https://datatracker.ietf.org/doc/html/rfc4035#section-2.2). Cloud DNS can only sign with one algorithm at a time. You cannot change algorithms during migration between providers.

  * You must be able to import DNSKEY records from Cloud DNS into the other operator's zone and have those records signed with the operator's keys. Cloud DNS allows adding DNSKEY records for zones in `Transfer` mode.

  * You must be able to add a second DS record from Cloud DNS to the parent zone. The registrar or parent zone must allow DS records that correspond to public keys that do not sign any records in the child zone.

  * You must be able to stop automated key rotation by the old or new operator for the zone until migration is complete. Cloud DNS automatically stops key rotation for zones in `Transfer` mode.




If the new operator does not support migration, do the following:

  1. [Deactivate DNSSEC at your registrar](https://docs.cloud.google.com/dns/docs/registrars#del-ds).
  2. Perform the transfer or migration.
  3. [Enable DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec-config#enabling).
  4. [Activate DNSSEC at your registrar](https://docs.cloud.google.com/dns/docs/registrars#add-ds).

**Note:** Because DNSSEC is deactivated during the transition, your zone is not secure. Do not attempt zone migration if the zone contains any [record types that rely on DNSSEC authenticity and integrity guarantees](https://docs.cloud.google.com/dns/docs/dnssec-advanced#using-new-dns-record-types) because migrating a zone in these conditions might cause loss of functionality or security.

For an informative presentation about DNSSEC and domain transfers and potential pitfalls, see [DNS/DNSSEC and Domain Transfers: Are they compatible?](https://atlarge.icann.org/files/9280/presentation-dnssec-transfers-gudmundsson-10mar10-en.pdf).

## Migration between operators

The technical approach that Cloud DNS uses for DNSSEC migrations is the Double-DS KSK rollover variant described in [RFC 6781 Appendix D Alternative Rollover Approach for Cooperating Operators](https://datatracker.ietf.org/doc/html/rfc6781#appendix-D).

DNSSEC migration works without exchanging private keys or signatures between DNS operators. Instead, the existing name servers and parent zone pre-publish signed records for the new operator's public keys in addition to the old operator's public keys. Likewise, the new name servers publish signed records for the old operator's keys in addition to the new operator's keys.

These keys from the other operator are signed, creating cross-trust between the two operators and the parent zone such that validating resolvers can use records from one operator to validate responses from the other operator. This process enables the transition to the new operator name servers without interruption.

After these records propagate, resolvers can validate responses from both operators during the subsequent transition period while the new name server delegation records propagate to all resolver caches.

After the updated name server records propagate, you can finalize the migration. You can remove the child zone from the old name servers and remove the old operator's trust anchor from the parent zone.

## Migrate DNSSEC-signed zones to Cloud DNS

Before you begin, review all instructions. You must also verify that your provider supports migration. Otherwise you cannot migrate the zone using this process.

To perform the migration, follow these steps:

  1. Stop all key rotation for the zone at the old name server.

  2. [Create a new DNSSEC-signed zone](https://docs.cloud.google.com/dns/docs/dnssec-advanced#advanced-signing-options) in DNSSEC `Transfer` state. `Transfer` state stops key rotation and allows DNSKEY import.

You must use the same [algorithms](https://docs.cloud.google.com/dns/docs/dnssec-advanced#advanced-signing-options) in use at the existing provider.

  3. Export your unsigned zone files, and then import them into the new zone.

Follow your provider's instructions for exporting zone data.

You may include DNSKEYs at this step, but do not include any other DNSSEC record types from the existing zone (CDS, CDNSKEY, NSEC, NSEC3, NSEC3PARAM, or RRSIG types).

You can import zones by using the [`gcloud dns record-sets import` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/import).

  4. Retrieve the previous DNSKEY records from the old name server.

You can also use `dig` or `delv` to query for DNSKEY records, but you must verify that the returned public keys are correct and valid for your zone.

  5. Retrieve the new DNSKEY records from Cloud DNS. In `Transfer` mode, DNSKEY records appear like normal records in the zone.

  6. Add the existing DNSKEY records to the Cloud DNS zone in addition to the automatically generated DNSKEY records.

You can also import DNSKEYs during step 3 and skip this step if your provider exports DNSKEYs along with the rest of the zone data.

  7. Add the new DNSKEY records from Cloud DNS to the zone in the existing operator. Be sure to re-sign the zone if necessary.

  8. [Add the DS record](https://docs.cloud.google.com/dns/docs/registrars#add-ds) for the Cloud DNS zone to your registrar in addition to the existing DS record.

  9. Wait until the new records propagate and old records expire from all resolver caches. Otherwise stale data might cause validation failures.

Wait until all of the following happen:

     * Records propagate to all name servers used by the old operator.

     * The parent zone NS record set TTL expires.

     * The parent zone DS record set TTL expires.

     * The child zone NS record set TTL at the old operator expires.

     * The child zone DNSKEY record set TTL at the old operator expires.

  10. Verify that the zone is ready by checking that the old operator is serving all the DNSKEY records and the parent zone is serving both DS records.

  11. Change the name server delegations to point to Cloud DNS.

[Update the name server records](https://docs.cloud.google.com/dns/docs/update-name-servers) at the registrar to the Cloud DNS name servers for the new zone.

  12. Wait until the new name server records propagate and old delegation records expire from all resolver caches. Otherwise stale data might cause validation failures.

Wait until all of the following happen:

     * The parent zone NS record set TTL expires.

     * The child zone NS record set TTL at the old operator expires.

After this step, you can safely stop serving the zone at the old operator.

  13. Remove the old zone's DNSKEY records added to the Cloud DNS zone.

  14. Change the DNSSEC state of the zone from `Transfer` to `On`.

Leaving transfer state enables automatic key rotation for the zone. Your zones can safely leave DNSSEC transfer state after a week, and must not remain in DNSSEC transfer state for more than a month or two.

  15. [Remove the DS record](https://docs.cloud.google.com/dns/docs/registrars#del-ds) for the old operator's zone from your registrar.




## Migrate DNSSEC-signed zones from Cloud DNS

Before you begin migration, review all instructions. You must also verify that your provider supports migration. Otherwise you cannot migrate the zone using this process.

To perform the migration, follow these steps:

  1. Change the DNSSEC state from `On` to `Transfer`. This step stops key rotation.

  2. Export your zone file and import it into the new operator.

You can use `gcloud dns record-sets export` to export a zone.

Exporting a zone in `Transfer` mode also exports DNSKEY records from Cloud DNS. If your provider accepts DNSKEY at this step, you can include them now and skip the steps below that transfer public keys from Cloud DNS to the new provider.

  3. Sign the zone at the new provider.

You must use the same [algorithms](https://docs.cloud.google.com/dns/docs/dnssec-advanced#advanced-signing-options) in use by Cloud DNS at the new provider.

You must stop key rotation for the zone at the new name server until migration completes.

  4. Retrieve the DNSKEY records from Cloud DNS. In `Transfer` mode DNSKEY records appear like normal records in the zone.

You can also use `dig` or `delv` to query the Cloud DNS name servers for DNSKEY records, but you must verify that the returned public keys are correct and valid for your zone.

  5. Retrieve the new DNSKEY records from the new operator.

You might have to first sign the zone or configure DNSSEC to obtain keys.

  6. Add the Cloud DNS DNSKEY records to the new operator's zone in addition to the DNSKEY records for the new zone.

  7. Add the DNSKEY records from the new operator to Cloud DNS.

  8. [Add the DS record](https://docs.cloud.google.com/dns/docs/registrars#add-ds) for the new operator's zone to your registrar in addition to the existing DS record from Cloud DNS.

  9. Wait until the new records propagate and old records expire from all resolver caches. Otherwise stale data might cause validation failures.

Wait until all of the following happen:

     * The parent zone NS record set TTL expires.

     * The parent zone DS record set TTL expires.

     * The Cloud DNS zone NS record set TTL expires.

     * The Cloud DNS zone DNSKEY record set TTL expires.

You can verify that the zone is ready by checking that Cloud DNS is serving all the DNSKEY records and the parent zone is serving both DS records.

  10. Migrate the name server delegations to point to the new operator.

[Update the name server records](https://docs.cloud.google.com/dns/docs/update-name-servers) at the registrar to the new operator's name servers for the zone.

  11. Wait until the new name server records propagate and old delegation records expire from all resolver caches. Otherwise stale data might cause validation failures.

Wait until all of the following expire:

     * The parent zone NS record set TTL.

     * The Cloud DNS zone NS record set TTL.

After this step, you can safely delete the zone from Cloud DNS.

  12. Remove the Cloud DNS DNSKEY records added to the new zone.

  13. [Remove the DS record](https://docs.cloud.google.com/dns/docs/registrars#del-ds) for Cloud DNS from your registrar.

  14. Finish the migration at the new operator as needed.




If the other DNS operator has a process for migrating a DNSSEC-signed zone, you must perform their steps in parallel with this procedure, after step 1.

## What's next

  * To get information about specific DNSSEC configurations, see [Use advanced DNSSEC](https://docs.cloud.google.com/dns/docs/dnssec-advanced).
  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
