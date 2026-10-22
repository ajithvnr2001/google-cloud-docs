---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-json/
title: Collect Zeek (Bro) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:55.820134+00:00
---

# Collect Zeek (Bro) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bro-json/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zeek (Bro) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can deploy Zeek (formerly Bro) and NXLog with Google Security Operations to collect Zeek logs in JSON format. This document also explains how Zeek log fields map to Google Security Operations Unified Data Model (UDM) fields.

For an overview about Google Security Operations data ingestion, see [Data ingestion to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the BRO_JSON ingestion label.

## Before you begin

  * To understand the components deployed to collect Zeek logs, review the deployment architecture. Each customer deployment might differ from this representation and might be more complex. The following diagram shows how you can configure a NXLog agent and a Google Security Operations forwarder on a Linux server and forward log data to Google Security Operations.

![Deployment architecture](https://docs.cloud.google.com/static/chronicle/docs/ingestion/default-parsers/images/parser-zeek-architecture.svg)

  * Verify the Zeek versions that the Google Security Operations parser supports. The Google Security Operations parser supports the following Zeek versions:

    * Zeek 4.1.0
    * Zeek 4.0.1
    * Zeek 5.2.0
    * Zeek 6.0.0
  * Before you use the Zeek parser, review the [changes in field mappings between the previous parser and the current Zeek parser](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/zeek-map-changes). As part of the migration, ensure that the rules, searches, dashboards, or other processes that depend on the original fields use the updated fields.

For example, in the previous parser version, the `server_name` field is mapped to the `target.hostname` UDM field. In the current Zeek parser, the `server_name` field is mapped to the `network.tls.client.server_name` UDM field. If you migrate to the current Zeek parser and use the `server_name` field in your rules, you need to modify the rules to use the `network.tls.client.server_name` UDM field of the current parser.

  * Verify the Zeek log types that the Google Security Operations parser supports. The following table lists the Zeek log types that the Google Security Operations parser supports:


**Log type** | **Description**  
---|---  
[Network protocols](https://docs.zeek.org/en/master/script-reference/log-files.html#network-protocols) | Includes log files of network protocols, such as Dynamic Host Configuration Protocol (DHCP) and Domain Name System (DNS).   
[Files](https://docs.zeek.org/en/master/script-reference/log-files.html#files) | Includes the following log files: File analysis results, Online Certificate Status Protocol (OCSP), Portable Executable (PE), and X.509 certificate.   
[NetControl](https://docs.zeek.org/en/master/script-reference/log-files.html#netcontrol) | Includes log files of NetControl actions and OpenFlow debug logs.   
[Detection](https://docs.zeek.org/en/master/script-reference/log-files.html#detection) | Includes log files of intelligence data matches, Zeek notices, alarm stream, signature matches, and traceroute detection.   
[Network observations](https://docs.zeek.org/en/master/script-reference/log-files.html#network-observations) | Includes log files of SSL certificates, hosts that have completed TCP handshakes, Modbus primary and replica, services running on hosts, and software used on the network.   
  
  * If you have not done so already, install and configure Zeek. For more information, see [Zeek installation](https://docs.zeek.org/en/master/install.html#installing-zeek).

  * Collect Zeek logs in JSON format. For more information, see [Output Zeek logs to JSON](https://www.ericooi.com/zeekurity-zen-part-iii-how-to-send-zeek-logs-to-splunk/#:%7E:text=OUTPUT%20ZEEK%20LOGS,less%20conn.log).

  * Ensure that all systems in the deployment architecture are configured with the UTC time zone.




## Configure NXLog and Google Security Operations forwarder

  1. Download and install NXLog Community Edition on the Linux machine on which Google Security Operations forwarder runs. 
     * For more information on downloading NXLog Community Edition, see [NXLog documentation](https://nxlog.co/products/nxlog-community-edition/download).
     * For more information on installing the required NXLog packages and dependencies, see [installing NXLog on a Linux system](https://nxlog.co/documentation/nxlog-user-guide/deploy-rhel.html).
  2. Create a configuration file for each NXLog instance.
  3. Use the NXLog [im_file](https://nxlog.co/documentation/nxlog-user-guide/im_file.html) module to read from the file and parse the lines into fields. Here is an example NXLog configuration:
         
         LogFile /var/log/nxlog/nxlog.log
         LogLevel INFO
         
         define ZEEK_OUTPUT_DESTINATION_ADDRESS <hostname>
         define ZEEK_OUTPUT_DESTINATION_PORT <port>
         
         <Input conn>
            Module      im_file
            File        '/opt/zeek/logs/current/conn.log'
            Exec $raw_event= "conn" + ' - ' + $raw_event;;
         </Input>
         
         <Input dce_rpc>
           Module      im_file
           File        '/opt/zeek/logs/current/dce_rpc.log'
           Exec $raw_event= "dce_rpc" + ' - ' + $raw_event;;
         </Input>
         
         <Output out_chronicle>
           Module  om_tcp
           Host    %ZEEK_OUTPUT_DESTINATION_ADDRESS%
           Port    %ZEEK_OUTPUT_DESTINATION_PORT%
         </Output>
         
         <Route zeek_to_chronicle>
           Path conn, dce_rpc => out_chronicle
         </Route>
         
         

To use the preceding example configuration, do the following:

     * Replace `<hostname>` and `<port>` values with information about the destination Linux server.
     * Add input, output, and route elements for each Zeek log type that you want to collect.
  4. Configure Google Security Operations forwarder to send logs to Google Security Operations. For more information, see [Installing and configuring the forwarder on Linux](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux.md). Here is an example forwarder configuration.
         
         output:
           url: URL
           identity:
           identity:
           collector_id: COLLECTOR_ID
           customer_id: CUSTOMER_ID
           secret_key: |
         
           {
           "type": "service_account",
           "project_id": "malachite-projectname",
           "private_key_id": `PRIVATE_KEY_ID`,
           "private_key": `PRIVATE_KEY`,
           "client_email":"`SERVICE_ACCOUNT_NAME`@malachite-`PROJECT_ID`.`SERVICE_ACCOUNT_DOMAIN`",
           "client_id": `CLIENT_ID`,
           "auth_uri": "https://accounts.google.com/o/oauth2/auth",
           "token_uri": "https://oauth2.googleapis.com/token",
           "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
           "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/`SERVICSERVICE_ACCOUNT_NAME`%40malachite-`PROJECT_ID`.`SERVICE_ACCOUNT_DOMAIN`",
           }
         
           collectors:
           - syslog:
               common:
                 enabled: true
                 data_type: BRO_JSON
                 batch_n_seconds: 10
                 batch_n_bytes: 1048576
               tcp_address: 0.0.0.0:10518
               connection_timeout_sec: 60
         

  5. Replace the `PRIVATE_KEY_ID`, `PRIVATE_KEY` `SERVICSERVICE_ACCOUNT_NAME`,`PROJECT_ID`, `CLIENT_ID`, `SERVICE_ACCOUNT_DOMAIN` `CUSTOMER_ID`,`URL`, `COLLECTOR_ID` and `CUSTOMER_ID` with the respective values from the service account JSON file which you can download from Google Cloud Platform.

  6. Start the NXLog service.




## Forward Logs to Google SecOps using Bindplane agent

  1. Install and set up a **Linux Virtual Machine**.
  2. Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see [the Bindplane agent installation and configuration instructions](https://bindplane.com/docs/getting-started/quickstart-guide).



If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

## Supported Zeek (Bro) log formats

The Zeek (Bro) parser supports logs in JSON and SYSLOG+JSON format.

## Supported Zeek (Bro) sample logs

  * JSON
        
        {
          "insertId": "1pvsdy2f8v21o8",
          "jsonPayload": {
            "message": "Jun 14 07:46:10 dummyhostname systemd[1]: Stopping System Logging Service..."
          },
          "resource": {
            "type": "gce_instance",
            "labels": {
              "project_id": "cl-tpt-dis-awkc-con17-p-922a",
              "zone": "us-central1-a",
              "instance_id": "4136884722753789246"
            }
          },
          "timestamp": "2024-09-03T19:31:32.353129233Z",
          "labels": {
            "compute.googleapis.com/resource_name": "dummyostname"
          },
          "logName": "projects/cl-tpt-dis-awkc-con17-p-922a/logs/syslog",
          "receiveTimestamp": "2024-09-03T19:31:33.388651657Z"
        }
        

  * SYSLOG + JSON
        
        <13>1 2021-12-21T23: 51: 25-08: 00 ia-cs-vubro-089 bro_http - - - {
          "ts": 1640159484.694295,
          "uid": "CTgT3z1adxn1EMPbmj",
          "id.orig_h": "198.51.100.27",
          "id.orig_p": 58729,
          "id.resp_h": "198.51.100.28",
          "id.resp_p": 8088,
          "trans_depth": 2284,
          "method": "POST",
          "host": "198.51.100.8",
          "uri": "/system/gateway",
          "version": "1.1",
          "user_agent": "Java/11.0.11",
          "request_body_len": 304,
          "response_body_len": 203,
          "status_code": 200,
          "status_msg": "OK",
          "tags": [],
          "orig_fuids": [
            "FefIdu4i8dzFTUONb5"
          ],
          "orig_mime_types": [
            "application/xml"
          ],
          "resp_fuids": [
            "Flqz7L3yyQR1eSN4Kf"
          ],
          "resp_mime_types": [
            "application/xml"
          ]
        }
        




## Field mapping reference: Zeek logs fields to UDM fields

To understand how the Google Security Operations parser maps Zeek log fields to Google Security Operations UDM event fields for each Zeek log type, refer to the following sections:

  * Network protocols
  * Files
  * Netcontrol
  * Detection
  * Network observations



### Network protocols

The following table lists the log fields of the network protocols log type and their corresponding UDM fields.

Original log field | Log type | UDM field  
---|---|---  
ts  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | metadata.event_timestamp   
uid  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | network.session_id   
id.orig_h  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | principal.ip   
id.orig_p  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | principal.port   
id.resp_h  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | target.ip   
id.resp_p  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | target.port   
proto  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | network.ip_protocol   
service  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | In case of exact match, service is mapped to network.application_protocol. In case of multiple values, service is mapped to additional.fields.key/value.   
duration  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | network.session_duration   
orig_bytes  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | network.sent_bytes   
resp_bytes  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | network.received_bytes   
conn_state  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | metadata.description   
local_orig  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
local_resp  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
missed_bytes  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
history  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
orig_pkts  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
orig_ip_bytes  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
resp_pkts  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
resp_ip_bytes  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
tunnel_parents  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
orig_l2_addr  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
resp_l2_addr  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
vlan  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
inner_vlan  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
speculative_service  | [conn.log](https://docs.zeek.org/en/master/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info) | additional.fields.key/value   
ts | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | metadata.event_timestamp   
uid  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | network.session_id   
id.orig_h  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | principal.ip   
id.orig_p  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | principal.port   
id.resp_h  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | target.ip   
id.resp_p  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | target.port   
rtt  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | additional.fields.key/value   
named_pipe  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | target.resource.name  Also, target.resource.resource_type is set to "PIPE".   
endpoint  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | additional.fields.key/value   
operation  | [dce_rpc.log](https://docs.zeek.org/en/master/scripts/base/protocols/dce-rpc/main.zeek.html#type-DCE_RPC::Info) | additional.fields.key/value   
ts  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | metadata.event_timestamp   
uids  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
client_addr  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | target.ip   
server_addr  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | principal.ip   
client_port  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | target.port   
server_port  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | principal.port   
mac  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | principal.mac  Machine ID is required for parsing NETWORK_DHCP events.   
host_name  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | network.dhcp.client_hostname   
client_fqdn  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | target.hostname   
domain  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | target.administrative_domain   
requested_addr  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | network.dhcp.requested_address   
assigned_addr  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | network.dhcp.yiaddr   
lease_time  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | network.dhcp.lease_time_seconds   
client_message  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
server_message  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
msg_types  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value  The log that Zeek produces is a collection of DORA messages in a single log.   
duration  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | network.dhcp.seconds   
client_chaddr  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | network.dhcp.chaddr   
msg_orig  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
client_software  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
server_software  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
circuit_id  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
agent_remote_id  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
subscriber_id  | [dhcp.log](https://docs.zeek.org/en/master/scripts/base/protocols/dhcp/main.zeek.html#type-DHCP::Info) | additional.fields.key/value   
ts  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | metadata.event_timestamp   
uid  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | network.session_id   
id.orig_h  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | principal.ip   
id.orig_p  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | principal.port   
id.resp_h  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | target.ip   
id.resp_p  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | target.port   
fc_request  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | additional.fields.key/value   
fc_reply  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | additional.fields.key/value   
iin  | [dnp3.log](https://docs.zeek.org/en/master/scripts/base/protocols/dnp3/main.zeek.html#type-DNP3::Info) | additional.fields.key/value   
ts  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | metadata.event_timestamp   
uid  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.session_id   
id.orig_h  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | principal.ip   
id.orig_p  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | principal.port   
id.resp_h  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | target.ip   
id.resp_p  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | target.port   
proto  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.ip_protocol   
trans_id  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.id   
rtt  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
query  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.questions.name  If the length of the `query` log field exceeds 255 characters, it is mapped to `additional.fields[original_query]` and truncated to 255 characters before mapping to `network.dns.questions.name`.   
qclass  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.questions.class   
qclass_name  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
qtype  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.questions.type   
qtype_name  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
rcode  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network,dns.response_code   
rcode_name  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
AA  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.authoritative   
TC  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.truncated   
RD  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.recursion_desired   
RA  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.recursion_available   
Z  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
answers  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.answers.data   
TTLs  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.answers.ttl   
rejected  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
total_answers  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
total_replies  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
saw_query  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
saw_reply  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
auth  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.authority.data   
addl  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | network.dns.additional.data   
original_query  | [dns.log](https://docs.zeek.org/en/master/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info) | additional.fields.key/value   
ts  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | metadata.event_timestamp   
uid  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | network.session_id   
id.orig_h  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | principal.ip   
id.orig_p  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | principal.port   
id.resp_h  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | target.ip   
id.resp_p  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | target.port   
user  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | principal.user.userid   
command  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | network.ftp.command   
arg  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
mime_type  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | src.file.mime_type   
file_size  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | src.file.size   
reply_code  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
reply_msg  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
data_channel.passive  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
data_channel.orig_h  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
data_channel.resp_h  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
data_channel.resp_p  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
cwd  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | src.file.full_path   
cmdarg.ts  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
cmdarg.cmd  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
cmdarg.arg  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
cmdarg.seq  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
pending_commands  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
passive  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
capture_password  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
fuid  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
last_auth_requested  | [ftp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info) | additional.fields.key/value   
ts  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | metadata.event_timestamp   
uid  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | network.session_id   
id.orig_h  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | principal.ip   
id.orig_p  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | principal.port   
id.resp_h  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | target.ip   
id.resp_p  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | target.port   
trans_depth  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
method  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | network.http.method   
host  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | target.hostname  If the length of the `host` log field exceeds 255 characters, it is mapped to `additional.fields[original_host]` and truncated to 255 characters before mapping to `target.hostname`.   
uri  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | If the URI log field value is not equal to host log field, then the target.url is set to "%{host}%{uri}" otherwise target.url is set to "%{uri}"   
referrer  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | network.http.referral_url   
version  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
user_agent  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | network.http.user_agent   
origin  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
request_body_len  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
response_body_len  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
status_code  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | network.http.response_code   
status_msg  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
info_code  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
info_msg  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
tags  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
username  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | principal.user.userid  If the length of the `username` log field exceeds 255 characters, it is mapped to `additional.fields[original_username]` and truncated to 255 characters before mapping to `principal.user.userid`.   
capture_password  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
proxied  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
range_request  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
orig_fuids  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
orig_filenames  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
orig_mime_types  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
resp_fuids  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
resp_filenames  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
resp_mime_types  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
current_entity  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
orig_mime_depth  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
resp_mime_depth  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
client_header_names  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
server_header_names  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
omniture  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
flash_version  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
cookie_vars  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
uri_vars  | [http.log](https://docs.zeek.org/en/master/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info) | additional.fields.key/value   
ts  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | metadata.event_timestamp   
uid  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | network.session_id   
id.orig_h  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | principal.ip   
id.orig_p  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | principal.port   
id.resp_h  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | target.ip   
id.resp_p  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | target.port   
nick  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | additional.fields.key/value   
user  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | principal.user.userid   
command  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | principal.process.command_line   
value  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | additional.fields.key/value   
addl  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | additional.fields.key/value   
dcc_file_name  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | additional.fields.key/value   
dcc_file_size  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | src.file.size   
dcc_mime_type  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | src.file.mime_type   
fuid  | [irc.log](https://docs.zeek.org/en/master/scripts/base/protocols/irc/main.zeek.html#type-IRC::Info) | additional.fields.key/value   
ts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | metadata.event_timestamp   
uid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.session_id   
id.orig_h  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | principal.ip   
id.orig_p  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | principal.port   
id.resp_h  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | target.ip   
id.resp_p  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | target.port   
request_type  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
service  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
success  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
error_code  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
error_msg  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | metadata.description is set to "KERBEROS: %{error_msg}"   
from  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
till  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
cipher  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.cipher   
forwardable  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
renewable  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
logged  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.ts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.fuid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.tx_hosts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.rx_hosts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.conn_uids  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.source  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.depth  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.analyzers  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.mime_type  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.filename  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.duration  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.local_orig  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.is_orig  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.seen_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.total_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.missing_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.overflow_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.timedout  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.parent_fuid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.md5  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.md5   
client_cert.sha1  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.sha1   
client_cert.sha256  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.sha256   
client_cert.x509.ts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.fingerprint  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.version  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.version   
client_cert.x509.certificate.serial  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.serial   
client_cert.x509.certificate.subject  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.issuer  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.issuer   
client_cert.x509.certificate.cn  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.not_valid_before  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.not_valid_after  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.key_alg  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.sig_alg  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.key_type  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.key_length  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.exponent  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.certificate.curve  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.handle  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.extensions.name  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.extensions.short_name  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.extensions.oid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.extensions.critical  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.extensions.value  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.san.dns  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.san.uri  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.san.email  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.san.ip  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.san.other_fields  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.basic_constraints.ca  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.basic_constraints.path_len  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.extensions_cache  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.host_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.client_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.deduplication_index.fingerprint  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.deduplication_index.host_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.deduplication_index.client_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.always_raise_x509_events  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.x509.cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.extracted  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.extracted_cutoff  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.extracted_size  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert.entropy  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
client_cert_subject  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.client.certificate.subject   
client_cert_fuid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.ts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.fuid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.tx_hosts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.rx_hosts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.conn_uids  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.source  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.depth  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.analyzers  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.mime_type  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.filename  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.duration  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.local_orig  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.is_orig  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.seen_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.total_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.missing_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.overflow_bytes  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.timedout  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.parent_fuid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.md5  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.md5   
server_cert.sha1  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.sha1   
server_cert.sha256  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.sha256   
server_cert.x509.ts  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.fingerprint  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.version  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.version   
server_cert.x509.certificate.serial  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.serial   
server_cert.x509.certificate.subject  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.issuer  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.issuer   
server_cert.x509.certificate.cn  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.not_valid_before  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.not_valid_after  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.key_alg  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.sig_alg  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.key_type  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.key_length  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.exponent  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.certificate.curve  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.handle  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.extensions.name  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.extensions.short_name  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.extensions.oid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.extensions.critical  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.extensions.value  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.san.dns  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.san.uri  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.san.email  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.san.ip  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.san.other_fields  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.basic_constraints.ca  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.basic_constraints.path_len  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.extensions_cache  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.host_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.client_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.deduplication_index.fingerprint  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.deduplication_index.host_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.deduplication_index.client_cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.always_raise_x509_events  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.x509.cert  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.extracted  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.extracted_cutoff  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.extracted_size  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert.entropy  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
server_cert_subject  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | network.tls.server.certificate.subject   
server_cert_fuid  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
auth_ticket  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
new_ticket  | [kerberos.log](https://docs.zeek.org/en/master/scripts/base/protocols/krb/main.zeek.html#type-KRB::Info) | additional.fields.key/value   
ts  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | metadata.event_timestamp   
uid  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | network.session_id   
id.orig_h  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | principal.ip   
id.orig_p  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | principal.port   
id.resp_h  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | target.ip   
id.resp_p  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | target.port   
func  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | additional.fields.key/value   
exception  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | additional.fields.key/value   
track_address  | [modbus.log](https://docs.zeek.org/en/master/scripts/base/protocols/modbus/main.zeek.html#type-Modbus::Info) | additional.fields.key/value   
ts  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | metadata.event_timestamp   
uid  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | network.session_id   
id.orig_h  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | principal.ip   
id.orig_p  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | principal.port   
id.resp_h  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | target.ip   
id.resp_p  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | target.port   
register  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | additional.fields.key/value   
old_val  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | additional.fields.key/value   
new_val  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | additional.fields.key/value   
delta  | [modbus_register_change.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/track-memmap.zeek.html#type-Modbus::MemmapInfo) | additional.fields.key/value   
ts  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | metadata.event_timestamp   
uid  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | network.session_id   
id.orig_h  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | principal.ip   
id.orig_p  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | principal.port   
id.resp_h  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | target.ip   
id.resp_p  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | target.port   
cmd  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | metadata.description   
arg  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | principal.process.command_line   
success  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) |  If the value of success is "T" or "true," security_result.action is set to "ALLOW" and security_result.summary is set to "Query successfully executed."  If the value of success is not "T" or "true," security_result.action is set to "BLOCK" and security_result.summary is set to "Query execution failed."   
rows  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | security_result.description is set to "Affected rows: %{rows}". If the log type is "mysql.log", the additional field security_result.severity is set to "INFORMATIONAL".   
response  | [mysql.log](https://docs.zeek.org/en/master/scripts/base/protocols/mysql/main.zeek.html#type-MySQL::Info) | additional.fields.key/value   
ts  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | metadata.event_timestamp   
uid  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | network.session_id   
id.orig_h  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | principal.ip   
id.orig_p  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | principal.port   
id.resp_h  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | target.ip   
id.resp_p  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | target.port   
username  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | principal.user.userid   
hostname  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | principal.hostname   
domainname  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | principal.administrative_domain   
server_nb_computer_name  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | additional.fields.key/value   
server_dns_computer_name  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | target.hostname   
server_tree_name  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | additional.fields.key/value   
success  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) |  If the value of success is "T" or "true", security_result.action is set to "ALLOW" and security_result.summary is set to "Query successfully executed".  If the value of success is not "T" or "true", security_result.action is set to "BLOCK" and security_result.summary is set to "Query execution failed".   
done  | [ntlm.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntlm/main.zeek.html#type-NTLM::Info) | additional.fields.key/value   
ts  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | metadata.event_timestamp   
uid  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | network.session_id   
id.orig_h  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | principal.ip   
id.orig_p  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | principal.port   
id.resp_h  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | target.ip   
id.resp_p  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | target.port   
version  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
mode  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
stratum  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
poll  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
precision  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
root_delay  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
root_disp  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
ref_id  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
ref_time  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
org_time  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
rec_time  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
xmt_time  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
num_exts  | [ntp.log](https://docs.zeek.org/en/master/scripts/base/protocols/ntp/main.zeek.html#type-NTP::Info) | additional.fields.key/value   
ts  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | metadata.event_timestamp   
uid  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | network.session_id   
id.orig_h  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | principal.ip   
id.orig_p  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | principal.port   
id.resp_h  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | target.ip   
id.resp_p  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | target.port   
username  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | principal.user.userid   
mac  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | principal.mac   
framed_addr  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | additional.fields.key/value   
tunnel_client  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | additional.fields.key/value   
connect_info  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | additional.fields.key/value   
reply_msg  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | additional.fields.key/value   
result  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | If the log type is "radius.log", the following fields are set: 
* extensions.auth.type is set to "MACHINE".
* metadata.description is set to "RADIUS authentication attempts %{result}".
* security_result.action
* security_result.summary
If the value of the "result" field is "success", security_result.action is set to "ALLOW" and security_result.summary is set to "User login successful".  If the value of "result" field is "failed", security_result.action is set to "BLOCK" and security_result.summary is set to "User login failed".   
ttl  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | additional.fields.key/value   
logged  | [radius.log](https://docs.zeek.org/en/master/scripts/base/protocols/radius/main.zeek.html#type-RADIUS::Info) | additional.fields.key/value   
ts  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | metadata.event_timestamp   
uid  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | network.session_id   
id.orig_h  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | principal.ip   
id.orig_p  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | principal.port   
id.resp_h  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | target.ip   
id.resp_p  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | target.port   
cookie  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | principal.user.userid   
result  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | security_result.severity is set to "INFORMATIONAL". security_result.description is set to "%{result} connection with security protocol %{security_protocol}".   
security_protocol  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | security_result.description is set to "%{result} connection with security protocol %{security_protocol}".   
client_channels  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
keyboard_layout  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
client_build  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | principal.asset.platform_software.platform_version   
client_name  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
client_dig_product_id  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | principal.asset.asset_id   
desktop_width  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
desktop_height  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
requested_color_depth  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
cert_type  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
cert_count  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
cert_permanent  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
encryption_level  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
encryption_method  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
analyzer_id  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
done  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
ssl  | [rdp.log](https://docs.zeek.org/en/master/scripts/base/protocols/rdp/main.zeek.html#type-RDP::Info) | additional.fields.key/value   
ts  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | metadata.event_timestamp   
uid  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | network.session_id   
id.orig_h  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | principal.ip   
id.orig_p  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | principal.port   
id.resp_h  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | target.ip   
id.resp_p  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | target.port   
client_major_version  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
client_minor_version  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
server_major_version  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
server_minor_version  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
authentication_method  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
auth  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
share_flag  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
desktop_name  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | target.asset.hostname   
width  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
height  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
done  | [rfb.log](https://docs.zeek.org/en/master/scripts/base/protocols/rfb/main.zeek.html#type-RFB::Info) | additional.fields.key/value   
ts  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | metadata.event_timestamp   
uid  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | network.session_id  Also, network.application_protocol is set to "SIP".   
id.orig_h  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | principal.ip   
id.orig_p  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | principal.port   
id.resp_h  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | target.ip   
id.resp_p  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | target.port   
trans_depth  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
method  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | metadata.description   
uri  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | about.url   
date  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
request_from  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | principal.user.userid and principal.user.user_display_name   
request_to  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | target.user.userid and target.user.user_display_name   
response_from  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
response_to  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
reply_to  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
call_id  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | network.session_id   
seq  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
subject  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
request_path  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
response_path  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
user_agent  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
status_code  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | security_result.summary is set to "Status Code: %{status_code}".   
status_msg  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | security_result.description   
warning  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
request_body_len  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | network.sent_bytes   
response_body_len  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | network.received_bytes   
content_type  | [sip.log](https://docs.zeek.org/en/master/scripts/base/protocols/sip/main.zeek.html#type-SIP::Info) | additional.fields.key/value   
ts  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | metadata.event_timestamp   
uid  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | network.session_id   
id.orig_h  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | principal.ip   
id.orig_p  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | principal.port   
id.resp_h  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | target.ip   
id.resp_p  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | target.port   
command  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | principal.process.command_line   
sub_command  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
argument  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
status  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
rtt  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
version  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | metadata.product_version   
username  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | principal.user.userid   
tree  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
tree_service  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
smb1_offered_dialects  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
smb2_offered_dialects  | [smb_cmd.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::CmdInfo) | additional.fields.key/value   
ts  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | metadata.event_timestamp   
uid  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | network.session_id   
id.orig_h  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | principal.ip   
id.orig_p  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | principal.port   
id.resp_h  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | target.ip   
id.resp_p  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | target.port   
fuid  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
action  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | metadata.description is set to "action: %{action} on: %{name}".   
path  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | target.file.full_path   
name  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
size  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | target.file.size   
prev_name  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.modified  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.modified_raw  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.accessed  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.accessed_raw  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.created  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.created_raw  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.changed  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
times.changed_raw  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
fid  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
uuid  | [smb_files.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::FileInfo) | additional.fields.key/value   
ts  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | metadata.event_timestamp   
uid  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | network.session_id   
id.orig_h  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | principal.ip   
id.orig_p  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | principal.port   
id.resp_h  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | target.ip   
id.resp_p  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | target.port   
path  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | target.file.full_path   
service  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | target.application   
native_file_system  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | additional.fields.key/value   
share_type  | [smb_mapping.log](https://docs.zeek.org/en/master/scripts/base/protocols/smb/main.zeek.html#type-SMB::TreeInfo) | target.resource.resource_type   
ts  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | metadata.event_timestamp   
uid  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | network.session_id   
id.orig_h  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | principal.ip   
id.orig_p  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | principal.port   
id.resp_h  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | target.ip   
id.resp_p  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | target.port   
trans_depth  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
helo  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
mailfrom  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
rcptto  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
date  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
from  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | network.email.from   
to  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | email.to   
cc  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | network.email.cc   
reply_to  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | email.reply_to   
msg_id  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | email.mail_id   
in_reply_to  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
subject  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | email.subject   
x_originating_ip  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
first_received  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
second_received  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
last_reply  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
path  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
user_agent  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
tls  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | network.tls.established   
process_received_from  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
has_client_activity  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
process_smtp_headers  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
entity.filename  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
entity.excerpt  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
fuids  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
is_webmail  | [smtp.log](https://docs.zeek.org/en/master/scripts/base/protocols/smtp/main.zeek.html#type-SMTP::Info) | additional.fields.key/value   
ts  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | metadata.event_timestamp   
uid  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | network.session_id   
id.orig_h  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | principal.ip   
id.orig_p  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | principal.port   
id.resp_h  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | target.ip   
id.resp_p  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | target.port   
duration  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | network.session_duration   
version  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | metadata.product_version   
community  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | network.community_id   
get_requests  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | additional.fields.key/value   
get_bulk_requests  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | additional.fields.key/value   
get_responses  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | additional.fields.key/value   
set_requests  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | additional.fields.key/value   
display_string  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | metadata.description   
up_since  | [snmp.log](https://docs.zeek.org/en/master/scripts/base/protocols/snmp/main.zeek.html#type-SNMP::Info) | additional.fields.key/value   
ts  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | metadata.event_timestamp   
uid  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | network.session_id   
id.orig_h  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | principal.ip   
id.orig_p  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | principal.port   
id.resp_h  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | target.ip   
id.resp_p  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | target.port   
version  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
user  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | principal.user.userid   
status  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
request.host  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | principal.hostname   
request.name  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
request_p  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
bound.host  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
bound.name  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
bound_p  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
capture_password  | [socks.log](https://docs.zeek.org/en/master/scripts/base/protocols/socks/main.zeek.html#type-SOCKS::Info) | additional.fields.key/value   
ts  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | metadata.event_timestamp   
uid  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | network.session_id   
id.orig_h  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | principal.ip   
id.orig_p  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | principal.port   
id.resp_h  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | target.ip   
id.resp_p  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | target.port   
version  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | metadata.product_version   
auth_success  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
auth_attempts  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | security_result.description is set to "%{auth_attempts} successful SSH authentication attempts were observed".   
direction  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | network.direction   
client  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | principal.platform_version   
server  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | target.platform_version   
cipher_alg  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
mac_alg  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
compression_alg  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
kex_alg  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
host_key_alg  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
host_key  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
logged  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.kex_algorithms  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.server_host_key_algorithms  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.encryption_algorithms  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.mac_algorithms  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.compression_algorithms  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.languages.client_to_server  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.languages.server_to_client  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
capabilities.is_server  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
analyzer_id  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
remote_location.country_code  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
remote_location.region  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | target.asset.location.country_or_region   
remote_location.city  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | target.asset.location.city   
remote_location.latitude  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
remote_location.longitude  | [ssh.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssh/main.zeek.html#type-SSH::Info) | additional.fields.key/value   
ts  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | metadata.event_timestamp   
uid  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | metadata.product_log_id   
id.orig_h  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | principal.ip   
id.orig_p  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | principal.port   
id.resp_h  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | target.ip   
id.resp_p  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | target.port   
version_num  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
version  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.version   
cipher  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.cipher   
curve  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.curve   
server_name  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.client.server_name   
session_id  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.session_id   
resumed  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.resumed   
client_ticket_empty_session_seen  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_key_exchange_seen  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_psk_seen  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
last_alert  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
next_protocol  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.next_protocol   
analyzer_id  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
established  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.established   
logged  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ssl_history  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
cert_chain_fps  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_cert_chain_fps  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
subject  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.server.certificate.subject   
issuer  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.server.certificate.issuer   
client_subject  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.client.certificate.subject   
client_issuer  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.client.certificate.issuer   
sni_matches_cert  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
server_depth  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_depth  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
always_raise_x509_events  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
last_originator_heartbeat_request_size  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
last_responder_heartbeat_request_size  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
originator_heartbeats  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
responder_heartbeats  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
heartbleed_detected  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
enc_appdata_packages  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
enc_appdata_bytes  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
server_version  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_version  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_ciphers  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | network.tls.client.supported_ciphers   
ssl_client_exts  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ssl_server_exts  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ticket_lifetime_hint  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
dh_param_size  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
point_formats  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_curves  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
orig_alpn  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_supported_versions  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
server_supported_version  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
psk_key_exchange_modes  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_key_share_groups  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
server_key_share_group  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
client_comp_methods  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
comp_method  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
sigalgs  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
hashalgs  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
validation_status  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
validation_code  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
valid_chain  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ocsp_status  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ocsp_response  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
valid_scts  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
invalid_scts  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
valid_ct_logs  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
valid_ct_operators  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
valid_ct_operators_list  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ct_proofs  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
notary.first_seen  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
notary.last_seen  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
notary.times_seen  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
notary.valid  | [ssl.log](https://docs.zeek.org/en/master/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info) | additional.fields.key/value   
ts  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | metadata.event_timestamp   
uid  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | network.session_id   
id.orig_h  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | principal.ip   
id.orig_p  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | principal.port   
id.resp_h  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | target.ip   
id.resp_p  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | target.port   
proto  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | network.ip_protocol   
facility  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | additional.fields.key/value   
severity  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | security_result.severity_details   
message  | [syslog.log](https://docs.zeek.org/en/master/scripts/base/protocols/syslog/main.zeek.html#type-Syslog::Info) | metadata.description   
ts  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | metadata.event_timestamp   
uid  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | network.session_id   
id.orig_h  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | principal.ip   
id.orig_p  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | principal.port   
id.resp_h  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | target.ip   
id.resp_p  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | target.port   
tunnel_type  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | security_result.description is set to "action %{action} on tunnel type {tunnel_type}".   
action  | [tunnel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/tunnels/main.zeek.html#type-Tunnel::Info) | security_result.description is set to "action %{action} on tunnel type {tunnel_type}".   
  
### Files

The following table lists the log fields of the files log type and their corresponding UDM fields. 

Original log field | Log type | UDM field  
---|---|---  
ts  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | metadata.event_timestamp   
fuid  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | metadata.product_log_id   
tx_hosts  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | principal.ip   
rx_hosts  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.ip   
conn_uids  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
source  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.application_protocol  target.file.full_path   
depth  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
analyzers  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
mime_type  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.file.mime_type   
filename  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.file.full_path   
duration  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
local_orig  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
is_orig  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
seen_bytes  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.file.size   
total_bytes  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
missing_bytes  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
overflow_bytes  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
timedout  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
parent_fuid  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
md5  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.file.md5   
sha1  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.file.sha1   
sha256  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | target.file.sha256   
md5  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.tls.client.certificate.md5   
sha1  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.tls.client.certificate.sha1   
sha256  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.tls.client.certificate.sha256   
md5  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.tls.server.certificate.md5   
sha1  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.tls.server.certificate.sha1   
sha256  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | network.tls.server.certificate.sha256   
x509  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value  This field is a nested field.   
extracted  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
extracted_cutoff  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
extracted_size  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
entropy  | [files.log](https://docs.zeek.org/en/master/scripts/base/frameworks/files/main.zeek.html#type-Files::Info) | additional.fields.key/value   
ts  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | metadata.event_timestamp   
id  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | metadata.product_log_id   
hashAlgorithm  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | additional.fields.key/value   
issuerNameHash  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | additional.fields.key/value   
issuerKeyHash  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | additional.fields.key/value   
serialNumber  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | tls.server.certificate.serial   
certStatus  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | additional.fields.key/value   
revoketime  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | network.tls.server.certificate.not_after   
revokereason  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | security_result.summary   
thisUpdate  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | additional.fields.key/value   
nextUpdate  | [ocsp.log](https://docs.zeek.org/en/master/scripts/base/files/x509/log-ocsp.zeek.html#type-OCSP::Info) | additional.fields.key/value   
ts  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | metadata.event_timestamp   
id  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | metadata.product_log_id   
machine  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | target.resource.resource_subtype   
compile_ts  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
os  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | target.platform_version  target.resource.resource_type is set to "DEVICE".   
subsystem  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | target.application   
is_exe  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
is_64bit  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
uses_aslr  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
uses_dep  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
uses_code_integrity  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
uses_seh  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
has_import_table  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
has_export_table  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
has_cert_table  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
has_debug_data  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
section_names  | [pe.log](https://docs.zeek.org/en/master/scripts/base/files/pe/main.zeek.html#type-PE::Info) | additional.fields.key/value   
ts  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | metadata.event_timestamp  Also, target.application is set to "x509".   
fingerprint  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
certificate.version  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.server.certificate.version   
certificate.serial  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.server.certificate.serial   
certificate.subject  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.server.certificate.subject   
certificate.issuer  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.server.certificate.issuer   
certificate.cn  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | target.hostname   
certificate.not_valid_before  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.server.certificate.not_before   
certificate.not_valid_after  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.server.certificate.not_after   
certificate.key_alg  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
certificate.sig_alg  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
certificate.key_type  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
certificate.key_length  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
certificate.exponent  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
certificate.curve  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | network.tls.curve   
handle  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
extensions.name  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
extensions.short_name  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
extensions.oid  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
extensions.critical  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
extensions.value  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
san.dns  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
san.uri  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
san.email  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
san.ip  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
san.other_fields  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
basic_constraints.ca  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
basic_constraints.path_len  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
extensions_cache  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
host_cert  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
client_cert  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
deduplication_index.fingerprint  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
deduplication_index.host_cert  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
deduplication_index.client_cert  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
always_raise_x509_events  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
cert  | [x509.log](https://docs.zeek.org/en/master/scripts/base/files/x509/main.zeek.html#type-X509::Info) | additional.fields.key/value   
  
### Netcontrol

The following table lists the log fields of the netcontrol log type and their corresponding UDM fields.

Original log field | Log type | UDM field  
---|---|---  
ts  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | metadata.event_timestamp   
rule_id  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | security_result.rule_id   
category  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | security_result.category_details   
cmd  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
state  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
action  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | security_result.action_details   
target  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
entity_type  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
entity  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | security_result.summary   
mod  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
msg  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | security_result.description   
priority  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | security_result.priority_details   
expire  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
location  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
plugin  | [netcontrol.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/main.zeek.html#type-NetControl::Info) | additional.fields.key/value   
ts  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | metadata.event_timestamp   
rule_id  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | security_result.rule_id   
orig_h  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | principal.ip   
orig_p  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | principal.port   
resp_h  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | target.ip   
resp_p  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | target.port   
expire  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | additional.fields.key/value   
location  | [netcontrol_drop.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/drop.zeek.html#type-NetControl::DropInfo) | additional.fields.key/value   
ts  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | metadata.event_timestamp   
rule_id  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | security_result.rule_id   
f.src_h  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | principal.ip   
f.src_p  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | principal.port   
f.dst_h  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | target.ip   
f.dst_p  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | target.port   
expire  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | additional.fields.key/value   
location  | [netcontrol_shunt.log](https://docs.zeek.org/en/master/scripts/base/frameworks/netcontrol/shunt.zeek.html#type-NetControl::ShuntInfo) | additional.fields.key/value   
ts  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | metadata.event_timestamp   
rule_id  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | security_result.rule_id   
ip  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | target.ip   
action  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | security_result.action_details   
block_interval  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | additional.fields.key/value   
watch_interval  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | additional.fields.key/value   
blocked_until  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | additional.fields.key/value   
watched_until  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | additional.fields.key/value   
num_blocked  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | additional.fields.key/value   
location  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | additional.fields.key/value   
message  | [netcontrol_catch_release.log](https://docs.zeek.org/en/master/scripts/policy/frameworks/netcontrol/catch-and-release.zeek.html#type-NetControl::CatchReleaseInfo) | security_result.description   
ts  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | metadata.event_timestamp   
dpid  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.in_port  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.dl_src  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.dl_dst  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.dl_vlan  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.dl_vlan_pcp  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.dl_type  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.nw_tos  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.nw_proto  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.nw_src  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.nw_dst  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.tp_src  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
match.tp_dst  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.cookie  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.table_id  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.command  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.idle_timeout  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.hard_timeout  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.priority  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.out_port  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.flags  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.out_ports  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.vlan_vid  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.vlan_pcp  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.vlan_strip  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.dl_src  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.dl_dst  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.nw_tos  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.nw_src  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.nw_dst  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.tp_src  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
flow_mod.actions.tp_dst  | [openflow.log](https://docs.zeek.org/en/master/scripts/base/frameworks/openflow/plugins/log.zeek.html#type-OpenFlow::Info) | additional.fields.key/value   
  
### Detection

The following table lists the log fields of the detection log type and their corresponding UDM fields.

Original log field | Log type | UDM field  
---|---|---  
ts  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | metadata.event_timestamp   
uid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | network.session_id   
id.orig_h  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | principal.ip   
id.orig_p  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | principal.port   
id.resp_h  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | target.ip   
id.resp_p  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | target.port   
seen.indicator  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.indicator_type  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.host  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.where  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.node  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.id.orig_h  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.id.orig_p  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.id.resp_h  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.id.resp_p  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.orig.size  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | network.sent_bytes   
seen.conn.orig.state  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.orig.num_pkts  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.orig.num_bytes_ip  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.orig.flow_label  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.orig.l2_addr  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.resp.size  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | network.received_bytes   
seen.conn.resp.state  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.resp.num_pkts  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.resp.num_bytes_ip  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.resp.flow_label  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.resp.l2_addr  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.start_time  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.duration  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | network.session_duration   
seen.conn.service  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.history  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | metadata.description   
seen.conn.uid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | network.session_id   
seen.conn.tunnel.queued  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.tunnel.dispatched  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.vlan  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.inner_vlan  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dpd_state  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.removal_hooks  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.extract_orig  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.extract_resp  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.thresholds.orig_byte  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.thresholds.resp_byte  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.thresholds.orig_packet  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.thresholds.resp_packet  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.thresholds.duration  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dce_rpc_state.uuid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dce_rpc_state.named_pipe  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dce_rpc_state.ctx_to_uuid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dce_rpc_backing  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dns_state.pending_query  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dns_state.pending_queries  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.dns_state.pending_replies  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.ftp_data_reuse  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.http_state.pending  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.http_state.current_request  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.http_state.current_response  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.http_state.trans_depth  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.sip_state.pending  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.sip_state.current_request  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.sip_state.current_response  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.current_cmd  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.current_file  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.current_tree  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.pending_cmds  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.fid_map  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.tid_map  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.uid_map  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.pipe_map  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smb_state.recent_files  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smtp_state.messages_transferred  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.smtp_state.mime_depth  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.known_services_done  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.mqtt_state.publish  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.mqtt_state.subscribe  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.conn.speculative_service  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.uid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.id  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.parent_id  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.source  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | target.file.full_path   
seen.f.is_orig  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.conns  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.last_active  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.seen_bytes  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.total_bytes  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.missing_bytes  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.overflow_bytes  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.timeout_interval  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.bof_buffer_size  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.bof_buffer  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.f.u2_events  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
seen.fuid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
matched  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
sources  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
fuid  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
file_mime_type  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | target.file.mime_type   
file_desc  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
cif.tags  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
cif.confidence  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
cif.source  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
cif.description  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
cif.firstseen  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
cif.lastseen  | [intel.log](https://docs.zeek.org/en/master/scripts/base/frameworks/intel/main.zeek.html#type-Intel::Info) | additional.fields.key/value   
ts  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | metadata.event_timestamp   
uid  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.session_id   
id.orig_h  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | principal.ip   
id.orig_p  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | principal.port   
id.resp_h  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | target.ip   
id.resp_p  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | target.port   
conn.id.orig_h  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.id.orig_p  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.id.resp_h  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.id.resp_p  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.orig.size  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.sent_bytes   
conn.orig.state  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.orig.num_pkts  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.orig.num_bytes_ip  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.orig.flow_label  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.orig.l2_addr  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.resp.size  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.received_bytes   
conn.resp.state  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.resp.num_pkts  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.resp.num_bytes_ip  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.resp.flow_label  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.resp.l2_addr  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.start_time  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.duration  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.session_duration   
conn.service  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.history  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | metadata.description   
conn.uid  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.session_id   
conn.tunnel.queued  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.tunnel.dispatched  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.vlan  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.inner_vlan  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dpd_state.violations  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.removal_hooks  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.extract_orig  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.extract_resp  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.thresholds.orig_byte  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.thresholds.resp_byte  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.thresholds.orig_packet  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.thresholds.resp_packet  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.thresholds.duration  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dce_rpc_state.uuid  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dce_rpc_state.named_pipe  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dce_rpc_state.ctx_to_uuid  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dce_rpc_backing  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dns_state.pending_query  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dns_state.pending_queries  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.dns_state.pending_replies  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.ftp_data_reuse  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.http_state.pending  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.http_state.current_request  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.http_state.current_response  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.http_state.trans_depth  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.sip_state.pending  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.sip_state.current_request  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.sip_state.current_response  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smb_state.pending_cmds  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smb_state.fid_map  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smb_state.tid_map  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smb_state.uid_map  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smb_state.pipe_map  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smb_state.recent_files  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smtp_state.messages_transferred  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.smtp_state.mime_depth  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.known_services_done  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.ts  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.uid  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.id  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.proto_name  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.proto_version  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.client_id  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.connect_status  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.will_topic  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
mqtt.will_payload  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.mqtt_state.publish  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.mqtt_state.subscribe  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
conn.speculative_service  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.orig_h  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.resp_h  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.itype  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.icode  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.len  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.hlim  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
iconn.v6  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.id  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.parent_id  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.source  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | target.file.full_path   
f.is_orig  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.conns  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.last_active  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.seen_bytes  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.total_bytes  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.missing_bytes  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.overflow_bytes  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.timeout_interval  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.bof_buffer_size  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.bof_buffer  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
f.u2_events  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
fuid  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
file_mime_type  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | target.file.mime_type   
file_desc  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
proto  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.ip_protocol   
note  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | security_result.description   
msg  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | security_result.summary   
sub  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
src  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | principal.ip   
dst  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | target.ip   
p  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | target.port   
n  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
peer_name  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
peer_descr  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
actions  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | security_result.action_details   
email_dest  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.email.to (repeated)   
email_body_sections  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | network.email.subject (repeated)   
email_delay_tokens  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
identifier  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
suppress_for  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
remote_location.country_code  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
remote_location.region  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | principal.asset.location.country_or_region   
remote_location.city  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | principal.asset.location.city   
remote_location.latitude  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
remote_location.longitude  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | additional.fields.key/value   
dropped  | [notice.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) [notice_alarm.log](https://docs.zeek.org/en/master/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info) | security_result.action_details   
ts  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | metadata.event_timestamp   
uid  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | network.session_id   
src_addr  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | principal.ip   
src_port  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | principal.port   
dst_addr  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | target.ip   
dst_port  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | target.port   
note  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | security_result.summary   
sig_id  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | additional.fields.key/value   
event_msg  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | metadata.description   
sub_msg  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | additional.fields.key/value   
sig_count  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | additional.fields.key/value   
host_count  | [signatures.log](https://docs.zeek.org/en/master/scripts/base/frameworks/signatures/main.zeek.html#type-Signatures::Info) | additional.fields.key/value   
ts  | [traceroute.log](https://docs.zeek.org/en/master/scripts/policy/misc/detect-traceroute/main.zeek.html#type-Traceroute::Info) | metadata.event_timestamp   
src  | [traceroute.log](https://docs.zeek.org/en/master/scripts/policy/misc/detect-traceroute/main.zeek.html#type-Traceroute::Info) | principal.ip   
dst  | [traceroute.log](https://docs.zeek.org/en/master/scripts/policy/misc/detect-traceroute/main.zeek.html#type-Traceroute::Info) | target.ip   
proto  | [traceroute.log](https://docs.zeek.org/en/master/scripts/policy/misc/detect-traceroute/main.zeek.html#type-Traceroute::Info) | network.ip_protocol   
  
### Network Observations

The following table lists the log fields of the network observations log type and their corresponding UDM fields.

Original log field | Log type | UDM field  
---|---|---  
ts  | [known_certs.log](https://docs.zeek.org/en/master/scripts/policy/protocols/ssl/known-certs.zeek.html#type-Known::CertsInfo) | metadata.event_timestamp   
host  | [known_certs.log](https://docs.zeek.org/en/master/scripts/policy/protocols/ssl/known-certs.zeek.html#type-Known::CertsInfo) | principal.ip   
port_num  | [known_certs.log](https://docs.zeek.org/en/master/scripts/policy/protocols/ssl/known-certs.zeek.html#type-Known::CertsInfo) | principal.port   
subject  | [known_certs.log](https://docs.zeek.org/en/master/scripts/policy/protocols/ssl/known-certs.zeek.html#type-Known::CertsInfo) | network.tls.client.certificate.subject   
issuer_subject  | [known_certs.log](https://docs.zeek.org/en/master/scripts/policy/protocols/ssl/known-certs.zeek.html#type-Known::CertsInfo) | network.tls.client.certificate.issuer   
serial  | [known_certs.log](https://docs.zeek.org/en/master/scripts/policy/protocols/ssl/known-certs.zeek.html#type-Known::CertsInfo) | network.tls.client.certificate.serial   
ts  | [known_hosts.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-hosts.zeek.html#type-Known::HostsInfo) | metadata.event_timestamp   
host  | [known_hosts.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-hosts.zeek.html#type-Known::HostsInfo) | principal.ip   
ts  | [known_modbus.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/known-masters-slaves.zeek.html#type-Known::ModbusInfo) | metadata.event_timestamp   
host  | [known_modbus.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/known-masters-slaves.zeek.html#type-Known::ModbusInfo) | principal.ip   
device_type  | [known_modbus.log](https://docs.zeek.org/en/master/scripts/policy/protocols/modbus/known-masters-slaves.zeek.html#type-Known::ModbusInfo) | target.resource.name  target.resource.resource_type = "DEVICE"   
ts  | [known_services.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-services.zeek.html#type-Known::ServicesInfo) | metadata.event_timestamp   
host  | [known_services.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-services.zeek.html#type-Known::ServicesInfo) | principal.ip   
port_num  | [known_services.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-services.zeek.html#type-Known::ServicesInfo) | principal.port   
port_proto  | [known_services.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-services.zeek.html#type-Known::ServicesInfo) | network.ip_protocol   
service  | [known_services.log](https://docs.zeek.org/en/master/scripts/policy/protocols/conn/known-services.zeek.html#type-Known::ServicesInfo) | target.application   
ts  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | metadata.event_timestamp   
host  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | principal.ip   
host_p  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | principal.port   
software_type  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | principal.resource.resource_subtype   
name  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | principal.resource.name   
version.major  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
version.minor  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
version.minor2  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
version.minor3  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
version.addl  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
unparsed_version  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
force_log  | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | additional.fields.key/value   
`url` | [software.log](https://docs.zeek.org/en/master/scripts/base/frameworks/software/main.zeek.html#type-Software::Info) | metadata.url_back_to_product   
  
## Field mapping reference: Event ID to UDM event type

To understand how the parser maps log names to UDM event types, refer to the following sections:

  * Network protocols
  * Files
  * Netcontrol
  * Detection
  * Network observations



### Network protocols

The following table lists the log names of the network protocols log type and their corresponding UDM event types.

Log name | Description | UDM event type  
---|---|---  
conn.log  | TCP/UDP/ICMP connections  | NETWORK_CONNECTION   
dce_rpc.log  | Distributed Computing Environment/RPC  | NETWORK_CONNECTION   
dhcp.log  | DHCP leases  | NETWORK_DHCP   
dnp3.log  | DNP3 (Distributed Network Protocol 3) requests and replies  | NETWORK_CONNECTION   
dns.log  | DNS activity  | NETWORK_DNS   
ftp.log  | FTP (File Transfer Protocol) activity  | NETWORK_FTP   
http.log  | HTTP requests and replies  | NETWORK_HTTP   
irc.log  | IRC (Internet Relay Chat) commands and responses  | NETWORK_CONNECTION   
kerberos.log  | Kerberos  | NETWORK_CONNECTION   
modbus.log  | Modbus commands and responses  | NETWORK_CONNECTION   
modbus_register_change.log  | Tracks changes to Modbus holding registers  | GENERIC_EVENT   
mysql.log  | MySQL  | NETWORK_UNCATEGORIZED   
ntlm.log  | NT LAN Manager (NTLM)  | NETWORK_CONNECTION   
ntp.log  | Network Time Protocol  | NETWORK_CONNECTION   
radius.log  | RADIUS authentication attempts  | USER_LOGIN   
rdp.log  | Remote Desktop Protocol (RDP)  | NETWORK_CONNECTION   
rfb.log  | Remote Framebuffer (RFB)  | NETWORK_CONNECTION   
sip.log  | Session Initiation Protocol (SIP)  | NETWORK_UNCATEGORIZED   
smb_cmd.log  | SMB (Server Message Block) commands  | NETWORK_CONNECTION   
smb_files.log  | SMB (Server Message Block) files  | NETWORK_UNCATEGORIZED   
smb_mapping.log  | SMB (Server Message Block) trees  | NETWORK_CONNECTION   
smtp.log  | SMTP (Simple Mail Transfer Protocol) transactions  | NETWORK_SMTP   
snmp.log  | SNMP (Simple Network Management Protocol) messages  | NETWORK_UNCATEGORIZED   
socks.log  | SOCKS proxy requests  | NETWORK_CONNECTION   
ssh.log  | SSH (Secure Shell) connections  | NETWORK_UNCATEGORIZED   
ssl.log  | SSL(Secure Sockets Layer)/TLS(Transport Layer Security) handshake info  | NETWORK_HTTP  NETWORK_CONNECTION   
syslog.log  | Syslog messages  | NETWORK_CONNECTION   
tunnel.log  | Tunneling protocol events  | NETWORK_CONNECTION   
  
### Files

The following table lists the log names of the files log type and their corresponding UDM event types.

Log name | Description | UDM event type  
---|---|---  
files.log  | File analysis results  | NETWORK_UNCATEGORIZED   
ocsp.log  | If policy script is loaded, the Online Certificate Status Protocol (OCSP) log is created.  | GENERIC_EVENT   
pe.log  | Portable Executable (PE)  | GENERIC_EVENT   
x509.log  | X.509 certificate info  | GENERIC_EVENT   
  
### Netcontrol

The following table lists the log names of the netcontrol log type and their corresponding UDM event types.

Log name | Description | UDM event type  
---|---|---  
netcontrol.log  | NetControl actions  | GENERIC_EVENT   
netcontrol_drop.log  | NetControl actions  | STATUS_UPDATE   
netcontrol_shunt.log  | NetControl shunt actions  | STATUS_UPDATE   
netcontrol_catch_release.log  | NetControl catch and release actions  | GENERIC_EVENT   
openflow.log  | OpenFlow debug log  | GENERIC_EVENT   
  
### Detection

The following table lists the log names of the detection log type and their corresponding UDM event types.

Log name | Description | UDM event type  
---|---|---  
intel.log  | Intelligence data matches  | GENERIC_EVENT   
notice.log  | Zeek notices  | NETWORK_CONNECTION   
notice_alarm.log  | The alarm stream  | NETWORK_CONNECTION   
signatures.log  | Signature matches  | GENERIC_EVENT   
traceroute.log  | Traceroute detection  | NETWORK_UNCATEGORIZED   
  
### Network observations

The following table lists the log names of the network observations log type and their corresponding UDM event types.

Log name | Description | UDM event type  
---|---|---  
known_certs.log  | SSL certificates  | GENERIC_EVENT   
known_hosts.log  | Hosts that completed TCP handshakes  | GENERIC_EVENT   
known_modbus.log  | Modbus master and secondary  | GENERIC_EVENT   
known_services.log  | Services running on hosts  | GENERIC_EVENT   
software.log  | Software used on the network  | GENERIC_EVENT   
  
## What's next

  * [Data ingestion to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow)



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bro-json-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
