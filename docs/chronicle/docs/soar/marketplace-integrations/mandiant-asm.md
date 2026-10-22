---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-asm/
title: Integrate Mandiant Attack Surface Management with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:49.468937+00:00
---

# Integrate Mandiant Attack Surface Management with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mandiant-asm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Mandiant Attack Surface Management with Google SecOps

This document explains how to integrate Mandiant Attack Surface Management with Google Security Operations (Google SecOps).

In the Google SecOps platform, the integration for Mandiant Attack Surface Management is called _Mandiant ASM_.

**Note:** We recommended using the **Google Threat Intelligence** integration as it provides more capabilities and features.

## Use cases

The **Mandiant ASM** integration uses Google SecOps capabilities to support the following use cases:

  * **Asset discovery** : Monitor and discover external-facing assets for potential security gaps.

  * **Ingest issues** : Ingest Mandiant Attack Surface Management issues as alerts in Google SecOps.

  * **Enrich incidents** : Enrich security incidents with detailed attack surface entity information.

  * **Prioritize remediation** : Prioritize remediation efforts based on Mandiant Attack Surface Management vulnerability and issue severity.

  * **Update issue statuses** : Update Mandiant Attack Surface Management issue statuses directly from the Google SecOps platform.




## Before you begin

This integration provides native platform capabilities and doesn't require external third-party API keys or credentials for authentication. Before you begin, ensure the integration is installed from the Content Hub within your Google SecOps instance.

## Integration parameters

The Mandiant Attack Surface Management integration requires the following parameters:

Parameters | Description  
---|---  
`API Root` | Required.The API root of the Mandiant instance. The default value is `https://asm-api.advantage.mandiant.com`. To authenticate with Google Threat Intelligence credentials, enter the following value: `https://www.virustotal.com`.  
`Access Key` | Optional.The API access key of the Mandiant Attack Surface Management account.To generate the access key in Mandiant Attack Surface Management, go to **Account settings > API keys > Generate new key**.   
`Secret Key` | Optional.The API secret key of the Mandiant Attack Surface Management account.To generate the secret key in Mandiant Attack Surface Management, go to **Account settings > API keys > Generate new key**.   
`Project Name` | Optional.The project name to use in the integration. If you use the `Access Key` and `Secret Key` parameters to authenticate, this parameter is required to run the **Search ASM Entities** and **Search Issues** actions.  
`GTI API Key` | Optional. The API key of Google Threat Intelligence.To authenticate using Google Threat Intelligence, set the `API Root` parameter value to `https://www.virustotal.com`. When you authenticate using the Google Threat Intelligence API key, it takes priority over other authentication methods.  
`Verify SSL` | Required.If selected, the integration verifies the validity of the SSL certificate for the connection to the Mandiant server. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get ASM Entity Details

Use the **Get ASM Entity Details** action to return information about a Mandiant Attack Surface Management entity.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Get ASM Entity Details** action requires the following parameters:

Parameter | Description  
---|---  
`Entity ID` | Required.A comma-separated list of entity IDs to retrieve details.  
  
#### Action outputs

The **Get ASM Entity Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get ASM Entity Details** action:
    
    
    {
     "uuid": "UUID",
     "dynamic_id": "Intrigue::Entity::Uri#http://192.0.2.73:80",
     "collection_name": "cpndemorange_oum28bu",
     "alias_group": 8515,
     "aliases": [
       "http://192.0.2.73:80"
     ],
     "allow_list": false,
     "ancestors": [
       {
         "type": "Intrigue::Entity::NetBlock",
         "name": "192.0.2.0/24"
       }
     ],
     "category": null,
     "collection_naics": null,
     "confidence": null,
     "deleted": false,
     "deny_list": false,
     "details": {
       "asn": null,
       "ssl": false,
       "uri": "http://192.0.2.73:80",
       "code": "404",
       "port": 80,
       "forms": false,
       "title": "404 Not Found",
       "verbs": null,
       "cookies": null,
       "headers": [
         "Date: Fri, 30 Sep 2022 06:51:11 GMT",
         "Content-Type: text/html",
         "Content-Length: 548",
         "Connection: keep-alive"
       ],
       "host_id": 8615,
       "net_geo": "US",
       "scripts": [],
       "service": "http",
       "auth.2fa": false,
       "auth.any": false,
       "dom_sha1": "540707399c1b58afd2463ec43da3b41444fbde32",
       "net_name": "",
       "protocol": "tcp",
       "alt_names": null,
       "auth.ntlm": false,
       "generator": null,
       "auth.basic": false,
       "auth.forms": false,
       "ip_address": "192.0.2.73",
       "favicon_md5": null,
       "fingerprint": [
         {
           "cpe": "cpe:2.3:a:example:example::",
           "hide": false,
           "tags": [
             "Web Server"
           ],
           "type": "fingerprint",
           "tasks": null,
           "issues": null,
           "method": "ident",
           "update": null,
           "vendor": "Example",
           "product": "Example",
           "version": null,
           "inference": false,
           "description": "example (default page)",
           "match_logic": "all",
           "positive_matches": [
             {
               "match_type": "content_body",
               "match_content": "(?i-mx:<hr><center>example\/?([\\d.]*)<\/center>)"
             }
           ]
         },
         {
           "cpe": "cpe:2.3:a:example:example::",
           "hide": false,
           "tags": [
             "Web Server"
           ],
           "type": "fingerprint",
           "tasks": null,
           "issues": null,
           "method": "ident",
           "update": null,
           "vendor": "example",
           "product": "example",
           "version": null,
           "inference": false,
           "description": "example (default page - could be redirect)",
           "match_logic": "all",
           "positive_matches": [
             {
               "match_type": "content_body",
               "match_content": "(?i-mx:<hr><center>example\/?[\\d.]*<\/center>)"
             }
           ]
         }
       ],
       "geolocation": {
         "asn": {
           "asn": 16509,
           "isp": "Example Inc.",
           "name": "example.com, Inc.",
           "organization": "Example Services",
           "connection_type": "Corporate"
         },
         "city": "Singapore",
         "country": "Singapore",
         "latitude": 1.35208,
         "continent": "Asia",
         "longitude": 103.82,
         "time_zone": "Asia/Singapore",
         "country_code": "SG",
         "continent_code": "AS"
       },
       "vuln_checks": [
         "log4shell_cve_2021_44228"
       ],
       "api_endpoint": false,
       "cloud_hosted": true,
       "favicon_sha1": null,
       "domain_cookies": null,
       "log4shell_uuid": "55be320622c4937c01738e092579edaa338fd90e2a",
       "redirect_chain": [],
       "redirect_count": 0,
       "cloud_providers": [
         "Cloud Provider Name"
       ],
       "hidden_original": "http://192.0.2.73:80",
       "net_country_code": null,
       "screenshot_exists": true,
       "cloud_fingerprints": [],
       "response_data_hash": "1GUXIXXTXUk/sWM+I3cAAivYSfoSMWR5CxaLgxissJA=",
       "extended_favicon_data": null,
       "extended_path_to_seed": [
         {
           "id": 8620,
           "_id": 8605,
           "name": "http://192.0.2.73:80",
           "seed": false,
           "type": "Intrigue::Entity::Uri",
           "_type": "Entity",
           "creates": [
             {
               "id": 6158,
               "_id": 6152,
               "name": "192.0.2.0/24",
               "seed": true,
               "type": "Intrigue::Entity::NetBlock",
               "_type": "Entity",
               "creates.verb": "queried",
               "creates.source_name": "search_shodan",
               "creates.source_type": "internet_scan_database"
             }
           ]
         }
       ],
       "extended_configuration": [
         {
           "hide": false,
           "name": "Example Page Content",
           "task": null,
           "type": "content",
           "issue": null,
           "result": 566218143
         },
         {
           "hide": false,
           "name": "Example",
           "task": null,
           "type": "content",
           "issue": null,
           "result": 566218143
         },
         {
           "cpe": "cpe:2.3:a:example:example::",
           "hide": false,
           "tags": [
             "Web Server"
           ],
           "type": "fingerprint",
           "tasks": null,
           "issues": null,
           "method": "ident",
           "update": null,
           "vendor": "Example",
           "product": "Example",
           "version": null,
           "inference": false,
           "description": "example (default page)",
           "match_logic": "all",
           "positive_matches": [
             {
               "match_type": "content_body",
               "match_content": "(?i-mx:<hr><center>example\/?([\\d.]*)<\/center>)"
             }
           ]
         },
         {
           "cpe": "cpe:2.3:a:example:example::",
           "hide": false,
           "tags": [
             "Web Server"
           ],
           "type": "fingerprint",
           "tasks": null,
           "issues": null,
           "method": "ident",
           "update": null,
           "vendor": "Example",
           "product": "Example",
           "version": null,
           "inference": false,
           "description": "example (default page - could be redirect)",
           "match_logic": "all",
           "positive_matches": [
             {
               "match_type": "content_body",
               "match_content": "(?i-mx:<hr><center>example\/?[\\d.]*<\/center>)"
             }
           ]
         }
       ],
       "extended_response_body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body>\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>example</center>\r\n</body>\r\n</html>\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n",
       "exfil_lookup_identifier": "55be320622c4937c01738e092579edaa",
       "extended_shodan_details": {
         "ip": 50387017,
         "os": null,
         "asn": "ASN",
         "isp": "Example.com, Inc.",
         "org": "Example Services",
         "data": "HTTP/1.1 404 Not Found\r\nDate: Fri, 30 Sep 2022 05:16:32 GMT\r\nContent-Type: text/html\r\nContent-Length: 548\r\nConnection: keep-alive\r\n\r\n",
         "hash": -744989972,
         "http": {
           "host": "192.0.2.73",
           "html": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body>\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>example</center>\r\n</body>\r\n</html>\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n",
           "title": "404 Not Found",
           "robots": null,
           "server": null,
           "status": 404,
           "sitemap": null,
           "location": "/",
           "html_hash": -2090962452,
           "redirects": [],
           "components": {},
           "robots_hash": null,
           "securitytxt": null,
           "headers_hash": -873436690,
           "sitemap_hash": null,
           "securitytxt_hash": null
         },
         "tags": [
           "cloud"
         ],
         "cloud": {
           "region": "ap-southeast-1",
           "service": "Example",
           "provider": "Example"
         },
         "ip_str": "192.0.2.73",
         "_shodan": {
           "id": "ID",
           "ptr": true,
           "module": "http",
           "region": "eu",
           "crawler": "f4bb88763d8ed3a0f3f91439c2c62b77fb9e06f3",
           "options": {}
         },
         "domains": [
           "example.com"
         ],
         "location": {
           "city": "Singapore",
           "latitude": 1.28967,
           "area_code": null,
           "longitude": 103.85007,
           "region_code": "01",
           "country_code": "SG",
           "country_name": "Singapore"
         },
         "hostnames": [
           "ec2-192-0-2-73.ap-southeast-1.compute.example.com"
         ],
         "timestamp": "2022-09-30T05:16:33.068993"
       },
       "hidden_port_open_confirmed": true,
       "extended_screenshot_contents": "iVBORw0KGgoAAA"
     },
     "details_file": "data/v4/cpndemorange_oum28bu/2022_09_30/cpndemorange_oum28bu/entities/ID.json",
     "description": null,
     "first_seen": "2022-09-30T21:20:19.000Z",
     "hidden": false,
     "last_seen": "2022-09-30T21:20:19.000Z",
     "name": "http://192.0.2.73:80",
     "scoped": true,
     "scoped_reason": "entity_scoping_rules: fallback value",
     "seed": false,
     "source": null,
     "status": null,
     "task_results": [],
     "type": "Intrigue::Entity::Uri",
     "uid": "UID",
     "created_at": "2022-09-30T21:25:05.232Z",
     "updated_at": "2022-09-30T21:25:05.239Z",
     "collection_id": 117139,
     "elasticsearch_mappings_hash": null,
     "collection": "cpndemorange_oum28bu",
     "collection_uuid": "UUID",
     "organization_uuid": "UUID",
     "collection_type": "user_collection",
     "fingerprint": [
       {
         "cpe": "cpe:2.3:a:example:example::",
         "hide": false,
         "tags": [
           "Web Server"
         ],
         "type": "fingerprint",
         "tasks": null,
         "issues": null,
         "method": "ident",
         "update": null,
         "vendor": "Example",
         "product": "Example",
         "version": null,
         "inference": false,
         "description": "example (default page)",
         "match_logic": "all",
         "positive_matches": [
           {
             "match_type": "content_body",
             "match_content": "(?i-mx:<hr><center>example\/?([\\d.]*)<\/center>)"
           }
         ],
         "local_icon_path": "/assets/fingerprints/example.png"
       },
       {
         "cpe": "cpe:2.3:a:example:example::",
         "hide": false,
         "tags": [
           "Web Server"
         ],
         "type": "fingerprint",
         "tasks": null,
         "issues": null,
         "method": "ident",
         "update": null,
         "vendor": "Example",
         "product": "Example",
         "version": null,
         "inference": false,
         "description": "example (default page - could be redirect)",
         "match_logic": "all",
         "positive_matches": [
           {
             "match_type": "content_body",
             "match_content": "(?i-mx:<hr><center>example\/?[\\d.]*<\/center>)"
           }
         ],
         "local_icon_path": "/assets/fingerprints/example.png"
       }
     ],
     "summary": {
       "scoped": true,
       "issues": {
         "current_with_cve": 0,
         "current_by_severity": {
           "1": 1
         },
         "all_time_by_severity": {
           "1": 1
         },
         "current_count": 1,
         "all_time_count": 1,
         "critical_or_high": true
       },
       "task_results": [
         "search_shodan",
         "port_scan",
         "port_scan_lambda",
         "search_shodan"
       ],
       "screenshot_exists": true,
       "geolocation": {
         "city": "Singapore",
         "country_code": "SG",
         "country_name": null,
         "latitude": 1.35208,
         "longitude": 103.82,
         "asn": null
       },
       "http": {
         "code": 404,
         "title": "404 Not Found",
         "content": {
           "favicon_hash": null,
           "hash": null,
           "forms": false
         },
         "auth": {
           "any": false,
           "basic": false,
           "ntlm": false,
           "forms": false,
           "2fa": false
         }
       },
       "ports": {
         "tcp": [
           80
         ],
         "udp": [],
         "count": 1
       },
       "network": {
         "name": "example.com, Inc.",
         "asn": 16509,
         "route": null,
         "type": null
       },
       "technology": {
         "cloud": true,
         "cloud_providers": [
           "Cloud Provider Name"
         ],
         "cpes": [],
         "technologies": [],
         "technology_labels": []
       },
       "vulns": {
         "current_count": 0,
         "vulns": []
       }
     },
     "tags": [],
     "id": "ID",
     "scoped_at": "2022-09-30 06:51:57 +0000",
     "detail_string": "Fingerprint: Example |  Title: 404 Not Found",
     "enrichment_tasks": [
       "enrich/uri",
       "sslcan"
     ],
     "generated_at": "2022-09-30T21:21:18Z"
    }
    

##### Output messages

The **Get ASM Entity Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully return details for the following entities using information from Mandiant ASM: ENTITY_ID` `Action wasn't able to return details for the following entities using information from Mandiant ASM: ENTITY_ID` | The action succeeded.  
`Error executing action "Get ASM Entity Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get ASM Entity Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search ASM Entities

Use the **Search ASM Entities** action to search entities in Mandiant Attack Surface Management.

If you use the `Access Key` and `Secret Key` parameters to authenticate, also configure the `Project Name` parameter in the integration parameters.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Search ASM Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Entity Name` | Optional.A comma-separated list of entity names to find entities.To prevent action failure, avoid using the `/` forward slash character when you configure values for this parameter.  
`Minimum Vulnerabilities Count` | Optional.The number of vulnerabilities related to the returned entity.  
`Minimum Issues Count` | Optional.The number of issues related to the returned entity.  
`Tags` | Optional.A comma-separated list of tag names to use when searching for entities.  
`Max Entities To Return` | Optional.The number of entities to return.The default value is `50`. The maximum value is `200`.  
`Critical or High Issue` | Optional.If selected, the action returns only entities with `High` or `Critical` issues.Not selected by default.  
  
#### Action outputs

The **Search ASM Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search ASM Entities** action:
    
    
    {
     "id": "ID",
     "dynamic_id": "Intrigue::Entity::IpAddress#192.0.2.92",
     "alias_group": "1935953",
     "name": "192.0.2.92",
     "type": "Intrigue::Entity::IpAddress",
     "first_seen": "2022-02-02T01:44:46Z",
     "last_seen": "2022-02-02T01:44:46Z",
     "collection": "cpndemorange_oum28bu",
     "collection_type": "Intrigue::Collections::UserCollection",
     "collection_naics": [],
     "collection_uuid": "COLLECTION_UUID",
     "organization_uuid": "ORGANIZATION_UUID",
     "tags": [],
     "issues": [],
     "exfil_lookup_identifier": null,
     "summary": {
         "scoped": true,
         "issues": {
             "current_by_severity": {},
             "current_with_cve": 0,
             "all_time_by_severity": {},
             "current_count": 0,
             "all_time_count": 0,
             "critical_or_high": false
         },
         "task_results": [
             "search_shodan"
         ],
         "geolocation": {
             "city": "San Jose",
             "country_code": "US",
             "country_name": null,
             "latitude": "-121.8896",
             "asn": null
         },
         "ports": {
             "count": 0,
             "tcp": null,
             "udp": null
         },
         "resolutions": [
             "ec2-192-0-2-92.us-west-1.compute.example.com"
         ],
         "network": {
             "name": "EXAMPLE-02",
             "asn": "16509.0",
             "route": "2001:db8::/32",
             "type": null
         },
         "technology": {
             "cloud": true,
             "cloud_providers": [
                 "Cloud Provider Name"
             ]
         }
     }
    }
    

##### Output messages

The **Search ASM Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned entities based on the provided criteria in Mandiant ASM.` `No entities were found based on the provided criteria in Mandiant ASM.` | The action succeeded.  
`Error executing action "Search ASM Entities". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search ASM Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Issues

Use the **Search Issues** action to search issues in Mandiant Attack Surface Management.

If you use the `Access Key` and `Secret Key` parameters to authenticate, also configure the `Project Name` parameter in the integration parameters.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Search Issues** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Optional.A comma-separated list of issue IDs to return the details.  
`Entity ID` | Optional.A comma-separated list of entity IDs to find related issues.  
`Entity Name` | Optional.A comma-separated list of entity names to find related issues.To prevent action failure, avoid using the `/` forward slash character when you configure values for this parameter.  
`Time Parameter` | Optional.A filter option to set the issue time. The possible values are `First Seen` and `Last Seen`.The default value is `First Seen`.  
`Time Frame` | Optional.A period to filter issues. If you select `Custom`, configure the `Start Time` parameter. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | Optional.The start time for the results.If you selected `Custom` for the `Time Frame` parameter, this parameter is required. Configure the value in the ISO 8601 format.  
`End Time` | Optional.The end time for the results.If you selected `Custom` for the `Time Frame` parameter and didn't set the end time, this parameter uses the current time as the end time. Configure the value in the ISO 8601 format.  
`Lowest Severity To Return` | Optional.The lowest severity of the issues to return. The possible values are as follows:

  * `Select One`
  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

The default value is `Select One`. If you select `Select One`, this filter doesn't apply to the search.  
`Status` | Optional.The status filter for the search. The possible values are `Open`, `Closed`, and `Select One`. The default value is `Select One`. If you select `Select One`, this filter doesn't apply to the search.  
`Tags` | Optional.A comma-separated list of tag names to use when searching for issues.  
`Max Issues To Return` | Optional.The number of issues to return.The default value is `50`. The maximum value is `200`.  
  
#### Action outputs

The **Search Issues** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search Issues** action:
    
    
    {
     "id": "ID",
     "uuid": "UUID",
     "dynamic_id": 20073997,
     "name": "exposed_ftp_service",
     "upstream": "intrigue",
     "last_seen": "2022-02-02T01:44:46.000Z",
     "first_seen": "2022-02-02T01:44:46.000Z",
     "entity_uid": "3443a638f951bdc23d3a089bff738cd961a387958c7f5e4975a26f12e544241f",
     "entity_type": "Intrigue::Entity::NetworkService",
     "entity_name": "192.0.2.204:24/tcp",
     "alias_group": "1937534",
     "collection": "cpndemorange_oum28bu",
     "collection_uuid": "COLLECTION_UUID",
     "collection_type": "user_collection",
     "organization_uuid": "ORGANIZATION_UUID",
     "summary": {
         "pretty_name": "Exposed FTP Service",
         "severity": 3,
         "scoped": true,
         "confidence": "confirmed",
         "status": "open_new",
         "category": "misconfiguration",
         "identifiers": null,
         "status_new": "open",
         "status_new_detailed": "new",
         "ticket_list": null
     },
     "tags": []
    }
    

##### Output messages

The **Search Issues** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned issues based on the provided criteria in Mandiant ASM.` `No issues were found based on the provided criteria in Mandiant ASM.` | The action succeeded.  
`Error executing action "Search Issues". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Issues** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Issue

Use the **Update Issue** action to update an issue in Mandiant Attack Surface Management.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Update Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The ID of the issue to update.  
`Status` | Required.The status to set for the issue. The possible values are as follows:

  * `Select One`
  * `New`
  * `Triaged`
  * `In Progress`
  * `Resolved`
  * `Duplicate`
  * `Out Of Scope`
  * `Not A Security Issue (Benign)`
  * `Risk Accepted`
  * `False Positive`
  * `Unable To Reproduce`
  * `Tracked Externally`
  * `Mitigated`

The default value is `Select One`.  
  
#### Action outputs

The **Update Issue** action provides the following outputs:

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

The **Update Issue** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated issue with ID "ISSUE_ID" in Mandiant ASM.` | The action succeeded.  
`Error executing action "Update Issue". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Issue** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Mandiant ASM – Issues Connector

Use the **Mandiant ASM – Issues Connector** to pull information about issues from Mandiant Attack Surface Management.

The dynamic list filter works with the `category` parameter.

The **Mandiant ASM – Issues Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | Required.The name of the field where the product name is stored.The default value is `Product Name`.The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value `Product Name` resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default.  
`Event Field Name` | Required.The name of the field where the event name is stored.The default value is `entity_type`.  
`Environment Field Name` | Optional. The name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.   
`Environment Regex Pattern` | Optional. A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Script Timeout (Seconds)` | Required.The timeout limit, in seconds, for the Python process running the current script.The default value is `180`.  
`API Root` | Required.The API root of the Mandiant instance. The default value is `https://asm-api.advantage.mandiant.com`. To authenticate with Google Threat Intelligence credentials, enter the following value: `https://www.virustotal.com`.  
`Access Key` | Optional.The API access key of the Mandiant Attack Surface Management account.To generate the access key in Mandiant Attack Surface Management, go to **Account settings > API keys > Generate new key**.   
`Secret Key` | Optional.The API secret key of the Mandiant Attack Surface Management account.To generate the secret key in Mandiant Attack Surface Management, go to **Account settings > API keys > Generate new key**.   
`Project Name` | Optional.The project name to use in the integration. Required if you use the `Access Key` and `Secret Key` parameters to authenticate.  
`GTI API Key` | Optional. The API key of Google Threat Intelligence.To authenticate using Google Threat Intelligence, set the `API Root` parameter value to `https://www.virustotal.com`. Authenticating using the Google Threat Intelligence API key has a priority over other authentication methods.  
`Lowest Severity To Fetch` | Optional.The lowest severity of the issues to retrieve. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

If you don't set a value, the connector ingests issues with all severity types.  
`Max Hours Backwards` | Optional.A number of hours prior to the first connector iteration to retrieve incidents. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Issues To Fetch` | Optional.The number of issues to process in a single connector iteration.The default value is `10`.  
`Use dynamic list as a blocklist` | Required. If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | Required. If selected, verifies that the SSL certificate for the connection to the Mandiant server is valid. Selected by default.  
`Proxy Server Address` | Optional.The address of the proxy server to use.  
`Proxy Username` | Optional.The proxy username to authenticate with.  
`Proxy Password` | Optional.The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
