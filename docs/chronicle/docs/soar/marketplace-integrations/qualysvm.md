---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/qualysvm/
title: Qualys VM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:31.080130+00:00
---

# Qualys VM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/qualysvm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Qualys VM

This document explains how to integrate Qualys VM with Google Security Operations.

**Important:** This integration refers to Qualys VMDR.

## Integration parameters

The **Qualys VM** integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` | Required. The base URL of the Qualys VM instance.  
`Username` | Required. The username associated with your Qualys VM API credentials.  
`Password` | Required. The password associated with your Qualys VM API credentials.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Qualys VM server. Enabled by default.  
`X-Requested-With Header` | Optional. The value for the `X-Requested-With` HTTP header used to identify the source of the API requests. The default value is `Google SecOps SOAR`.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Download Vm Scan Results

#### Description

Fetch a vulnerability scan results by the scan ID.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scan ID | String | N/A | Yes | Scan ID value.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
           "username": "username",
            "city": "New York",
            "zip": "10024",
            "name": "user name",
            "add1": "Broadway",
            "country": "United States of America",
            "company": "X",
            "state": "New York",
            "scan_report_template_title": "Scan Results",
            "result_date": "01/28/2019 12:16:42",
            "role": "Manager",
            "add2": "Suite"
         },{
            "status": "Finished",
            "scanner_appliance": "1.1.1.1 (Scanner 10.10.10-1, Vulnerability Signatures 10.10.10-2)",
            "network": "Global Default Network",
            "reference": "scan/1533110666.07264",
            "ips": "1.1.1.1",
            "launch_date": "08/01/2018 08:04:26",
            "option_profile": "Initial Options",
            "total_hosts": "1",
            "scan_title": "My first scan",
            "duration": "00:06:20",
            "excluded_ips": "",
            "asset_groups": null,
            "type": "API",
            "active_hosts": "1"
        },{
            "protocol": "tcp",
            "qid": 86000,
            "results": "Server Version\\tServer Banner\\ncloudflare-nginx\\tcloudflare-nginx",
            "solution": "N/A",
            "ip_status": "host scanned, found vuln",
            "port": "80",
            "category": "Web server",
            "severity": "1",
            "title": "Web Server Version",
            "instance": null,
            "dns": "1dot1dot1dot1.cloudflare-dns.com",
            "ip": "1.1.1.1",
            "type": "Ig",
            "vendor_reference": null,
            "cve_id": null,
            "ssl": "no",
            "netbios": null,
            "associated_malware": null,
            "pci_vuln": "no",
            "impact": "N/A",
            "fqdn": "",
            "bugtraq_id": null,
            "threat": "N/A",
            "os": "Linux 3.13",
            "exploitability": null
         },{
            "target_distribution_across_scanner_appliances": "External : 1.1.1.1"
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Enrich Host

#### Description

Enrich a host with information from Qualys VMDR.

**Note:** The AssetView module is required.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
       {
         "EntityResult":
          {
           "LAST_VM_SCANNED_DATE": "2019-01-06T12: 39: 00Z",
           "LAST_VM_SCANNED_DURATION": "490",
           "NETWORK_ID": "0",
           "IP": "1.1.1.1",
           "LAST_VULN_SCAN_DATETIME": "2019-01-06T12: 39: 00Z",
           "COMMENTS": "AddedbyX",
           "TRACKING_METHOD": "IP",
           "DNS": "one.one.one.one",
           "OS": "Linux3.13",
           "ID": "54664176"
          },
        "Entity": "1.1.1.1"
       }
    ]
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
LAST_VM_SCANNED_DATE | Returns if it exists in JSON result  
LAST_VM_SCANNED_DURATION | Returns if it exists in JSON result  
NETWORK_ID | Returns if it exists in JSON result  
IP | Returns if it exists in JSON result  
LAST_VULN_SCAN_DATETIME | Returns if it exists in JSON result  
COMMENTS | Returns if it exists in JSON result  
TRACKING_METHOD | Returns if it exists in JSON result  
DNS | Returns if it exists in JSON result  
OS | Returns if it exists in JSON result  
ID | Returns if it exists in JSON result  
Entity | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one host (is_success=true):_ "The following hosts were enriched: {entity.identifier}."_If data is not available for one host (is_success=true):_ "Action wasn't able to enrich the following entities using information from Qualys VMDR: {entity.identifier}."_If data is not available for all hosts (is_success=false):_ "No hosts were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities"." Reason: {0}''.format(error.Stacktrace) | General  
  
### Download Report

#### Description

Fetch report by the ID.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Report ID | String | N/A | Yes | Report ID value.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "STATUS":
        {
         "STATE": "Finished"
         },
      "EXPIRATION_DATETIME": "2019-02-04T13:11:15Z",
      "TITLE": "Scan scan/1533110666.07264 Report",
      "USER_LOGIN": "sempf3mh",
      "OUTPUT_FORMAT": "PDF",
      "LAUNCH_DATETIME": "2019-01-28T13:11:14Z",
      "TYPE": "Scan",
      "ID": "775111",
      "SIZE": "22.17 KB"
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Launch Compliance Report

#### Description

You can run compliance scans and create compliance reports on hosts (IP addresses) that have been added to the PC.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Report Title | String | N/A | Yes | A user-defined report title. The title may have a maximum of 128 characters. For a PCI compliance report, the report title is provided by Qualys and cannot be changed.  
Report Type | String | N/A | Yes | Template name.  
Output Format | String | N/A | Yes | One output format may be specified. When output_format=pdf is specified, the Secure PDF Distribution may be used. Example: pdf, mht, and html  
IPs/Ranges | String | N/A | No | Specify IPs or ranges to change (override) the report target, as defined in the patch report template. Multiple IPs or ranges are comma-separated.  
Asset Groups | String | N/A | No | A comma-separated list of asset groups.  
Scan Reference | String | N/A | No | Show only a scan with a certain scan reference code.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
report_id | True/False | report_id:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Launch Patch Report

#### Description

Launch patch reports to find out about the patches you need to apply to fix your current vulnerabilities. You'll be able to use the links in this report to quickly download and install any missing patches.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Report Title | String | N/A | Yes | A user-defined report title. The title may have a maximum of 128 characters. For a PCI compliance report, the report title is provided by Qualys and cannot be changed.  
Report Type | String | N/A | Yes | Template name.  
Output Format | String | N/A | Yes | One output format may be specified. When output_format=pdf is specified, the Secure PDF Distribution may be used. Example: pdf, mht and html  
IPs/Ranges | String | N/A | No | Specify IPs or ranges to change (override) the report target, as defined in the patch report template. Multiple IPs or ranges are comma-separated.  
Asset Groups | String | N/A | No | Asset groups. If more than one has to be comma-separated.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
report_id | True/False | report_id:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Launch Remediation Report

#### Description

Launch remediation reports to get information on remediation tickets, like ticket status and overall trend information. You can choose from these reports:

  * Executive Remediation Report
  * Tickets per Asset Group
  * Tickets per User
  * Tickets per Vulnerability



#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Report Title | String | N/A | Yes | A user-defined report title. The title may have a maximum of 128 characters. For a PCI compliance report, the report title is provided by Qualys and cannot be changed.  
Report Type | String | N/A | Yes | Template name.  
Output Format | String | N/A | Yes | One output format may be specified. When output_format=pdf is specified, the Secure PDF Distribution may be used. Example: pdf, mht and html  
IPs/Ranges | String | N/A | No | Specify IPs or ranges to change (override) the report target, as defined in the patch report template. Multiple IPs or ranges are comma separated.  
Asset Groups | String | N/A | No | Asset groups. If more than one has to be comma-separated.  
Display Results For All tickets | Checkbox | Checked | No | Specifies whether the report includes tickets assigned to the current user (User is set by default), or all tickets in the user account. By default tickets assigned to the current user are included.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
report_id | True/False | report_id:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Launch Scan Report

#### Description

Launch a scan report.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Report Title | String | N/A | Yes | A user-defined report title. The title may have a maximum of 128 characters. For a PCI compliance report, the report title is provided by Qualys and cannot be changed.  
Report Type | String | N/A | Yes | Template name.  
Output Format | String | N/A | Yes | One output format may be specified. When output_format=pdf is specified, the Secure PDF Distribution may be used. Example: pdf, mht and html.  
IPs/Ranges | String | N/A | No | Specify IPs or ranges to change (override) the report target, as defined in the patch report template. Multiple IPs or ranges are comma-separated.  
Asset Groups | String | N/A | No | Asset groups. If more than one has to be comma-separated.  
Scan Reference | String | N/A | No | Show only a scan with a certain scan reference code.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
report_id | True/False | report_id:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Launch VM Scan and Fetch Results

#### Description

Launch vulnerability scan on a host in your network and fetch results.

**Note:** This action automatically adds new hosts to Qualys as assets. Note that the license limiting the number of hosts depends on your subscription.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Title | String | N/A | No | The scan title. It can be up to 2000 characters (ASCII) long.  
Processing Priority | String | N/A | Yes | Specify a value between 0 and 9 to set a processing priority level for the scan. When not specified, a value of 0 (no priority) is used. Valid values are:

  * 0 for No Priority (the default)
  * 1 for Emergency
  * 2 for Ultimate
  * 3 for Critical
  * 4 for Major
  * 5 for High
  * 6 for Standard
  * 7 for Medium
  * 8 for Minor
  * 9 for Low

  
Scan Profile | String | N/A | Yes | The title of the compliance option profile to be used. One of these parameters must be specified in a request:

  * option_title
  * option_id

  
Scanner Appliance | String | N/A | No | The friendly names of the scanner appliances to be used or "External" for external scanners. Multiple entries are comma-separated.  
Network | String | N/A | No | The ID of a network used to filter the IPs or ranges specified in the "ip" parameter. Set to a custom network ID. **Note:** This does not filter IPs or ranges specified in "asset_groups" or "asset_group_ids". Or set to "0" (the default) for the Global Default Network. This is used to scan hosts outside of your custom networks.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
username | Returns if it exists in JSON result  
city | Returns if it exists in JSON result  
zip | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
add1 | Returns if it exists in JSON result  
country | Returns if it exists in JSON result  
company | Returns if it exists in JSON result  
state | Returns if it exists in JSON result  
can_report_template_title | Returns if it exists in JSON result  
result_date | Returns if it exists in JSON result  
role | Returns if it exists in JSON result  
add2 | Returns if it exists in JSON result  
status | Returns if it exists in JSON result  
scanner_appliance | Returns if it exists in JSON result  
network | Returns if it exists in JSON result  
reference | Returns if it exists in JSON result  
ips | Returns if it exists in JSON result  
launch_date | Returns if it exists in JSON result  
option_profile | Returns if it exists in JSON result  
total_hosts | Returns if it exists in JSON result  
scan_title | Returns if it exists in JSON result  
duration | Returns if it exists in JSON result  
excluded_ips | Returns if it exists in JSON result  
asset_groups | Returns if it exists in JSON result  
type | Returns if it exists in JSON result  
active_hosts | Returns if it exists in JSON result  
protocol | Returns if it exists in JSON result  
qid | Returns if it exists in JSON result  
results | Returns if it exists in JSON result  
solution | Returns if it exists in JSON result  
severity | Returns if it exists in JSON result  
title | Returns if it exists in JSON result  
instance | Returns if it exists in JSON result  
dns | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
vendor_reference | Returns if it exists in JSON result  
cve_id | Returns if it exists in JSON result  
ssl | Returns if it exists in JSON result  
netbios | Returns if it exists in JSON result  
associated_malware | Returns if it exists in JSON result  
pci_vuln | Returns if it exists in JSON result  
fqdn | Returns if it exists in JSON result  
bugtraq_id | Returns if it exists in JSON result  
threat | Returns if it exists in JSON result  
os | Returns if it exists in JSON result  
exploitability | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
scan_ref | N/A | N/A  
  
##### JSON Result
    
    
    [
      {
        "username": "username",
        "city": "New York",
        "zip": "10024",
        "name": "user name",
        "add1": "Broadway",
        "country": "United States of America",
        "company": "X",
        "state": "New York",
        "scan_report_template_title": "Scan Results",
        "result_date": "01/28/2019 12:16:42",
        "role": "Manager",
        "add2": "Suite"
      },{
        "status": "Finished",
        "scanner_appliance": "1.1.1.1 (Scanner 10.10.10-1, Vulnerability Signatures 10.10.10-2)",
        "network": "Global Default Network",
        "reference": "scan/1533110666.07264",
        "ips": "1.1.1.1",
        "launch_date": "08/01/2018 08:04:26",
        "option_profile": "Initial Options",
        "total_hosts": "1",
        "scan_title": "My first scan",
        "duration": "00:06:20",
        "excluded_ips": "",
        "asset_groups": null,
        "type": "API",
        "active_hosts": "1"
      },{
        "protocol": "tcp",
        "qid": 86000,
        "results": "Server VersiontServer Banner\\ncloudflare-nginx\\tcloudflare-nginx",
        "solution": "N/A",
        "ip_status": "host scanned, found vuln",
        "port": "80",
        "category": "Web server",
        "severity": "1",
        "title": "Web Server Version",
        "instance": null,
        "dns": "1dot1dot1dot1.cloudflare-dns.com",
        "ip": "1.1.1.1",
        "type": "Ig",
        "vendor_reference": null,
        "cve_id": null,
        "ssl": "no",
        "netbios": null,
        "associated_malware": null,
        "pci_vuln": "no",
        "impact": "N/A",
        "fqdn": "",
        "bugtraq_id": null,
        "threat": "N/A",
        "os": "Linux 3.13",
        "exploitability": null
       },{
        "target_distribution_across_scanner_appliances": "External : 1.1.1.1"
       }
    ]
    

### List Groups

#### Description

List of asset groups in the user's account.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "TITLE": "All",
       "IP_SET":
          {
            "IP": ["1.1.1.1"]
           },
       "DOMAIN_LIST":
          {
            "DOMAIN":
              [{
                 "@network_id": "0",
                 "#text": "google.com"
               },{
                 "@network_id": "0",
                 "#text": "none",
                 "@netblock": "1.1.1.1-1.1.1.1"
               }]
          },
       "LAST_UPDATE": "2018-07-25T14:56:05Z",
       "NETWORK_ID": "0",
       "OWNER_USER_NAME": "Global User",
       "BUSINESS_IMPACT": "High",
       "ID": "1111"
     },{
       "TITLE": "G",
       "NETWORK_ID": "0",
       "LAST_UPDATE": "2018-08-13T08:14:55Z",
       "OWNER_USER_NAME": "user (Manager)",
       "OWNER_USER_ID": "11111",
       "BUSINESS_IMPACT": "High",
       "ID": "11111"
     }]
    

##### Entity Enrichment

N/A ##### Insights

N/A

### List IPs

#### Description

List of IP addresses in the user's account. By default, all hosts in the user's account are included.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ip_list | True/False | ip_list:False  
  
##### JSON Result
    
    
    [
      "1.1.1.1",
      "1.1.100.100",
      "10.10.10.10"
    ]
    

##### Entity Enrichment

N/A ##### Insights

N/A

### List Reports

#### Description

List of reports in the user's account when the Report Share feature is enabled. The report list output includes all report types, including scorecard reports.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
        "STATUS":
          {
            "STATE": "Finished"
          },
        "EXPIRATION_DATETIME": "2019-02-04T13:11:15Z",
        "TITLE": "Scan scan/1533110666.07264 Report",
        "USER_LOGIN": "sempf3mh",
        "OUTPUT_FORMAT": "PDF",
        "LAUNCH_DATETIME": "2019-01-28T13:11:14Z",
        "TYPE": "Scan",
        "ID": "775111",
        "SIZE": "22.17 KB"
      }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

### List Scans

#### Description

List of scans launched within the past 30 days.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
        [
           {
             "STATUS":
               {
                  "STATE": "Finished"
               },
            "TARGET": "1.1.1.1",
            "TITLE": "Test Scan",
            "USER_LOGIN": "sempf3mh",
            "LAUNCH_DATETIME": "2019-01-06T12:29:52Z",
            "PROCESSED": "1",
            "REF": "scan/1546777792.44756",
            "PROCESSING_PRIORITY": "0 - No Priority",
            "DURATION": "00:08:24",
            "TYPE": "On-Demand"
           }
         ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### List Endpoint Detections

#### Description

List endpoint detections in Qualys VMDR.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Status Filter | CSV | new, active, re-opened | No | Specify a comma-separated list of statuses that should be used during ingestion. If nothing is provided, the action ingests detections with "New, Active, Re-Opened" statuses. Possible values: New, Active, Fixed, Re-Opened.  
Ingest Ignored Detections | Checkbox | Unchecked | No | If enabled, the action also returns ignored detections.  
Ingest Disabled Detections | Checkbox | Unchecked | No | If enabled, the action also returns disabled detections.  
Lowest Severity To Fetch | DDL | Medium | No | Specify the lowest severity that is used to fetch detections.  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing information about vulnerabilities found on the entity.  
Max Detections To Return | Integer | 50 | No | Specify the number of detections to return per entity. Maximum: 200  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data for at least one endpoint is found (is_success=true):_ "Successfully listed detections related to the following endpoints in Qualys VMDR: {entity.identifier}_If one endpoint is not found or invalid IP is provided (is_success=true):_ "Action wasn't able to find the following endpoints in Qualys VMDR: {entity.identifier}."I _f no data for at least one endpoint is found (is_success=true):_ "No vulnerabilities were found for the following endpoints: {entity.identifier}."_If no data for all endpoints is found (is_success=true):_ "No vulnerabilities were found for the provided endpoints."_If no endpoints are found or invalid IP is provided (is_success=false):_ "Provided endpoints were not found in Qualys VMDR."__**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Endpoint Detections''. Reason: {0}''.format(error.Stacktrace) _If invalid "Status Filter" is reported:_ "Error executing action "List Endpoint Detections''." Reason: invalid value provided for the parameter "Status Filter": {value}. Possible values: new, open, reopened, fixed. | General  
Case Wall | **Table Columns:**

  * QID
  * Title
  * Severity
  * Diagnosis
  * Consequences
  * Solution
  * Patchable
  * Category

| Entity  
  
## Connectors

### Qualys VM - Detections Connector

#### Description

Pull detections from Qualys VMDR.

**Note:** Whitelist works with the "Type" parameter.

#### Configure Qualys VM - Detections Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | Event Type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 300 | Yes | Timeout limit for the python process running the current script.  
API root | String | N/A |  | API Root of the Qualis VM instance.  
Username | String | N/A | Yes | Username of the Qualis VM instance.  
Password | Password | N/A | Yes | Password of the Qualis VM instance.  
Lowest Severity To Fetch | Integer | 0 | No | Lowest severity that will be used to fetch detections. If nothing is provided, the connector will fetch all detections. Maximum: 5.  
Status Filter | CSV | NEW, ACTIVE, REOPENED | No | Status filter for the connector. If nothing is provided, the connector will ingest detections with "New, Active, Reopened" statuses. Possible values: NEW, ACTIVE, FIXED, REOPENED.  
Ingest Ignored Detections | Checkbox | Unchecked | No | If enabled, the connector will ingest ignored detections.  
Ingest Disabled Detections | Checkbox | Unchecked | No | If enabled, the connector will ingest disabled detections.  
Grouping Mechanism | String | Detection | Yes | Grouping mechanism that will be used to create Google SecOps alerts. Possible values: Host, Detection, None. If Host is provided, the connector will create 1 Google SecOps alert containing all of the detection related to the host. If Detection is provided, the connector will create 1 Google SecOps alert containing information about all of the hosts that have that detection. If None or invalid value is provided, the connector will create a new Google SecOps alert for each separate detection per host.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Qualys VMDR server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
X-Requested-With Header | String | Google SecOps SOAR | No | The value for the `X-Requested-With` HTTP header used to identify the source of the API requests.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
