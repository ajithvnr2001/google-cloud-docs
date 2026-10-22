---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gti-ioc-changelog/
title: Change log for GTI_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:46.915034+00:00
---

# Change log for GTI_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gti-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GTI_IOC

Date | Changes  
---|---  
2026-07-10 |  \- `event.idm.entity.entity.type`: Corrected the mapping `eventvalue.attributes.type` raw log field to `event.idm.entity.entity.type` entity field for partial files.   
2026-04-22 |  \- `event.timestamp`: Newly mapped `eventvalue.attributes.last_modification_date` raw log field to `event.timestamp` entity field.   
2026-04-02 |  \- `event.idm.entity.metadata.ati_prioritization.active_ir`: Newly mapped `eventvalue.attributes.ati_metadata.is_pwn` to `event.idm.entity.metadata.ati_prioritization.active_ir` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.active_ir_first_tagged_time`: Newly mapped `eventvalue.attributes.ati_metadata.pwn_last_tagged_time` to `event.idm.entity.metadata.ati_prioritization.active_ir_first_tagged_time` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.global_customer_count`: Newly mapped `eventvalue.attributes.ati_metadata.global_customer_count` to `event.idm.entity.metadata.ati_prioritization.global_customer_count` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.global_hits_count`: Newly mapped `eventvalue.attributes.ati_metadata.global_hits_count` to `event.idm.entity.metadata.ati_prioritization.global_hits_count` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.exclusive`: Newly mapped `eventvalue.attributes.ati_metadata.is_exclusive` to `event.idm.entity.metadata.ati_prioritization.exclusive` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.osint`: Newly mapped `eventvalue.attributes.ati_metadata.is_osint` to `event.idm.entity.metadata.ati_prioritization.osint` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.reviewed`: Newly mapped `eventvalue.attributes.ati_metadata.is_reviewed` to `event.idm.entity.metadata.ati_prioritization.reviewed` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_threat_actors`: Newly mapped `eventvalue.attributes.ati_metadata.threat_actors` to `event.idm.entity.metadata.ati_prioritization.attributed_threat_actors` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_threat_actors.first_reference_time`: Newly mapped `eventvalue.attributes.ati_metadata.threatActors.firstReferenceTime` to `event.idm.entity.metadata.ati_prioritization.attributed_threat_actors.first_reference_time` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_threat_actors.last_reference_time`: Newly mapped `eventvalue.attributes.ati_metadata.threatActors.lastReferenceTime` to `event.idm.entity.metadata.ati_prioritization.attributed_threat_actors.last_reference_time` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_malware.first_reference_time`: Newly mapped `eventvalue.attributes.ati_metadata.malwareFamilies.firstReferenceTime` to `event.idm.entity.metadata.ati_prioritization.attributed_malware.first_reference_time` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_malware.last_reference_time`: Newly mapped `eventvalue.attributes.ati_metadata.malwareFamilies.lastReferenceTime` to `event.idm.entity.metadata.ati_prioritization.attributed_malware.last_reference_time` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_malware.associated_threat_actors.first_reference_time`: Newly mapped `eventvalue.attributes.ati_metadata.malwareFamilies.associatedActors.firstReferenceTime` to `event.idm.entity.metadata.ati_prioritization.attributed_malware.associated_threat_actors.first_reference_time` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.attributed_malware.associated_threat_actors.last_reference_time`: Newly mapped `eventvalue.attributes.ati_metadata.malwareFamilies.associatedActors.lastReferenceTime` to `event.idm.entity.metadata.ati_prioritization.attributed_malware.associated_threat_actors.last_reference_time` entity field.   
2026-04-01 |  \- `event.idm.entity.metadata.ati_prioritization.attributed_malware`: Newly mapped `eventvalue.attributes.ati_metadata.malware_families` to `event.idm.entity.metadata.ati_prioritization.attributed_malware`  
2026-03-31 |  \- `event.idm.entity.metadata.threat.verdict_info[`GTI Verdict`].verdict_time`: Newly mapped `eventvalue.attributes.ati_metadata.gti_verdict_time` to `event.idm.entity.metadata.threat.verdict_info.verdict_time`[`GTI Verdict`]  
\- `event.idm.entity.metadata.threat.verdict_info[`GTI Threat Score`].verdict_time`: Newly mapped `eventvalue.attributes.ati_metadata.gti_verdict_time` to `event.idm.entity.metadata.threat.verdict_info.verdict_time`[`GTI Threat Score`]  
\- `event.idm.entity.metadata.threat.verdict_info[`GTI Severity`].verdict_time`: Newly mapped `eventvalue.attributes.ati_metadata.gti_verdict_time` to `event.idm.entity.metadata.threat.verdict_info.verdict_time`[`GTI Severity`]  
\- `event.idm.entity.metadata.threat.verdict_info[`GTI Threat Score`].confidence_score`: Fixed incorrect mapping where `eventvalue.attributes.gti_assessment.threat_score.value` was not being mapped to `event.idm.entity.metadata.threat.verdict_info[`GTI Threat Score`].confidence_score`  
\- `event.idm.entity.metadata.ati_prioritization.gti_update_time`: Newly mapped `eventvalue.attributes.ati_metadata.gtiVerdictTime`(or `eventvalue.attributes.ati_metadata.gti_verdict_time`) to `event.idm.entity.metadata.ati_prioritization.gti_update_time`  
\- `event.idm.entity.metadata.ati_prioritization.gti_verdict`: Newly mapped `eventvalue.attributes.gti_assessment.verdict.value` and `eventvalue.attributes.gti_assessment.verdict.gti_verdict` raw log fields to `event.idm.entity.metadata.ati_prioritization.gti_verdict` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.gti_severity`: Newly mapped `eventvalue.attributes.gti_assessment.severity.gti_severity` raw log fields to `event.idm.entity.metadata.ati_prioritization.gti_severity` entity field.  
\- `event.idm.entity.metadata.ati_prioritization.gti_threat_score`: Newly mapped `eventvalue.attributes.gti_assessment.threat_score.gti_threat_score` raw log fields to `event.idm.entity.metadata.ati_prioritization.gti_threat_score` entity field.   
2026-03-24 |  \- `event.ioc.domain_and_ports.domain`: Newly mapped `id` raw log field to `event.ioc.domain_and_ports` entity field if the log is for a domain.  
\- `event.ioc.ip_and_ports.ip_address`: Newly mapped `id` raw log field to `event.ioc.ip_and_ports` entity field if the log is for an IP.  
\- `event.ioc.feed_name`: mapped to `GTI`.  
\- `event.ioc.confidence_score`: Mapped `eventvalue.attributes.gti_assessment.threat_score.value` raw log field to `event.ioc.confidence_score` entity field.  
\- `event.ioc.active_timerange.start`: mapped to 1 to indicate that this is a timeless IOC that is always valid. This parallels how `event.ioc.active_timerange.start` is set for other global IOC feeds (e.g. OPEN_SOURCE_INTEL_IOC, MANDIANT_ACTIVE_BREACH_IOC, etc).  
\- `event.ioc.active_timerange.end`: mapped to max int value to indicate that this is a timeless IOC that is always valid. This parallels how `event.ioc.active_timerange.end` is set for other global IOC feeds (e.g. OPEN_SOURCE_INTEL_IOC, MANDIANT_ACTIVE_BREACH_IOC, etc).  
\- `event.ioc.raw_severity`: Newly mapped `eventvalue.attributes.gti_assessment.severity.gti_severity` raw log field to `event.ioc.raw_severity` entity field.  
\- `event.ioc.description`: Newly mapped `eventvalue.attributes.gti_assessment.description` raw log field to `event.ioc.description` entity field.   
2026-03-19 |  Enhancement of GTI_IOC:  
\- `event.idm.entity.metadata.creation_timestamp`: Newly mapped `eventvalue.attributes.first_submission_date` or `eventvalue.attributes.first_seen_itw_date` raw log field to `event.idm.entity.metadata.creation_timestamp` entity field.  
\- `event.idm.entity.metadata.product_entity_id`: Newly mapped `eventvalue.id` raw log field to `event.idm.entity.metadata.product_entity_id` entity field.   
2026-03-18 |  \- `event.idm.entity.metadata.threat.severity_details`: remove `SEVERITY_` prefix to conform with existing formatting of IOC severity in IOC entities.  
\- `event.idm.entity.metadata.threat.last_updated_time`: Newly mapped `eventvalue.attributes.last_modification_date` raw log field to `event.idm.entity.metadata.threat.last_updated_time` entity field.  
\- `event.idm.entity.metadata.threat.first_discovered_time`: Newly mapped `eventvalue.attributes.first_seen_itw_date` and `eventvalue.attributes.first_submission_date` raw log fields to `event.idm.entity.metadata.threat.first_discovered_time` entity field.  
\- `event.idm.entity.metadata.threat.last_discovered_time`: Newly mapped `eventvalue.attributes.last_seen_itw_date` and `eventvalue.attributes.last_analysis_date` raw log fields to `event.idm.entity.metadata.threat.last_discovered_time` entity field.  
\- `event.idm.entity.metadata.threat.verdict_info`[`GTI Verdict`]: newly mapped `eventvalue.attributes.gti_assessment.verdict.value` and `eventvalue.attributes.gti_assessment.verdict.gti_verdict` raw log fields to `event.idm.entity.metadata.threat.verdict_info`[`GTI Verdict`] entity field.  
\- `event.idm.entity.metadata.threat.verdict_info`[`GTI Severity`]: newly mapped `eventvalue.attributes.gti_assessment.severity.gti_severity` raw log fields to `event.idm.entity.metadata.threat.verdict_info`[`GTI Severity`] entity field.  
\- `event.idm.entity.metadata.threat.verdict_info`[`GTI Threat Score`]: newly mapped `eventvalue.attributes.gti_assessment.threat_score.gti_threat_score` raw log fields to `event.idm.entity.metadata.threat.verdict_info`[`GTI Threat Score`] entity field.  
\- Ensure single `event.idm.entity.metadata.threat` field.   
2026-03-16 |  Enhancement of GTI_IOC:  
\- `event.idm.entity.metadata.interval.start_time`: mapped to 1 to indicate that this is a timeless IOC that is always valid. This parallels how `entity.metadata.interval.start_time` is set for other global IOC feeds (e.g. OPEN_SOURCE_INTEL_IOC, MANDIANT_ACTIVE_BREACH_IOC, etc).  
\- `event.idm.entity.metadata.interval.end_time`: removed mapping as this field is automatically set as part of the entity enrichment process   
2026-03-11 |  \- `event.idm.entity.additional.fields`: Removed mapping of `eventvalue.relationships.campaigns.data.id` from `event.idm.entity.additional.fields` entity field in order to introduce more accurate mapping to its entity field.  
\- `event.idm.entity.metadata.threat.threat_collections`: Mapped `eventvalue.relationships.campaigns.data.id`, `eventvalue.relationships.reports.data.id` raw log fields with `event.idm.entity.metadata.threat.threat_collections` entity field.  
\- `event.idm.entity.metadata.threat.threat_collections.type`:Mapped `CAMPAIGN` to `event.idm.entity.metadata.threat.threat_collections.type` when `eventvalue.relationships.campaigns.data.id` is present.  
\- `event.idm.entity.metadata.threat.threat_collections.type`: Mapped `REPORT` to `event.idm.entity.metadata.threat.threat_collections.type` when `eventvalue.relationships.reports.data.id` is present.  
\- `event.idm.entity.metadata.threat.associations`: Newly mapped `eventvalue.relationships.malware_families.data.id`, `eventvalue.relationships.threat_actors.data.id` raw log fields with `event.idm.entity.metadata.threat.associations` entity field.  
\- `event.idm.entity.metadata.threat.associations.type`: Mapped `MALWARE` to `event.idm.entity.metadata.threat.associations.type` when `eventvalue.relationships.malware_families.data.id` is present.  
\- `event.idm.entity.metadata.threat.associations.type`: Mapped `THREAT_ACTOR` to `event.idm.entity.metadata.threat.associations.type` when `eventvalue.relationships.threat_actors.data.id` is present.  
\- `event.idm.entity.security_result.detection_fields`: Newly mapped `eventvalue.relationships.reports.data.context_attributes.related_from.attributes.name`, `eventvalue.relationships.reports.data.context_attributes.related_from.attributes.origin`, `eventvalue.relationships.reports.data.context_attributes.related_from.id` raw log fields with `event.idm.entity.security_result.detection_fields` entity field.  
\- `event.idm.entity.additional.fields`: Newly mapped `eventvalue.relationships.threat_actors.links.self`, `eventvalue.relationships.threat_actors.links.related` raw log fields with `event.idm.entity.additional.fields` entity field.   
2026-02-12 |  \- `event.idm.entity.entity.security_result.detection_fields`: Newly mapped `eventvalue.attributes.gti_assessment.contributing_factors.google_malware_analysis`, `eventvalue.attributes.gti_assessment.contributing_factors.mandiant_association_report`, `eventvalue.attributes.gti_assessment.contributing_factors.mandiant_association_actor`, `eventvalue.attributes.gti_assessment.contributing_factors.mandiant_association_malware`, `eventvalue.attributes.mandiant_id`, `eventvalue.relationships.campaigns.links.related`, `eventvalue.relationships.campaigns.links.self`, `eventvalue.relationships.malware_families.links.related`, and `eventvalue.relationships.malware_families.links.self` raw log field to `event.idm.entity.entity.security_result.detection_fields` entity field.  
\- `event.idm.entity.additional.fields`: Newly mapped `eventvalue.attributes.continent`, `eventvalue.attributes.regional_internet_registry`, `eventvalue.attributes.asn`, `eventvalue.attributes.gti_assessment.contributing_factors.mandiant_confidence_score`, `eventvalue.attributes.as_owner`, `eventvalue.attributes.network`, `eventvalue.attributes.country`, `eventvalue.relationships.campaigns.data`, `relationshipvalues.id` raw log field to `event.idm.entity.additional.fields` entity field.  
\- `event.idm.entity.metadata.interval.start_time`: Newly mapped `eventvalue.attributes.first_seen_itw_date` raw log field to `event.idm.entity.metadata.interval.start_time` entity field.  
\- `event.idm.entity.metadata.interval.end_time`: Newly mapped `eventvalue.attributes.last_seen_itw_date` raw log field to `event.idm.entity.metadata.interval.end_time` entity field.   
2025-11-13 |  \- `event.idm.entity.entity.security_result.detection_fields`: Newly mapped `eventvalue.attributes.gti_assessment.verdict.value`, `eventvalue.attributes.threat_severity.threat_severity_level`, `eventvalue.attributes.threat_severity.level_description`, `eventvalue.attributes.threat_severity.version`, `eventvalue.attributes.last_https_certificate_raw.extensions.ca_information_access.CA_Issuers`, `eventvalue.attributes.last_https_certificate_raw.extensions.ca_information_access.OCSP`, `eventvalue.attributes.last_https_certificate_raw.extensions.authority_key_identifier.keyid`, `eventvalue.attributes.last_https_certificate_raw.issuer.C`, `eventvalue.attributes.last_https_certificate_raw.issuer.CN`, `eventvalue.attributes.last_https_certificate_raw.issuer.O` raw log field as a key-value pair to `event.idm.entity.entity.security_result.detection_fields` entity field.  
\- `event.idm.entity.additional.fields`: Newly mapped `eventvalue.attributes.gti_assessment.threat_score.value`, `eventvalue.attributes.last_https_certificate_raw.public_key.rsa.exponent`, `eventvalue.attributes.last_https_certificate_raw.public_key.rsa.key_size`, `eventvalue.attributes.last_https_certificate_raw.public_key.rsa.modulus`, `eventvalue.attributes.last_https_certificate_raw.serial_number`, `eventvalue.attributes.last_https_certificate_raw.size`, `eventvalue.attributes.last_https_certificate_raw.thumbprint`, `eventvalue.attributes.last_https_certificate_raw.thumbprint_sha256`, `eventvalue.attributes.last_https_certificate_raw.version`, `eventvalue.attributes.last_https_certificate_raw.extensions.CA`, `eventvalue.attributes.last_dns_records_date`, `eventvalue.attributes.last_analysis_stats_raw.timeout`, `eventvalue.attributes.threat_severity.last_analysis_date`, `eventvalue.attributes.last_https_certificate_raw.last_https_certificate_date`, `eventvalue.attributes.last_https_certificate_raw.validity.not_before`, `eventvalue.attributes.last_https_certificate_raw.validity.not_after` raw log field as a key-value pair to `event.idm.entity.additional.fields` entity field.  
\- `event.idm.entity.entity.labels`: Newly mapped `eventvalue.attributes.total_votes.harmless`, `eventvalue.attributes.total_votes.malicious`, `eventvalue.attributes.last_https_certificate_raw.signature_algorithm` raw log field as a key-value pair to `event.idm.entity.entity.labels` entity field.  
\- `event.idm.entity.entity.security_result.detection_fields`: Newly mapped values from the loop over `eventvalue.attributes.last_https_certificate_raw.extensions.extended_key_usage` raw log field as key-value pairs to `event.idm.entity.entity.security_result.detection_fields` entity field.  
\- Newly added gsub for the `message` and `last_analysis_stats`, `last_https_certificate`, `last_dns_records`, `CA Issuers` data field to parse the logs in correct manner.  
\- `event.idm.entity.metadata.interval.start_time`: Newly mapped `eventvalue.attributes.creation_date`, `eventvalue.attributes.last_analysis_date` raw log field with `event.idm.entity.metadata.interval.start_time` entity field.  
\- `event.idm.entity.metadata.interval.end_time`: Newly mapped `eventvalue.attributes.expiration_date`, `eventvalue.attributes.last_modification_date` raw log field with `event.idm.entity.metadata.interval.end_time` entity field.   
2025-10-15 |  \- `event.idm.entity.metadata.interval.start_time`: Newly mapped `eventvalue.attributes.creation_date.seconds` or `eventvalue.attributes.last_analysis_date.seconds` raw log field with `event.idm.entity.metadata.interval.start_time` entity field.  
\- `event.idm.entity.metadata.interval.end_time`: Newly mapped `eventvalue.attributes.expiration_date.seconds` or `eventvalue.attributes.last_modification_date.seconds` raw log field with `event.idm.entity.metadata.interval.end_time` entity field.  
\- `event.idm.entity.metadata.threat.confidence_details`: Newly mapped `eventvalue.attributes.gti_assessment.contributing_factors.gti_confidence_score` raw log field with `event.idm.entity.metadata.threat.confidence_details` entity field.  
\- `event.idm.entity.metadata.threat.description`: Newly mapped `eventvalue.attributes.gti_assessment.description` raw log field with `event.idm.entity.metadata.threat.description` entity field.  
\- `event.idm.entity.metadata.threat.severity_details`: Newly mapped `eventvalue.attributes.gti_assessment.severity.gti_severity` raw log field with `event.idm.entity.metadata.threat.severity_details` entity field.  
\- `event.idm.entity.metadata.threat.risk_score`: Newly mapped `eventvalue.attributes.gti_assessment.threat_score.gti_threat_score` raw log field with `event.idm.entity.metadata.threat.risk_score` entity field.  
\- `event.idm.entity.metadata.threat.url_back_to_product`: Newly mapped `eventvalue.links.self` raw log field with `event.idm.entity.metadata.threat.url_back_to_product` entity field.  
\- `event.idm.entity.entity.file.md5`: Newly mapped `eventvalue.attributes.md5` raw log field with `event.idm.entity.entity.file.md5` entity field.  
\- `event.idm.entity.entity.file.sha1`: Newly mapped `eventvalue.attributes.sha1` raw log field with `event.idm.entity.entity.file.sha1` entity field.  
\- `event.idm.entity.entity.file.sha256`: Newly mapped `eventvalue.id` raw log field with `event.idm.entity.entity.file.sha256` entity field.  
\- `event.idm.entity.entity.url`: Newly mapped `eventvalue.attributes.url` raw log field with `event.idm.entity.entity.url` entity field.  
\- `event.idm.entity.entity.ip`: Newly mapped `eventvalue.id` raw log field with `event.idm.entity.entity.ip` entity field.  
\- `event.idm.entity.entity.hostname`: Newly mapped `eventvalue.id` raw log field with `event.idm.entity.entity.hostname` entity field.  
\- `event.idm.entity.entity.domain.jarm`: Newly mapped `eventvalue.attributes.jarm` raw log field with `event.idm.entity.entity.domain.jarm` entity field.  
\- `event.idm.entity.entity.domain.registrar`: Newly mapped `eventvalue.attributes.registrar` raw log field with `event.idm.entity.entity.domain.registrar` entity field.  
\- `event.idm.entity.entity.labels`: Newly mapped various fields from `eventvalue.attributes.gti_assessment.contributing_factors.`, and `eventvalue.attributes.last_analysis_stats_raw.` raw log fields with `event.idm.entity.entity.labels` entity field.  
\- `event.idm.entity.entity.security_result.detection_fields`: Newly mapped `eventvalue.attributes.gti_assessment.verdict.gti_verdict`, `eventvalue.attributes.last_https_certificate_raw.cert_signature.signature`, and fields within `eventvalue.attributes.last_analysis_results_raw` raw log fields with `event.idm.entity.entity.security_result.detection_fields` entity field.  
\- `event.idm.entity.additional.fields`: Newly mapped a large number of fields from `eventvalue.attributes.last_analysis_results_raw.`, `eventvalue.attributes.last_dns_records_raw.`, `eventvalue.attributes.last_https_certificate_raw.`, `eventvalue.attributes.signature_info.`, `eventvalue.attributes.pe_info_raw.`, `eventvalue.attributes.trid.`, `eventvalue.attributes.magic`, `eventvalue.attributes.main_icon.`, `eventvalue.attributes.meaningful_name`, and `eventvalue.attributes.exiftool_raw.` raw log fields with `event.idm.entity.additional.fields` entity field.  
\- Added a Grok pattern on `id` to extract `IP:id`.  
\- The parser transforms the input message by replacing `}{` with `},{` and wrapping it to form a valid JSON array structure.  
\- Newly added gsub for the `message` and `event_data_string` data field to parse the logs in correct manner.  
\- Newly added JSON filter for `event_data_string` data field to parse the logs in correct manner.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
