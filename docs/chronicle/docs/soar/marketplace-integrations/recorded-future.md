---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/recorded-future/
title: Recorded Future \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:54.107110+00:00
---

# Recorded Future  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/recorded-future/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Recorded Future

This document provides guidance on how to integrate Recorded Future with Google SecOps.

## Use Cases

  1. Vulnerability Prioritization.
  2. Threat Indicator Investigation, Enrichment, and Response.



## Configure Recorded Future to work with Google Security Operations

### Product Permission

An API Token is used for authentication which is user specific and tied to the users' enterprise deployment.

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apitoken  
**Note:** For detailed information on API tokens, see the [Recorded Future's API Documentation](https://api.recordedfuture.com/v2/).

## Configure Recorded Future integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Url | Sring | https://api.recordedfuture.com | Yes | Address of the Recorded Futureinstance.  
API Key | String | N/A | Yes | Generated in Recorded Future's console.  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your Recorded Future connection requires an SSL verification.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Enrich IOC

#### Description

Fetch information about multiple entities, with different types, from Google SecOps.

**Note:** We recommend using this action first, and then, if additional information is needed - use the other enrich methods.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Risk Score Threshold | Integer | 25 | Yes | Represents the minimum malicious risk score for each entity to be marked is suspicious.  
  
#### Run On

Action should take each one of the following entities and send them to enrichment with recorded future:

  * IP Address
  * URL
  * Filehash
  * CVE
  * DOomain



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
isSuspicious | If exceeds threshold parameter | When available in JSON  
RF_id | Results[ ].Entity.id | When available in JSON  
RF_name | Results[ ].Entity.name | When available in JSON  
RF_type | Results[ ].Entity.type | When available in JSON  
RF_descrription | Results[ ].Entity.description | When available in JSON  
RF_risk_level | Results[ ].Risk.level | When available in JSON  
RF_risk_score | Results[ ].Risk.score | When available in JSON  
RF_number_of_matched_rules | Results[ ].Risk.Rule.count | When available in JSON  
RF_most_critical_rule | Results[ ].Risk.Rule.mostCritical | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "results": [
                {
                    "entity": {
                        "id": "J_IWqd",
                        "name": "CVE-2012-1723",
                        "type": "CyberVulnerability",
                        "description": "Unspecified vulnerability in the Java Runtime Environment (JRE) component in Oracle Java SE 7 update 4 and earlier, 6 update 32 and earlier, 5 update 35 and earlier, and 1.4.2_37 and earlier allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors related to Hotspot."
                    },
                    "risk": {
                        "level": 5.0,
                        "rule": {
                            "count": 9,
                            "mostCritical": "Exploited in the Wild by Recently Active Malware",
                            "maxCount": 22,
                            "evidence": {
                                "linkedToCyberExploit": {
                                    "count": 55.0,
                                    "timestamp": "2019-06-18T13:19:28.000Z",
                                    "description": "2682 sightings on 55 sources including: Guided Collection, fakegogle.blogspot.com, netdna-cdn.com, GitHub, Ver007 APT Tools. Most recent tweet: KAV/Checkpoint CVE-2012-1723 Generic Exploit Kit. Most recent link (Jun 18, 2019): https://twitter.com/EskimoTrolled/statuses/1140972295894249472",
                                    "rule": "Linked to Historical Cyber Exploit",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "recentMalwareActivity": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-07T00:00:00.000Z",
                                    "description": "66 sightings on 1 source: Recorded Future Malware Hunting. Activity seen on 12 out of the last 28 days with 255 all-time daily sightings. Exploited in the wild by 11 malware families including <e id=LXUcJk>ExpJava</e>, <e id=K05qo4>JavaKC</e>, <e id=KeKuaF>Maljava</e>. Last observed on Oct 7, 2020. Sample hash: <e id=hash:7c0ed2b98af4076c64ec84f7ea38b05ea2432ec0337b963756ffced54a6f69c4>7c0ed2b98af4076c64ec84f7ea38b05ea2432ec0337b963756ffced54a6f69c4</e>.",
                                    "rule": "Exploited in the Wild by Recently Active Malware",
                                    "mitigation": "",
                                    "level": 5.0
                                },
                                "linkedToRAT": {
                                    "count": 26.0,
                                    "timestamp": "2020-08-03T00:00:00.000Z",
                                    "description": "174 sightings on 26 sources including: Guided Collection, GitHub, medium.com, MarketWatch, SYS-CON Media. 4 related malwares: Uroburos Rootkit, Blackhole, Icefog, Zeroaccess. Most recent link (Aug 3, 2020): https://reportcybercrime.com/the-epic-turla-snake-uroburos-attacks/",
                                    "rule": "Historically Linked to Remote Access Trojan",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "linkedToExploitKit": {
                                    "count": 13.0,
                                    "timestamp": "2019-07-30T01:01:59.793Z",
                                    "description": "62 sightings on 13 sources including: Guided Collection, medium.com, GitHub, Avast Blog, TechNet Blogs. 12 related malwares including Nuclear Pack Exploit Kit, Blackhole, Angler Exploit Kit, Blacole, Egypack. Most recent link (Jul 30, 2019): http://blog.malwaremustdie.org/2012/09/monitoring-blackhole-exploit-kit.html",
                                    "rule": "Historically Linked to Exploit Kit",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "nistCritical": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-01T03:03:20.930Z",
                                    "description": "1 sighting on 1 source: Recorded Future Vulnerability Analysis. CVSS v2 Score (10) calculated using NIST reported CVSS Base Score (10) and Recorded Future Temporal Metrics. Base vector string: AV:N/AC:L/Au:N/C:C/I:C/A:C. Temporal vector string: E:H/RL:X/RC:C.",
                                    "rule": "NIST Severity: Critical",
                                    "mitigation": "",
                                    "level": 4.0
                                },
                                "pocVerifiedRemote": {
                                    "count": 1.0,
                                    "timestamp": "2012-07-11T00:00:00.000Z",
                                    "description": "1 sighting on 1 source: ExploitDB. 1 execution type: Remote. Most recent link (Jul 11, 2012): https://www.exploit-db.com/exploits/19717",
                                    "rule": "Historical Verified Proof of Concept Available Using Remote Execution",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "linkedToIntrusionMethod": {
                                    "count": 9.0,
                                    "timestamp": "2019-06-18T13:19:28.000Z",
                                    "description": "140 sightings on 9 sources including: fakegogle.blogspot.com, Guided Collection, GitHub, McAfee, @xjfftw. 16 related malwares including BrobanDel, Fanny Worm, Ransomware, Banking Trojan, Artemis. Most recent tweet: @PortSwigger Was wondering if you knew why @Virustotal was flagging BS Pro on multiple AVs when scanning the unpacked JAR? KAV/Checkpoint CVE-2012-1723 Generic Exploit Kit. Most recent link (Jun 18, 2019): https://twitter.com/EskimoTrolled/statuses/1140972295894249472",
                                    "rule": "Historically Linked to Malware",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "linkedToRecentCyberExploit": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-05T17:19:29.000Z",
                                    "description": "35 sightings on 1 source: VirusTotal. Most recent link (Oct 5, 2020): https://www.virustotal.com/gui/file/1a3fa1cac28dffe79752df9bc92932d8b40b6d562d98e3315af7875d2f944edf/",
                                    "rule": "Linked to Recent Cyber Exploit",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "scannerUptake": {
                                    "count": 5.0,
                                    "timestamp": "2019-10-01T02:58:24.000Z",
                                    "description": "29 sightings on 5 sources: Guided Collection, GitHub, VirusTotal, ReversingLabs, PasteBin. Most recent link (Oct 1, 2019): https://www.virustotal.com/gui/file/911c69c02f5194ccbb5703869c4478e7ff68232ebb78affe98cb86de5b146b20",
                                    "rule": "Historically Linked to Penetration Testing Tools",
                                    "mitigation": "",
                                    "level": 1.0
                                }
                            },
                            "summary": [
                                {
                                    "count": 1.0,
                                    "level": 2.0
                                },
                                {
                                    "count": 1.0,
                                    "level": 5.0
                                },
                                {
                                    "count": 1.0,
                                    "level": 4.0
                                },
                                {
                                    "count": 6.0,
                                    "level": 1.0
                                }
                            ]
                        },
                        "context": {
                            "malware": {
                                "rule": {
                                    "count": 1,
                                    "maxCount": 2
                                },
                                "score": 90.0
                            },
                            "public": {
                                "rule": {
                                    "maxCount": 22
                                },
                                "summary": [
                                    {
                                        "count": 1.0,
                                        "level": 2.0
                                    },
                                    {
                                        "count": 1.0,
                                        "level": 5.0
                                    },
                                    {
                                        "count": 1.0,
                                        "level": 4.0
                                    },
                                    {
                                        "count": 6.0,
                                        "level": 1.0
                                    }
                                ],
                                "mostCriticalRule": "Exploited in the Wild by Recently Active Malware",
                                "score": 99.0
                            }
                        },
                        "score": 99.0
                    }
                },
                {
                    "entity": {
                        "id": "url:http://www.plexipr.com/vAHzWX.php",
                        "name": "http://www.plexipr.com/vAHzWX.php",
                        "type": "URL"
                    },
                    "risk": {
                        "level": 4.0,
                        "rule": {
                            "count": 3,
                            "mostCritical": "C&C URL",
                            "maxCount": 29,
                            "evidence": {
                                "cncUrl": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-12T02:55:38.670Z",
                                    "description": "1 sighting on 1 source: Abuse.ch: Ransomware C&C URL Blocklist.",
                                    "rule": "C&C URL",
                                    "mitigation": "",
                                    "level": 4.0
                                },
                                "maliciousSiteDetected": {
                                    "count": 1.0,
                                    "timestamp": "2019-09-13T18:53:31.000Z",
                                    "description": "9 sightings on 1 source: Recorded Future URL Analysis.",
                                    "rule": "Historically Detected Malicious Browser Exploits",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "malwareSiteDetected": {
                                    "count": 1.0,
                                    "timestamp": "2019-09-13T18:53:31.000Z",
                                    "description": "9 sightings on 1 source: Recorded Future URL Analysis.",
                                    "rule": "Historically Detected Malware Distribution",
                                    "mitigation": "",
                                    "level": 1.0
                                }
                            },
                            "summary": [
                                {
                                    "count": 1.0,
                                    "level": 4.0
                                },
                                {
                                    "count": 2.0,
                                    "level": 1.0
                                }
                            ]
                        },
                        "context": {
                            "malware": {
                                "rule": {
                                    "count": 0,
                                    "maxCount": 4
                                },
                                "score": 0.0
                            },
                            "public": {
                                "rule": {
                                    "maxCount": 26
                                },
                                "summary": [
                                    {
                                        "count": 1.0,
                                        "level": 4.0
                                    },
                                    {
                                        "count": 2.0,
                                        "level": 1.0
                                    }
                                ],
                                "mostCriticalRule": "C&C URL",
                                "score": 91.0
                            },
                            "c2": {
                                "score": 90.0,
                                "rule": {
                                    "maxCount": 1,
                                    "count": 1
                                }
                            },
                            "phishing": {
                                "score": 0.0,
                                "rule": {
                                    "maxCount": 3,
                                    "count": 0
                                }
                            }
                        },
                        "score": 91.0
                    }
                },
                {
                    "entity": {
                        "id": "hash:44d88612fea8a8f36de82e1278abb02f",
                        "name": "44d88612fea8a8f36de82e1278abb02f",
                        "type": "Hash"
                    },
                    "risk": {
                        "level": 3.0,
                        "rule": {
                            "count": 4,
                            "mostCritical": "Positive Malware Verdict",
                            "maxCount": 13,
                            "evidence": {
                                "linkedToVuln": {
                                    "count": 1.0,
                                    "timestamp": "2019-09-21T12:00:07.000Z",
                                    "description": "1 sighting on 1 source: dfir.pro. 2 related cyber vulnerabilities: CVE-2018-11776, CWE-20. Most recent link (Sep 21, 2019): http://dfir.pro/index.php?link_id=98319",
                                    "rule": "Linked to Vulnerability",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "linkedToVector": {
                                    "count": 2.0,
                                    "timestamp": "2018-08-06T20:50:41.819Z",
                                    "description": "3 sightings on 2 sources: PyPI Recent Updates, Malwr.com. 2 related attack vectors: ShellCode, Phishing. Most recent link (Aug 6, 2018): https://pypi.org/project/python-virustotal/0.0.1a0/",
                                    "rule": "Linked to Attack Vector",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "linkedToMalware": {
                                    "count": 4.0,
                                    "timestamp": "2020-10-02T14:11:26.000Z",
                                    "description": "40 sightings on 4 sources: GitHub, PyPI Recent Updates, VirusTotal, Malwr.com. 3 related malwares: EICAR-AV-Test, Eicar_test_file, EICAR Test String. Most recent link (Oct 2, 2020): https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/",
                                    "rule": "Linked to Malware",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "positiveMalwareVerdict": {
                                    "count": 4.0,
                                    "timestamp": "2020-10-10T00:34:03.497Z",
                                    "description": "21 sightings on 4 sources: VirusTotal, Malwr.com, ReversingLabs, PolySwarm. Most recent link (Apr 8, 2020): https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                                    "rule": "Positive Malware Verdict",
                                    "mitigation": "",
                                    "level": 3.0
                                }
                            },
                            "summary": [
                                {
                                    "count": 3.0,
                                    "level": 2.0
                                },
                                {
                                    "count": 1.0,
                                    "level": 3.0
                                }
                            ]
                        },
                        "context": {
                            "malware": {
                                "rule": {
                                    "count": 1,
                                    "maxCount": 2
                                },
                                "score": 80.0
                            },
                            "public": {
                                "rule": {
                                    "maxCount": 11
                                },
                                "summary": [
                                    {
                                        "count": 3.0,
                                        "level": 2.0
                                    },
                                    {
                                        "count": 1.0,
                                        "level": 3.0
                                    }
                                ],
                                "mostCriticalRule": "Positive Malware Verdict",
                                "score": 83.0
                            }
                        },
                        "score": 83.0
                    }
                },
                {
                    "entity": {
                        "id": "ip:66.240.205.34",
                        "name": "66.240.205.34",
                        "type": "IpAddress"
                    },
                    "risk": {
                        "level": 2.0,
                        "rule": {
                            "count": 13,
                            "mostCritical": "Recent Multicategory Blacklist",
                            "maxCount": 53,
                            "evidence": {
                                "cncServer": {
                                    "count": 1.0,
                                    "timestamp": "2020-09-23T01:46:30.620Z",
                                    "description": "17 sightings on 1 source: GitHub. Most recent link (Jul 23, 2019): https://gist.github.com/techhelplist/2a208ae6fc9859f2ff3282d3ff893b46",
                                    "rule": "Historical C&C Server",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "recentMultiBlacklist": {
                                    "count": 2.0,
                                    "timestamp": "2020-10-08T01:30:47.833Z",
                                    "description": "13 sightings on 2 sources: AbuseIP Database, AlienVault: IP Reputation Data. Most recent link (Oct 7, 2020): https://www.abuseipdb.com/check/66.240.205.34",
                                    "rule": "Recent Multicategory Blacklist",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "honeypot": {
                                    "count": 8.0,
                                    "timestamp": "2020-06-19T00:58:26.000Z",
                                    "description": "979 sightings on 8 sources including: @atma_es, @WebironBots, @gosint2, @HoneyFog, @HoneyPyLog. Most recent tweet: BFB-attack detected from 66.240.205.34 to Portscan on 19.06.2020 02:58:19. Most recent link (Jun 19, 2020): https://twitter.com/EIS_BFB/statuses/1273782158067404803",
                                    "rule": "Historical Honeypot Sighting",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "linkedIntrusion": {
                                    "count": 4.0,
                                    "timestamp": "2019-08-05T19:06:11.000Z",
                                    "description": "37 sightings on 4 sources: GitHub, Recorded Future URL Analysis, ReversingLabs, @EIS_BFB. 5 related intrusion methods: Browser Targeted Code Injection, Web Application Exploitation, Brute Force Blocking (BFB), Cross site scripting, Trojan. Most recent tweet: BFB-attack detected from 66.240.205.34 to Portscan on 05.08.2019 21:06:05.",
                                    "rule": "Historically Linked to Intrusion Method",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "recentDhsAis": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-09T12:44:44.895Z",
                                    "description": "3 sightings on 1 source: DHS Automated Indicator Sharing. 3 reports including NCCIC:STIX_Package-00e3c8ca-0a3c-4a70-9edc-534ea7b51474, from Infoblox Inc, Information Technology Sector, NCCIC:STIX_Package-00e3c8ca-0a3c-4a70-9edc-534ea7b51474 (Oct 9, 2020).",
                                    "rule": "Recently Reported by DHS AIS",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "linkedToCyberAttack": {
                                    "count": 2.0,
                                    "timestamp": "2019-06-15T09:01:52.000Z",
                                    "description": "483 sightings on 2 sources: @HoneyPyLog, @EIS_BFB. Most recent tweet: honeydbz: #Citrix-ICA-Browser Possible Citrix-ICA-Browser attack from 66.240.205.34 https://t.co/Wpmfyo4di1. Most recent link (Jun 15, 2019): https://twitter.com/HoneyPyLog/statuses/1139820304996478976",
                                    "rule": "Historically Linked to Cyber Attack",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "dhsAis": {
                                    "count": 1.0,
                                    "timestamp": "2020-09-14T11:12:55.000Z",
                                    "description": "22 sightings on 1 source: DHS Automated Indicator Sharing. 22 reports including NCCIC:STIX_Package-427425f9-cd82-49bc-a4b4-c609aaeddd7d, from Infoblox Inc, Information Technology Sector, NCCIC:STIX_Package-427425f9-cd82-49bc-a4b4-c609aaeddd7d (Sep 14, 2020).",
                                    "rule": "Historically Reported by DHS AIS",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "recentLinkedIntrusion": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-11T22:30:12.000Z",
                                    "description": "14 sightings on 1 source: Recorded Future URL Analysis. 3 related intrusion methods: Browser Targeted Code Injection, Web Application Exploitation, Cross site scripting.",
                                    "rule": "Recently Linked to Intrusion Method",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "historicalThreatListMembership": {
                                    "count": 2.0,
                                    "timestamp": "2020-10-11T23:18:11.344Z",
                                    "description": "Previous sightings on 2 sources: University of Science and Technology of China Black IP List, Project Turris Attempted Access Greylist. Observed between Jul 1, 2019, and Jan 28, 2020.",
                                    "rule": "Historically Reported in Threat List",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "rfTrending": {
                                    "count": 1.0,
                                    "timestamp": "2020-08-03T15:09:58.796Z",
                                    "description": "1 sighting on 1 source: Recorded Future Analyst Community Trending Indicators. Recently viewed by many analysts in many organizations in the Recorded Future community.",
                                    "rule": "Trending in Recorded Future Analyst Community",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "maliciousPacketSource": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-11T23:18:11.344Z",
                                    "description": "1 sighting on 1 source: CINS: CI Army List.",
                                    "rule": "Malicious Packet Source",
                                    "mitigation": "",
                                    "level": 2.0
                                },
                                "multiBlacklist": {
                                    "count": 1.0,
                                    "timestamp": "2017-04-28T10:00:20.345Z",
                                    "description": "7 sightings on 1 source: AbuseIP Database. Most recent link (Apr 28, 2017): https://www.abuseipdb.com/check/66.240.205.34?page=10",
                                    "rule": "Historical Multicategory Blacklist",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "spam": {
                                    "count": 1.0,
                                    "timestamp": "2019-04-16T13:04:45.428Z",
                                    "description": "284 sightings on 1 source: Daily Botnet Statistics. Most recent link (Apr 16, 2019): http://botnet-tracker.blogspot.com/2019/04/suspected-bot-list-2019-04-06.html",
                                    "rule": "Historical Spam Source",
                                    "mitigation": "",
                                    "level": 1.0
                                }
                            },
                            "summary": [
                                {
                                    "count": 4.0,
                                    "level": 2.0
                                },
                                {
                                    "count": 9.0,
                                    "level": 1.0
                                }
                            ]
                        },
                        "context": {
                            "public": {
                                "rule": {
                                    "maxCount": 50
                                },
                                "summary": [
                                    {
                                        "count": 3.0,
                                        "level": 2.0
                                    },
                                    {
                                        "count": 9.0,
                                        "level": 1.0
                                    }
                                ],
                                "mostCriticalRule": "Recent Multicategory Blacklist",
                                "score": 59.0
                            },
                            "c2": {
                                "score": 0.0,
                                "rule": {
                                    "maxCount": 2,
                                    "count": 0
                                }
                            },
                            "phishing": {
                                "score": 0.0,
                                "rule": {
                                    "maxCount": 1,
                                    "count": 0
                                }
                            }
                        },
                        "score": 59.0
                    }
                },
                {
                    "entity": {
                        "id": "idn:passbolt.siemplify.co",
                        "name": "passbolt.siemplify.co",
                        "type": "InternetDomainName"
                    },
                    "risk": {
                        "level": 0.0,
                        "rule": {
                            "count": 0,
                            "mostCritical": "",
                            "summary": [],
                            "maxCount": 47
                        },
                        "context": {
                            "malware": {
                                "rule": {
                                    "count": 0,
                                    "maxCount": 2
                                },
                                "score": 0.0
                            },
                            "public": {
                                "rule": {
                                    "maxCount": 41
                                },
                                "summary": [],
                                "mostCriticalRule": "",
                                "score": 0.0
                            },
                            "c2": {
                                "score": 0.0,
                                "rule": {
                                    "maxCount": 2,
                                    "count": 0
                                }
                            },
                            "phishing": {
                                "score": 0.0,
                                "rule": {
                                    "maxCount": 2,
                                    "count": 0
                                }
                            }
                        },
                        "score": 0.0
                    }
                },
                {
                    "entity": {
                        "id": "url:http://bolizarsospos.com/703hjdr3ez72",
                        "name": "http://bolizarsospos.com/703hjdr3ez72",
                        "type": "URL"
                    },
                    "risk": {
                        "level": 4.0,
                        "rule": {
                            "count": 3,
                            "mostCritical": "C&C URL",
                            "maxCount": 29,
                            "evidence": {
                                "cncUrl": {
                                    "count": 1.0,
                                    "timestamp": "2020-10-12T02:46:13.823Z",
                                    "description": "1 sighting on 1 source: Abuse.ch: Ransomware C&C URL Blocklist.",
                                    "rule": "C&C URL",
                                    "mitigation": "",
                                    "level": 4.0
                                },
                                "maliciousSiteDetected": {
                                    "count": 1.0,
                                    "timestamp": "2019-12-07T23:10:05.000Z",
                                    "description": "4 sightings on 1 source: Recorded Future URL Analysis.",
                                    "rule": "Historically Detected Malicious Browser Exploits",
                                    "mitigation": "",
                                    "level": 1.0
                                },
                                "malwareSiteDetected": {
                                    "count": 1.0,
                                    "timestamp": "2019-12-07T23:10:05.000Z",
                                    "description": "4 sightings on 1 source: Recorded Future URL Analysis.",
                                    "rule": "Historically Detected Malware Distribution",
                                    "mitigation": "",
                                    "level": 1.0
                                }
                            },
                            "summary": [
                                {
                                    "count": 1.0,
                                    "level": 4.0
                                },
                                {
                                    "count": 2.0,
                                    "level": 1.0
                                }
                            ]
                        },
                        "context": {
                            "malware": {
                                "rule": {
                                    "count": 0,
                                    "maxCount": 4
                                },
                                "score": 0.0
                            },
                            "public": {
                                "rule": {
                                    "maxCount": 26
                                },
                                "summary": [
                                    {
                                        "count": 1.0,
                                        "level": 4.0
                                    },
                                    {
                                        "count": 2.0,
                                        "level": 1.0
                                    }
                                ],
                                "mostCriticalRule": "C&C URL",
                                "score": 91.0
                            },
                            "c2": {
                                "score": 90.0,
                                "rule": {
                                    "maxCount": 1,
                                    "count": 1
                                }
                            },
                            "phishing": {
                                "score": 0.0,
                                "rule": {
                                    "maxCount": 3,
                                    "count": 0
                                }
                            }
                        },
                        "score": 91.0
                    }
                }
            ]
        },
        "counts": {
            "returned": 6,
            "total": 6
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
_If successful and at least one of the provided entities were enriched (is_success = true):_  
Print "Successfully enriched the following entities in Recorded Future: \n {0}".format(entity.identifier list)  
_If fail to enrich specific entities(is_success = true):_  
Print "Action was not able to enrich the following entities in Recorded Future: \n {0}".format([entity.identifier])  
_If no entities were enriched (is_success=false):_**Print "No entities were enriched."**  
**The action should fail and stop a playbook execution:**  
_If not successful:_ Print "Error executing action "Enrich IOC". Reason: {0}''.format(error.Stacktrace)  
_If we get HTTP code 401 - unauthorized:_ Print " Unauthorized - please check your API token and try again" | General  
  
### Enrich CVE

#### Description

The action enables a user to send a CVE to lookup threat intelligence information that summarizes the CVE's reputation.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Risk Score Threshold | String | 25 | Yes | Represents the minimum malicious risk score for a CVE to be marked malicious. The risk score threshold must be a numeric value. Has a range of 0-99. Below is the band levels: Very Malicious: 90-99Malicious: 65-89 Suspicious: 25-64Unusual: 5-24 No Malicious content: 0.  
  
#### Use cases

A security analyst runs a security assessment on their information technology infrastructure. The user discovers from the findings that their information system is vulnerable to an identified vulnerability whose CVE identity is known. The analyst lacks more details on the vulnerability and would like to find out its reputation. The user can use Recorded Future to lookup for the vulnerability's CVE reputation.

#### Run On

This action runs on the CVE entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Last Reference | Returns if it exists in JSON result  
Triggered Rules | Returns if it exists in JSON result  
First Reference | Returns if it exists in JSON result  
Risk Score | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched hash. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious Threshold set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "Last Reference": "2019-10-04T18:19:19.044Z",
                "Triggered Rules": "7/51",
                "First Reference": "16-05-25T11:47:06.812Z",
                "Risk Score": "45"
            },
            "Entity": "CVE-2019-9925"
        }
    ]
    

### Enrich Hash

#### Description

The action enables a user to send a hash to lookup threat intelligence information that summarizes the Hash's reputation.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Risk Score Threshold | String | 25 | Represents the minimum malicious risk score for a CVE to be marked malicious. The risk score threshold must be a numeric value. Has a range of 0-99. Below is the band levels:Very Malicious: 90-99Malicious: 65-89 Suspicious: 25-64 Unusual: 5-24 No Malicious content: 0.  
  
#### Use cases

A file is suspected to be infected with a virus on an endpoint. Using Recorded Future a user sends the files hash where its reputation can be obtained through lookup.

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Last Reference | Returns if it exists in JSON result  
Triggered Rules | Returns if it exists in JSON result  
First Reference | Returns if it exists in JSON result  
Risk Score | Returns if it exists in JSON result  
Hash Algorithm  | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched Hash. The insight will be created when the risk score equals or exceeds the minimum suspicious risk score Threshold.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
         {
             "EntityResult":
             {
                 "Last Reference": "2019-10-04T18:19:19.044Z",
                 "Triggered Rules": "7/51",
                 "First Reference": "16-05-25T11:47:06.812Z",
                 "Risk Score": "45",
                 "Hash Algorithm": "MD5"
             },
             "Entity": "MD5"
         }
    ]
    

### Enrich Host

#### Description

The action enables a user to send a host name to look up for threat intelligence information that summarizes the host's reputation.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Risk Score Threshold | String | 25 | Represents the minimum malicious risk score for a CVE to be marked malicious. The risk score threshold must be a numeric value. Has a range of 0-99. Below is the band levels: Very Malicious: 90-99 Malicious: 65-89 Suspicious: 25-64 Unusual: 5-24 No Malicious content: 0.  
  
#### Use cases

A user receives an email redirecting them to a web domain replica of their own domain. The domain claims to be of their registrar of the domain requesting them to input credentials for access while the fake domain has phishing intent. The user can use Recorded Future to lookup for the domain reputation.

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Last Reference | Returns if it exists in JSON result  
Triggered Rules | Returns if it exists in JSON result  
First Reference | Returns if it exists in JSON result  
Risk Score | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched hash. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious Threshold set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "Last Reference": "2019-10-04T18:19:19.044Z",
                "Triggered Rules": "7/51",
                "First Reference": "16-05-25T11:47:06.812Z",
                "Risk Score": "45",
                "Geo-City": "Beijing",
                "Geo-Country": "China",
                "Org": "DigitalOcean",
                "Asn": "AS393406"
            },
            "Entity": "8.8.8.8"
        }
    ]
    

### Enrich IP

#### Description

The action enables a user to send an IP address to look up threat intelligence information that summarizes the IPs reputation.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Risk Score Threshold | String | 25 | Represents the minimum malicious risk score for a CVE to be marked malicious. The risk score threshold must be a numeric value. Has a range of 0-99. Below is the band levels: Very Malicious: 90-99 Malicious: 65-89 Suspicious: 25-64 Unusual: 5-24 No Malicious content: 0.  
  
#### Use cases

N/A

#### Run On

This action run on the IP Address entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Last Reference | Returns if it exists in JSON result  
Triggered Rules | Returns if it exists in JSON result  
First Reference | Returns if it exists in JSON result  
Risk Score | Returns if it exists in JSON result  
Geo-City | Returns if it exists in JSON result  
Geo-Country | Returns if it exists in JSON result  
Org | Returns if it exists in JSON result  
Asn | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched hash. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious Threshold set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "Last Reference": "2019-10-04T18:19:19.044Z",
                "Triggered Rules": "7/51",
                "First Reference": "16-05-25T11:47:06.812Z",
                "Risk Score": "45",
                "Geo-City": "Beijing",
                "Geo-Country": "China",
                "Org": "DigitalOcean",
                "Asn": "AS393406"
            },
            "Entity": "8.8.8.8"
        }
    ]
    

### Enrich URL

#### Description

The action enables a user to send a URL to look up threat intelligence information that summarizes the URLs reputation.

#### Parameters

Parameters | Type | Default Value | Description  
---|---|---|---  
Risk Score Threshold | string | 25 | Represents the minimum malicious risk score for a CVE to be marked malicious. The risk score threshold must be a numeric value. Has a range of 0-99. Below is the band levels: Very Malicious: 90-99 Malicious: 65-89 Suspicious: 25-64 Unusual: 5-24 No Malicious content: 0.  
  
#### Use cases

A user opens their mailbox and finds a suspicious email with instructions given to them directing them to follow a given URL in order to conduct a crucial password change or software update. The user can use Recorded Future to lookup for the URL reputation.

#### Run On

This action runs on the URL entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Triggered Rules | Returns if it exists in JSON result  
Risk Score | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
**Warn** | A warning insight shall be created to inform on the malicious status of the enriched hash. The insight will be created when the number of detected engines equals or exceeds the minimum suspicious Threshold set before scan.  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_risky | True/False | is_risky:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "Triggered Rules": "7\/51",
                "Risk Score": "45"
            },
            "Entity": "8.8.8.8"
        }
    ]
    

### Get Alert Details

#### Description

Fetch information about specific Alert and return results to the case.

Use action to get more information available regarding Recorded Future Alerts - Documents, Related Entities, Evidence, etc.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert for which you would like to fetch details  
  
#### Run On

This action shouldn't run on entities, and only on Google SecOps TicketId - which will be Recorded future alertID.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "review": {
                "assignee": null,
                "noteAuthor": null,
                "note": null,
                "status": "no-action",
                "noteDate": null
            },
            "entities": [
                {
                    "entity": {
                        "id": "idn:gmail.com.sabsepehlelic.com",
                        "name": "gmail.com.sabsepehlelic.com",
                        "type": "InternetDomainName"
                    },
                    "risk": {
                        "criticalityLabel": "Suspicious",
                        "score": null,
                        "documents": [
                            {
                                "references": [
                                    {
                                        "fragment": "A certificate for the domain gmail.com.sabsepehlelic.com has been registered",
                                        "entities": [
                                            {
                                                "id": "idn:gmail.com.sabsepehlelic.com",
                                                "name": "gmail.com.sabsepehlelic.com",
                                                "type": "InternetDomainName"
                                            }
                                        ],
                                        "language": "eng"
                                    }
                                ],
                                "source": {
                                    "id": "beD_4-",
                                    "name": "New Certificate Registrations",
                                    "type": "Source"
                                },
                                "url": null,
                                "title": "Certificate Registration"
                            }
                        ],
                        "evidence": [
                            {
                                "mitigationString": "",
                                "timestamp": "2020-09-28T02:36:23.924Z",
                                "criticalityLabel": "Suspicious",
                                "evidenceString": "1 sighting on 1 source: New Certificate Registrations. Certificate registered on Sep 28, 2020.",
                                "rule": "Newly Registered Certificate With Potential for Abuse - DNS Sandwich",
                                "criticality": 2
                            },
                            {
                                "mitigationString": "",
                                "timestamp": "2020-09-28T02:36:25.000Z",
                                "criticalityLabel": "Suspicious",
                                "evidenceString": "Identified by Recorded Future as potential typosquatting: DNS Sandwich similarity found between gmail.com.sabsepehlelic.com and 1 possible target: gmail.com.",
                                "rule": "Recent Typosquat Similarity - DNS Sandwich",
                                "criticality": 2
                            }
                        ],
                        "criticality": 2
                    },
                    "trend": {},
                    "documents": []
                },
                {
                    "entity": {
                        "id": "idn:www.gmail.com.sabsepehlelic.com",
                        "name": "www.gmail.com.sabsepehlelic.com",
                        "type": "InternetDomainName"
                    },
                    "risk": {
                        "criticalityLabel": "Suspicious",
                        "score": null,
                        "documents": [
                            {
                                "references": [
                                    {
                                        "fragment": "A certificate for the domain www.gmail.com.sabsepehlelic.com has been registered",
                                        "entities": [
                                            {
                                                "id": "idn:www.gmail.com.sabsepehlelic.com",
                                                "name": "www.gmail.com.sabsepehlelic.com",
                                                "type": "InternetDomainName"
                                            }
                                        ],
                                        "language": "eng"
                                    }
                                ],
                                "source": {
                                    "id": "beD_4-",
                                    "name": "New Certificate Registrations",
                                    "type": "Source"
                                },
                                "url": null,
                                "title": "Certificate Registration"
                            }
                        ],
                        "evidence": [
                            {
                                "mitigationString": "",
                                "timestamp": "2020-09-28T02:36:23.924Z",
                                "criticalityLabel": "Suspicious",
                                "evidenceString": "1 sighting on 1 source: New Certificate Registrations. Certificate registered on Sep 28, 2020.",
                                "rule": "Newly Registered Certificate With Potential for Abuse - DNS Sandwich",
                                "criticality": 2
                            },
                            {
                                "mitigationString": "",
                                "timestamp": "2020-09-28T02:36:25.000Z",
                                "criticalityLabel": "Suspicious",
                                "evidenceString": "Identified by Recorded Future as potential typosquatting: DNS Sandwich similarity found between www.gmail.com.sabsepehlelic.com and 1 possible target: gmail.com.",
                                "rule": "Recent Typosquat Similarity - DNS Sandwich",
                                "criticality": 2
                            }
                        ],
                        "criticality": 2
                    },
                    "trend": {},
                    "documents": []
                }
            ],
            "url": "https://app.recordedfuture.com/live/sc/notification/?id=feRS3x",
            "rule": {
                "url": "https://app.recordedfuture.com/live/sc/ViewIdkobra_view_report_item_alert_editor?view_opts=%7B%22reportId%22%3A%22eOFFb0%22%2C%22bTitle%22%3Atrue%2C%22title%22%3A%22Infrastructure+and+Brand+Risk%2C+Potential+Typosquatting+Watch+List+Domains%22%7D&state.bNavbar=false",
                "name": "Infrastructure and Brand Risk, Potential Typosquatting Watch List Domains",
                "id": "eOFFb0"
            },
            "triggered": "2020-09-28T10:13:40.466Z",
            "id": "feRS3x",
            "counts": {
                "references": 2,
                "entities": 2,
                "documents": 1
            },
            "title": "Infrastructure and Brand Risk, Potential Typosquatting Watch List Domains ...",
            "type": "ENTITY"
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
_if successful (is_success = true):_  
Print "Successfully fetched the following Alert ID details from Recorded Future: \n {0}".format(AlertID)  
**The action should fail and stop a playbook execution:**  
Pay attention - Recorded Future will return 404 code in cases the alert ID wasn't found or missing. But, 404 might also indicate other problems. So:  
If we have a way to differentiate between the cases :

  * If alert id not found - print "Requested Alert ID wasn't found in Recorded Future. Please check the Alert ID and try again"
  * If another http problem occurred - print "Error executing action "Get Alert's Details". Reason: {0}''.format(error.Stacktrace)

If we don't have a way to differentiate between the cases :

  * Print "Requested Alert ID wasn't found in Recorded Future, or something went wrong in executing action "Get Alert's Details". Reason: {0}''.format(error.Stacktrace)

_If we get HTTP code 401 - unauthorized:_ Print " Unauthorized - please check your API token and try again"  
| General  
  
### Get CVE Related Entities

#### Description

The action allows a user to send a CVE to search for all CVE related entities. Very important information, which is raw information that is important for decisions, can be gathered from the context information provided.

#### Parameters

N/A

#### Use cases

During a system vulnerability assessment an analyst realizes that their system is vulnerable to a CVE. The analyst performs a lookup action and the CVE is found malicious. The analyst decides to get related entities information to learn more about the technologies and vectors used by the CVE.

#### Run On

This action runs on the CVE entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_successful | True/False | is_successful:False  
  
### Get Hash Related Entities

#### Description

Query the RecordedFuture to get related entities for the Hash.

#### Parameters

N/A

#### Use cases

A user identifies a malicious hash in one of the endpoints' antivirus quarantine at their organization. The would like to get more information concerning the hash that can assist them with coming up with a way to mitigate it. Using Recorded future he can get more threat information on it.

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_successful | True/False | is_successful:False  
  
### Get Host Related Entities

#### Description

The action enables a user to send a host to look up all entities related to the host. Very important information can be gathered from the context information provided which is raw information that is important for decision making.

#### Parameters

N/A

#### Use cases

A user identifies a malicious hash in one of the endpoints antivirus quarantine at their organization. the user would like to get more information concerning the hash that can assist him coming up with a way to mitigate it. Using Recorded Future he can get more threat information on it.

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_successful | True/False | is_successful:False  
  
### Get IP Related Entities

#### Description

The action enables a user to send an IP address to look up for all entities related to the IP. The information gathered enables a user to acquire vital insights as to who is attacking them, what their motivation and capabilities are, and what indicators of compromises are in your systems. Through the information a user can make an informed decision on security.

#### Parameters

N/A

#### Use cases

A WAF (Web Application Firewall) makes a log entry for suspicious web traffic from an IP address. Once the log entry is acknowledged by the analyst, the IP address is sent for enrichment by Recorded Future in an effort to find its reputation. If the IP was found risky the playbook will block the IP.

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_successful | True/False | is_successful:False  
  
### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_successful | True/False | is_successful:False  
  
### Add Analyst Note

#### Description

Add an analyst note to previously enriched entities in Google SecOps, to Recorded Future entities. Action will add the note to the relevant scope entities.

**Note:** If entity will not contain the Recorded Future ID field - this action will perform "Enrich IOC" action on it for better results. You can choose whether to update the entity with the enrichment data or not. For more information you can refer to "Recorded Future API UI" - [Here](https://api.recordedfuture.com/v2/?soar=true#!/Analyst32Notes/Publish_Analyst_Note)

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Note Title | String | Note Title | Yes | Specify the title for the note  
Note Text | String | Note Text | Yes | Specify the Text for the note  
Note Source | String | N/A | Yes | Specify the RF ID for note source; the API explorer shows what RF IDs are accessible to the user whose API token is enabled. For example, VWKdVr is the RF ID for an analyst note and is only available to user in the same enterprise account in Recorded Future.   
  
Topic | DDL(see table below) | None | No | Specify the relevant Note topic from the list, if needed.  
Enrich Entity? | Checkbox | Checked | Yes | Specify whether the action should enrich the entity with the "Enrich IOC" output.  
  
**DDL Values for the "Topic" field**

**Display text** | **String to send in the request**  
---|---  
None (default) | Send nothing  
Actor Profile | TXSFt2  
Analyst On-Demand Report | VlIhvH  
Cyber Threat Analysis | TXSFt1  
Flash Report | TXSFt0  
Indicator | TXSFt4  
Informational | UrMRnT  
Malware/Tool Profile | UX0YlU  
Source Profile | UZmDut  
Threat Lead | TXSFt3  
Validated Intelligence Event | TXSFt5  
Weekly Threat Landscape | VlIhvG  
YARA Rule | VTrvnW  
  
##### Run On

This action runs on the following entity types:

  * IP Address
  * URL
  * Filehash
  * CVE
  * Domain



##### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
RF_doc_id | When available in JSON.  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if at least one of the provided entities was found in RF, or already had an RF ID, and note added successfully:**  
"Successfully published analyst note with the following entities in Recorded Future: (entity.identifier list)  
**If couldn't find at least one entity on Recorded Future when running Enrich IOC,:** "Following entities does not exist in Recorded Future -{non_existing_entities}  
**The action should fail :****If no entities had an RF_ID , and they weren't found in enrich IOC:** "Recorded Future couldn't find any of the entities provided in the "Enrich IOC", and thus, couldn't publish the analyst note."  
  
**The action should fail and stop a playbook execution:**  
**if not successful:** print "Error executing action "Publish Analyst Note". Reason: (error.Stacktrace)  
**If we get HTTP code 401 - unauthorized -** " Unauthorized - please check your API token and try again" | General  
  
### Update Alert

#### Description

Update alert in Recorded Future.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert that needs to be updated.  
Status | DDL | Select OnePossible Values:UnassignedAssignedPendingDismissedNewResolvedFlag For Tuning | No | Specify the new status for the alert.  
Assign To | String |  | No | Specify to whom to assign the alert. You can provide id, username, user hash, or email.  
Note | String |  |  | Specify a note that should be updated on the alert.  
  
##### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if updated (is_success = true):** "Successfully updated alert {id} in Recorded Future.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Update Alert". Reason: {0}''.format(error.Stacktrace)  
******If error list is not empty:** "Error executing action "Update Alert". Reason: {0}''.format(error/reason)  
******If Status is "Select One" and none of the other values are provided:** "Error executing action "Update Alert". Reason: at least one of the action parameters should have a provided value.  | General  
  
## Connectors

### Recorded Future - Security Alerts Connector

#### Description

Pull security alerts from Recorded Future.

Whitelist and blacklist work with Recorded Future rule names.

#### Configure Recorded Future - Security Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | title | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | ID | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name  
| String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API URL | String | https://api.recordedfuture.com | Yes | API Root of the Recorded Future instance.  
API Key | Password | N/A | Yes | API Key of the Recorded Future.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch events.  
Max Alerts To Fetch | Integer | 100 | No | How many alerts to process per one connector iteration.  
Severity | String | Medium | Yes | Severity will be one from the following values Low, Medium, High, Critical.  
Will be assigned to Google SecOps alerts created from this connector.   
Get Alert's Details | Checkbox | Unchecked | Yes | Get alert's full details from Recorded Future.  
Note: each query "costs" 1 Recorded Future API credit.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Recorded Future server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
