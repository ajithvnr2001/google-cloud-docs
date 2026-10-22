---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/apivoid/
title: Integrate APIVoid with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:48.244391+00:00
---

# Integrate APIVoid with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/apivoid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate APIVoid with Google SecOps 

This document describes how to integrate APIVoid with Google Security Operations (Google SecOps).

## Before you begin

Before you configure the APIVoid integration in Google SecOps for v2, verify that you have the following:

  * **APIVoid v2 Account** : An active account with access to v2 API services.

  * **APIVoid v2 API key** : A new API key generated specifically for v2 APIs from your APIVoid user dashboard.

  * **Updated API endpoints** : Familiarity with the updated v2 API endpoint URLs for the specific APIVoid services you plan to use (such as, IP Reputation API, Domain Reputation API).




### Generate an APIVoid v2 API key

To generate your APIVoid v2 API key, complete these steps:

  1. Sign in to your APIVoid [user dashboard](https://www.apivoid.com/).

  2. Navigate to the **API Keys** section. (The location may vary depending on dashboard updates.)

  3. Generate a new API Key. Immediately copy and store the key securely. It may only be displayed once.




### Network

Function | Default port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Root | String | https://endpoint.apivoid.com | Yes | Address of the APIVoid instance.  
Api Key | Password | N/A | Yes | API key generated in APIVoid's console.  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your APIVoid connection requires an SSL verification.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Domain Reputation

Get domain reputation checks if a domain is excluded by a popular and trusted domain blocklist services, such as URLVir, ThreatLog, OpenPhish, Spam404, PhishTank, ZeuS Tracker, and more. The multiple domain blocklist services identify potentially malicious and fraudulent websites involved in malware distribution, phishing incidents, and fake online shops.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Threshold | String | 0 | Yes | Domain risk threshold. The threshold must be a numeric value. Example: 3  
Create Insights | Checkbox | Checked | Yes | Specify whether the action should create insights or not.  
  
#### Use cases

One of the use cases of Domain Reputation API is to check if the client's websites are excluded, check URLs submitted by users on your application, or to identify potentially malicious and unsafe websites.

#### Run on

This action runs on the following entities:

  * Hostname
  * URL



#### Action results

##### Entity enrichment

Mark entity as suspicious if the number of negative engines is equal or above the given threshold.

Enrichment field name | Logic - When to apply  
---|---  
alexa_top_100k | Returns if it exists in JSON result  
domain_length | Returns if it exists in JSON result  
alexa_top_10k | Returns if it exists in JSON result  
blacklists | Returns if it exists in JSON result  
server | Returns if it exists in JSON result  
host | Returns if it exists in JSON result  
most_abused_tld | Returns if it exists in JSON result  
alexa_top_250k | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
Warn | A warning insight is created to inform on the malicious status of the enriched entity. The is created when the number of detected engines equals or exceeds the minimum suspicious Threshold set before scan.  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "alexa_top_100k": false,
                "domain_length": 17,
                "alexa_top_10k": false,
                "blacklists": {
                    "scantime": "0.07",
                    "detection_rate": "0%",
                    "detections": 0,
                    "engines_count": 29,
                    "engines": [{
                        "engine": "ThreatLog",
                        "detected": false,
                        "confidence": "high",
                        "reference": "http://www.threatlog.com/"
                    }, {
                        "engine": "Threat Sourcing",
                        "detected": false,
                        "confidence": "high",
                        "reference": "https://www.threatsourcing.com/"
                    }, {
                        "engine": "URLVir",
                        "detected": false,
                        "confidence": "high",
                        "reference": "http://www.urlvir.com/"
                    }]},
                "server": {
                    "region_name": null,
                    "reverse_dns": " ",
                    "ip": " ",
                    "isp": null,
                    "continent_code": null,
                    "latitude": null,
                    "city_name": null,
                    "longitude": null,
                    "country_code": null,
                    "country_name": null,
                    "continent_name": null
                },
                "host": "example.com",
                "most_abused_tld": false,
                "alexa_top_250k": false
            },
            "Entity": "example.com"
        }, {
            "EntityResult": {
                "alexa_top_100k": false,
                "domain_length": 9,
                "alexa_top_10k": false,
                "blacklists": {
                    "scantime": "0.03",
                    "detection_rate": "0%",
                    "detections": 0,
                    "engines_count": 29,
                    "engines": [{
                        "engine": "ThreatLog",
                        "detected": false,
                        "confidence": "high",
                        "reference": "http://www.threatlog.com/"
                    }, {
                        "engine": "Threat Sourcing",
                        "detected": false,
                        "confidence": "high",
                        "reference": "https://www.threatsourcing.com/"
                    }, {
                        "engine": "URLVir",
                        "detected": false,
                        "confidence": "high",
                        "reference": "http://www.urlvir.com/"
                    }]},
                "server": {
                    "region_name": null,
                    "reverse_dns": " ",
                    "ip": " ",
                    "isp": null,
                    "continent_code": null,
                    "latitude": null,
                    "city_name": null,
                    "longitude": null,
                    "country_code": null,
                    "country_name": null,
                    "continent_name": null
                },
                "host": "192.0.2.1",
                "most_abused_tld": false,
                "alexa_top_250k": false
            },
            "Entity": "192.0.2.1"
        }
    ]
    

### Get Ip Reputation

IP Reputation API detects potentially malicious IP addresses which are commonly used for spam, website attacks or fraudulent activity.

#### Parameters

Parameter | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Threshold | String | N/A | Yes | IP risk threshold. The threshold must be a numeric value. Example: 3.  
Create Insights | Checkbox | Checked | Yes | Specify whether the action should create insights or not.  
  
#### Run on

This action runs on the IP Address entity.

#### Action results

##### Entity enrichment

Mark entity as suspicious if the number of negative engines is equal or above the given threshold.

Enrichment field name | Logic - When to apply  
---|---  
information | Returns if it exists in JSON result  
blacklists | Returns if it exists in JSON result  
anonymity | Returns if it exists in JSON result  
ip | Returns if it exists in JSON result  
  
##### Insights

Severity | Description  
---|---  
Warn | A warning insight is created to inform on the malicious status of the enriched hash. The insight is created when the number of detected engines equals or exceeds the minimum suspicious Threshold set before scan.  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
success | True/False | success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "information": {
                    "is_proxy": false,
                    "is_vpn": false,
                    "region_name": "Zhejiang",
                    "is_webproxy": false,
                    "latitude": 28.680280685424805,
                    "isp": "ChinaNet Zhejiang Province Network",
                    "continent_code": "AS",
                    "is_tor": false,
                    "reverse_dns": " ",
                    "detections": 18,
                    "engines_count": 76,
                    "longitude": 121.44277954101562,
                    "city_name": "Jiaojiang",
                    "country_name": "China",
                    "continent_name": "Asia",
                    "detection_rate": "24%",
                    "country_code": "CN",
                    "is_hosting": false
                },
                "blacklists": {
                    "scantime": "0.57",
                    "detection_rate":
                    "24%",
                    "detections": 18,
                    "engines_count": 76,
                    "engines": [{
                        "engine": "PlonkatronixBL",
                        "detected": false,
                        "reference": "http://bl.plonkatronix.com/"
                    }, {
                        "engine": "Engine",
                        "detected": true,
                        "reference": "https://home.nuug.no/~engine/"
                    }, {"engine": "Malc0de",
                        "detected": false,
                        "reference": "http://malc0de.com/database/index.php"
                       }]},
                "anonymity": {
                    "is_tor": false,
                    "is_proxy": false,
                    "is_vpn": false,
                    "is_webproxy": false,
                    "is_hosting": false
                },
                "ip": "192.0.2.1"
            },
            "Entity": "192.0.2.1"
        }
    ]
    

### Get URL Reputation

Get safety reputation and risk score of a URL.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Threshold | Integer | N/A | Yes | URL risk threshold. The threshold must be a numeric value. Example: 3  
  
#### Use cases

An analyst can retrieve the URL reputation, similar to how to retrieve the reputation of a domain or IP address.

#### Run on

This action runs on the URL entity.

#### Action results

##### Entity enrichment

Mark entity as suspicious if the number of negative engines is equal or above the given threshold. if data.get("report", {}).get("risk_score", {}).get("result") > threshold

Enrichment field name | Logic - When to apply  
---|---  
domain_blacklist | Returns if it exists in JSON result  
html_forms | Returns if it exists in JSON result  
server_details | Returns if it exists in JSON result  
response_headers | Returns if it exists in JSON result  
redirection | Returns if it exists in JSON result  
file_type | Returns if it exists in JSON result  
risk_score | Returns if it exists in JSON result  
security_checks | Returns if it exists in JSON result  
geo_location | Returns if it exists in JSON result  
url_parts | Returns if it exists in JSON result  
site_category | Returns if it exists in JSON result  
web_page | Returns if it exists in JSON result  
dns_records | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "domain_blacklist": {
                    "detections": 0,
                    "engines": [{
                        "detected": false,
                            "name": "SpamhausDBL", "reference": "https://www.spamhaus.org/lookup/"
                        }, {
                            "detected": false,
                            "name": "ThreatLog",
                            "reference": "http://www.threatlog.com/"
                        }, {
                            "detected": false,
                            "name": "OpenPhish",
                            "reference": "http://www.openphish.com/"
                        }, {
                            "detected": false,
                            "name": "PhishTank",
                            "reference": "http://www.phishtank.com/"
                        }, {
                            "detected": false,
                            "name": "Phishing.Database",
                            "reference": "https://github.com/mitchellkrogza/Phishing.Database"
                        }, {
                            "detected": false,
                            "name": "PhishStats",
                            "reference": "https://phishstats.info/"
                        }, {
                            "detected": false,
                            "name": "URLVir",
                            "reference": "http://www.urlvir.com/"
                        }, {
                            "detected": false,
                            "name": "URLhaus",
                            "reference": "https://urlhaus.abuse.ch/"
                        }, {
                            "detected": false,
                            "name": "RPiList Not Serious",
                            "reference": "https://github.com/RPiList/specials"
                        }, {
                            "detected": false,
                            "name": "precisionsec",
                            "reference": "https://precisionsec.com/"
                        }, {
                            "detected": false,
                            "name": "AntiSocial Blacklist",
                            "reference": "https://theantisocialengineer.com/"
                        }, {
                            "detected": false,
                            "name": "PhishFeed",
                            "reference": "https://phishfeed.com/"
                        }, {
                            "detected": false,
                            "name": "Spam404",
                            "reference": "https://www.spam404.com/"
                        }]},
                "html_forms": {
                    "number_of_total_input_fields": 0,
                    "email_field_present": false,
                    "number_of_total_forms": 0,
                    "password_field_present": false,
                    "two_text_inputs_in_a_form": false,
                    "credit_card_field_present": false
                },
                "server_details": {
                    "continent_name": "Asia",
                    "hostname": "example.com",
                    "region_name": "Seoul-teukbyeolsi",
                    "ip": "192.0.2.141",
                    "isp": "Example Corporation",
                    "continent_code": "AS",
                    "country_name": "Korea (Republic of)",
                    "city_name": "Seoul",
                    "longitude": 126.97782897949219,
                    "country_code": "KR",
                    "latitude": 37.568260192871094
                },
                "response_headers": {
                    "status": "HTTP/1.1 404 Not Found",
                    "content-length": "177",
                    "code": 404,
                    "server": "nginx/1.4.6 (Ubuntu)",
                    "connection": "keep-alive",
                    "date": "Wed, 15 Jul 2020 08:21:54 GMT",
                    "content-type": "text/html"
                },
                "redirection": {
                    "url": null,
                    "found": false,
                    "external": false
                },
                "file_type": {
                    "headers": "HTML",
                    "extension": "HTML",
                    "signature": " "
                },
                "risk_score": {
                    "result": 10
                },
                "security_checks": {
                    "is_suspended_page": false,
                    "is_defaced_heuristic": false,
                    "is_windows_exe_file": false,
                    "is_credit_card_field": false,
                    "is_windows_exe_file_on_free_hosting": false,
                    "is_masked_linux_elf_file": false,
                    "is_exe_on_directory_listing": false,
                    "is_php_on_directory_listing": false,
                    "is_masked_windows_exe_file": false,
                    "is_sinkholed_domain": false,
                    "is_robots_noindex": false,
                    "is_windows_exe_file_on_free_dynamic_dns": false,
                    "is_doc_on_directory_listing": false,
                    "is_non_standard_port": false,
                    "is_linux_elf_file_on_free_dynamic_dns": false,
                    "is_suspicious_domain": false, "is_suspicious_url_pattern": false,
                    "is_china_country": false,
                    "is_risky_geo_location": false,
                    "is_pdf_on_directory_listing": false,
                    "is_valid_https": false,
                    "is_external_redirect": false, "is_windows_exe_file_on_ipv4": false,
                    "is_phishing_heuristic": false,
                    "is_linux_elf_file_on_ipv4": false,
                    "is_email_address_on_url_query": false,
                    "is_uncommon_clickable_url": false,
                    "is_most_abused_tld": false,
                    "is_domain_blacklisted": false,
                    "is_host_an_ipv4": false,
                    "is_linux_elf_file_on_free_hosting": false,
                    "is_zip_on_directory_listing": false,
                    "is_password_field": false,
                    "is_linux_elf_file": false,
                    "is_empty_page_title": false,
                    "is_directory_listing": false,
                    "is_masked_file": false,
                    "is_suspicious_file_extension": false,
                    "is_suspicious_content": false
                },
                "geo_location": {
                    "countries": ["KR"]
                },
                "url_parts": {
                    "host_nowww": "example.com",
                    "host": "www.example.com",
                    "path": "/dynamic/example.html",
                    "query": null,
                    "scheme": "http",
                    "port": 80},
                "site_category": {
                    "is_vpn_provider": false,
                    "is_url_shortener": false,
                    "is_anonymizer": false,
                    "is_torrent": false,
                    "is_free_dynamic_dns": false,
                    "is_free_hosting": false
                },
                "web_page": {
                    "keywords": "",
                    "description": "",
                    "title": "404 Not Found"
                },
                "dns_records": {
                    "ns": {
                        "records": [{
                            "country_name": "Korea (Republic of)",
                            "ip": "192.0.2.95",
                            "isp": "Example Corporation",
                            "target": "example.com",
                            "country_code": "KR"
                        }, {
                            "country_name": "Korea (Republic of)",
                            "ip": "192.0.2.26",
                            "isp": "LX",
                            "target": "example.com",
                            "country_code": "KR"
                        }]},
                    "mx": {
                        "records": []
                    }}},
            "Entity": "www.example.com:80/dynamic/example.html"
        }
    ]
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | 

  1. _Successful entities:_ "APIVoid: Fetched reputation for the following entities: <entities identifer list>
  2. _Failed entities:_ "An error occurred on the following entities: <entities identifer list>"
  3. _Missing entities (no data):_ 'Can not found reputation for the following entities: <entities identifer list>"
  4. _Alert without URL entities:_ "APIVoid: No URLs found."

| General  
CSV Case wall | If data available create new entity csv table:

  1. domain blocklist report: data.get("report",{}).get("domain_blacklist",{}).get("engines", [])

| General  
Enrichment | If data available add the following as entity enrichment: (don't forget to add prefix "APIVoid")

  1. geo_location: data.get("report",{}).get("geo_location",{}).get("countries", [])
  2. is_suspicious_domain: data.get("report",{}).get("security_checks",{}).get("is_suspicious_domain")
  3. is_domain_blacklisted: data.get("report",{}).get("security_checks",{}).get("is_domain_blacklisted")
  4. is_risky_geo_location: data.get("report",{}).get("security_checks",{}).get("is_risky_geo_location")
  5. risk_score: data.get("report", {}).get("risk_score", {}).get("result")
  6. is_external_redirect: data.get("report",{}).get("security_checks",{}).get("is_external_redirect")

| Entity  
  
### Get Screenshot

Capture a high-quality screenshot of any website or URL.

#### Parameters

N/A

#### Use cases

An analyst can capture high-quality screenshots of any website or URL, in PNG or JPG image format.

#### Run on

This action runs on the User entity.

#### Action results

##### Entity enrichment

Mark entity as suspicious if the number of negative engines is equal or above the given threshold. is_suspicious: if data.get("score") > threshold

Enrichment field name | Logic - When to apply  
---|---  
domain | Returns if it exists in JSON result  
should_block | Returns if it exists in JSON result  
score | Returns if it exists in JSON result  
disposable | Returns if it exists in JSON result  
has_mx_records | Returns if it exists in JSON result  
has_spf_records | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "domain": "example.com",
                "valid_tld": true,
                "email": "user@example.co",
                "role_address": false,
                "should_block": false,
                "risky_tld": false,
                "dirty_words_username": false,
                "suspicious_domain": false,
                "score": 100,
                "educational_domain": false,
                "dirty_words_domain": false,
                "did_you_mean": " ",
                "username": "user",
                "valid_format": true,
                "is_spoofable ": false,
                "disposable": false,
                "government_domain": false,
                "has_spf_records": true,
                "domain_popular": false,
                "has_mx_records": true,
                "china_free_email": false,
                "free_email": false,
                "russian_free_email": false,
                "police_domain": false,
                "dmarc_enforced": false,
                "suspicious_username": false
            },
            "Entity": "USER@EXAMPLE.COM"
        }
    ]
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | 

  1. _Successful entities:_ "APIVoid: Added screenshots for the following entities: <entities identifier list>"
  2. _Failed entities:_ "An error occurred on the following entities: <entities identifier list>"
  3. _Missing entities (no data):_ 'No screenshots found for the following entities: <entities identifier list>"
  4. _Alert without URL entities:_ "APIVoid: No URL entities found for capturing screenshots."
  5. _To big entities (attachment file size > 3MB):_ "Failed to add screenshots as attachments on the following entities: <<entities identifier list>>"

| General  
Attachments | If data is available, create a new file object:

  1. attachment title: 'Screenshot - {0}'.format(entity.identifier)
  2. filename should be the URL without the suffix (https/http) + '_capture.<file format>'
  3. screenshot is returned in base64 encoded string --> file content should be b64decode(data.get('base64_file'))
  4. Don't forget to add try, except - we have 3MB limitation from the platform. In case of an error - add relevant message to the logger.

| General  
  
### Ping

Test the connectivity.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
success | True/False | success:False  
  
### Verify Email

Check if an email is disposable, has MX records, and more.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Threshold | Integer | N/A | Yes | Email risk threshold. The threshold must be a numeric value. Example: 3  
  
#### Use cases

An analyst can check if an email is disposable, get MX records, and more.

#### Run on

This action runs on the User entity.

#### Action results

##### Entity enrichment

Mark entity as suspicious if the number of negative engines is equal or above the given threshold. is_suspicious: if data.get("score") > threshold

Enrichment field name | Logic - When to apply  
---|---  
domain | Returns if it exists in JSON result  
should_block | Returns if it exists in JSON result  
score | Returns if it exists in JSON result  
disposable | Returns if it exists in JSON result  
has_mx_records | Returns if it exists in JSON result  
has_spf_records | Returns if it exists in JSON result  
  
##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "EntityResult": {
                "domain": "example.com",
                "valid_tld": true,
                "email": "user@example.com",
                "role_address": false,
                "should_block": false,
                "risky_tld": false,
                "dirty_words_username": false,
                "suspicious_domain": false,
                "score": 100,
                "educational_domain": false,
                "dirty_words_domain": false,
                "did_you_mean": " ",
                "username": "user",
                "valid_format": true,
                "is_spoofable ": false,
                "disposable": false,
                "government_domain": false,
                "has_spf_records": true,
                "domain_popular": false,
                "has_mx_records": true,
                "china_free_email": false,
                "free_email": false,
                "russian_free_email": false,
                "police_domain": false,
                "dmarc_enforced": false,
                "suspicious_username": false
            },
            "Entity": "USER@EXAMPLE.COm"
        }
    ]
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | 

  1. _successful entities:_ "APIVoid: Fetched information for the following entities: <entities identifer list>
  2. _Failed entities:_ "An error occurred on the following entities: <entities identifer list>"
  3. _Missing entities (no data):_ 'Can not found information for the following entities: <entities identifer list>"
  4. _Alert without URL entities:_ "APIVoid: No emails found."

| General  
CSV Case wall | CSV content: entity data(example below) | General  
Enrichment | If data available add the following as entity enrichment: (don't forget to add prefix "APIVoid")

  1. suspicious_domain: data.get("suspicious_domain")
  2. should_block: data.get("should_block")
  3. score: data.get("score")
  4. disposable: data.get("disposable")
  5. has_mx_records: data.get("has_mx_records")
  6. has_spf_records: data.get("has_spf_records")

| Entity  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
