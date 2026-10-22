---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/nmap/
title: Integrate Nmap with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:05.390585+00:00
---

# Integrate Nmap with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/nmap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Nmap with Google SecOps

This document explains how to integrate Nmap with Google Security Operations.

**Note:** The Nmap integration is designed exclusively for Remote Agents and Nmap capabilities that require root permissions aren't supported.

## Integration parameters

The Nmap integration requires no parameters.

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Nmap. 

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Nmap server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Nmap server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Scan Entities

Use the **Scan Entities** action to scan Google SecOps entities using Nmap.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Hostname`
  * `Domain`



#### Action inputs

The **Scan Entities** action requires the following parameters:

Parameter | Description  
---|---  
`IP Address` | Optional. The IP addresses to scan. These IP addresses are processed alongside entities.  
`Hostname` | Optional. The hostnames to scan. These hostnames are processed alongside entities.  
`Options` | Required. Specifies the Nmap scan parameters. The default value is `-sT -sV -p- -T4 -v`. These options initiate a TCP connect scan (`-sT`), enable version detection (`-sV`), scan all 65,535 ports (`-p-`), use an aggressive timing template (`-T4`), and increase verbosity (`-v`).  
  
#### Action outputs

The **Scan Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The **Scan Entities** action supports the following entity enrichment:

Enrichment field | Source (JSON key) | Logic  
---|---|---  
`NMAP_state` | `status_state` | When available  
`NMAP_related_addresses_{addrtype}` | For each `addrtype`, provide a comma-separated list of `{addr}` values. | When available  
`NMAP_related_hostnames` | `hostnames.name` | When available  
`NMAP_port_{ports.portid}` | `{ports.state.state}` \- `{ports.service.product}` This entry dynamically creates a field for each detected port, displaying its state (e.g., open, closed) and the service running on it. | When available  
`NMAP_os_matches` | CSV of `{os.osmatches.name}` | When available  
`NMAP_last_boot` | `{uptime.lastboot}` | When available  
  
##### JSON result

The following example shows the JSON result output received when using the **Scan Entities** action:
    
    
    [
      {
          "Entity": "50.116.62.192",
          "EntityResult": {
              "status": {
                  "state": "up",
                  "reason": "syn-ack",
                  "reason_ttl": "0"
              },
              "addresses": [
                  {
                      "addr": "50.116.62.192",
                      "addrtype": "ipv4"
                  }
              ],
              "hostnames": [
                  {
                      "name": "k3s-agent1.hegedus.wtf",
                      "type": "PTR"
                  }
              ],
              "ports": {
                  "extraports": [
                      {
                          "state": "closed",
                          "count": "996",
                          "reasons": [
                              {
                                  "reason": "conn-refused",
                                  "count": "996"
                              }
                          ]
                      }
                  ],
                  "ports": [
                      {
                          "protocol": "tcp",
                          "portid": "80",
                          "status": {state.state},
                          "service_name": {service.name},
                          "state": {
                              "state": "open",
                              "reason": "syn-ack",
                              "reason_ttl": "0"
                          },
                          "service": {
                              "name": "http",
                              "servicefp": "SF-Por\r\\n400\\x20Bad\\x20Request\");",
                              "method": "table",
                              "conf": "3"
                          }
                      },
                      {
                          "protocol": "tcp",
                          "portid": "443",
                          "state": {
                              "state": "open",
                              "reason": "syn-ack",
                              "reason_ttl": "0"
                          },
                          "service": {
                              "name": "https",
                              "servicefp": 
    "SF-Port443-TCP:V=6.40%I=7%D=5/23%Time=68305D69%P=x86_64-redhat-linux-gnu%r(HTTPOptions,B0,\"HTTP/1\\.0\\x20404\\x20Not\\x20Found\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nX-Content-Type-Options:\\x20nosniff\\r\\nDate:\\x20Fri,\\x2023\\x20May\\x202025\\x2011:35:05\\x20GMT\\r\\nContent-Length:\\x2019\\r\\n\\r\\n404\\x20page\\x20not\\x20found\\n\")%r(SSLSessionReq,7,\"\\x15\\x03\\x01\\0\\x02\\x02F\")%r(SSLv23SessionReq,7,\"\\x15\\x03\\x01\\0\\x02\\x02F\")%r(GenericLines,67,\"HTTP/1\\.1\\x20400\\x20Bad\\x20Request\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nConnection:\\x20close\\r\\n\\r\\n400\\x20Bad\\x20Request\")%r(GetRequest,B0,\"HTTP/1\\.0\\x20404\\x20Not\\x20Found\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nX-Content-Type-Options:\\x20nosniff\\r\\nDate:\\x20Fri,\\x2023\\x20May\\x202025\\x2011:35:16\\x20GMT\\r\\nContent-Length:\\x2019\\r\\n\\r\\n404\\x20page\\x20not\\x20found\\n\")%r(RTSPRequest,67,\"HTTP/1\\.1\\x20400\\x20Bad\\x20Request\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nConnection:\\x20close\\r\\n\\r\\n400\\x20Bad\\x20Request\")%r(RPCCheck,7,\"\\x15\\x03\\x01\\0\\x02\\x02F\")%r(Help,67,\"HTTP/1\\.1\\x20400\\x20Bad\\x20Request\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nConnection:\\x20close\\r\\n\\r\\n400\\x20Bad\\x20Request\")%r(Kerberos,67,\"HTTP/1\\.1\\x20400\\x20Bad\\x20Request\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nConnection:\\x20close\\r\\n\\r\\n400\\x20Bad\\x20Request\")%r(FourOhFourRequest,B0,\"HTTP/1\\.0\\x20404\\x20Not\\x20Found\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nX-Content-Type-Options:\\x20nosniff\\r\\nDate:\\x20Fri,\\x2023\\x20May\\x202025\\x2011:35:32\\x20GMT\\r\\nContent-Length:\\x2019\\r\\n\\r\\n404\\x20page\\x20not\\x20found\\n\")%r(LPDString,67,\"HTTP/1\\.1\\x20400\\x20Bad\\x20Request\\r\\nContent-Type:\\x20text/plain;\\x20charset=utf-8\\r\\nConnection:\\x20close\\r\\n\\r\\n400\\x20Bad\\x20Request\")%r(SIPOptions,67,\"HTTP/1\\.1\\x20400\\x20Bad\\x20Request\\r\\nContent-Type:\\x20text/plain;\\x
    20charset=utf-8\\r\\nConnection:\\x20close\\r\\n\\r\\n400\\x20Bad\\x20Request\");",
                              "method": "table",
                              "conf": "3"
                          }
                      },
                      {
                          "protocol": "tcp",
                          "portid": "2222",
                          "state": {
                              "state": "open",
                              "reason": "syn-ack",
                              "reason_ttl": "0"
                          },
                          "service": {
                              "name": "ssh",
                              "product": "OpenSSH",
                              "version": "8.4p1 Debian 5",
                              "extrainfo": "protocol 2.0",
                              "ostype": "Linux",
                              "method": "probed",
                              "conf": "10",
                              "cpes": [
                                  "cpe:/a:openbsd:openssh:8.4p1",
                                  "cpe:/o:linux:linux_kernel"
                              ]
                          }
                      },
                      {
                          "protocol": "tcp",
                          "portid": "9100",
                          "state": {
                              "state": "open",
                              "reason": "syn-ack",
                              "reason_ttl": "0"
                          },
                          "service": {
                              "name": "jetdirect",
                              "method": "table",
                              "conf": "3"
                          }
                      }
                  ]
              }
          }
      }
    ]
    

##### Output messages

The **Scan Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully scanned the following entities using Nmap: entity.identifier` `No information was found for the following entities: entity.identifier` `No information was found for the provided entities.` | The action succeeded.  
`Error executing action "Scan Entities". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Scan Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
