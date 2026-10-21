---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/windows-dns-field-map/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:19:23.189475+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/windows-dns-field-map/




Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists the log fields of the `WINDOWS_DNS` log type and their corresponding UDM fields.

### Common fields

**NXLog field** | **UDM field** | **Comment**  
---|---|---  
`SourceName` | `metadata.vendor_name = "Microsoft"`  
  
`metadata.product_name = "Windows DNS Server"` |   
`EventID` | `security_result.rule_name` | Stored as "`EventID: %{EventID}`". In events with `Error` and `Warning` level.  
`Severity` | `security_result.severity` | The values are mapped to the UDM field enum as follows:  
0 (None) - `UNKNOWN_SEVERITY`  
1 (Critical) - `INFORMATIONAL`  
2 (Error) - `ERROR`  
3 (Warning) - `ERROR`  
4 (Informational) - `INFORMATIONAL`  
5 (Verbose) - `INFORMATIONAL`  
`EventTime` | `metadata.event_timestamp` |   
`ExecutionProcessID` | `principal.process.pid / target.process.pid` | Value stored in `target.process.pid` for the following Event IDs 256, 259, 261, 263, 266, 268, 270, 272, 273, 275, 278, 279, 280.  
Value stored in `principal.process.pid` for all other Event IDs.  
`Channel` | `metadata.product_event_type` |   
`Hostname` | `principal.hostname / target.hostname` | Value stored in `target.hostname` for the following Event IDs: 256, 259, 261, 263, 266, 268, 270, 272, 273, 275, 278, 279, 280.  
  
Value stored in `principal.hostname` from all other Event IDs.  
`UserID` | `principal.user.windows_sid / target.user.windows_sid` | Stored in `target.user.windows_sid` for the following Event IDs: 256, 259, 261, 263, 266, 268, 270, 272,273, 275, 278, 279, 280.  
  
Stored in `principal.user.windows_sid` for all other Event IDs  
  
### Analytic logs

**Original log field** | **UDM field** | **Comment**  
---|---|---  
`AA` | `network.dns.authoritative` |   
`Destination` | `target.ip / principal.ip` | Populated in either principal and target.  
`InterfaceIP` | `target.ip / principal.ip` | Stores DNS Server's IP address in `target.ip` for following Event IDs, 256, 259, 261, 263, 266, 268, 270, 272, 273, 275, 278, 279, 280.  
Stored in `principal.ip` for all other Event IDs (DNS response).  
`PacketData` | `network.dns.answers.binary_data` |   
`Port` | `target.port / principal.port` |   
`QNAME` | `network.dns.questions.name, target.hostname` | Do not store `QNAME` in `target.hostname` for following Event IDs: 256, 259, 261, 263, 266, 268, 270, 272, 273, 275, 278, 279, and 280  
`QTYPE` | `network.dns.questions.type` |   
`RCODE` | `network.dns.response_code` |   
`RD` | `network.dns.recursion_desired` |   
`Reason` | `security_result.summary` |   
`Source` | `principal.ip / target.ip` | Source IPv4/IPv6 address of the machine that initiated the DNS request.  
Stored in `target.ip` for Event ID 274. Stored in `target.ip` for Event ID 265 and 269. `InterfaceIP` contains the secondary server's IP address (principal) and Source (target) is the primary server's IP address.  
`TCP` | `network.ip_protocol` |   
`XID` | `network.dns.id` |   
`EventID` | `network.direction` | If the `EventID` log field value contains one of the following values, then the `network.direction` UDM field is set to `OUTBOUND`. 

  * `256`
  * `259`
  * `261`
  * `263`
  * `266`
  * `268`
  * `270`
  * `272`
  * `273`
  * `275`
  * `278`
  * `279`
  * `280`

  
Else, the `network.direction` UDM field is set to `INBOUND`.  
`Flags` | `additional.fields` |   
`Zone` | `target.resource.name` |   
`ZoneScope` | `target.resource.name` |   
`ForwardInterfaceIP` | `target.ip / principal.ip` | Stores DNS Server's IP address in `target.ip` for following Event IDs, 256, 259, 261, 263, 266, 268, 270, 272, 273, 275, 278, 279, 280.  
Stored in `principal.ip` for all other Event IDs (DNS response).  
`PolicyName` | `security_result.detection_fields` |   
`SECURE` | `additional.fields` |   
`ServerScope` | `additional.fields` |   
`CacheScope` | `additional.fields` |   
`AD` | `additional.fields` |   
`DNSSEC` | `additional.fields` |   
`Scope` | `target.resource.name` |   
`Computer` | `principal.hostname / target.hostname` | Value stored in `target.hostname` for the following Event IDs: 256, 259, 261, 263, 266, 268, 270, 272, 273, 275, 278, 279, 280.  
  
Value stored in `principal.hostname` from all other Event IDs.  
  
### Audit logs

**Note:** The original attribute collected and stored to target.resource.name is different for each Event ID.**Original log field** | **UDM field** | **Note**  
---|---|---  
`Name` | `target.resource.name` | Value is collected from events with Event ID 512.  
`Policy` | `target.resource.name` | Value is collected from events with Event ID 577, 578, 579, 580, 581, and 582, which are mapped to the `SETTING_*` event types.  
`QNAME` | `network.dns.questions.name, target.hostname` |   
`QTYPE` | `network.dns.questions.type` |   
`RecursionScope` | `target.resource.name` | Value is collected from events with Event IDs mapped to `SETTING_*` event types.  
`Scope` | `target.resource.name` | Value is collected from events with Event IDs mapped to `SETTING_*` event types.  
`Setting` | `target.resource.name` | Value is collected from events with Event IDs mapped to `SETTING_*` event types.  
`Source` | `principal.ip` |   
`Zone` | `target.resource.name` | Value is collected from events with Event IDs mapped to `SETTING_*` event types.  
`ZoneScope` | `target.resource.name` | Value is collected from events with Event IDs mapped to `SETTING_*` event types.  
  
### SourceModuleType im_file logs

**Deprecated:**

The following `labels` fields for UDM nouns are deprecated: `about.labels`, `intermediary.labels`, `observer.labels`, `principal.labels`, `src.labels`, `security_result.about.labels`, and `target.labels`. For existing parsers, in addition to these UDM fields, the logs fields are also mapped to key/value `additional.fields` UDM fields. For new parsers, the key/value settings in `additional.fields` UDM fields are used instead of the deprecated `labels` UDM fields. We recommend that you update the existing rules to use the key/value settings in the `additional.fields` UDM fields instead of the deprecated `labels` UDM fields.

**Original log field** | **UDM field** | **Note**  
---|---|---  
`EventReceivedTime` | `metadata.collected_timestamp` |   
`Expire` | `about.labels` (deprecated) |   
`Expire` | `additional.fields` |   
`InternalPacketIdentifier` | `about.labels` (deprecated) |   
`InternalPacketIdentifier` | `additional.fields` |   
`` | `about.labels` (deprecated) | Grok: Extracted the `internal_packet_identifier` field from the raw log and then mapped the `internal_packet_identifier` field to the `about.labels` UDM field.  
`` | `additional.fields` | Grok: Extracted the `internal_packet_identifier` field from the raw log and then mapped the `internal_packet_identifier` field to the `additional.fields` UDM field.  
`packet_identifier` | `about.labels` (deprecated) |   
`packet_identifier` | `additional.fields` |   
`LogInfo` | `metadata.description` |   
`PortNum` | `principal.port` |   
`Queued` | `about.labels` (deprecated) |   
`Queued` | `additional.fields` |   
`Socket` | `principal.labels` (deprecated) |   
`Socket` | `additional.fields` |   
`TimeQuery` | `about.labels` (deprecated) |   
`TimeQuery` | `additional.fields` |   
`BufLen` | `about.labels` (deprecated) |   
`BufLen` | `additional.fields` |   
`Opcode` | `network.dns.opcode` | If the `Opcode` log field value is equal to `Q`, then the `network.dns.opcode` UDM field is set to `0`.  
Else, if the `Opcode` log field value is equal to `I`, then the `network.dns.opcode` UDM field is set to `1`.  
Else, if the `Opcode` log field value is equal to `S`, then the `network.dns.opcode` UDM field is set to `2`.  
Else, if the `Opcode` log field value is equal to `N`, then the `network.dns.opcode` UDM field is set to `4`.  
Else, if the `Opcode` log field value is equal to `U`, then the `network.dns.opcode` UDM field is set to `5`.  
`opcode` | `network.dns.opcode` | Grok: Extracted the `opcode` field from the raw log.  
If the `opcode` field value is equal to `Q`, then the `network.dns.opcode` UDM field is set to `0`.  
Else, if the `opcode` field value is equal to `I`, then the `network.dns.opcode` UDM field is set to `1`.  
Else, if the `opcode` field value is equal to `S`, then the `network.dns.opcode` UDM field is set to `2`.  
Else, if the `opcode` field value is equal to `N`, then the `network.dns.opcode` UDM field is set to `4`.  
Else, if the `opcode` field value is equal to `U`, then the `network.dns.opcode` UDM field is set to `5`.  
`Protocol` | `network.ip_protocol` | If the `Protocol` log field value is equal to `1` or `ICMP`, then the `network.ip_protocol` UDM field is set to `ICMP`.  
Else, if the `Protocol` log field value is equal to `2` or `IGMP`, then the `network.ip_protocol` UDM field is set to `IGMP`.  
Else, if the `Protocol` log field value is equal to `6` or `TCP`, then the `network.ip_protocol` UDM field is set to `TCP`.  
Else, if the `Protocol` log field value is equal to `17` or `UDP`, then the `network.ip_protocol` UDM field is set to `UDP`.  
Else, if the `Protocol` log field value is equal to `41` or `IP6IN4`, then the `network.ip_protocol` UDM field is set to `IP6IN4`.  
Else, if the `Protocol` log field value is equal to `47` or `GRE`, then the `network.ip_protocol` UDM field is set to `GRE`.  
Else, if the `Protocol` log field value is equal to `50` or `ESP`, then the `network.ip_protocol` UDM field is set to `ESP`.  
Else, if the `Protocol` log field value is equal to `88` or `EIGRP`, then the `network.ip_protocol` UDM field is set to `EIGRP`.  
Else, if the `Protocol` log field value is equal to `97` or `ETHERIP`, then the `network.ip_protocol` UDM field is set to `ETHERIP`.  
Else, if the `Protocol` log field value is equal to `103` or `PIM`, then the `network.ip_protocol` UDM field is set to `PIM`.  
Else, if the `Protocol` log field value is equal to `112` or `VRRP`, then the `network.ip_protocol` UDM field is set to `VRRP`.  
`` | `network.ip_protocol` | Grok: Extracted the `ip_protocol` field from the raw log.  
If the `ip_protocol` field value is equal to `1` or `ICMP`, then the `network.ip_protocol` UDM field is set to `ICMP`.  
Else, if the `ip_protocol` field value is equal to `2` or `IGMP`, then the `network.ip_protocol` UDM field is set to `IGMP`.  
Else, if the `ip_protocol` field value is equal to `6` or `TCP`, then the `network.ip_protocol` UDM field is set to `TCP`.  
Else, if the `ip_protocol` field value is equal to `17` or `UDP`, then the `network.ip_protocol` UDM field is set to `UDP`.  
Else, if the `ip_protocol` field value is equal to `41` or `IP6IN4`, then the `network.ip_protocol` UDM field is set to `IP6IN4`.  
Else, if the `ip_protocol` field value is equal to `47` or `GRE`, then the `network.ip_protocol` UDM field is set to `GRE`.  
Else, if the `ip_protocol` field value is equal to `50` or `ESP`, then the `network.ip_protocol` UDM field is set to `ESP`.  
Else, if the `ip_protocol` field value is equal to `88` or `EIGRP`, then the `network.ip_protocol` UDM field is set to `EIGRP`.  
Else, if the `ip_protocol` field value is equal to `97` or `ETHERIP`, then the `network.ip_protocol` UDM field is set to `ETHERIP`.  
Else, if the `ip_protocol` field value is equal to `103` or `PIM`, then the `network.ip_protocol` UDM field is set to `PIM`.  
Else, if the `ip_protocol` field value is equal to `112` or `VRRP`, then the `network.ip_protocol` UDM field is set to `VRRP`.  
`` | `network.dns.response_code` | Grok: Extracted the `dns_response_code` field from the raw log.  
If the `dns_response_code` field value is equal to `NOERROR`, then the `network.dns.response_code` UDM field is set to `0`.  
Else, if the `dns_response_code` field value is equal to `FORMERR`, then the `network.dns.response_code` UDM field is set to `1`.  
Else, if the `dns_response_code` field value is equal to `SERVFAIL`, then the `network.dns.response_code` UDM field is set to `2`.  
Else, if the `dns_response_code` field value is equal to `NXDOMAIN`, then the `network.dns.response_code` UDM field is set to `3`.  
Else, if the `dns_response_code` field value is equal to `NOTIMP`, then the `network.dns.response_code` UDM field is set to `4`.  
Else, if the `dns_response_code` field value is equal to `REFUSED`, then the `network.dns.response_code` UDM field is set to `5`.  
Else, if the `dns_response_code` field value is equal to `YXDOMAIN`, then the `network.dns.response_code` UDM field is set to `6`.  
Else, if the `dns_response_code` field value is equal to `YXRRSET`, then the `network.dns.response_code` UDM field is set to `7`.  
Else, if the `dns_response_code` field value is equal to `NXRRSET`, then the `network.dns.response_code` UDM field is set to `8`.  
Else, if the `dns_response_code` field value is equal to `NOTAUTH`, then the `network.dns.response_code` UDM field is set to `9`.  
Else, if the `dns_response_code` field value is equal to `NOTZONE`, then the `network.dns.response_code` UDM field is set to `10`.  
Else, if the `dns_response_code` field value is equal to `DSOTYPENI`, then the `network.dns.response_code` UDM field is set to `11`.  
Else, if the `dns_response_code` field value is equal to `BADVERS`, then the `network.dns.response_code` UDM field is set to `16`.  
Else, if the `dns_response_code` field value is equal to `BADSIG`, then the `network.dns.response_code` UDM field is set to `16`.  
Else, if the `dns_response_code` field value is equal to `BADKEY`, then the `network.dns.response_code` UDM field is set to `17`.  
Else, if the `dns_response_code` field value is equal to `BADTIME`, then the `network.dns.response_code` UDM field is set to `18`.  
Else, if the `dns_response_code` field value is equal to `BADMODE`, then the `network.dns.response_code` UDM field is set to `19`.  
Else, if the `dns_response_code` field value is equal to `BADNAME`, then the `network.dns.response_code` UDM field is set to `20`.  
Else, if the `dns_response_code` field value is equal to `BADALG`, then the `network.dns.response_code` UDM field is set to `21`.  
Else, if the `dns_response_code` field value is equal to `BADTRUNC`, then the `network.dns.response_code` UDM field is set to `22`.  
Else, if the `dns_response_code` field value is equal to `BADCOOKIE`, then the `network.dns.response_code` UDM field is set to `23`.  
`` | `network.dns.authoritative` | Grok: Extracted the `authoritative` field from the raw log.  
If the `authoritative` field value is equal to `A`, then the `network.dns.authoritative` UDM field is set to `true`.  
`` | `network.dns.truncated` | Grok: Extracted the `truncated` field from the raw log.  
If the truncated field value is equal to T, then the network.dns.truncated UDM field is set to true.  
`` | `network.dns.recursion_desired` | Grok: Extracted the `recursion_desired` field from the raw log.  
If the `recursion_desired` field value is equal to `D`, then the `network.dns.recursion_desired` UDM field is set to `true`.  
`` | `network.dns.recursion_available` | Grok: Extracted the `recursion_available` field from the raw log.  
If the `recursion_available` field value is equal to `R`, then the `network.dns.recursion_available` UDM field is set to `true`.  
`QueryType` | `network.dns.response` | If the `QueryType` log field value is equal to `R`, then the `network.dns.response` UDM field is set to `true`.  
Else, the `network.dns.response` UDM field is set to `false`.  
`req_or_resp` | `network.dns.response` | Grok: Extracted the `req_or_resp` field from the raw log.   
If the `req_or_resp` field value is equal to `R`, then the `network.dns.response` UDM field is set to `true`.  
Else, the `network.dns.response` UDM field is set to `false`.  
`QuestionName` | `network.dns.questions.name, target.hostname` |   
`domain` | `network.dns.questions.name, target.hostname` | Grok: Extracted the `domain` field from the raw log and then mapped the `domain` field to the `network.dns.questions.name` and `target.hostname` UDM field.  
`QuestionType` | `network.dns.questions.type` | If the `QuestionType` field value is equal to `A`, then the `network.dns.question.type` UDM field is set to `1`.  
Else, if the `QuestionType` field value is equal to `NS`, then the `network.dns.question.type` UDM field is set to `2`.  
Else, if the `QuestionType` field value is equal to `MD`, then the `network.dns.question.type` UDM field is set to `3`.  
Else, if the `QuestionType` field value is equal to `MF`, then the `network.dns.question.type` UDM field is set to `4`.  
Else, if the `QuestionType` field value is equal to `CNAME`, then the `network.dns.question.type` UDM field is set to `5`.  
Else, if the `QuestionType` field value is equal to `SOA`, then the `network.dns.question.type` UDM field is set to `6`.  
Else, if the `QuestionType` field value is equal to `MB`, then the `network.dns.question.type` UDM field is set to `7`.  
Else, if the `QuestionType` field value is equal to `MG`, then the `network.dns.question.type` UDM field is set to `8`.  
Else, if the `QuestionType` field value is equal to `MR`, then the `network.dns.question.type` UDM field is set to `9`.  
Else, if the `QuestionType` field value is equal to `NULL`, then the `network.dns.question.type` UDM field is set to `10`.  
Else, if the `QuestionType` field value is equal to `WKS`, then the `network.dns.question.type` UDM field is set to `11`.  
Else, if the `QuestionType` field value is equal to `PTR`, then the `network.dns.question.type` UDM field is set to `12`.  
Else, if the `QuestionType` field value is equal to `HINFO`, then the `network.dns.question.type` UDM field is set to `13`.  
Else, if the `QuestionType` field value is equal to `MINFO`, then the `network.dns.question.type` UDM field is set to `14`.  
Else, if the `QuestionType` field value is equal to `MX`, then the `network.dns.question.type` UDM field is set to `15`.  
Else, if the `QuestionType` field value is equal to `TXT`, then the `network.dns.question.type` UDM field is set to `16`.  
Else, if the `QuestionType` field value is equal to `RP`, then the `network.dns.question.type` UDM field is set to `17`.  
Else, if the `QuestionType` field value is equal to `AFSDB`, then the `network.dns.question.type` UDM field is set to `18`.  
Else, if the `QuestionType` field value is equal to `X25`, then the `network.dns.question.type` UDM field is set to `19`.  
Else, if the `QuestionType` field value is equal to `ISDN`, then the `network.dns.question.type` UDM field is set to `20`.  
Else, if the `QuestionType` field value is equal to `RT`, then the `network.dns.question.type` UDM field is set to `21`.  
Else, if the `QuestionType` field value is equal to `NSAP`, then the `network.dns.question.type` UDM field is set to `22`.  
Else, if the `QuestionType` field value is equal to `NSAP-PT`, then the `network.dns.question`.type UDM field is se`t` to 23.  
Else, if the `QuestionType` field value is equal to `SIG`, then the `network.dns.question.type` UDM field is set to `24`.  
Else, if the `QuestionType` field value is equal to `KEY`, then the `network.dns.question.type` UDM field is set to `25`.  
Else, if the `QuestionType` field value is equal to `PX`, then the `network.dns.question.type` UDM field is set to `26`.  
Else, if the `QuestionType` field value is equal to `GPOS`, then the `network.dns.question.type` UDM field is set to `27`.  
Else, if the `QuestionType` field value is equal to `AAAA`, then the `network.dns.question.type` UDM field is set to `28`.  
Else, if the `QuestionType` field value is equal to `LOC`, then the `network.dns.question.type` UDM field is set to `29`.  
Else, if the `QuestionType` field value is equal to `NXT`, then the `network.dns.question.type` UDM field is set to `30`.  
Else, if the `QuestionType` field value is equal to `EID`, then the `network.dns.question.type` UDM field is set to `31`.  
Else, if the `QuestionType` field value is equal to `NIMLOC`, then the `network.dns.question.type` UDM field is set to `32`.  
Else, if the `QuestionType` field value is equal to `SRV`, then the `network.dns.question.type` UDM field is set to `33`.  
Else, if the `QuestionType` field value is equal to `ATMA`, then the `network.dns.question.type` UDM field is set to `34`.  
Else, if the `QuestionType` field value is equal to `NAPTR`, then the `network.dns.question.type` UDM field is set to `35`.  
Else, if the `QuestionType` field value is equal to `KX`, then the `network.dns.question.type` UDM field is set to `36`.  
Else, if the `QuestionType` field value is equal to `CERT`, then the `network.dns.question.type` UDM field is set to `37`.  
Else, if the `QuestionType` field value is equal to `A6`, then the `network.dns.question.type` UDM field is set to `38`.  
Else, if the `QuestionType` field value is equal to `DNAME`, then the `network.dns.question.type` UDM field is set to `39`.  
Else, if the `QuestionType` field value is equal to `SINK`, then the `network.dns.question.type` UDM field is set to `40`.  
Else, if the `QuestionType` field value is equal to `OPT`, then the `network.dns.question.type` UDM field is set to `41`.  
Else, if the `QuestionType` field value is equal to `APL`, then the `network.dns.question.type` UDM field is set to `42`.  
Else, if the `QuestionType` field value is equal to `DS`, then the `network.dns.question.type` UDM field is set to `43`.  
Else, if the `QuestionType` field value is equal to `SSHFP`, then the `network.dns.question.type` UDM field is set to `44`.  
Else, if the `QuestionType` field value is equal to `IPSECKE`, then the `network.dns.question.type` UDM field is set to `45`.  
Else, if the `QuestionType` field value is equal to `RRSIG`, then the `network.dns.question.type` UDM field is set to `46`.  
Else, if the `QuestionType` field value is equal to `NSEC`, then the `network.dns.question.type` UDM field is set to `47`.  
Else, if the `QuestionType` field value is equal to `DNSKEY`, then the `network.dns.question.type` UDM field is set to `48`.  
Else, if the `QuestionType` field value is equal to `DHCID`, then the `network.dns.question.type` UDM field is set to `49`.  
Else, if the `QuestionType` field value is equal to `NSEC3`, then the `network.dns.question.type` UDM field is set to `50`.  
Else, if the `QuestionType` field value is equal to `NSEC3PA`, then the `network.dns.question.type` UDM field is set to `51`.  
Else, if the `QuestionType` field value is equal to `TLSA`, then the `network.dns.question.type` UDM field is set to `52`.  
Else, if the `QuestionType` field value is equal to `SMIMEA`, then the `network.dns.question.type` UDM field is set to `53`.  
Else, if the `QuestionType` field value is equal to `UNASSIG`, then the `network.dns.question.type` UDM field is set to `54`.  
Else, if the `QuestionType` field value is equal to `HIP`, then the `network.dns.question.type` UDM field is set to `55`.  
Else, if the `QuestionType` field value is equal to `NINFO`, then the `network.dns.question.type` UDM field is set to `56`.  
Else, if the `QuestionType` field value is equal to `RKEY`, then the `network.dns.question.type` UDM field is set to `57`.  
Else, if the `QuestionType` field value is equal to `TALINK`, then the `network.dns.question.type` UDM field is set to `58`.  
Else, if the `QuestionType` field value is equal to `CDS`, then the `network.dns.question.type` UDM field is set to `59`.  
Else, if the `QuestionType` field value is equal to `CDNSKEY`, then the `network.dns.question.type` UDM field is set to `60`.  
Else, if the `QuestionType` field value is equal to `OPENPGP`, then the `network.dns.question.type` UDM field is set to `61`.  
Else, if the `QuestionType` field value is equal to `CSYNC`, then the `network.dns.question.type` UDM field is set to `62`.  
Else, if the `QuestionType` field value is equal to `ZONEMD`, then the `network.dns.question.type` UDM field is set to `63`.  
Else, if the `QuestionType` field value is equal to `SVCB`, then the `network.dns.question.type` UDM field is set to `64`.  
Else, if the `QuestionType` field value is equal to `HTTPS`, then the `network.dns.question.type` UDM field is set to `65`.  
Else, if the `QuestionType` field value is equal to `SPF`, then the `network.dns.question.type` UDM field is set to `99`.  
Else, if the `QuestionType` field value is equal to `UINFO`, then the `network.dns.question.type` UDM field is set to `100`.  
Else, if the `QuestionType` field value is equal to `UID`, then the `network.dns.question.type` UDM field is set to `101`.  
Else, if the `QuestionType` field value is equal to `GID`, then the `network.dns.question.type` UDM field is set to `102`.  
Else, if the `QuestionType` field value is equal to `UNSPEC`, then the `network.dns.question.type` UDM field is set to `103`.  
Else, if the `QuestionType` field value is equal to `NID`, then the `network.dns.question.type` UDM field is set to `104`.  
Else, if the `QuestionType` field value is equal to `L32`, then the `network.dns.question.type` UDM field is set to `105`.  
Else, if the `QuestionType` field value is equal to `L64`, then the `network.dns.question.type` UDM field is set to `106`.  
Else, if the `QuestionType` field value is equal to `LP`, then the `network.dns.question.type` UDM field is set to `107`.  
Else, if the `QuestionType` field value is equal to `EUI48`, then the `network.dns.question.type` UDM field is set to `108`.  
Else, if the `QuestionType` field value is equal to `EUI64`, then the `network.dns.question.type` UDM field is set to `109`.  
Else, if the `QuestionType` field value is equal to `TKEY`, then the `network.dns.question.type` UDM field is set to `249`.  
Else, if the `QuestionType` field value is equal to `TSIG`, then the `network.dns.question.type` UDM field is set to `250`.  
Else, if the `QuestionType` field value is equal to `IXFR`, then the `network.dns.question.type` UDM field is set to `251`.  
Else, if the `QuestionType` field value is equal to `AXFR`, then the `network.dns.question.type` UDM field is set to `252`.  
Else, if the `QuestionType` field value is equal to `MAILB`, then the `network.dns.question.type` UDM field is set to `253`.  
Else, if the `QuestionType` field value is equal to `MAILA`, then the `network.dns.question.type` UDM field is set to `254`.  
Else, if the `QuestionType` field value is equal to `ALL`, then the `network.dns.question.type` UDM field is set to `255`.  
Else, if the `QuestionType` field value is equal to `URI`, then the `network.dns.question.type` UDM field is set to `256`.  
Else, if the `QuestionType` field value is equal to `CAA`, then the `network.dns.question.type` UDM field is set to `257`.  
Else, if the `QuestionType` field value is equal to `AVC`, then the `network.dns.question.type` UDM field is set to `258`.  
Else, if the `QuestionType` field value is equal to `DOA`, then the `network.dns.question.type` UDM field is set to `259`.  
Else, if the `QuestionType` field value is equal to `AMTRELA`, then the `network.dns.question.type` UDM field is set to `260`.  
Else, if the `QuestionType` field value is equal to `TA`, then the `network.dns.question.type` UDM field is set to `32768`.  
Else, if the `QuestionType` field value is equal to `DLV`, then the `network.dns.question.type` UDM field is set to `32769`.  
`` | `network.dns.questions.type` | Grok: Extracted the `dns_record_type` field from the raw log.  
If the `dns_record_type` field value is equal to `A`, then the `network.dns.question.type` UDM field is set to `1`.  
Else, if the `dns_record_type` field value is equal to `NS`, then the `network.dns.question.type` UDM field is set to `2`.  
Else, if the `dns_record_type` field value is equal to `MD`, then the `network.dns.question.type` UDM field is set to `3`.  
Else, if the `dns_record_type` field value is equal to `MF`, then the `network.dns.question.type` UDM field is set to `4`.  
Else, if the `dns_record_type` field value is equal to `CNAME`, then the `network.dns.question.type` UDM field is set to `5`.  
Else, if the `dns_record_type` field value is equal to `SOA`, then the `network.dns.question.type` UDM field is set to `6`.  
Else, if the `dns_record_type` field value is equal to `MB`, then the `network.dns.question.type` UDM field is set to `7`.  
Else, if the `dns_record_type` field value is equal to `MG`, then the `network.dns.question.type` UDM field is set to `8`.  
Else, if the `dns_record_type` field value is equal to `MR`, then the `network.dns.question.type` UDM field is set to `9`.  
Else, if the `dns_record_type` field value is equal to `NULL`, then the `network.dns.question.type` UDM field is set to `10`.  
Else, if the `dns_record_type` field value is equal to `WKS`, then the `network.dns.question.type` UDM field is set to `11`.  
Else, if the `dns_record_type` field value is equal to `PTR`, then the `network.dns.question.type` UDM field is set to `12`.  
Else, if the `dns_record_type` field value is equal to `HINFO`, then the `network.dns.question.type` UDM field is set to `13`.  
Else, if the `dns_record_type` field value is equal to `MINFO`, then the `network.dns.question.type` UDM field is set to `14`.  
Else, if the `dns_record_type` field value is equal to `MX`, then the `network.dns.question.type` UDM field is set to `15`.  
Else, if the `dns_record_type` field value is equal to `TXT`, then the `network.dns.question.type` UDM field is set to `16`.  
Else, if the `dns_record_type` field value is equal to `RP`, then the `network.dns.question.type` UDM field is set to `17`.  
Else, if the `dns_record_type` field value is equal to `AFSDB`, then the `network.dns.question.type` UDM field is set to `18`.  
Else, if the `dns_record_type` field value is equal to `X25`, then the `network.dns.question.type` UDM field is set to `19`.  
Else, if the `dns_record_type` field value is equal to `ISDN`, then the `network.dns.question.type` UDM field is set to `20`.  
Else, if the `dns_record_type` field value is equal to `RT`, then the `network.dns.question.type` UDM field is set to `21`.  
Else, if the `dns_record_type` field value is equal to `NSAP`, then the `network.dns.question.type` UDM field is set to `22`.  
Else, if the `dns_record_type` field value is equal to `NSAP-PT`, then the `network.dns.question`.type UDM field is set` to` 23.  
Else, if the `dns_record_type` field value is equal to `SIG`, then the `network.dns.question.type` UDM field is set to `24`.  
Else, if the `dns_record_type` field value is equal to `KEY`, then the `network.dns.question.type` UDM field is set to `25`.  
Else, if the `dns_record_type` field value is equal to `PX`, then the `network.dns.question.type` UDM field is set to `26`.  
Else, if the `dns_record_type` field value is equal to `GPOS`, then the `network.dns.question.type` UDM field is set to `27`.  
Else, if the `dns_record_type` field value is equal to `AAAA`, then the `network.dns.question.type` UDM field is set to `28`.  
Else, if the `dns_record_type` field value is equal to `LOC`, then the `network.dns.question.type` UDM field is set to `29`.  
Else, if the `dns_record_type` field value is equal to `NXT`, then the `network.dns.question.type` UDM field is set to `30`.  
Else, if the `dns_record_type` field value is equal to `EID`, then the `network.dns.question.type` UDM field is set to `31`.  
Else, if the `dns_record_type` field value is equal to `NIMLOC`, then the `network.dns.question.type` UDM field is set to `32`.  
Else, if the `dns_record_type` field value is equal to `SRV`, then the `network.dns.question.type` UDM field is set to `33`.  
Else, if the `dns_record_type` field value is equal to `ATMA`, then the `network.dns.question.type` UDM field is set to `34`.  
Else, if the `dns_record_type` field value is equal to `NAPTR`, then the `network.dns.question.type` UDM field is set to `35`.  
Else, if the `dns_record_type` field value is equal to `KX`, then the `network.dns.question.type` UDM field is set to `36`.  
Else, if the `dns_record_type` field value is equal to `CERT`, then the `network.dns.question.type` UDM field is set to `37`.  
Else, if the `dns_record_type` field value is equal to `A6`, then the `network.dns.question.type` UDM field is set to `38`.  
Else, if the `dns_record_type` field value is equal to `DNAME`, then the `network.dns.question.type` UDM field is set to `39`.  
Else, if the `dns_record_type` field value is equal to `SINK`, then the `network.dns.question.type` UDM field is set to `40`.  
Else, if the `dns_record_type` field value is equal to `OPT`, then the `network.dns.question.type` UDM field is set to `41`.  
Else, if the `dns_record_type` field value is equal to `APL`, then the `network.dns.question.type` UDM field is set to `42`.  
Else, if the `dns_record_type` field value is equal to `DS`, then the `network.dns.question.type` UDM field is set to `43`.  
Else, if the `dns_record_type` field value is equal to `SSHFP`, then the `network.dns.question.type` UDM field is set to `44`.  
Else, if the `dns_record_type` field value is equal to `IPSECKE`, then the `network.dns.question.type` UDM field is set to `45`.  
Else, if the `dns_record_type` field value is equal to `RRSIG`, then the `network.dns.question.type` UDM field is set to `46`.  
Else, if the `dns_record_type` field value is equal to `NSEC`, then the `network.dns.question.type` UDM field is set to `47`.  
Else, if the `dns_record_type` field value is equal to `DNSKEY`, then the `network.dns.question.type` UDM field is set to `48`.  
Else, if the `dns_record_type` field value is equal to `DHCID`, then the `network.dns.question.type` UDM field is set to `49`.  
Else, if the `dns_record_type` field value is equal to `NSEC3`, then the `network.dns.question.type` UDM field is set to `50`.  
Else, if the `dns_record_type` field value is equal to `NSEC3PA`, then the `network.dns.question.type` UDM field is set to `51`.  
Else, if the `dns_record_type` field value is equal to `TLSA`, then the `network.dns.question.type` UDM field is set to `52`.  
Else, if the `dns_record_type` field value is equal to `SMIMEA`, then the `network.dns.question.type` UDM field is set to `53`.  
Else, if the `dns_record_type` field value is equal to `UNASSIG`, then the `network.dns.question.type` UDM field is set to `54`.  
Else, if the `dns_record_type` field value is equal to `HIP`, then the `network.dns.question.type` UDM field is set to `55`.  
Else, if the `dns_record_type` field value is equal to `NINFO`, then the `network.dns.question.type` UDM field is set to `56`.  
Else, if the `dns_record_type` field value is equal to `RKEY`, then the `network.dns.question.type` UDM field is set to `57`.  
Else, if the `dns_record_type` field value is equal to `TALINK`, then the `network.dns.question.type` UDM field is set to `58`.  
Else, if the `dns_record_type` field value is equal to `CDS`, then the `network.dns.question.type` UDM field is set to `59`.  
Else, if the `dns_record_type` field value is equal to `CDNSKEY`, then the `network.dns.question.type` UDM field is set to `60`.  
Else, if the `dns_record_type` field value is equal to `OPENPGP`, then the `network.dns.question.type` UDM field is set to `61`.  
Else, if the `dns_record_type` field value is equal to `CSYNC`, then the `network.dns.question.type` UDM field is set to `62`.  
Else, if the `dns_record_type` field value is equal to `ZONEMD`, then the `network.dns.question.type` UDM field is set to `63`.  
Else, if the `dns_record_type` field value is equal to `SVCB`, then the `network.dns.question.type` UDM field is set to `64`.  
Else, if the `dns_record_type` field value is equal to `HTTPS`, then the `network.dns.question.type` UDM field is set to `65`.  
Else, if the `dns_record_type` field value is equal to `SPF`, then the `network.dns.question.type` UDM field is set to `99`.  
Else, if the `dns_record_type` field value is equal to `UINFO`, then the `network.dns.question.type` UDM field is set to `100`.  
Else, if the `dns_record_type` field value is equal to `UID`, then the `network.dns.question.type` UDM field is set to `101`.  
Else, if the `dns_record_type` field value is equal to `GID`, then the `network.dns.question.type` UDM field is set to `102`.  
Else, if the `dns_record_type` field value is equal to `UNSPEC`, then the `network.dns.question.type` UDM field is set to `103`.  
Else, if the `dns_record_type` field value is equal to `NID`, then the `network.dns.question.type` UDM field is set to `104`.  
Else, if the `dns_record_type` field value is equal to `L32`, then the `network.dns.question.type` UDM field is set to `105`.  
Else, if the `dns_record_type` field value is equal to `L64`, then the `network.dns.question.type` UDM field is set to `106`.  
Else, if the `dns_record_type` field value is equal to `LP`, then the `network.dns.question.type` UDM field is set to `107`.  
Else, if the `dns_record_type` field value is equal to `EUI48`, then the `network.dns.question.type` UDM field is set to `108`.  
Else, if the `dns_record_type` field value is equal to `EUI64`, then the `network.dns.question.type` UDM field is set to `109`.  
Else, if the `dns_record_type` field value is equal to `TKEY`, then the `network.dns.question.type` UDM field is set to `249`.  
Else, if the `dns_record_type` field value is equal to `TSIG`, then the `network.dns.question.type` UDM field is set to `250`.  
Else, if the `dns_record_type` field value is equal to `IXFR`, then the `network.dns.question.type` UDM field is set to `251`.  
Else, if the `dns_record_type` field value is equal to `AXFR`, then the `network.dns.question.type` UDM field is set to `252`.  
Else, if the `dns_record_type` field value is equal to `MAILB`, then the `network.dns.question.type` UDM field is set to `253`.  
Else, if the `dns_record_type` field value is equal to `MAILA`, then the `network.dns.question.type` UDM field is set to `254`.  
Else, if the `dns_record_type` field value is equal to `ALL`, then the `network.dns.question.type` UDM field is set to `255`.  
Else, if the `dns_record_type` field value is equal to `URI`, then the `network.dns.question.type` UDM field is set to `256`.  
Else, if the `dns_record_type` field value is equal to `CAA`, then the `network.dns.question.type` UDM field is set to `257`.  
Else, if the `dns_record_type` field value is equal to `AVC`, then the `network.dns.question.type` UDM field is set to `258`.  
Else, if the `dns_record_type` field value is equal to `DOA`, then the `network.dns.question.type` UDM field is set to `259`.  
Else, if the `dns_record_type` field value is equal to `AMTRELA`, then the `network.dns.question.type` UDM field is set to `260`.  
Else, if the `dns_record_type` field value is equal to `TA`, then the `network.dns.question.type` UDM field is set to `32768`.  
Else, if the `dns_record_type` field value is equal to `DLV`, then the `network.dns.question.type` UDM field is set to `32769`.  
`dns_record_name` | `network.dns.questions.type` | If the `dns_record_name` field value is equal to `A`, then the `network.dns.question.type` UDM field is set to `1`.  
Else, if the `dns_record_name` field value is equal to `NS`, then the `network.dns.question.type` UDM field is set to `2`.  
Else, if the `dns_record_name` field value is equal to `MD`, then the `network.dns.question.type` UDM field is set to `3`.  
Else, if the `dns_record_name` field value is equal to `MF`, then the `network.dns.question.type` UDM field is set to `4`.  
Else, if the `dns_record_name` field value is equal to `CNAME`, then the `network.dns.question.type` UDM field is set to `5`.  
Else, if the `dns_record_name` field value is equal to `SOA`, then the `network.dns.question.type` UDM field is set to `6`.  
Else, if the `dns_record_name` field value is equal to `MB`, then the `network.dns.question.type` UDM field is set to `7`.  
Else, if the `dns_record_name` field value is equal to `MG`, then the `network.dns.question.type` UDM field is set to `8`.  
Else, if the `dns_record_name` field value is equal to `MR`, then the `network.dns.question.type` UDM field is set to `9`.  
Else, if the `dns_record_name` field value is equal to `NULL`, then the `network.dns.question.type` UDM field is set to `10`.  
Else, if the `dns_record_name` field value is equal to `WKS`, then the `network.dns.question.type` UDM field is set to `11`.  
Else, if the `dns_record_name` field value is equal to `PTR`, then the `network.dns.question.type` UDM field is set to `12`.  
Else, if the `dns_record_name` field value is equal to `HINFO`, then the `network.dns.question.type` UDM field is set to `13`.  
Else, if the `dns_record_name` field value is equal to `MINFO`, then the `network.dns.question.type` UDM field is set to `14`.  
Else, if the `dns_record_name` field value is equal to `MX`, then the `network.dns.question.type` UDM field is set to `15`.  
Else, if the `dns_record_name` field value is equal to `TXT`, then the `network.dns.question.type` UDM field is set to `16`.  
Else, if the `dns_record_name` field value is equal to `RP`, then the `network.dns.question.type` UDM field is set to `17`.  
Else, if the `dns_record_name` field value is equal to `AFSDB`, then the `network.dns.question.type` UDM field is set to `18`.  
Else, if the `dns_record_name` field value is equal to `X25`, then the `network.dns.question.type` UDM field is set to `19`.  
Else, if the `dns_record_name` field value is equal to `ISDN`, then the `network.dns.question.type` UDM field is set to `20`.  
Else, if the `dns_record_name` field value is equal to `RT`, then the `network.dns.question.type` UDM field is set to `21`.  
Else, if the `dns_record_name` field value is equal to `NSAP`, then the `network.dns.question.type` UDM field is set to `22`.  
Else, if the `dns_record_name` field value is equal to `NSAP-PT`, then the `network.dns.question`.type UDM field is se`t` to 23.  
Else, if the `dns_record_name` field value is equal to `SIG`, then the `network.dns.question.type` UDM field is set to `24`.  
Else, if the `dns_record_name` field value is equal to `KEY`, then the `network.dns.question.type` UDM field is set to `25`.  
Else, if the `dns_record_name` field value is equal to `PX`, then the `network.dns.question.type` UDM field is set to `26`.  
Else, if the `dns_record_name` field value is equal to `GPOS`, then the `network.dns.question.type` UDM field is set to `27`.  
Else, if the `dns_record_name` field value is equal to `AAAA`, then the `network.dns.question.type` UDM field is set to `28`.  
Else, if the `dns_record_name` field value is equal to `LOC`, then the `network.dns.question.type` UDM field is set to `29`.  
Else, if the `dns_record_name` field value is equal to `NXT`, then the `network.dns.question.type` UDM field is set to `30`.  
Else, if the `dns_record_name` field value is equal to `EID`, then the `network.dns.question.type` UDM field is set to `31`.  
Else, if the `dns_record_name` field value is equal to `NIMLOC`, then the `network.dns.question.type` UDM field is set to `32`.  
Else, if the `dns_record_name` field value is equal to `SRV`, then the `network.dns.question.type` UDM field is set to `33`.  
Else, if the `dns_record_name` field value is equal to `ATMA`, then the `network.dns.question.type` UDM field is set to `34`.  
Else, if the `dns_record_name` field value is equal to `NAPTR`, then the `network.dns.question.type` UDM field is set to `35`.  
Else, if the `dns_record_name` field value is equal to `KX`, then the `network.dns.question.type` UDM field is set to `36`.  
Else, if the `dns_record_name` field value is equal to `CERT`, then the `network.dns.question.type` UDM field is set to `37`.  
Else, if the `dns_record_name` field value is equal to `A6`, then the `network.dns.question.type` UDM field is set to `38`.  
Else, if the `dns_record_name` field value is equal to `DNAME`, then the `network.dns.question.type` UDM field is set to `39`.  
Else, if the `dns_record_name` field value is equal to `SINK`, then the `network.dns.question.type` UDM field is set to `40`.  
Else, if the `dns_record_name` field value is equal to `OPT`, then the `network.dns.question.type` UDM field is set to `41`.  
Else, if the `dns_record_name` field value is equal to `APL`, then the `network.dns.question.type` UDM field is set to `42`.  
Else, if the `dns_record_name` field value is equal to `DS`, then the `network.dns.question.type` UDM field is set to `43`.  
Else, if the `dns_record_name` field value is equal to `SSHFP`, then the `network.dns.question.type` UDM field is set to `44`.  
Else, if the `dns_record_name` field value is equal to `IPSECKE`, then the `network.dns.question.type` UDM field is set to `45`.  
Else, if the `dns_record_name` field value is equal to `RRSIG`, then the `network.dns.question.type` UDM field is set to `46`.  
Else, if the `dns_record_name` field value is equal to `NSEC`, then the `network.dns.question.type` UDM field is set to `47`.  
Else, if the `dns_record_name` field value is equal to `DNSKEY`, then the `network.dns.question.type` UDM field is set to `48`.  
Else, if the `dns_record_name` field value is equal to `DHCID`, then the `network.dns.question.type` UDM field is set to `49`.  
Else, if the `dns_record_name` field value is equal to `NSEC3`, then the `network.dns.question.type` UDM field is set to `50`.  
Else, if the `dns_record_name` field value is equal to `NSEC3PA`, then the `network.dns.question.type` UDM field is set to `51`.  
Else, if the `dns_record_name` field value is equal to `TLSA`, then the `network.dns.question.type` UDM field is set to `52`.  
Else, if the `dns_record_name` field value is equal to `SMIMEA`, then the `network.dns.question.type` UDM field is set to `53`.  
Else, if the `dns_record_name` field value is equal to `UNASSIG`, then the `network.dns.question.type` UDM field is set to `54`.  
Else, if the `dns_record_name` field value is equal to `HIP`, then the `network.dns.question.type` UDM field is set to `55`.  
Else, if the `dns_record_name` field value is equal to `NINFO`, then the `network.dns.question.type` UDM field is set to `56`.  
Else, if the `dns_record_name` field value is equal to `RKEY`, then the `network.dns.question.type` UDM field is set to `57`.  
Else, if the `dns_record_name` field value is equal to `TALINK`, then the `network.dns.question.type` UDM field is set to `58`.  
Else, if the `dns_record_name` field value is equal to `CDS`, then the `network.dns.question.type` UDM field is set to `59`.  
Else, if the `dns_record_name` field value is equal to `CDNSKEY`, then the `network.dns.question.type` UDM field is set to `60`.  
Else, if the `dns_record_name` field value is equal to `OPENPGP`, then the `network.dns.question.type` UDM field is set to `61`.  
Else, if the `dns_record_name` field value is equal to `CSYNC`, then the `network.dns.question.type` UDM field is set to `62`.  
Else, if the `dns_record_name` field value is equal to `ZONEMD`, then the `network.dns.question.type` UDM field is set to `63`.  
Else, if the `dns_record_name` field value is equal to `SVCB`, then the `network.dns.question.type` UDM field is set to `64`.  
Else, if the `dns_record_name` field value is equal to `HTTPS`, then the `network.dns.question.type` UDM field is set to `65`.  
Else, if the `dns_record_name` field value is equal to `SPF`, then the `network.dns.question.type` UDM field is set to `99`.  
Else, if the `dns_record_name` field value is equal to `UINFO`, then the `network.dns.question.type` UDM field is set to `100`.  
Else, if the `dns_record_name` field value is equal to `UID`, then the `network.dns.question.type` UDM field is set to `101`.  
Else, if the `dns_record_name` field value is equal to `GID`, then the `network.dns.question.type` UDM field is set to `102`.  
Else, if the `dns_record_name` field value is equal to `UNSPEC`, then the `network.dns.question.type` UDM field is set to `103`.  
Else, if the `dns_record_name` field value is equal to `NID`, then the `network.dns.question.type` UDM field is set to `104`.  
Else, if the `dns_record_name` field value is equal to `L32`, then the `network.dns.question.type` UDM field is set to `105`.  
Else, if the `dns_record_name` field value is equal to `L64`, then the `network.dns.question.type` UDM field is set to `106`.  
Else, if the `dns_record_name` field value is equal to `LP`, then the `network.dns.question.type` UDM field is set to `107`.  
Else, if the `dns_record_name` field value is equal to `EUI48`, then the `network.dns.question.type` UDM field is set to `108`.  
Else, if the `dns_record_name` field value is equal to `EUI64`, then the `network.dns.question.type` UDM field is set to `109`.  
Else, if the `dns_record_name` field value is equal to `TKEY`, then the `network.dns.question.type` UDM field is set to `249`.  
Else, if the `dns_record_name` field value is equal to `TSIG`, then the `network.dns.question.type` UDM field is set to `250`.  
Else, if the `dns_record_name` field value is equal to `IXFR`, then the `network.dns.question.type` UDM field is set to `251`.  
Else, if the `dns_record_name` field value is equal to `AXFR`, then the `network.dns.question.type` UDM field is set to `252`.  
Else, if the `dns_record_name` field value is equal to `MAILB`, then the `network.dns.question.type` UDM field is set to `253`.  
Else, if the `dns_record_name` field value is equal to `MAILA`, then the `network.dns.question.type` UDM field is set to `254`.  
Else, if the `dns_record_name` field value is equal to `ALL`, then the `network.dns.question.type` UDM field is set to `255`.  
Else, if the `dns_record_name` field value is equal to `URI`, then the `network.dns.question.type` UDM field is set to `256`.  
Else, if the `dns_record_name` field value is equal to `CAA`, then the `network.dns.question.type` UDM field is set to `257`.  
Else, if the `dns_record_name` field value is equal to `AVC`, then the `network.dns.question.type` UDM field is set to `258`.  
Else, if the `dns_record_name` field value is equal to `DOA`, then the `network.dns.question.type` UDM field is set to `259`.  
Else, if the `dns_record_name` field value is equal to `AMTRELA`, then the `network.dns.question.type` UDM field is set to `260`.  
Else, if the `dns_record_name` field value is equal to `TA`, then the `network.dns.question.type` UDM field is set to `32768`.  
Else, if the `dns_record_name` field value is equal to `DLV`, then the `network.dns.question.type` UDM field is set to `32769`.  
`RemoteIP` | `principal.ip` | If the value of the `RemoteIP` field matches the regular expression ip, then the `principal.ip` UDM field is mapped to `RemoteIP`.  
Else, `principal.hostname` UDM field is mapped to `RemoteIP`  
`` | `principal.ip` | Grok: Extracted the `client` field from the raw log.  
If the value of the `client` field matches the regular expression ip, then the `principal.ip` UDM field is mapped to `client`.  
Else, `principal.hostname` UDM field is mapped to `client`.  
`` | `intermediary.hostname` | Grok: Extracted the `syslog_host` field from the raw log.  
If the value of the `client` field matches the regular expression syslog_host, then the `intermediary.hostname` UDM field is mapped to the `syslog_host`.  
`SendReceiveIndicator` | `network.direction` | If the `SendReceiveIndicator` log field value is equal to `Snd`, then the `network.direction` UDM field is set to `OUTBOUND`.  
Else, if the `SendReceiveIndicator` log field value is equal to `Rcv`, then the `network.direction` UDM field is set to `INBOUND`.  
`send_receive_indicator` | `network.direction` | Grok: Extracted the `send_receive_indicator` field from the raw log.  
If the `send_receive_indicator` field value is equal to `Snd`, then the `network.direction` UDM field is set to `OUTBOUND`.  
Else, if the `send_receive_indicator` field value is equal to `Rcv`, then the `network.direction` UDM field is set to `INBOUND`.  
`Xid` | `network.dns.id` |   
`xid` | `network.dns.id` | Grok: Extracted the `xid` field from the raw log and then mapped the `xid` field to the `network.dns.id` UDM field.  
`` | `network.dns.answers.data` | Grok: Extracted the `DATA` field from the raw log and then mapped the `DATA` field to the `network.dns.answers.data` UDM field.  
`` | `network.dns.answers.type` | Grok: Extracted the `TYPE` field from the raw log and then mapped the `TYPE` field to the `network.dns.answers.type` UDM field.  
`` | `network.dns.answers.name` | Grok: Extracted the `Name` field from the raw log and then mapped the `Name` field to the `network.dns.answers.name` UDM field.  
`` | `network.dns.answers.ttl` | Grok: Extracted the `TTL` field from the raw log and then mapped the `TTL` field to the `network.dns.answers.ttl` UDM field.  
`` | `network.dns.answers.class` | Grok: Extracted the `CLASS` field from the raw log and then mapped the `CLASS` field to the `network.dns.answers.class` UDM field.  
  
### Legacy debug logs

**Deprecated:**

The following `labels` fields for UDM nouns are deprecated: `about.labels`, `intermediary.labels`, `observer.labels`, `principal.labels`, `src.labels`, `security_result.about.labels`, and `target.labels`. For existing parsers, in addition to these UDM fields, the logs fields are also mapped to key/value `additional.fields` UDM fields. For new parsers, the key/value settings in `additional.fields` UDM fields are used instead of the deprecated `labels` UDM fields. We recommend that you update the existing rules to use the key/value settings in the `additional.fields` UDM fields instead of the deprecated `labels` UDM fields.

**Original log field** | **UDM field** | **Note**  
---|---|---  
`BufLen` | `about.labels.key/value` (deprecated) | Grok: Extracted the `BufLen` field from the raw log and then mapped the `BufLen` field to the `about.labels` UDM field.  
`BufLen` | `additional.fields` | Grok: Extracted the `BufLen` field from the raw log and then mapped the `BufLen` field to the `additional.fields` UDM field.  
`client` | `principal.ip` | Grok: Extracted the `client` field from the raw log.   
If the value of the `client` field matches the regular expression ip, then the `principal.ip` UDM field is mapped to `client`.  
Else, `principal.hostname` UDM field is mapped to `client`.  
`domain` |  `network.dns.questions.name` `target.hostname` `target.asset.hostname` | Grok: Extracted the `domain` field from the raw log and then mapped the `domain` field to the `network.dns.questions.name, target.hostname and target.asset.hostname` UDM field.  
`Expire` | `about.labels.key/value` (deprecated) | Grok: Extracted the `Expire` field from the raw log and then mapped the `Expire` field to the `about.labels` UDM field.  
`Expire` | `additional.fields` | Grok: Extracted the `Expire` field from the raw log and then mapped the `Expire` field to the `additional.fields` UDM field.  
`internal_packet_identifier` | `about.labels.key/value` (deprecated) | Grok: Extracted the `internal_packet_identifier` field from the raw log and then mapped the `internal_packet_identifier` field to the `about.labels` UDM field.  
`internal_packet_identifier` | `additional.fields` | Grok: Extracted the `internal_packet_identifier` field from the raw log and then mapped the `internal_packet_identifier` field to the `additional.fields` UDM field.  
`ip_protocol` | `network.ip_protocol` | Grok: Extracted the `ip_protocol` field from the raw log.  
If the `ip_protocol` field value is equal to `1` or `ICMP`, then the `network.ip_protocol` UDM field is set to `ICMP`.  
Else, if the `ip_protocol` field value is equal to `2` or `IGMP`, then the `network.ip_protocol` UDM field is set to `IGMP`.  
Else, if the `ip_protocol` field value is equal to `6` or `TCP`, then the `network.ip_protocol` UDM field is set to `TCP`.  
Else, if the `ip_protocol` field value is equal to `17` or `UDP`, then the `network.ip_protocol` UDM field is set to `UDP`.  
Else, if the `ip_protocol` field value is equal to `41` or `IP6IN4`, then the `network.ip_protocol` UDM field is set to `IP6IN4`.  
Else, if the `ip_protocol` field value is equal to `47` or `GRE`, then the `network.ip_protocol` UDM field is set to `GRE`.  
Else, if the `ip_protocol` field value is equal to `50` or `ESP`, then the `network.ip_protocol` UDM field is set to `ESP`.  
Else, if the `ip_protocol` field value is equal to `88` or `EIGRP`, then the `network.ip_protocol` UDM field is set to `EIGRP`.  
Else, if the `ip_protocol` field value is equal to `97` or `ETHERIP`, then the `network.ip_protocol` UDM field is set to `ETHERIP`.  
Else, if the `ip_protocol` field value is equal to `103` or `PIM`, then the `network.ip_protocol` UDM field is set to `PIM`.  
Else, if the `ip_protocol` field value is equal to `112` or `VRRP`, then the `network.ip_protocol` UDM field is set to `VRRP`.  
`LogInfo` | `metadata.description` | Grok: Extracted the `LogInfo` field from the raw log and then mapped the `LogInfo` field to the `metadata.description` UDM field.  
`opcode` | `network.dns.opcode` | Grok: Extracted the `opcode` field from the raw log.  
If the `opcode` field value is equal to `Q`, then the `network.dns.opcode` UDM field is set to `0`.  
Else, if the `opcode` field value is equal to `I`, then the `network.dns.opcode` UDM field is set to `1`.  
Else, if the `opcode` field value is equal to `S`, then the `network.dns.opcode` UDM field is set to `2`.  
Else, if the `opcode` field value is equal to `N`, then the `network.dns.opcode` UDM field is set to `4`.  
Else, if the `opcode` field value is equal to `U`, then the `network.dns.opcode` UDM field is set to `5`.  
`PortNum` | `principal.port` | Grok: Extracted the `PortNum` field from the raw log and then mapped the `PortNum` field to the `principal.port` UDM field.  
`Queued` | `about.labels.key/value` (deprecated) | Grok: Extracted the `Queued` field from the raw log and then mapped the `Queued` field to the `about.labels` UDM field.  
`Queued` | `additional.fields` | Grok: Extracted the `Queued` field from the raw log and then mapped the `Queued` field to the `additional.fields` UDM field.  
`req_or_resp` | `network.dns.response` | Grok: Extracted `req_or_resp` from the raw log,  
If the `req_or_resp` field value is equal to `R`, then the `network.dns.response` UDM field is set to `true`.  
Else, the `network.dns.response` UDM field is set to `false`  
`send_receive_indicator` | `network.direction` | Grok: Extracted the `send_receive_indicator` field from the raw log.  
If the `send_receive_indicator` field value is equal to `Snd`, then the `network.direction` UDM field is set to `OUTBOUND`.  
Else, if the `send_receive_indicator` field value is equal to `Rcv`, then the `network.direction` UDM field is set to `INBOUND`.  
`Socket` | `principal.labels.key/value` (deprecated) | Grok: Extracted the `Socket` field from the raw log and then mapped the `Socket` field to the `principal.labels` UDM field.  
`Socket` | `additional.fields` | Grok: Extracted the `Socket` field from the raw log and then mapped the `Socket` field to the `additional.fields` UDM field.  
`TimeQuery` | `about.labels.key/value` (deprecated) | Grok: Extracted the `TimeQuery` field from the raw log and then mapped the `TimeQuery` field to the `about.labels` UDM field.  
`TimeQuery` | `additional.fields` | Grok: Extracted the `TimeQuery` field from the raw log and then mapped the `TimeQuery` field to the `additional.fields` UDM field.  
`xid` | `network.dns.id` | Grok: Extracted the `xid` field from the raw log and then mapped the `xid` field to the `network.dns.id` UDM field.  
`dns_record_type` |  `additional.fields.key/value.string_value` `network.dns.questions.type` | Grok: Extracted the `dns_record_type` field from the raw log.  
If the `dns_record_type` field value is equal to `A`, then the `network.dns.question.type` UDM field is set to `1`.  
Else, if the `dns_record_type` field value is equal to `NS`, then the `network.dns.question.type` UDM field is set to `2`.  
Else, if the `dns_record_type` field value is equal to `MD`, then the `network.dns.question.type` UDM field is set to `3`.  
Else, if the `dns_record_type` field value is equal to `MF`, then the `network.dns.question.type` UDM field is set to `4`.  
Else, if the `dns_record_type` field value is equal to `CNAME`, then the `network.dns.question.type` UDM field is set to `5`.  
Else, if the `dns_record_type` field value is equal to `SOA`, then the `network.dns.question.type` UDM field is set to `6`.  
Else, if the `dns_record_type` field value is equal to `MB`, then the `network.dns.question.type` UDM field is set to `7`.  
Else, if the `dns_record_type` field value is equal to `MG`, then the `network.dns.question.type` UDM field is set to `8`.  
Else, if the `dns_record_type` field value is equal to `MR`, then the `network.dns.question.type` UDM field is set to `9`.  
Else, if the `dns_record_type` field value is equal to `NULL`, then the `network.dns.question.type` UDM field is set to `10`.  
Else, if the `dns_record_type` field value is equal to `WKS`, then the `network.dns.question.type` UDM field is set to `11`.  
Else, if the `dns_record_type` field value is equal to `PTR`, then the `network.dns.question.type` UDM field is set to `12`.  
Else, if the `dns_record_type` field value is equal to `HINFO`, then the `network.dns.question.type` UDM field is set to `13`.  
Else, if the `dns_record_type` field value is equal to `MINFO`, then the `network.dns.question.type` UDM field is set to `14`.  
Else, if the `dns_record_type` field value is equal to `MX`, then the `network.dns.question.type` UDM field is set to `15`.  
Else, if the `dns_record_type` field value is equal to `TXT`, then the `network.dns.question.type` UDM field is set to `16`.  
Else, if the `dns_record_type` field value is equal to `RP`, then the `network.dns.question.type` UDM field is set to `17`.  
Else, if the `dns_record_type` field value is equal to `AFSDB`, then the `network.dns.question.type` UDM field is set to `18`.  
Else, if the `dns_record_type` field value is equal to `X25`, then the `network.dns.question.type` UDM field is set to `19`.  
Else, if the `dns_record_type` field value is equal to `ISDN`, then the `network.dns.question.type` UDM field is set to `20`.  
Else, if the `dns_record_type` field value is equal to `RT`, then the `network.dns.question.type` UDM field is set to `21`.  
Else, if the `dns_record_type` field value is equal to `NSAP`, then the `network.dns.question.type` UDM field is set to `22`.  
Else, if the `dns_record_type` field value is equal to `NSAP-PT`, then the `network.dns.question`.type UDM field is set` to` 23.  
Else, if the `dns_record_type` field value is equal to `SIG`, then the `network.dns.question.type` UDM field is set to `24`.  
Else, if the `dns_record_type` field value is equal to `KEY`, then the `network.dns.question.type` UDM field is set to `25`.  
Else, if the `dns_record_type` field value is equal to `PX`, then the `network.dns.question.type` UDM field is set to `26`.  
Else, if the `dns_record_type` field value is equal to `GPOS`, then the `network.dns.question.type` UDM field is set to `27`.  
Else, if the `dns_record_type` field value is equal to `AAAA`, then the `network.dns.question.type` UDM field is set to `28`.  
Else, if the `dns_record_type` field value is equal to `LOC`, then the `network.dns.question.type` UDM field is set to `29`.  
Else, if the `dns_record_type` field value is equal to `NXT`, then the `network.dns.question.type` UDM field is set to `30`.  
Else, if the `dns_record_type` field value is equal to `EID`, then the `network.dns.question.type` UDM field is set to `31`.  
Else, if the `dns_record_type` field value is equal to `NIMLOC`, then the `network.dns.question.type` UDM field is set to `32`.  
Else, if the `dns_record_type` field value is equal to `SRV`, then the `network.dns.question.type` UDM field is set to `33`.  
Else, if the `dns_record_type` field value is equal to `ATMA`, then the `network.dns.question.type` UDM field is set to `34`.  
Else, if the `dns_record_type` field value is equal to `NAPTR`, then the `network.dns.question.type` UDM field is set to `35`.  
Else, if the `dns_record_type` field value is equal to `KX`, then the `network.dns.question.type` UDM field is set to `36`.  
Else, if the `dns_record_type` field value is equal to `CERT`, then the `network.dns.question.type` UDM field is set to `37`.  
Else, if the `dns_record_type` field value is equal to `A6`, then the `network.dns.question.type` UDM field is set to `38`.  
Else, if the `dns_record_type` field value is equal to `DNAME`, then the `network.dns.question.type` UDM field is set to `39`.  
Else, if the `dns_record_type` field value is equal to `SINK`, then the `network.dns.question.type` UDM field is set to `40`.  
Else, if the `dns_record_type` field value is equal to `OPT`, then the `network.dns.question.type` UDM field is set to `41`.  
Else, if the `dns_record_type` field value is equal to `APL`, then the `network.dns.question.type` UDM field is set to `42`.  
Else, if the `dns_record_type` field value is equal to `DS`, then the `network.dns.question.type` UDM field is set to `43`.  
Else, if the `dns_record_type` field value is equal to `SSHFP`, then the `network.dns.question.type` UDM field is set to `44`.  
Else, if the `dns_record_type` field value is equal to `IPSECKE`, then the `network.dns.question.type` UDM field is set to `45`.  
Else, if the `dns_record_type` field value is equal to `RRSIG`, then the `network.dns.question.type` UDM field is set to `46`.  
Else, if the `dns_record_type` field value is equal to `NSEC`, then the `network.dns.question.type` UDM field is set to `47`.  
Else, if the `dns_record_type` field value is equal to `DNSKEY`, then the `network.dns.question.type` UDM field is set to `48`.  
Else, if the `dns_record_type` field value is equal to `DHCID`, then the `network.dns.question.type` UDM field is set to `49`.  
Else, if the `dns_record_type` field value is equal to `NSEC3`, then the `network.dns.question.type` UDM field is set to `50`.  
Else, if the `dns_record_type` field value is equal to `NSEC3PA`, then the `network.dns.question.type` UDM field is set to `51`.  
Else, if the `dns_record_type` field value is equal to `TLSA`, then the `network.dns.question.type` UDM field is set to `52`.  
Else, if the `dns_record_type` field value is equal to `SMIMEA`, then the `network.dns.question.type` UDM field is set to `53`.  
Else, if the `dns_record_type` field value is equal to `UNASSIG`, then the `network.dns.question.type` UDM field is set to `54`.  
Else, if the `dns_record_type` field value is equal to `HIP`, then the `network.dns.question.type` UDM field is set to `55`.  
Else, if the `dns_record_type` field value is equal to `NINFO`, then the `network.dns.question.type` UDM field is set to `56`.  
Else, if the `dns_record_type` field value is equal to `RKEY`, then the `network.dns.question.type` UDM field is set to `57`.  
Else, if the `dns_record_type` field value is equal to `TALINK`, then the `network.dns.question.type` UDM field is set to `58`.  
Else, if the `dns_record_type` field value is equal to `CDS`, then the `network.dns.question.type` UDM field is set to `59`.  
Else, if the `dns_record_type` field value is equal to `CDNSKEY`, then the `network.dns.question.type` UDM field is set to `60`.  
Else, if the `dns_record_type` field value is equal to `OPENPGP`, then the `network.dns.question.type` UDM field is set to `61`.  
Else, if the `dns_record_type` field value is equal to `CSYNC`, then the `network.dns.question.type` UDM field is set to `62`.  
Else, if the `dns_record_type` field value is equal to `ZONEMD`, then the `network.dns.question.type` UDM field is set to `63`.  
Else, if the `dns_record_type` field value is equal to `SVCB`, then the `network.dns.question.type` UDM field is set to `64`.  
Else, if the `dns_record_type` field value is equal to `HTTPS`, then the `network.dns.question.type` UDM field is set to `65`.  
Else, if the `dns_record_type` field value is equal to `SPF`, then the `network.dns.question.type` UDM field is set to `99`.  
Else, if the `dns_record_type` field value is equal to `UINFO`, then the `network.dns.question.type` UDM field is set to `100`.  
Else, if the `dns_record_type` field value is equal to `UID`, then the `network.dns.question.type` UDM field is set to `101`.  
Else, if the `dns_record_type` field value is equal to `GID`, then the `network.dns.question.type` UDM field is set to `102`.  
Else, if the `dns_record_type` field value is equal to `UNSPEC`, then the `network.dns.question.type` UDM field is set to `103`.  
Else, if the `dns_record_type` field value is equal to `NID`, then the `network.dns.question.type` UDM field is set to `104`.  
Else, if the `dns_record_type` field value is equal to `L32`, then the `network.dns.question.type` UDM field is set to `105`.  
Else, if the `dns_record_type` field value is equal to `L64`, then the `network.dns.question.type` UDM field is set to `106`.  
Else, if the `dns_record_type` field value is equal to `LP`, then the `network.dns.question.type` UDM field is set to `107`.  
Else, if the `dns_record_type` field value is equal to `EUI48`, then the `network.dns.question.type` UDM field is set to `108`.  
Else, if the `dns_record_type` field value is equal to `EUI64`, then the `network.dns.question.type` UDM field is set to `109`.  
Else, if the `dns_record_type` field value is equal to `TKEY`, then the `network.dns.question.type` UDM field is set to `249`.  
Else, if the `dns_record_type` field value is equal to `TSIG`, then the `network.dns.question.type` UDM field is set to `250`.  
Else, if the `dns_record_type` field value is equal to `IXFR`, then the `network.dns.question.type` UDM field is set to `251`.  
Else, if the `dns_record_type` field value is equal to `AXFR`, then the `network.dns.question.type` UDM field is set to `252`.  
Else, if the `dns_record_type` field value is equal to `MAILB`, then the `network.dns.question.type` UDM field is set to `253`.  
Else, if the `dns_record_type` field value is equal to `MAILA`, then the `network.dns.question.type` UDM field is set to `254`.  
Else, if the `dns_record_type` field value is equal to `ALL`, then the `network.dns.question.type` UDM field is set to `255`.  
Else, if the `dns_record_type` field value is equal to `URI`, then the `network.dns.question.type` UDM field is set to `256`.  
Else, if the `dns_record_type` field value is equal to `CAA`, then the `network.dns.question.type` UDM field is set to `257`.  
Else, if the `dns_record_type` field value is equal to `AVC`, then the `network.dns.question.type` UDM field is set to `258`.  
Else, if the `dns_record_type` field value is equal to `DOA`, then the `network.dns.question.type` UDM field is set to `259`.  
Else, if the `dns_record_type` field value is equal to `AMTRELA`, then the `network.dns.question.type` UDM field is set to `260`.  
Else, if the `dns_record_type` field value is equal to `TA`, then the `network.dns.question.type` UDM field is set to `32768`.  
Else, if the `dns_record_type` field value is equal to `DLV`, then the `network.dns.question.type` UDM field is set to `32769`.  
`CLASS` | `network.dns.additional.class` | `PREREQUISITE SECTION CLASS`  
`DATA` | `network.dns.additional.data` | `PREREQUISITE SECTION DATA`  
`Name` | `network.dns.additional.name` | `PREREQUISITE SECTION Name`  
`TTL` | `network.dns.additional.ttl` | `PREREQUISITE SECTION TTL`  
`TYPE` | `network.dns.additional.type` | `PREREQUISITE SECTION TYPE`  
`Flags` | `additional.fields.key/value.string_value` | Grok: Extracted the `Flags` field from the raw log and then mapped the `Flags` field to the `additional.fields.key/value.string_value` UDM field.  
`CLASS` | `network.dns.additional.class` | `UPDATE SECTION CLASS`  
`DATA` | `network.dns.additional.data` | `UPDATE SECTION DATA`  
`Name` | `network.dns.additional.name` | `UPDATE SECTION Name`  
`TTL` | `network.dns.additional.ttl` | `UPDATE SECTION TTL`  
`TYPE` | `network.dns.additional.type` | `UPDATE SECTION TYPE`  
`ZCLASS` | `network.dns.additional.class` | `ZONE SECTION ZCLASS`  
`Name` | `network.dns.additional.name` | `ZONE SECTION Name`  
`ZTYPE` | `network.dns.additional.type` | `ZONE SECTION ZTYPE`  
`QR` | `additional.fields.key/value.string_value` |   
`OPCODE` | `additional.fields.key/value.string_value` |   
`AA` | `additional.fields.key/value.string_value` |   
`TC` | `additional.fields.key/value.string_value` |   
`RD` | `additional.fields.key/value.string_value` |   
`RA` | `additional.fields.key/value.string_value` |   
`Z` | `additional.fields.key/value.string_value` |   
`CD` | `additional.fields.key/value.string_value` |   
`AD` | `additional.fields.key/value.string_value` |   
`RCODE` | `additional.fields.key/value.string_value` |   
`ZCOUNT` | `additional.fields.key/value.string_value` |   
`PRECOUNT` | `additional.fields.key/value.string_value` |   
`ARCOUNT` | `additional.fields.key/value.string_value` |   
`UPCOUNT` | `additional.fields.key/value.string_value` |   
`QCOUNT` | `additional.fields.key/value.string_value` |   
`ACOUNT` #NOTYPO | `additional.fields.key/value.string_value` |   
`NSCOUNT` | `additional.fields.key/value.string_value` |   
`host_name` | `intermediary.hostname` | Grok: Extracted the `host_name` field from the raw log and then mapped the `host_name` field to the `intermediary.hostname` UDM field.  
`os_type` | `intermediary.asset.platform_software.platform` | Grok: Extracted the `os_type` field from the raw log.  
If the `os_type` extracted field value matches the regular expression pattern `(?i)windows`, then the `intermediary.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
  
Else, if the `os_type` extracted field value matches the regular expression pattern `(?i)linux`, then the `intermediary.asset.platform_software.platform` UDM field is set to `LINUX`.  
  
Else, if the `os_type` extracted field is _not_ empty, then the `os_type` extracted field is mapped with the `intermediary.asset.attribute.labels` UDM field.  
  
### Other logs

**Original log field** | **UDM field** | **Note**  
---|---|---  
`` | `network.dns.questions.name, target.hostname` | Grok: Extracted the `record_name` field from the raw log and then mapped the `record_name` field to the `network.dns.questions.name and target.hostname` UDM field.  
`` | `network.dns.questions.type` | Grok: Extracted the `record_type` field from the raw log.  
If the `record_type` field value is equal to `A`, then the `network.dns.question.type` UDM field is set to `1`.  
Else, if the `record_type` field value is equal to `NS`, then the `network.dns.question.type` UDM field is set to `2`.  
Else, if the `record_type` field value is equal to `MD`, then the `network.dns.question.type` UDM field is set to `3`.  
Else, if the `record_type` field value is equal to `MF`, then the `network.dns.question.type` UDM field is set to `4`.  
Else, if the `record_type` field value is equal to `CNAME`, then the `network.dns.question.type` UDM field is set to `5`.  
Else, if the `record_type` field value is equal to `SOA`, then the `network.dns.question.type` UDM field is set to `6`.  
Else, if the `record_type` field value is equal to `MB`, then the `network.dns.question.type` UDM field is set to `7`.  
Else, if the `record_type` field value is equal to `MG`, then the `network.dns.question.type` UDM field is set to `8`.  
Else, if the `record_type` field value is equal to `MR`, then the `network.dns.question.type` UDM field is set to `9`.  
Else, if the `record_type` field value is equal to `NULL`, then the `network.dns.question.type` UDM field is set to `10`.  
Else, if the `record_type` field value is equal to `WKS`, then the `network.dns.question.type` UDM field is set to `11`.  
Else, if the `record_type` field value is equal to `PTR`, then the `network.dns.question.type` UDM field is set to `12`.  
Else, if the `record_type` field value is equal to `HINFO`, then the `network.dns.question.type` UDM field is set to `13`.  
Else, if the `record_type` field value is equal to `MINFO`, then the `network.dns.question.type` UDM field is set to `14`.  
Else, if the `record_type` field value is equal to `MX`, then the `network.dns.question.type` UDM field is set to `15`.  
Else, if the `record_type` field value is equal to `TXT`, then the `network.dns.question.type` UDM field is set to `16`.  
Else, if the `record_type` field value is equal to `RP`, then the `network.dns.question.type` UDM field is set to `17`.  
Else, if the `record_type` field value is equal to `AFSDB`, then the `network.dns.question.type` UDM field is set to `18`.  
Else, if the `record_type` field value is equal to `X25`, then the `network.dns.question.type` UDM field is set to `19`.  
Else, if the `record_type` field value is equal to `ISDN`, then the `network.dns.question.type` UDM field is set to `20`.  
Else, if the `record_type` field value is equal to `RT`, then the `network.dns.question.type` UDM field is set to `21`.  
Else, if the `record_type` field value is equal to `NSAP`, then the `network.dns.question.type` UDM field is set to `22`.  
Else, if the `record_type` field value is equal to `NSAP-PT`, then the `network.dns.question`.type UDM field is se`t` to 23.  
Else, if the `record_type` field value is equal to `SIG`, then the `network.dns.question.type` UDM field is set to `24`.  
Else, if the `record_type` field value is equal to `KEY`, then the `network.dns.question.type` UDM field is set to `25`.  
Else, if the `record_type` field value is equal to `PX`, then the `network.dns.question.type` UDM field is set to `26`.  
Else, if the `record_type` field value is equal to `GPOS`, then the `network.dns.question.type` UDM field is set to `27`.  
Else, if the `record_type` field value is equal to `AAAA`, then the `network.dns.question.type` UDM field is set to `28`.  
Else, if the `record_type` field value is equal to `LOC`, then the `network.dns.question.type` UDM field is set to `29`.  
Else, if the `record_type` field value is equal to `NXT`, then the `network.dns.question.type` UDM field is set to `30`.  
Else, if the `record_type` field value is equal to `EID`, then the `network.dns.question.type` UDM field is set to `31`.  
Else, if the `record_type` field value is equal to `NIMLOC`, then the `network.dns.question.type` UDM field is set to `32`.  
Else, if the `record_type` field value is equal to `SRV`, then the `network.dns.question.type` UDM field is set to `33`.  
Else, if the `record_type` field value is equal to `ATMA`, then the `network.dns.question.type` UDM field is set to `34`.  
Else, if the `record_type` field value is equal to `NAPTR`, then the `network.dns.question.type` UDM field is set to `35`.  
Else, if the `record_type` field value is equal to `KX`, then the `network.dns.question.type` UDM field is set to `36`.  
Else, if the `record_type` field value is equal to `CERT`, then the `network.dns.question.type` UDM field is set to `37`.  
Else, if the `record_type` field value is equal to `A6`, then the `network.dns.question.type` UDM field is set to `38`.  
Else, if the `record_type` field value is equal to `DNAME`, then the `network.dns.question.type` UDM field is set to `39`.  
Else, if the `record_type` field value is equal to `SINK`, then the `network.dns.question.type` UDM field is set to `40`.  
Else, if the `record_type` field value is equal to `OPT`, then the `network.dns.question.type` UDM field is set to `41`.  
Else, if the `record_type` field value is equal to `APL`, then the `network.dns.question.type` UDM field is set to `42`.  
Else, if the `record_type` field value is equal to `DS`, then the `network.dns.question.type` UDM field is set to `43`.  
Else, if the `record_type` field value is equal to `SSHFP`, then the `network.dns.question.type` UDM field is set to `44`.  
Else, if the `record_type` field value is equal to `IPSECKE`, then the `network.dns.question.type` UDM field is set to `45`.  
Else, if the `record_type` field value is equal to `RRSIG`, then the `network.dns.question.type` UDM field is set to `46`.  
Else, if the `record_type` field value is equal to `NSEC`, then the `network.dns.question.type` UDM field is set to `47`.  
Else, if the `record_type` field value is equal to `DNSKEY`, then the `network.dns.question.type` UDM field is set to `48`.  
Else, if the `record_type` field value is equal to `DHCID`, then the `network.dns.question.type` UDM field is set to `49`.  
Else, if the `record_type` field value is equal to `NSEC3`, then the `network.dns.question.type` UDM field is set to `50`.  
Else, if the `record_type` field value is equal to `NSEC3PA`, then the `network.dns.question.type` UDM field is set to `51`.  
Else, if the `record_type` field value is equal to `TLSA`, then the `network.dns.question.type` UDM field is set to `52`.  
Else, if the `record_type` field value is equal to `SMIMEA`, then the `network.dns.question.type` UDM field is set to `53`.  
Else, if the `record_type` field value is equal to `UNASSIG`, then the `network.dns.question.type` UDM field is set to `54`.  
Else, if the `record_type` field value is equal to `HIP`, then the `network.dns.question.type` UDM field is set to `55`.  
Else, if the `record_type` field value is equal to `NINFO`, then the `network.dns.question.type` UDM field is set to `56`.  
Else, if the `record_type` field value is equal to `RKEY`, then the `network.dns.question.type` UDM field is set to `57`.  
Else, if the `record_type` field value is equal to `TALINK`, then the `network.dns.question.type` UDM field is set to `58`.  
Else, if the `record_type` field value is equal to `CDS`, then the `network.dns.question.type` UDM field is set to `59`.  
Else, if the `record_type` field value is equal to `CDNSKEY`, then the `network.dns.question.type` UDM field is set to `60`.  
Else, if the `record_type` field value is equal to `OPENPGP`, then the `network.dns.question.type` UDM field is set to `61`.  
Else, if the `record_type` field value is equal to `CSYNC`, then the `network.dns.question.type` UDM field is set to `62`.  
Else, if the `record_type` field value is equal to `ZONEMD`, then the `network.dns.question.type` UDM field is set to `63`.  
Else, if the `record_type` field value is equal to `SVCB`, then the `network.dns.question.type` UDM field is set to `64`.  
Else, if the `record_type` field value is equal to `HTTPS`, then the `network.dns.question.type` UDM field is set to `65`.  
Else, if the `record_type` field value is equal to `SPF`, then the `network.dns.question.type` UDM field is set to `99`.  
Else, if the `record_type` field value is equal to `UINFO`, then the `network.dns.question.type` UDM field is set to `100`.  
Else, if the `record_type` field value is equal to `UID`, then the `network.dns.question.type` UDM field is set to `101`.  
Else, if the `record_type` field value is equal to `GID`, then the `network.dns.question.type` UDM field is set to `102`.  
Else, if the `record_type` field value is equal to `UNSPEC`, then the `network.dns.question.type` UDM field is set to `103`.  
Else, if the `record_type` field value is equal to `NID`, then the `network.dns.question.type` UDM field is set to `104`.  
Else, if the `record_type` field value is equal to `L32`, then the `network.dns.question.type` UDM field is set to `105`.  
Else, if the `record_type` field value is equal to `L64`, then the `network.dns.question.type` UDM field is set to `106`.  
Else, if the `record_type` field value is equal to `LP`, then the `network.dns.question.type` UDM field is set to `107`.  
Else, if the `record_type` field value is equal to `EUI48`, then the `network.dns.question.type` UDM field is set to `108`.  
Else, if the `record_type` field value is equal to `EUI64`, then the `network.dns.question.type` UDM field is set to `109`.  
Else, if the `record_type` field value is equal to `TKEY`, then the `network.dns.question.type` UDM field is set to `249`.  
Else, if the `record_type` field value is equal to `TSIG`, then the `network.dns.question.type` UDM field is set to `250`.  
Else, if the `record_type` field value is equal to `IXFR`, then the `network.dns.question.type` UDM field is set to `251`.  
Else, if the `record_type` field value is equal to `AXFR`, then the `network.dns.question.type` UDM field is set to `252`.  
Else, if the `record_type` field value is equal to `MAILB`, then the `network.dns.question.type` UDM field is set to `253`.  
Else, if the `record_type` field value is equal to `MAILA`, then the `network.dns.question.type` UDM field is set to `254`.  
Else, if the `record_type` field value is equal to `ALL`, then the `network.dns.question.type` UDM field is set to `255`.  
Else, if the `record_type` field value is equal to `URI`, then the `network.dns.question.type` UDM field is set to `256`.  
Else, if the `record_type` field value is equal to `CAA`, then the `network.dns.question.type` UDM field is set to `257`.  
Else, if the `record_type` field value is equal to `AVC`, then the `network.dns.question.type` UDM field is set to `258`.  
Else, if the `record_type` field value is equal to `DOA`, then the `network.dns.question.type` UDM field is set to `259`.  
Else, if the `record_type` field value is equal to `AMTRELA`, then the `network.dns.question.type` UDM field is set to `260`.  
Else, if the `record_type` field value is equal to `TA`, then the `network.dns.question.type` UDM field is set to `32768`.  
Else, if the `record_type` field value is equal to `DLV`, then the `network.dns.question.type` UDM field is set to `32769`.  
`client` | `principal.ip` | Grok: Extracted the `client` field from the raw log.   
If the value of the `client` field matches the regular expression ip, then the `principal.ip` UDM field is mapped to `client`.  
Else, `principal.hostname` UDM field is mapped to client.  
`` | `intermediary.hostname` | Grok: Extracted the `syslog_host` field from the raw log.  
If the value of the `client` field matches the regular expression ip, then the `intermediary.hostname` UDM field is mapped to `the` syslog_host.  
`` | `network.dns.questions.class` | Grok: Extracted the `qclass` field from the raw log.  
If the `qclass` field value is equal to `IN`, then `network.dns.questions.class` is set to `1`.  
Else, if the `qclass` field value is equal to `CH`, then `network.dns.questions.class` is set to `3`.  
Else, if the `qclass` field value is equal to `HS`, then `network.dns.questions.class` is set to `4`.  
  
## Field mapping reference: Event ID to UDM event type

This section describes how the parser maps Event Ids to UDM event_types. In general, events are mapped to the NETWORK_DNS metadata.event_type, except for Event IDs in the following section. 

**Note:** The % values (e.g. %1, %2, %3, %{EventID}) are variable placeholders.

**Event Id** | **Event Text** | **UDM Event Type** | **Notes**  
---|---|---|---  
`275` | XFR_NOTIFY_ACK_IN: Source=%1; InterfaceIP=%2; PacketData=%4 | `GENERIC_EVENT` |   
`276` | IXFR_RESP_OUT: TCP=%1; InterfaceIP=%2; Destination=%3; QNAME=%4; XID=%5; ZoneScope=%6; Zone=%7; RCODE=%8; PacketData=%10 | `GENERIC_EVENT` |   
`512` |  | `SETTING_CREATION` |   
`513` | The zone %1 was deleted. | `SETTING_DELETION` |   
`514` | The zone %1 was updated. The %2 setting has been set to %3. | `SETTING_MODIFICATION` |   
`515` | A resource record of type %1, name %2, TTL %3 and RDATA %5 was created in scope %7 of zone %6. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`516` | A resource record of type %1, name %2 and RDATA %5 was deleted from scope %7 of zone %6. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`517` | All resource records of type %1, name %2 were deleted from scope %4 of zone %3. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`518` | All resource records at Node name %1 were deleted from scope %3 of zone %2. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`519` | A resource record of type %1, name %2, TTL %3 and RDATA %5 was created in scope %7 of zone %6 via dynamic update from IP Address %8. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`520` | A resource record of type %1, name %2 and RDATA %5 was deleted from scope %7 of zone %6 via dynamic update from IP Address %8. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`521` | A resource record of type %1, name %2, TTL %3 and RDATA %5 was scavenged from scope %7 of zone %6. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`522` | The scope %1 was created in zone %2. | `SETTING_CREATION` |   
`523` | The scope %1 was deleted in zone %2. | `SETTING_DELETION` |   
`525` | The zone %1 was signed with following properties: DenialOfExistence=%2; DistributeTrustAnchor=%3; DnsKeyRecordSetTtl=%4; DSRecordGenerationAlgorithm=%5; DSRecordSetTtl=%6; EnableRfc5011KeyRollover=%7; IsKeyMasterServer=%8; KeyMasterServer=%9; NSec3HashAlgorithm=%10; NSec3Iterations=%11; NSec3OptOut=%12; NSec3RandomSaltLength=%13; NSec3UserSalt=%14; ParentHasSecureDelegation=%15; PropagationTime=%16; SecureDelegationPollingPeriod=%17; SignatureInceptionOffset=%18. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`526` | The zone %1 was unsigned. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`527` | The zone %1 was re-signed with following properties: DenialOfExistence=%2; DistributeTrustAnchor=%3; DnsKeyRecordSetTtl=%4; DSRecordGenerationAlgorithm=%5; DSRecordSetTtl=%6; EnableRfc5011KeyRollover=%7; IsKeyMasterServer=%8; KeyMasterServer=%9; NSec3HashAlgorithm=%10; NSec3Iterations=%11; NSec3OptOut=%12; NSec3RandomSaltLength=%13; NSec3UserSalt=%14; ParentHasSecureDelegation=%15; PropagationTime=%16; SecureDelegationPollingPeriod=%17; SignatureInceptionOffset=%18. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`528` | Rollover was started on the type %1 with GUID %2 of zone %3. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`529` | Rollover was completed on the type %1 with GUID %2 of zone %3. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`530` | The type %1 with GUID %2 of zone %3 was marked for retiral. The key will be removed after the rollover completion. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`531` | Manual rollover was triggered on the type %1 with GUID %2 of zone %3. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`533` | The keys signing key with GUID %1 on zone %2 that was waiting for a Delegation Signer(DS) update on the parent has been forced to move to rollover completion. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`534` | DNSSEC setting metadata was exported %1 key signing key metadata from zone %2. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`535` | DNSSEC setting metadata was imported on zone %1. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`536` | A record of type %1, QNAME %2 was purged from scope %3 in cache. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`537` | The forwarder list on scope %2 has been reset to %1. | `SETTING_MODIFICATION` | `target.resource.name` is set to "`Forwarder list on scope: %{scope_name}`"  
`540` | The root hints have been modified. | `SETTING_MODIFICATION` | `target.resource.name` populated with text "`Root hints`"  
`541` | The setting %1 on scope %2 has been set to %3. | `SETTING_MODIFICATION` |   
`542` | The scope %1 of DNS server was created. | `SETTING_CREATION` |   
`543` | The scope %1 of DNS server was deleted. | `SETTING_DELETION` |   
`544` | The DNSKEY with Key Protocol %2, Base64 Data %4 and Crypto Algorithm %5 has been added at the trust point %1. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`545` | The DS with Key Tag: %2, Digest Type: %3, Digest: %5 and Crypto Algorithm: %6 has been added at the trust point %1. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`546` | The trust point at %1 of type %2 has been removed. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`547` | The trust anchor for the root zone has been added. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`548` | A request to restart the DNS server service has been received. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`549` | The debug logs have been cleared from %1 on DNS server. | `SYSTEM_AUDIT_LOG_WIPE` |   
`550` | The in-memory contents of all the zones on DNS server have been flushed to their respective files. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`551` | All the statistical data for the DNS server has been cleared. | `SYSTEM_AUDIT_LOG_WIPE` |   
`552` | A resource record scavenging cycle has been started on the DNS Server. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`553` | %1 | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`554` | The resource record scavenging cycle has been terminated on the DNS Server. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`555` | The DNS server has been prepared for demotion by removing references to it from all zones stored in the Active Directory. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`556` | The information about the root hints on the DNS server has been written back to the persistent storage. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`557` | The addresses on which DNS server will listen has been changed to %1. | `SETTING_MODIFICATION` | `target.resource.name` populated with text "`Listen Addresses`"  
`558` | An immediate RFC 5011 active refresh has been scheduled for all trust points. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`559` | The zone %1 is paused. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`560` | The zone %1 is resumed. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`561` | The data for zone %1 has been reloaded from %2. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`562` | The data for zone %1 has been refreshed from the master server %2. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
563 | The secondary zone %1 has been expired and new data has been requested from the master server %2. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`564` | The zone %1 has been reloaded from the Active Directory. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`565` | The content of the zone %1 has been written to the disk and the notification has been sent to all the notify servers. | `SETTING_MODIFICATION` |   
`566` | All DNS records at the node %1 in the zone %2 will have their aging time stamp set to the current time.%3 | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`567` | The Active Directory-integrated zone %1 has been updated. Only %2 can run scavenging. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`568` | The key master role for zone %1 has been %2.%3 | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`569` | A %1 singing key (%2) descriptor has been added on the zone %3 with following properties: KeyId=%4; KeyType=%5; CurrentState=%6; KeyStorageProvider=%7; StoreKeysInAD=%8; CryptoAlgorithm=%9; KeyLength=%10; DnsKeySignatureValidityPeriod=%11; DSSignatureValidityPeriod=%12; ZoneSignatureValidityPeriod=%13; InitialRolloverOffset=%14; RolloverPeriod=%15; RolloverType=%16; NextRolloverAction=%17; LastRolloverTime=%18; NextRolloverTime=%19; CurrentRolloverStatus=%20; ActiveKey=%21; StandbyKey=%22; NextKey=%23. The zone will be resigned with the %2 generated with these properties. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`570` | A %1 singing key (%2) descriptor with GUID %3 has been updated on the zone %4. The properties of this %2 descriptor have been set to: KeyId=%5; KeyType=%6; CurrentState=%7; KeyStorageProvider=%8; StoreKeysInAD=%9; CryptoAlgorithm=%10; KeyLength=%11; DnsKeySignatureValidityPeriod=%12; DSSignatureValidityPeriod=%13; ZoneSignatureValidityPeriod=%14; InitialRolloverOffset=%15; RolloverPeriod=%16; RolloverType=%17; NextRolloverAction=%18; LastRolloverTime=%19; NextRolloverTime=%20; CurrentRolloverStatus=%21; ActiveKey=%22; StandbyKey=%23; NextKey=%24. The zone will be resigned with the %2 generated with these properties. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`571` | A %1 singing key (%2) descriptor %4 has been removed from the zone %3. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`572` | The state of the %1 signing key (%2) %3 has been modified on zone %4. The new active key is %5, standby key is %6 and next key is %7. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`573` | A delegation for %1 in the scope %2 of zone %3 with the name server %4 has been added. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`574` | The client subnet record with name %1 value %2 has been added to the client subnet map. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`575` | The client subnet record with name %1 has been deleted from the client subnet map. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`576` | The client subnet record with name %1 has been updated from the client subnet map. The new client subnets that it refers to are %2. | `SYSTEM_AUDIT_LOG_UNCATEGORIZED` |   
`577` | A server level policy %6 for %1 has been created on server %2 with following properties: ProcessingOrder:%3; Criteria:%4; Action:%5. | `SETTING_CREATION` |   
`578` | A zone level policy %8 for %1 has been created on zone %6 on server %2 with following properties: ProcessingOrder:%3; Criteria:%4; Action:%5; Scopes:%7. | `SETTING_CREATION` |   
`579` | A forwarding policy %6 has been created on server %2 with following properties: ProcessingOrder:%3; Criteria:%4; Action:%5; Scope:%1. | `SETTING_CREATION` |   
`580` | The server level policy %1 has been deleted from server %2. | `SETTING_DELETION` |   
`581` | The zone level policy %1 has been deleted from zone %3 on server %2. | `SETTING_DELETION` |   
`582` | The forwarding policy %1 has been deleted from server %2. | `SETTING_DELETION` |   
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-19 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-19 UTC."],[],[]] 
