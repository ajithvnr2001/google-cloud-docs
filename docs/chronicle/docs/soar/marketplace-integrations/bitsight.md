---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/bitsight/
title: BitSight \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:06.978322+00:00
---

# BitSight  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/bitsight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BitSight

This document describes how to integrate BitSight with Google Security Operations.

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.bitsighttech.com | Yes | API root of the BitSight instance.  
API Key | String | N/A | Yes | API key of the BitSight account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the BitSight server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

### How to generate API Key

To generate API Key, follow steps described in the [API Token Management](https://help.bitsighttech.com/hc/en-us/articles/115014888388-API-Token-Management) document available within the BitSight Product Documentation.

## Actions

### Get Company Details

#### Description

Get information about a company in BitSight.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Company Name | String | N/A | Yes | Specify the name of the company for which you want to return details.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "rating": "{rating from first response}"
      "guid": "a940bb61-33c4-42c9-9231-c8194c305db3",
      "custom_id": null,
      "name": "Saperix, Inc.",
      "description": "Saperix Technologies LLC develops risk analysis software solutions.",
      "ipv4_count": 4320,
      "people_count": 500,
      "shortname": "Saperix",
      "industry": "Technology",
      "industry_slug": "technology",
      "sub_industry": "Computer & Network Security",
      "sub_industry_slug": "computer_network_security",
      "homepage": "http://www.saperix.com",
      "primary_domain": "saperix.com",
      "type": "CURATED",
      "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/overview/",
      "rating_details": {
          "botnet_infections": {
              "name": "Botnet Infections",
              "rating": 730,
              "grade": "C",
              "percentile": 61,
              "grade_color": "#ecb870",
              "category": "Compromised Systems",
              "category_order": 0,
              "beta": false,
              "order": 0,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/compromised-systems/?filter=Botnet%20Infections"
          },
          "spam_propagation": {
              "name": "Spam Propagation",
              "rating": 820,
              "grade": "A",
              "percentile": 100,
              "grade_color": "#2c4d7f",
              "category": "Compromised Systems",
              "category_order": 0,
              "beta": false,
              "order": 1,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/compromised-systems/?filter=Spam%20Propagation"
          },
          "malware_servers": {
              "name": "Malware Servers",
              "rating": 820,
              "grade": "A",
              "percentile": 100,
              "grade_color": "#2c4d7f",
              "category": "Compromised Systems",
              "category_order": 0,
              "beta": false,
              "order": 2,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/compromised-systems/?filter=Malware%20Servers"
          },
          "unsolicited_comm": {
              "name": "Unsolicited Communications",
              "rating": 820,
              "grade": "A",
              "percentile": 100,
              "grade_color": "#2c4d7f",
              "category": "Compromised Systems",
              "category_order": 0,
              "beta": false,
              "order": 3,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/compromised-systems/?filter=Unsolicited%20Communications"
          },
          "potentially_exploited": {
              "name": "Potentially Exploited",
              "rating": 580,
              "grade": "F",
              "percentile": 15,
              "grade_color": "#b24053",
              "category": "Compromised Systems",
              "category_order": 0,
              "beta": false,
              "order": 4,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/compromised-systems/?filter=Potentially%20Exploited"
          },
          "spf": {
              "name": "SPF",
              "rating": 770,
              "grade": "B",
              "percentile": 81,
              "grade_color": "#526d96",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 5,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=spf"
          },
          "dkim": {
              "name": "DKIM",
              "rating": 700,
              "grade": "C",
              "percentile": 55,
              "grade_color": "#ecb870",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 6,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=dkim"
          },
          "ssl_certificates": {
              "name": "SSL Certificates",
              "rating": 760,
              "grade": "B",
              "percentile": 77,
              "grade_color": "#526d96",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 7,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=certificate"
          },
          "ssl_configurations": {
              "name": "SSL Configurations",
              "rating": 680,
              "grade": "C",
              "percentile": 48,
              "grade_color": "#ecb870",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 8,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=ssl"
          },
          "open_ports": {
              "name": "Open Ports",
              "rating": 760,
              "grade": "B",
              "percentile": 77,
              "grade_color": "#526d96",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 9,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=open_port"
          },
          "application_security": {
              "name": "Web Application Headers",
              "rating": 480,
              "grade": "F",
              "percentile": 6,
              "grade_color": "#b24053",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 10,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=http_headers"
          },
          "patching_cadence": {
              "name": "Patching Cadence",
              "rating": 720,
              "grade": "C",
              "percentile": 61,
              "grade_color": "#ecb870",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 11,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=pc"
          },
          "insecure_systems": {
              "name": "Insecure Systems",
              "rating": 620,
              "grade": "D",
              "percentile": 34,
              "grade_color": "#c77481",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 12,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=insecure_sys"
          },
          "server_software": {
              "name": "Server Software",
              "rating": 810,
              "grade": "A",
              "percentile": 99,
              "grade_color": "#2c4d7f",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 13,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=server_software"
          },
          "desktop_software": {
              "name": "Desktop Software",
              "rating": 470,
              "grade": "F",
              "percentile": 5,
              "grade_color": "#b24053",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 14,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=endpoint_pc"
          },
          "mobile_software": {
              "name": "Mobile Software",
              "rating": 590,
              "grade": "D",
              "percentile": 25,
              "grade_color": "#c77481",
              "category": "Diligence",
              "category_order": 1,
              "beta": false,
              "order": 15,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=endpoint_mobile"
          },
          "dnssec": {
              "name": "DNSSEC",
              "rating": 300,
              "grade": "F",
              "percentile": 0,
              "grade_color": "#b24053",
              "category": "Diligence",
              "category_order": 1,
              "beta": true,
              "order": 16,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=dnssec"
          },
          "mobile_application_security": {
              "name": "Mobile Application Security",
              "rating": "N/A",
              "grade": "N/A",
              "percentile": "N/A",
              "grade_color": "#495057",
              "category": "Diligence",
              "category_order": 1,
              "beta": true,
              "order": 17,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/diligence-details/?filter=mobile_appsec"
          },
          "file_sharing": {
              "name": "File Sharing",
              "rating": 550,
              "grade": "F",
              "percentile": 11,
              "grade_color": "#b24053",
              "category": "User Behavior",
              "category_order": 2,
              "beta": false,
              "order": 18,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/user-behavior"
          },
          "data_breaches": {
              "name": "Security Incidents",
              "rating": 810,
              "grade": "A",
              "percentile": 90,
              "grade_color": "#2c4d7f",
              "category": "Public Disclosures",
              "category_order": 3,
              "beta": false,
              "order": 19,
              "display_url": "https://service.bitsighttech.com/app/company/a940bb61-33c4-42c9-9231-c8194c305db3/rating-details/?vector=news"
          }
      },
      "search_count": 11185,
      "subscription_type": "Total Risk Monitoring",
      "sparkline": "https://api.bitsighttech.com/ratings/v1/companies/a940bb61-33c4-42c9-9231-c8194c305db3/sparkline?size=small",
      "subscription_type_key": "continuous_monitoring",
      "subscription_end_date": null,
      "bulk_email_sender_status": "NONE",
      "service_provider": false,
      "customer_monitoring_count": 232,
      "available_upgrade_types": [],
      "has_company_tree": true,
      "has_preferred_contact": true,
      "is_bundle": false,
      "rating_industry_median": "below",
      "primary_company": {
          "guid": "eed24cfa-c3ea-4467-aefa-89648881e277",
          "name": "Saperix Corporate"
      },
      "permissions": {
          "can_manage_primary_company": true,
          "can_annotate": true,
          "can_view_ip_attributions": true,
          "can_view_infrastructure": true,
          "can_view_forensics": true,
          "can_download_company_report": true,
          "can_view_company_reports": true,
          "can_view_service_providers": true,
          "can_request_self_published_entity": true,
          "has_control": true
      },
      "is_primary": false,
      "security_grade": null,
      "in_spm_portfolio": true,
      "is_mycomp_mysubs_bundle": false,
      "company_features": [],
      "compliance_claim": {
          "trust_page": "https://saperix.com/compliance",
          "certifications": [
              {
                  "name": "SOC 2 Type 2",
                  "slug": "soc-2-type-2"
              },
              {
                  "name": "ISO-27001",
                  "slug": "iso-27001"
              },
              {
                  "name": "ISO-9001",
                  "slug": "iso-9001"
              },
              {
                  "name": "GDPR",
                  "slug": "gdpr"
              },
              {
                  "name": "PCI DSS",
                  "slug": "pci-dss"
              },
              {
                  "name": "NIST CSF",
                  "slug": "nist-csf"
              }
          ]
      },
      "is_csp": false,
      "related_companies": []
    }
    

##### Case Wall

Result type | Value / Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If returned company information (is_success=true):_ "Successfully returned information about the "{name}" company in BitSight.**The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "Get Company Details". Reason: {0}''.format(error.Stacktrace)_If the company is not found:_ "Error executing action "Get Company Details". Reason: company "{name}" wasn't found in BitSight. Please check the spelling.'  | General  
Case Wall Table | **Company "{name}" Details**

  * Name name
  * Description description industry Sub_industry
  * Certification - CSV of compliance_claim/certifications/name
  * Rating - rating

| General  
Link | display\\_url | General  
  
### List Company Highlights

#### Description

List highlights related to the company in BitSight.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Company Name | String | N/A | Yes | Specify the name of the company for which you want to return highlights.  
Time Frame | DDL | Last MonthPossible values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| No | Specify a time frame for the results.If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results.This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter.Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results.If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.Format: ISO 8601.  
Max Highlights To Return | Integer | 20 | No | Specify the number of highlights you want to return.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
          "date": "2022-07-11",
          "guid": "97239caf-40de-4236-b0b2-d1bd1094098d",
          "start_score": 530,
          "end_score": 510,
          "reasons": [
              {
                  "start_percentile": 100.0,
                  "risk_vector": "botnet",
                  "evidence": [
                      {
                          "type": "infection",
                          "name": "ZeroAccess",
                          "kbid": 117
                      }
                  ],
                  "start_score": 820,
                  "end_percentile": 82.0,
                  "end_score": 780
              }
          ],
          "type": "rating-change",
          "entity": "a940bb61-33c4-42c9-9231-c8194c305db3"
      },
      {
          "date": "2022-06-30",
          "guid": "d76ea1c3-cfc0-4d27-82c2-dd8da2df13e0",
          "start_score": 560,
          "end_score": 540,
          "reasons": [
              {
                  "start_percentile": 79.0,
                  "risk_vector": "torrent",
                  "evidence": [
                      {
                          "end_grade": "D",
                          "start_grade": "B"
                      }
                  ],
                  "start_score": 750,
                  "end_percentile": 36.0,
                  "end_score": 640
              }
          ],
          "type": "rating-change",
          "entity": "a940bb61-33c4-42c9-9231-c8194c305db3"
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If returned company information (is_success=true):_ "Successfully returned information about the "{name}" company highlights in BitSight._If company information is not found (is_success=true):_ "No highlights were found for the "{name}" company in BitSight.**The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "List Company Highlights". Reason: {0}''.format(error.Stacktrace)_If the company is not found:_ "Error executing action "List Company Highlights". Reason: company "{name}" wasn't found in BitSight. Please check the spelling.' | General  
  
### List Company Vulnerabilities

#### Description

List vulnerabilities related to the company in BitSight.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Company Name | String | N/A | Yes | Specify the name of the company for which you want to return highlights.  
Only High Confidence | Checkbox | Checked | No | If enabled, the action only returns vulnerabilities with high confidence.  
Max Vulnerabilities To Return | Integer | 50 | No | Specify the number of vulnerabilities you want to return.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "start_date": "2022-10-02",
      "end_date": "2022-10-09",
      "stats": [
          {
              "id": "CVE-2008-0455",
              "name": "CVE-2008-0455",
              "first_seen": "2021-07-15",
              "event_count": 4,
              "host_count": 4,
              "confidence": "LOW",
          },
          {
              "id": "CVE-2010-1452",
              "name": "CVE-2010-1452",
              "first_seen": "2021-07-15",
              "event_count": 4,
              "host_count": 4,
              "confidence": "LOW",
          }
      ]
    }
    

##### Case Wall

Result type | Value / Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If returned company information (is_success=true):_ "Successfully returned information about the "{name}" company vulnerabilities in BitSight._If company information is not found (is_success=true):_ "No vulnerabilities were found for the "{name}" company in BitSight.**The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Error executing action "List Company Highlights". Reason: {0}''.format(error.Stacktrace)_If the company is not found:_ "Error executing action "List Company Highlights". Reason: company "{name}" wasn't found in BitSight. Please check the spelling.' | General  
Case Wall Table | **Company "{name}" Vulnerabilities**

  * ID - id
  * Name - name
  * First Seen - first_seen
  * Event Count - event_count
  * Affected Hosts - host_count
  * Confidence - confidence

| General  
  
### Ping

#### Description

Test connectivity to BitSight with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run on

This action doesn't run on the entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description |   
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful (is_success=true):_ ****"Successfully connected to the BitSight server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful (is_success= false):****_"Failed to connect to the BitSight server! Error is {0}".format(exception.stacktrace) | General  
  
## Connectors

### BitSight - Alerts Connector

#### Description

Pull information about alerts from BitSight.

**Note:** The dynamic list filter works with the "trigger" parameter.

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | siemplify_type | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | trigger | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://api.bitsighttech.com | Yes | API root of the BitSight instance.  
API Key | String | N/A | Yes | API key of the BitSight account.  
Lowest Severity Score To Fetch | String | WARN | No | The lowest severity that needs to be used to fetch insights. Possible values: Informational, Increase,Warn, Critical. If nothing is specified, the connector ingests alerts with all severities.  
Max Days Backwards | Integer | 1 | No | Specify the number of days from where to fetch alerts.  
Max Alerts To Fetch | Integer | 20 | No | Specify the number of alerts to process per one connector iteration.  
Use dynamic list as a blacklist | Checkbox | Unchecked | Yes | If enabled, the dynamic list is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Crowdstrike server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
