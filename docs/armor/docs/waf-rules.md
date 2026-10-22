---
url: https://docs.cloud.google.com/armor/docs/waf-rules/
title: Preconfigured WAF rules overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:53.196944+00:00
---

# Preconfigured WAF rules overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/waf-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Preconfigured WAF rules overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor preconfigured WAF rules are complex web application firewall (WAF) rules with dozens of _signatures_ that are compiled from open source industry standards. Each signature corresponds to an attack detection rule in the ruleset. Google offers these rules as is. The rules let Cloud Armor evaluate dozens of distinct traffic signatures by referring to conveniently named rules rather than requiring you to define each signature manually.

Cloud Armor preconfigured WAF rules can be tuned to best suit your needs. For more information about how to tune the rules, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).

The following table lists the preconfigured preconfigured WAF rules available for use in a Cloud Armor security policy. These rules are based on the OWASP ModSecurity Core Rule Set (CRS), such as [OWASP Core Rule Set 4.22](https://github.com/coreruleset/coreruleset/releases/tag/v4.22.0) . We recommend using version 4.22 for the most up-to-date protection against modern threats. While support for CRS 3.3 and 3.0 is ongoing, we recommend avoiding older versions, especially CRS version 3.0, whenever your workloads allow for version 4.22.

###  CRS 4.22 

Cloud Armor rule name | OWASP rule name | Current status  
---|---|---  
SQL injection | `sqli-v422-stable` | In sync with `sqli-v422-canary`  
`sqli-v422-canary` | Latest  
Cross-site scripting | `xss-v422-stable` | In sync with `xss-v422-canary`  
`xss-v422-canary` | Latest  
Local file inclusion | `lfi-v422-stable` | In sync with `lfi-v422-canary`  
`lfi-v422-canary` | Latest  
Remote file inclusion | `rfi-v422-stable` | In sync with `rfi-v422-canary`  
`rfi-v422-canary` | Latest  
Remote code execution | `rce-v422-stable` | In sync with `rce-v422-canary`  
`rce-v422-canary` | Latest  
Method enforcement | `methodenforcement-v422-stable` | In sync with `methodenforcement-v422-canary`  
`methodenforcement-v422-canary` | Latest  
Scanner detection | `scannerdetection-v422-stable` | In sync with `scannerdetection-v422-canary`  
`scannerdetection-v422-canary` | Latest  
Protocol attack | `protocolattack-v422-stable` | In sync with `protocolattack-v422-canary`  
`protocolattack-v422-canary` | Latest  
PHP injection attack | `php-v422-stable` | In sync with `php-v422-canary`  
`php-v422-canary` | Latest  
Session fixation attack | `sessionfixation-v422-stable` | In sync with `sessionfixation-v422-canary`  
`sessionfixation-v422-canary` | Latest  
Java attack | `java-v422-stable` | In sync with `java-v422-canary`  
`java-v422-canary` | Latest  
Generic attack | `generic-v422-stable` | In sync with `generic-v422-canary`  
`generic-v422-canary` | Latest  
**Note:** The `nodejs` rule set in v3.3 was reclassified as `generic` in v4.22. Both versions use the same three-digit number _934_ as the starting digits for the rule ID.

###  CRS 3.3 

Cloud Armor rule name | OWASP rule name | Current status  
---|---|---  
SQL injection | `sqli-v33-stable` | In sync with `sqli-v33-canary`  
`sqli-v33-canary` | Latest  
Cross-site scripting | `xss-v33-stable` | In sync with `xss-v33-canary`  
`xss-v33-canary` | Latest  
Local file inclusion | `lfi-v33-stable` | In sync with `lfi-v33-canary`  
`lfi-v33-canary` | Latest  
Remote file inclusion | `rfi-v33-stable` | In sync with `rfi-v33-canary`  
`rfi-v33-canary` | Latest  
Remote code execution | `rce-v33-stable` | In sync with `rce-v33-canary`  
`rce-v33-canary` | Latest  
Method enforcement | `methodenforcement-v33-stable` | In sync with `methodenforcement-v33-canary`  
`methodenforcement-v33-canary` | Latest  
Scanner detection | `scannerdetection-v33-stable` | In sync with `scannerdetection-v33-canary`  
`scannerdetection-v33-canary` | Latest  
Protocol attack | `protocolattack-v33-stable` | In sync with `protocolattack-v33-canary`  
`protocolattack-v33-canary` | Latest  
PHP injection attack | `php-v33-stable` | In sync with `php-v33-canary`  
`php-v33-canary` | Latest  
Session fixation attack | `sessionfixation-v33-stable` | In sync with `sessionfixation-v33-canary`  
`sessionfixation-v33-canary` | Latest  
Java attack | `java-v33-stable` | In sync with `java-v33-canary`  
`java-v33-canary` | Latest  
NodeJS attack | `nodejs-v33-stable` | In sync with `nodejs-v33-canary`  
`nodejs-v33-canary` | Latest  
  
###  CRS 3.0 

Cloud Armor rule name | OWASP rule name | Current status  
---|---|---  
SQL injection | `sqli-stable` | In sync with `sqli-canary`  
`sqli-canary` | Latest  
Cross-site scripting | `xss-stable` | In sync with `xss-canary`  
`xss-canary` | Latest  
Local file inclusion | `lfi-stable` | In sync with `lfi-canary`  
`lfi-canary` | Latest  
Remote file inclusion | `rfi-stable` | In sync with `rfi-canary`  
`rfi-canary` | Latest  
Remote code execution | `rce-stable` | In sync with `rce-canary`  
`rce-canary` | Latest  
Method enforcement | `methodenforcement-stable` | In sync with `methodenforcement-canary`  
`methodenforcement-canary` | Latest  
Scanner detection | `scannerdetection-stable` | In sync with `scannerdetection-canary`  
`scannerdetection-canary` | Latest  
Protocol attack | `protocolattack-stable` | In sync with `protocolattack-canary`  
`protocolattack-canary` | Latest  
PHP injection attack | `php-stable` | In sync with `php-canary`  
`php-canary` | Latest  
Session fixation attack | `sessionfixation-stable` | In sync with `sessionfixation-canary`  
`sessionfixation-canary` | Latest  
Java attack | `Not included`  
NodeJS attack | `Not included`  
  
In addition, the following `cve-canary` rules are available to all Cloud Armor customers to help detect and optionally block the following vulnerabilities:

  * `CVE-2021-44228` and `CVE-2021-45046` Log4j RCE vulnerabilities
  * `942550-sqli` JSON-formatted content vulnerability
  * `google-mrs-v202512-id000001-rce` and `google-mrs-v202512-id000002-rce` React RCE vulnerabilities

Cloud Armor rule name | Covered vulnerability types  
---|---  
`cve-canary` | Log4j and React RCE vulnerabilities  
`json-sqli-canary` | JSON-based SQL injection bypass vulnerability  
  
## Best practices

To optimize your use of preconfigured WAF rules, consider the following best practices:

  * **Tuning and sensitivity** : start with sensitivity level 1 in preview mode to understand how rules affect your application. For more information, see [Choose your preconfigured WAF rule sensitivity level](https://docs.cloud.google.com/armor/docs/best-practices#sensitivity-level).
  * **Request body inspection limit** : configure the inspection limit based on your needs. Cloud Armor preconfigured WAF rules can inspect up to 64 kB of the request body. For more information, see [Update inspection limit for preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/configure-waf#update-waf-inspection-limit).
  * **Canary and stable rulesets** : maintain canary rulesets in preview mode with a higher priority, and keep stable rulesets in enforced mode with a lower priority. This approach lets you validate rule changes before they affect your production traffic.



For a complete list of recommendations, see [Cloud Armor best practices](https://docs.cloud.google.com/armor/docs/best-practices).

## Preconfigured OWASP rules

Each preconfigured WAF rule has a sensitivity level that corresponds to a OWASP CRS [paranoia level](https://coreruleset.org/faq/#paranoialevel). A lower sensitivity level indicates a higher confidence signature, which is less likely to generate a false positive. A higher sensitivity level increases security, but also increases the risk of generating a false positive. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set once enabled.

### SQL injection (SQLi)

The following table provides the signature ID, sensitivity level, and description of each supported signature in the SQLi preconfigured WAF rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id942100-sqli` | 1 | SQL injection attack detected using libinjection  
`owasp-crs-v042200-id942140-sqli` | 1 | SQL injection attack: Common DB names detected  
`owasp-crs-v042200-id942151-sqli` | 1 | SQL injection attack: SQL function name detected  
`owasp-crs-v042200-id942160-sqli` | 1 | Detects SQLi tests using `sleep` or `benchmark`  
`owasp-crs-v042200-id942170-sqli` | 1 | Detects SQL `benchmark` and `sleep` injection attempts including conditional queries  
`owasp-crs-v042200-id942190-sqli` | 1 | Detects MSSQL code execution and information gathering attempts  
`owasp-crs-v042200-id942220-sqli` | 1 | Looks for integer overflow attacks  
`owasp-crs-v042200-id942230-sqli` | 1 | Detects conditional SQL injection attempts  
`owasp-crs-v042200-id942240-sqli` | 1 | Detects MySQL charset switch and MSSQL DoS attempts  
`owasp-crs-v042200-id942250-sqli` | 1 | Detects MATCH AGAINST, MERGE, and EXECUTE IMMEDIATE injections  
`owasp-crs-v042200-id942270-sqli` | 1 | Looks for basic SQL injection; common attack string for MySql, Oracle, and others  
`owasp-crs-v042200-id942280-sqli` | 1 | Detects Postgres `pg_sleep` injection, `waitfor` delay attacks and database shutdown attempts  
`owasp-crs-v042200-id942290-sqli` | 1 | Finds basic MongoDB SQL injection attempts  
`owasp-crs-v042200-id942320-sqli` | 1 | Detects MySQL and PostgreSQL stored procedure or function injections  
`owasp-crs-v042200-id942350-sqli` | 1 | Detects MySQL UDF injection and other data or structure manipulation attempts  
`owasp-crs-v042200-id942360-sqli` | 1 | Detects concatenated basic SQL injection and SQLLFI attempts  
`owasp-crs-v042200-id942500-sqli` | 1 | MySQL inline comment detected  
`owasp-crs-v042200-id942540-sqli` | 1 | SQL Authentication bypass (split query)  
`owasp-crs-v042200-id942560-sqli` | 1 | MySQL scientific notation payload detected  
`owasp-crs-v042200-id942550-sqli` | 1 | JSON-Based SQL injection  
`owasp-crs-v042200-id942120-sqli` | 2 | SQL injection attack: SQL operator detected  
`owasp-crs-v042200-id942130-sqli` | 2 | SQL injection attack: SQL boolean-based attack detected  
`owasp-crs-v042200-id942131-sqli` | 2 | SQL injection attack: SQL boolean-based attack detected  
`owasp-crs-v042200-id942150-sqli` | 2 | SQL injection attack: SQL function name detected  
`owasp-crs-v042200-id942180-sqli` | 2 | Detects basic SQL authentication bypass attempts 1/3  
`owasp-crs-v042200-id942200-sqli` | 2 | Detects MySQL comment- or space-obfuscated injections and backtick termination  
`owasp-crs-v042200-id942210-sqli` | 2 | Detects chained SQL injection attempts 1/2  
`owasp-crs-v042200-id942260-sqli` | 2 | Detects basic SQL authentication bypass attempts 2/3  
`owasp-crs-v042200-id942300-sqli` | 2 | Detects MySQL comments, conditions and ch(a)r injections  
`owasp-crs-v042200-id942310-sqli` | 2 | Detects chained SQL injection attempts 2/2  
`owasp-crs-v042200-id942330-sqli` | 2 | Detects classic SQL injection probings 1/3  
`owasp-crs-v042200-id942340-sqli` | 2 | Detects basic SQL authentication bypass attempts 3/3  
`owasp-crs-v042200-id942361-sqli` | 2 | Detects basic SQL injection based on keyword alter or union  
`owasp-crs-v042200-id942362-sqli` | 2 | Detects concatenated basic SQL injection and SQLLFI attempts  
`owasp-crs-v042200-id942370-sqli` | 2 | Detects classic SQL injection probings 2/3  
`owasp-crs-v042200-id942380-sqli` | 2 | SQL injection attack  
`owasp-crs-v042200-id942390-sqli` | 2 | SQL injection attack  
`owasp-crs-v042200-id942400-sqli` | 2 | SQL injection attack  
`owasp-crs-v042200-id942410-sqli` | 2 | SQL injection attack  
`owasp-crs-v042200-id942470-sqli` | 2 | SQL injection attack  
`owasp-crs-v042200-id942480-sqli` | 2 | SQL injection attack  
`owasp-crs-v042200-id942430-sqli` | 2 | Restricted SQL character anomaly detection (args): # of special characters exceeded (12)  
`owasp-crs-v042200-id942440-sqli` | 2 | SQL comment sequence detected  
`owasp-crs-v042200-id942450-sqli` | 2 | SQL hex encoding identified  
`owasp-crs-v042200-id942510-sqli` | 2 | SQLi bypass attempt by ticks or backticks detected  
`owasp-crs-v042200-id942520-sqli` | 2 | Detects basic SQL authentication bypass attempts 4.0/4  
`owasp-crs-v042200-id942521-sqli` | 2 | Detects basic SQL authentication bypass attempts 4.1/4  
`owasp-crs-v042200-id942522-sqli` | 2 | Detects basic SQL authentication bypass attempts 4.1/4  
`owasp-crs-v042200-id942101-sqli` | 2 | SQL injection attack detected using libinjection  
`owasp-crs-v042200-id942152-sqli` | 2 | SQL injection attack: SQL function name detected  
`owasp-crs-v042200-id942321-sqli` | 2 | Detects MySQL and PostgreSQL stored procedure or function injections  
`owasp-crs-v042200-id942251-sqli` | 3 | Detects HAVING injections  
`owasp-crs-v042200-id942490-sqli` | 3 | Detects classic SQL injection probings 3/3  
`owasp-crs-v042200-id942420-sqli` | 3 | Restricted SQL character anomaly detection (cookies): # of special characters exceeded (8)  
`owasp-crs-v042200-id942431-sqli` | 3 | Restricted SQL character anomaly detection (args): # of special characters exceeded (6)  
`owasp-crs-v042200-id942460-sqli` | 3 | Meta-character anomaly detection alert - repetitive non-word characters  
`owasp-crs-v042200-id942511-sqli` | 3 | SQLi bypass attempt by ticks detected  
`owasp-crs-v042200-id942530-sqli` | 3 | SQLi query termination detected  
`owasp-crs-v042200-id942421-sqli` | 4 | Restricted SQL character anomaly detection (cookies): # of special characters exceeded (3)  
`owasp-crs-v042200-id942432-sqli` | 4 | Restricted SQL character anomaly detection (args): # of special characters exceeded (2)  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id942100-sqli` | 1 | SQL injection attack detected using libinjection  
`owasp-crs-v030301-id942140-sqli` | 1 | SQL injection attack: common DB names detected  
`owasp-crs-v030301-id942160-sqli` | 1 | Detects SQLi tests using `sleep` or `benchmark`  
`owasp-crs-v030301-id942170-sqli` | 1 | Detects SQL `sleep` or `benchmark` injection attempts including conditional queries  
`owasp-crs-v030301-id942190-sqli` | 1 | Detects MSSQL code execution and information gathering attempts  
`owasp-crs-v030301-id942220-sqli` | 1 | Looks for integer overflow attacks  
`owasp-crs-v030301-id942230-sqli` | 1 | Detects conditional SQL injection attempts  
`owasp-crs-v030301-id942240-sqli` | 1 | Detects MySQL charset switch and MSSQL DoS attempts  
`owasp-crs-v030301-id942250-sqli` | 1 | Detects MATCH AGAINST  
`owasp-crs-v030301-id942270-sqli` | 1 | Looks for basic SQL injection; common attack string for MySql  
`owasp-crs-v030301-id942280-sqli` | 1 | Detects Postgres `pg_sleep` injection  
`owasp-crs-v030301-id942290-sqli` | 1 | Finds basic MongoDB SQL injection attempts  
`owasp-crs-v030301-id942320-sqli` | 1 | Detects MySQL and PostgreSQL stored procedure or function injections  
`owasp-crs-v030301-id942350-sqli` | 1 | Detects MySQL UDF injection and other data or structure manipulation attempts  
`owasp-crs-v030301-id942360-sqli` | 1 | Detects concatenated basic SQL injection and SQLLFI attempts  
`owasp-crs-v030301-id942500-sqli` | 1 | MySQL inline comment detected  
`owasp-crs-v030301-id942110-sqli` | 2 | SQL injection attack: common injection testing detected  
`owasp-crs-v030301-id942120-sqli` | 2 | SQL injection attack: SQL operator detected  
`owasp-crs-v030301-id942130-sqli` | 2 | SQL injection attack: SQL tautology detected  
`owasp-crs-v030301-id942150-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942180-sqli` | 2 | Detects basic SQL authentication bypass attempts 1/3  
`owasp-crs-v030301-id942200-sqli` | 2 | Detects MySQL comment- or space-obfuscated injections and backtick termination  
`owasp-crs-v030301-id942210-sqli` | 2 | Detects chained SQL injection attempts 1/2  
`owasp-crs-v030301-id942260-sqli` | 2 | Detects basic SQL authentication bypass attempts 2/3  
`owasp-crs-v030301-id942300-sqli` | 2 | Detects MySQL comments  
`owasp-crs-v030301-id942310-sqli` | 2 | Detects chained SQL injection attempts 2/2  
`owasp-crs-v030301-id942330-sqli` | 2 | Detects classic SQL injection probings 1/2  
`owasp-crs-v030301-id942340-sqli` | 2 | Detects basic SQL authentication bypass attempts 3/3  
`owasp-crs-v030301-id942361-sqli` | 2 | Detects basic SQL injection based on keyword alter or union  
`owasp-crs-v030301-id942370-sqli` | 2 | Detects classic SQL injection probings 2/3  
`owasp-crs-v030301-id942380-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942390-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942400-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942410-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942470-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942480-sqli` | 2 | SQL injection attack  
`owasp-crs-v030301-id942430-sqli` | 2 | Restricted SQL character anomaly detection (args): # of special characters exceeded (12)  
`owasp-crs-v030301-id942440-sqli` | 2 | SQL comment sequence detected  
`owasp-crs-v030301-id942450-sqli` | 2 | SQL hex encoding identified  
`owasp-crs-v030301-id942510-sqli` | 2 | SQLi bypass attempt by ticks or backticks detected  
`owasp-crs-v030301-id942251-sqli` | 3 | Detects HAVING injections  
`owasp-crs-v030301-id942490-sqli` | 3 | Detects classic SQL injection probings 3/3  
`owasp-crs-v030301-id942420-sqli` | 3 | Restricted SQL character anomaly detection (cookies): # of special characters exceeded (8)  
`owasp-crs-v030301-id942431-sqli` | 3 | Restricted SQL character anomaly detection (args): # of special characters exceeded (6)  
`owasp-crs-v030301-id942460-sqli` | 3 | Meta-character anomaly detection alert - repetitive non-word characters  
`owasp-crs-v030301-id942101-sqli` | 3 | SQL injection attack detected using libinjection  
`owasp-crs-v030301-id942511-sqli` | 3 | SQLi bypass attempt by ticks detected  
`owasp-crs-v030301-id942421-sqli` | 4 | Restricted SQL character anomaly detection (cookies): # of special characters exceeded (3)  
`owasp-crs-v030301-id942432-sqli` | 4 | Restricted SQL character anomaly detection (args): # of special characters exceeded (2)  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`Not included` | 1 | SQL injection attack detected using libinjection  
`owasp-crs-v030001-id942140-sqli` | 1 | SQL injection attack: common DB names detected  
`owasp-crs-v030001-id942160-sqli` | 1 | Detects SQLi tests using `sleep` or `benchmark`  
`owasp-crs-v030001-id942170-sqli` | 1 | Detects SQL `sleep` or `benchmark` injection attempts including conditional queries  
`owasp-crs-v030001-id942190-sqli` | 1 | Detects MSSQL code execution and information gathering attempts  
`owasp-crs-v030001-id942220-sqli` | 1 | Looks for integer overflow attacks  
`owasp-crs-v030001-id942230-sqli` | 1 | Detects conditional SQL injection attempts  
`owasp-crs-v030001-id942240-sqli` | 1 | Detects MySQL charset switch and MSSQL DoS attempts  
`owasp-crs-v030001-id942250-sqli` | 1 | Detects MATCH AGAINST  
`owasp-crs-v030001-id942270-sqli` | 1 | Looks for basic SQL injection; common attack string for MySql  
`owasp-crs-v030001-id942280-sqli` | 1 | Detects Postgres `pg_sleep` injection  
`owasp-crs-v030001-id942290-sqli` | 1 | Finds basic MongoDB SQL injection attempts  
`owasp-crs-v030001-id942320-sqli` | 1 | Detects MySQL and PostgreSQL stored procedure or function injections  
`owasp-crs-v030001-id942350-sqli` | 1 | Detects MySQL UDF injection and other data or structure manipulation attempts  
`owasp-crs-v030001-id942360-sqli` | 1 | Detects concatenated basic SQL injection and SQLLFI attempts  
`Not included` | 1 | MySQL inline comment detected  
`owasp-crs-v030001-id942110-sqli` | 2 | SQL injection attack: common injection testing detected  
`owasp-crs-v030001-id942120-sqli` | 2 | SQL injection attack: SQL operator detected  
`Not included` | 2 | SQL injection attack: SQL tautology detected  
`owasp-crs-v030001-id942150-sqli` | 2 | SQL injection attack  
`owasp-crs-v030001-id942180-sqli` | 2 | Detects basic SQL authentication bypass attempts 1/3  
`owasp-crs-v030001-id942200-sqli` | 2 | Detects MySQL comment- or space-obfuscated injections and backtick termination  
`owasp-crs-v030001-id942210-sqli` | 2 | Detects chained SQL injection attempts 1/2  
`owasp-crs-v030001-id942260-sqli` | 2 | Detects basic SQL authentication bypass attempts 2/3  
`owasp-crs-v030001-id942300-sqli` | 2 | Detects MySQL comments  
`owasp-crs-v030001-id942310-sqli` | 2 | Detects chained SQL injection attempts 2/2  
`owasp-crs-v030001-id942330-sqli` | 2 | Detects classic SQL injection probings 1/2  
`owasp-crs-v030001-id942340-sqli` | 2 | Detects basic SQL authentication bypass attempts 3/3  
`Not included` | 2 | Detects basic SQL injection based on keyword alter or union  
`Not included` | 2 | Detects classic SQL injection probings 2/3  
`owasp-crs-v030001-id942380-sqli` | 2 | SQL injection attack  
`owasp-crs-v030001-id942390-sqli` | 2 | SQL injection attack  
`owasp-crs-v030001-id942400-sqli` | 2 | SQL injection attack  
`owasp-crs-v030001-id942410-sqli` | 2 | SQL injection attack  
`Not included` | 2 | SQL injection attack  
`Not included` | 2 | SQL injection attack  
`owasp-crs-v030001-id942430-sqli` | 2 | Restricted SQL character anomaly detection (args): # of special characters exceeded (12)  
`owasp-crs-v030001-id942440-sqli` | 2 | SQL comment sequence detected  
`owasp-crs-v030001-id942450-sqli` | 2 | SQL hex encoding identified  
`Not included` | 2 | SQLi bypass attempt by ticks or backticks detected  
`owasp-crs-v030001-id942251-sqli` | 3 | Detects HAVING injections  
`Not included` | 2 | Detects classic SQL injection probings 3/3  
`owasp-crs-v030001-id942420-sqli` | 3 | Restricted SQL character anomaly detection (cookies): # of special characters exceeded (8)  
`owasp-crs-v030001-id942431-sqli` | 3 | Restricted SQL character anomaly detection (args): # of special characters exceeded (6)  
`owasp-crs-v030001-id942460-sqli` | 3 | Meta-character anomaly detection alert - repetitive non-word characters  
`Not included` | 3 | SQL injection attack detected using libinjection  
`Not included` | 3 | SQLi bypass attempt by ticks detected  
`owasp-crs-v030001-id942421-sqli` | 4 | Restricted SQL character anomaly detection (cookies): # of special characters exceeded (3)  
`owasp-crs-v030001-id942432-sqli` | 4 | Restricted SQL character anomaly detection (args): # of special characters exceeded (2)  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('sqli-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('sqli-v422-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('sqli-v422-stable', {'sensitivity': 3})  
4 | evaluatePreconfiguredWaf('sqli-v422-stable', {'sensitivity': 4})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('sqli-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('sqli-v33-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('sqli-v33-stable', {'sensitivity': 3})  
4 | evaluatePreconfiguredWaf('sqli-v33-stable', {'sensitivity': 4})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('sqli-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('sqli-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('sqli-stable', {'sensitivity': 3})  
4 | evaluatePreconfiguredWaf('sqli-stable', {'sensitivity': 4})  
  
### Cross-site scripting (XSS)

The following table provides the signature ID, sensitivity level, and description of each supported signature in the XSS preconfigured WAF rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id941100-xss` | 1 | XSS attack detected using libinjection  
`owasp-crs-v042200-id941110-xss` | 1 | XSS filter - category 1: script tag vector  
`owasp-crs-v042200-id941130-xss` | 1 | XSS filter - category 3: attribute vector  
`owasp-crs-v042200-id941140-xss` | 1 | XSS filter - category 4: JavaScript URI vector  
`owasp-crs-v042200-id941160-xss` | 1 | NoScript XSS InjectionChecker: HTML injection  
`owasp-crs-v042200-id941170-xss` | 1 | NoScript XSS InjectionChecker: attribute injection  
`owasp-crs-v042200-id941180-xss` | 1 | Node-validator denylist keywords  
`owasp-crs-v042200-id941190-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941200-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941210-xss` | 1 | Javascript word detected  
`owasp-crs-v042200-id941220-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941230-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941240-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941250-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941260-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941270-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941280-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941290-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941300-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941310-xss` | 1 | US-ASCII malformed encoding XSS filter - attack detected  
`owasp-crs-v042200-id941350-xss` | 1 | UTF-7 encoding IE XSS - attack detected  
`owasp-crs-v042200-id941360-xss` | 1 | Hieroglyphy obfuscation detected  
`owasp-crs-v042200-id941370-xss` | 1 | JavaScript global variable found  
`owasp-crs-v042200-id941390-xss` | 1 | Javascript method detected  
`owasp-crs-v042200-id941400-xss` | 1 | XSS JavaScript function without parentheses  
`owasp-crs-v042200-id941101-xss` | 2 | XSS attack detected using libinjection  
`owasp-crs-v042200-id941120-xss` | 2 | XSS filter - category 2: event handler vector  
`owasp-crs-v042200-id941150-xss` | 2 | XSS filter - category 5: disallowed HTML attributes  
`owasp-crs-v042200-id941181-xss` | 2 | Node-validator denylist keywords  
`owasp-crs-v042200-id941320-xss` | 2 | Possible XSS attack detected - HTML tag handler  
`owasp-crs-v042200-id941330-xss` | 2 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941340-xss` | 2 | IE XSS filters - attack detected  
`owasp-crs-v042200-id941380-xss` | 2 | AngularJS client side template injection detected  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id941100-xss` | 1 | XSS attack detected using libinjection  
`owasp-crs-v030301-id941110-xss` | 1 | XSS filter - category 1: script tag vector  
`owasp-crs-v030301-id941120-xss` | 1 | XSS filter - category 2: event handler vector  
`owasp-crs-v030301-id941130-xss` | 1 | XSS filter - category 3: attribute vector  
`owasp-crs-v030301-id941140-xss` | 1 | XSS filter - category 4: JavaScript URI vector  
`owasp-crs-v030301-id941160-xss` | 1 | NoScript XSS InjectionChecker: HTML injection  
`owasp-crs-v030301-id941170-xss` | 1 | NoScript XSS InjectionChecker: attribute injection  
`owasp-crs-v030301-id941180-xss` | 1 | Node-validator denylist keywords  
`owasp-crs-v030301-id941190-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941200-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941210-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941220-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941230-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941240-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941250-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941260-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941270-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941280-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941290-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941300-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941310-xss` | 1 | US-ASCII malformed encoding XSS filter - attack detected  
`owasp-crs-v030301-id941350-xss` | 1 | UTF-7 encoding IE XSS - attack detected  
`owasp-crs-v030301-id941360-xss` | 1 | Hieroglyphy obfuscation detected  
`owasp-crs-v030301-id941370-xss` | 1 | JavaScript global variable found  
`owasp-crs-v030301-id941101-xss` | 2 | XSS attack detected using libinjection  
`owasp-crs-v030301-id941150-xss` | 2 | XSS filter - category 5: disallowed HTML attributes  
`owasp-crs-v030301-id941320-xss` | 2 | Possible XSS attack detected - HTML tag handler  
`owasp-crs-v030301-id941330-xss` | 2 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941340-xss` | 2 | IE XSS filters - attack detected  
`owasp-crs-v030301-id941380-xss` | 2 | AngularJS client side template injection detected  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`Not included` | 1 | XSS attack detected using libinjection  
`owasp-crs-v030001-id941110-xss` | 1 | XSS filter - category 1: script tag vector  
`owasp-crs-v030001-id941120-xss` | 1 | XSS filter - category 2: event handler vector  
`owasp-crs-v030001-id941130-xss` | 1 | XSS filter - category 3: attribute vector  
`owasp-crs-v030001-id941140-xss` | 1 | XSS filter - category 4: JavaScript URI vector  
`owasp-crs-v030001-id941160-xss` | 1 | NoScript XSS InjectionChecker: HTML injection  
`owasp-crs-v030001-id941170-xss` | 1 | NoScript XSS InjectionChecker: attribute injection  
`owasp-crs-v030001-id941180-xss` | 1 | Node-validator denylist keywords  
`owasp-crs-v030001-id941190-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941200-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941210-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941220-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941230-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941240-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941250-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941260-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941270-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941280-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941290-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941300-xss` | 1 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941310-xss` | 1 | US-ASCII malformed encoding XSS filter - attack detected  
`owasp-crs-v030001-id941350-xss` | 1 | UTF-7 encoding IE XSS - attack detected  
`Not included` | 1 | JSF*ck or hieroglyphy obfuscation detected  
`Not included` | 1 | JavaScript global variable found  
`Not included` | 2 | XSS attack detected using libinjection  
`owasp-crs-v030001-id941150-xss` | 2 | XSS filter - category 5: disallowed HTML attributes  
`owasp-crs-v030001-id941320-xss` | 2 | Possible XSS attack detected - HTML tag handler  
`owasp-crs-v030001-id941330-xss` | 2 | IE XSS filters - attack detected  
`owasp-crs-v030001-id941340-xss` | 2 | IE XSS filters - attack detected  
`Not included` | 2 | AngularJS client side template injection detected  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('xss-v422-stable', {'sensitivity': 2})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('xss-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('xss-v33-stable', {'sensitivity': 2})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('xss-stable', {'sensitivity': 1})  
  
### Local file inclusion (LFI)

The following table provides the signature ID, sensitivity level, and description of each supported signature in the LFI preconfigured WAF rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id930100-lfi` | 1 | Path traversal attack (/../) or (/.../)  
`owasp-crs-v042200-id930110-lfi` | 1 | Path traversal attack (/../) or (/.../)  
`owasp-crs-v042200-id930120-lfi` | 1 | OS file access attempt  
`owasp-crs-v042200-id930130-lfi` | 1 | Restricted file access attempt  
`owasp-crs-v042200-id930121-lfi` | 2 | OS file access attempt in REQUEST_HEADERS  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id930100-lfi` | 1 | Path traversal attack (/../)  
`owasp-crs-v030301-id930110-lfi` | 1 | Path traversal attack (/../)  
`owasp-crs-v030301-id930120-lfi` | 1 | OS file access attempt  
`owasp-crs-v030301-id930130-lfi` | 1 | Restricted file access attempt  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id930100-lfi` | 1 | Path traversal attack (/../)  
`owasp-crs-v030001-id930110-lfi` | 1 | Path traversal attack (/../)  
`owasp-crs-v030001-id930120-lfi` | 1 | OS file access attempt  
`owasp-crs-v030001-id930130-lfi` | 1 | Restricted file access attempt  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('lfi-v422-stable', {'sensitivity': 1})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('lfi-v33-stable', {'sensitivity': 1})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('lfi-stable', {'sensitivity': 1})  
  
### Remote code execution (RCE)

The following table provides the signature ID, sensitivity level, and description of each supported signature in the RCE preconfigured WAF rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id932230-rce` | 1 | Remote command execution: UNIX command injection (2-3 chars)  
`owasp-crs-v042200-id932235-rce` | 1 | Remote command execution: UNIX command injection (command without evasion)  
`owasp-crs-v042200-id932120-rce` | 1 | Remote command execution: Windows HTML tag handler command found  
`owasp-crs-v042200-id932125-rce` | 1 | Remote command execution: Windows HTML tag handler alias command injection  
`owasp-crs-v042200-id932130-rce` | 1 | Remote command execution: UNIX shell expression found  
`owasp-crs-v042200-id932140-rce` | 1 | Remote command execution: Windows FOR or IF command found  
`owasp-crs-v042200-id932270-rce` | 1 | Remote command execution: UNIX shell expression found  
`owasp-crs-v042200-id932250-rce` | 1 | Remote command execution: Direct UNIX command execution  
`owasp-crs-v042200-id932260-rce` | 1 | Remote command execution: Direct UNIX command execution  
`owasp-crs-v042200-id932330-rce` | 1 | Remote command execution: UNIX shell history invocation  
`owasp-crs-v042200-id932160-rce` | 1 | Remote command execution: UNIX shell code found  
`owasp-crs-v042200-id932170-rce` | 1 | Remote command execution: shellshock (CVE-2014-6271)  
`owasp-crs-v042200-id932171-rce` | 1 | Remote command execution: shellshock (CVE-2014-6271)  
`owasp-crs-v042200-id932175-rce` | 1 | Remote command execution: UNIX shell alias invocation  
`owasp-crs-v042200-id932180-rce` | 1 | Restricted file upload attempt  
`owasp-crs-v042200-id932370-rce` | 1 | Remote command execution: Windows command injection  
`owasp-crs-v042200-id932380-rce` | 1 | Remote command execution: Windows command injection  
`owasp-crs-v042200-id932280-rce` | 1 | Remote command execution: brace expansion found  
`owasp-crs-v042200-id932231-rce` | 2 | Remote command execution: UNIX command injection  
`owasp-crs-v042200-id932131-rce` | 2 | Remote command execution: UNIX shell expression found  
`owasp-crs-v042200-id932200-rce` | 2 | RCE bypass technique  
`owasp-crs-v042200-id932205-rce` | 2 | RCE bypass technique  
`owasp-crs-v042200-id932206-rce` | 2 | RCE bypass technique  
`owasp-crs-v042200-id932220-rce` | 2 | Remote command execution: UNIX command injection with pipe  
`owasp-crs-v042200-id932240-rce` | 2 | Remote command execution: UNIX command injection evasion attempt detected  
`owasp-crs-v042200-id932210-rce` | 2 | Remote command execution: SQLite system command execution  
`owasp-crs-v042200-id932271-rce` | 2 | Remote command execution: UNIX shell expression found  
`owasp-crs-v042200-id932300-rce` | 2 | Remote command execution: SMTP command execution  
`owasp-crs-v042200-id932310-rce` | 2 | Remote command execution: IMAP command execution  
`owasp-crs-v042200-id932320-rce` | 2 | Remote command execution: POP3 command execution  
`owasp-crs-v042200-id932236-rce` | 2 | Remote command execution: UNIX command injection (command without evasion)  
`owasp-crs-v042200-id932239-rce` | 2 | Remote command execution: UNIX command injection found in user-agent or referer header  
`owasp-crs-v042200-id932161-rce` | 2 | Remote command execution: UNIX shell code found in REQUEST_HEADERS  
`owasp-crs-v042200-id932371-rce` | 2 | Remote command execution: Windows command injection  
`owasp-crs-v042200-id932281-rce` | 2 | Remote command execution: brace expansion found  
`owasp-crs-v042200-id932207-rce` | 2 | RCE bypass technique  
`owasp-crs-v042200-id932232-rce` | 3 | Remote command execution: UNIX command injection  
`owasp-crs-v042200-id932237-rce` | 3 | Remote command execution: UNIX shell code found in REQUEST_HEADERS  
`owasp-crs-v042200-id932238-rce` | 3 | Remote command execution: UNIX shell code found in REQUEST_HEADERS  
`owasp-crs-v042200-id932190-rce` | 3 | Remote command execution: wildcard bypass technique attempt  
`owasp-crs-v042200-id932301-rce` | 3 | Remote command execution: SMTP command execution  
`owasp-crs-v042200-id932311-rce` | 3 | Remote command execution: IMAP command execution  
`owasp-crs-v042200-id932321-rce` | 3 | Remote command execution: POP3 command execution  
`owasp-crs-v042200-id932331-rce` | 3 | Remote command execution: UNIX shell history invocation  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id932100-rce` | 1 | UNIX command injection  
`owasp-crs-v030301-id932105-rce` | 1 | UNIX command injection  
`owasp-crs-v030301-id932110-rce` | 1 | Windows command injection  
`owasp-crs-v030301-id932115-rce` | 1 | Windows command injection  
`owasp-crs-v030301-id932120-rce` | 1 | Windows PowerShell command found  
`owasp-crs-v030301-id932130-rce` | 1 | UNIX shell expression found  
`owasp-crs-v030301-id932140-rce` | 1 | Windows FOR or IF command found  
`owasp-crs-v030301-id932150-rce` | 1 | Direct UNIX command execution  
`owasp-crs-v030301-id932160-rce` | 1 | UNIX shell code found  
`owasp-crs-v030301-id932170-rce` | 1 | Shellshock (CVE-2014-6271)  
`owasp-crs-v030301-id932171-rce` | 1 | Shellshock (CVE-2014-6271)  
`owasp-crs-v030301-id932180-rce` | 1 | Restricted file upload attempt  
`owasp-crs-v030301-id932200-rce` | 2 | RCE bypass technique  
`owasp-crs-v030301-id932106-rce` | 3 | Remote command execution: UNIX command injection  
`owasp-crs-v030301-id932190-rce` | 3 | Remote command execution: wildcard bypass technique attempt  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id932100-rce` | 1 | UNIX command injection  
`owasp-crs-v030001-id932105-rce` | 1 | UNIX command injection  
`owasp-crs-v030001-id932110-rce` | 1 | Windows command injection  
`owasp-crs-v030001-id932115-rce` | 1 | Windows command injection  
`owasp-crs-v030001-id932120-rce` | 1 | Windows PowerShell command found  
`owasp-crs-v030001-id932130-rce` | 1 | UNIX shell expression found  
`owasp-crs-v030001-id932140-rce` | 1 | Windows FOR or IF command found  
`owasp-crs-v030001-id932150-rce` | 1 | Direct UNIX command execution  
`owasp-crs-v030001-id932160-rce` | 1 | UNIX shell code found  
`owasp-crs-v030001-id932170-rce` | 1 | Shellshock (CVE-2014-6271)  
`owasp-crs-v030001-id932171-rce` | 1 | Shellshock (CVE-2014-6271)  
`Not included` | 1 | Restricted file upload attempt  
`Not included` | 2 | RCE bypass technique  
`Not included` | 3 | Remote command execution: UNIX command injection  
`Not included` | 3 | Remote command execution: wildcard bypass technique attempt  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('rce-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('rce-v422-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('rce-v422-stable', {'sensitivity': 3})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('rce-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('rce-v33-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('rce-v33-stable', {'sensitivity': 3})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('rce-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('rce-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('rce-stable', {'sensitivity': 3})  
  
### Remote file inclusion (RFI)

The following table provides the signature ID, sensitivity level, and description of each supported signature in the RFI preconfigured WAF rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id931100-rfi` | 1 | Possible remote file inclusion (RFI) attack: URL parameter using IP address  
`owasp-crs-v042200-id931110-rfi` | 1 | Possible remote file inclusion (RFI) attack: common RFI vulnerable parameter name used with URL payload  
`owasp-crs-v042200-id931120-rfi` | 1 | Possible remote file inclusion (RFI) attack: URL payload used with trailing question mark character (?)  
`owasp-crs-v042200-id931130-rfi` | 2 | Possible remote file inclusion (RFI) attack: off-domain reference or link  
`owasp-crs-v042200-id931131-rfi` | 2 | Possible remote file inclusion (RFI) attack: off-domain reference or link  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id931100-rfi` | 1 | URL parameter using IP address  
`owasp-crs-v030301-id931110-rfi` | 1 | Common RFI vulnerable parameter name used with URL payload  
`owasp-crs-v030301-id931120-rfi` | 1 | URL payload used with trailing question mark character (?)  
`owasp-crs-v030301-id931130-rfi` | 2 | Off-domain reference or link  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id931100-rfi` | 1 | URL parameter using IP address  
`owasp-crs-v030001-id931110-rfi` | 1 | Common RFI vulnerable parameter name used with URL payload  
`owasp-crs-v030001-id931120-rfi` | 1 | URL payload used with trailing question mark character (?)  
`owasp-crs-v030001-id931130-rfi` | 2 | Off-domain reference or link  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('rfi-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('rfi-v422-stable', {'sensitivity': 2})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('rfi-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('rfi-v33-stable', {'sensitivity': 2})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('rfi-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('rfi-stable', {'sensitivity': 2})  
  
### Method enforcement

**Note:** CRS 4.22 allows only the `GET`, `HEAD`, `POST`, and `OPTIONS` HTTP methods.

The following table provides the signature ID, sensitivity level, and description of each supported signature in the method enforcement preconfigured rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id911100-methodenforcement` | 1 | Method isn't allowed by policy  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id911100-methodenforcement` | 1 | Method isn't allowed by policy  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id911100-methodenforcement` | 1 | Method isn't allowed by policy  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('methodenforcement-v422-stable', {'sensitivity': 1})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('methodenforcement-v33-stable', {'sensitivity': 1})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('methodenforcement-stable', {'sensitivity': 1})  
  
### Scanner detection

The following table provides the signature ID, sensitivity level, and description of each supported signature in the scanner detection preconfigured rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id913100-scannerdetection` | 1 | Found user-agent associated with security scanner  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id913100-scannerdetection` | 1 | Found user-agent associated with security scanner  
`owasp-crs-v030301-id913110-scannerdetection` | 1 | Found request header associated with security scanner  
`owasp-crs-v030301-id913120-scannerdetection` | 1 | Found request filename or argument associated with security scanner  
`owasp-crs-v030301-id913101-scannerdetection` | 2 | Found user-agent associated with scripting or generic HTTP client  
`owasp-crs-v030301-id913102-scannerdetection` | 2 | Found user-agent associated with web crawler or bot  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id913100-scannerdetection` | 1 | Found user-agent associated with security scanner  
`owasp-crs-v030001-id913110-scannerdetection` | 1 | Found request header associated with security scanner  
`owasp-crs-v030001-id913120-scannerdetection` | 1 | Found request filename or argument associated with security scanner  
`owasp-crs-v030001-id913101-scannerdetection` | 2 | Found user-agent associated with scripting or generic HTTP client  
`owasp-crs-v030001-id913102-scannerdetection` | 2 | Found user-agent associated with web crawler or bot  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('scannerdetection-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('scannerdetection-v422-stable', {'sensitivity': 2})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('scannerdetection-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('scannerdetection-v33-stable', {'sensitivity': 2})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('scannerdetection-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('scannerdetection-stable', {'sensitivity': 2})  
  
### Protocol attack

The following table provides the signature ID, sensitivity level, and description of each supported signature in the protocol attack preconfigured rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id921110-protocolattack` | 1 | HTTP request smuggling attack  
`owasp-crs-v042200-id921120-protocolattack` | 1 | HTTP response splitting attack  
`owasp-crs-v042200-id921130-protocolattack` | 1 | HTTP response splitting attack  
`owasp-crs-v042200-id921140-protocolattack` | 1 | HTTP header injection attack using headers  
`owasp-crs-v042200-id921150-protocolattack` | 1 | HTTP header injection attack using payload (CR/LF detected)  
`owasp-crs-v042200-id921160-protocolattack` | 1 | HTTP header injection attack using payload (CR/LF and header-name detected)  
`owasp-crs-v042200-id921190-protocolattack` | 1 | HTTP splitting (CR/LF in request filename detected)  
`owasp-crs-v042200-id921200-protocolattack` | 1 | LDAP injection attack  
`owasp-crs-v042200-id921421-protocolattack` | 1 | Content-Type header: dangerous Content-Type outside the mime type declaration  
`owasp-crs-v042200-id921240-protocolattack` | 1 | mod_proxy attack attempt detected  
`owasp-crs-v042200-id921250-protocolattack` | 1 | Old cookies v1 usage attempt detected  
`owasp-crs-v042200-id921151-protocolattack` | 2 | HTTP header injection attack using payload (CR/LF detected)  
`owasp-crs-v042200-id921422-protocolattack` | 2 | Content-Type header: dangerous Content-Type outside the mime type declaration  
`owasp-crs-v042200-id921230-protocolattack` | 3 | HTTP range header detected  
`owasp-crs-v042200-id921170-protocolattack` | 3 | HTTP parameter pollution (%{MATCHED_VAR_NAME})  
`owasp-crs-v042200-id921210-protocolattack` | 3 | HTTP parameter pollution after detecting bogus character after parameter array  
`owasp-crs-v042200-id921220-protocolattack` | 4 | HTTP parameter pollution possible using array notation  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`Not included` | 1 | HTTP request smuggling attack  
`owasp-crs-v030301-id921110-protocolattack` | 1 | HTTP request smuggling attack  
`owasp-crs-v030301-id921120-protocolattack` | 1 | HTTP response splitting attack  
`owasp-crs-v030301-id921130-protocolattack` | 1 | HTTP response splitting attack  
`owasp-crs-v030301-id921140-protocolattack` | 1 | HTTP header injection attack using headers  
`owasp-crs-v030301-id921150-protocolattack` | 1 | HTTP header injection attack using payload (CR/LF detected)  
`owasp-crs-v030301-id921160-protocolattack` | 1 | HTTP header injection attack using payload (CR/LF and header-name detected)  
`owasp-crs-v030301-id921190-protocolattack` | 1 | HTTP splitting (CR/LF in request filename detected)  
`owasp-crs-v030301-id921200-protocolattack` | 1 | LDAP injection attack  
`owasp-crs-v030301-id921151-protocolattack` | 2 | HTTP header injection attack using payload (CR/LF detected)  
`owasp-crs-v030301-id921170-protocolattack` | 3 | HTTP parameter pollution  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id921100-protocolattack` | 1 | HTTP request smuggling attack  
`owasp-crs-v030001-id921110-protocolattack` | 1 | HTTP request smuggling attack  
`owasp-crs-v030001-id921120-protocolattack` | 1 | HTTP response splitting attack  
`owasp-crs-v030001-id921130-protocolattack` | 1 | HTTP response splitting attack  
`owasp-crs-v030001-id921140-protocolattack` | 1 | HTTP header injection attack using headers  
`owasp-crs-v030001-id921150-protocolattack` | 1 | HTTP header injection attack using payload (CR/LF detected)  
`owasp-crs-v030001-id921160-protocolattack` | 1 | HTTP header injection attack using payload (CR/LF and header-name detected)  
`Not included` | 1 | HTTP splitting (CR/LF in request filename detected)  
`Not included` | 1 | LDAP injection attack  
`owasp-crs-v030001-id921151-protocolattack` | 2 | HTTP header injection attack using payload (CR/LF detected)  
`owasp-crs-v030001-id921170-protocolattack` | 3 | HTTP parameter pollution  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('protocolattack-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('protocolattack-v422-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('protocolattack-v422-stable', {'sensitivity': 3})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('protocolattack-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('protocolattack-v33-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('protocolattack-v33-stable', {'sensitivity': 3})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('protocolattack-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('protocolattack-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('protocolattack-stable', {'sensitivity': 3})  
  
### PHP

The following table provides the signature ID, sensitivity level, and description of each supported signature in the PHP preconfigured WAF rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id933100-php` | 1 | PHP injection attack: PHP open tag found  
`owasp-crs-v042200-id933110-php` | 1 | PHP injection attack: PHP script file upload found  
`owasp-crs-v042200-id933120-php` | 1 | PHP injection attack: configuration directive found  
`owasp-crs-v042200-id933130-php` | 1 | PHP injection attack: variables found  
`owasp-crs-v042200-id933135-php` | 1 | PHP injection attack: variables access found  
`owasp-crs-v042200-id933140-php` | 1 | PHP injection attack: I/O stream found  
`owasp-crs-v042200-id933200-php` | 1 | PHP injection attack: wrapper scheme detected  
`owasp-crs-v042200-id933150-php` | 1 | PHP injection attack: high-risk PHP function name found  
`owasp-crs-v042200-id933160-php` | 1 | PHP injection attack: high-risk PHP function call found  
`owasp-crs-v042200-id933170-php` | 1 | PHP injection attack: serialized object injection  
`owasp-crs-v042200-id933180-php` | 1 | PHP injection attack: variable function call found  
`owasp-crs-v042200-id933210-php` | 1 | PHP injection attack: variable function call found  
`owasp-crs-v042200-id933151-php` | 2 | PHP injection attack: medium-risk PHP function name found  
`owasp-crs-v042200-id933152-php` | 2 | PHP injection attack: medium-risk PHP function name found  
`owasp-crs-v042200-id933153-php` | 2 | PHP injection attack: medium-risk PHP function name found  
`owasp-crs-v042200-id933131-php` | 3 | PHP injection attack: variables found  
`owasp-crs-v042200-id933161-php` | 3 | PHP injection attack: low-value PHP function call found  
`owasp-crs-v042200-id933111-php` | 3 | PHP injection attack: PHP script file upload found  
`owasp-crs-v042200-id933190-php` | 3 | PHP injection attack: PHP closing tag found  
`owasp-crs-v042200-id933211-php` | 3 | PHP injection attack: variable function call found  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id933100-php` | 1 | PHP injection attack: PHP open tag found  
`owasp-crs-v030301-id933110-php` | 1 | PHP injection attack: PHP script file upload found  
`owasp-crs-v030301-id933120-php` | 1 | PHP injection attack: configuration directive found  
`owasp-crs-v030301-id933130-php` | 1 | PHP injection attack: variables found  
`owasp-crs-v030301-id933140-php` | 1 | PHP injection attack: I/O stream found  
`owasp-crs-v030301-id933200-php` | 1 | PHP injection attack: wrapper scheme detected  
`owasp-crs-v030301-id933150-php` | 1 | PHP injection attack: high-risk PHP function name found  
`owasp-crs-v030301-id933160-php` | 1 | PHP injection attack: high-risk PHP function call found  
`owasp-crs-v030301-id933170-php` | 1 | PHP injection attack: serialized object injection  
`owasp-crs-v030301-id933180-php` | 1 | PHP injection attack: variable function call found  
`owasp-crs-v030301-id933210-php` | 1 | PHP injection attack: variable function call found  
`owasp-crs-v030301-id933151-php` | 2 | PHP injection attack: medium-risk PHP function name found  
`owasp-crs-v030301-id933131-php` | 3 | PHP injection attack: variables found  
`owasp-crs-v030301-id933161-php` | 3 | PHP injection attack: low-value PHP function call found  
`owasp-crs-v030301-id933111-php` | 3 | PHP injection attack: PHP script file upload found  
`owasp-crs-v030301-id933190-php` | 3 | PHP injection attack: PHP closing tag found  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id933100-php` | 1 | PHP injection attack: PHP open tag found  
`owasp-crs-v030001-id933110-php` | 1 | PHP injection attack: PHP script file upload found  
`owasp-crs-v030001-id933120-php` | 1 | PHP injection attack: configuration directive found  
`owasp-crs-v030001-id933130-php` | 1 | PHP injection attack: variables found  
`owasp-crs-v030001-id933140-php` | 1 | PHP injection attack: I/O stream found  
`Not included` | 1 | PHP injection attack: wrapper scheme detected  
`owasp-crs-v030001-id933150-php` | 1 | PHP injection attack: high-risk PHP function name found  
`owasp-crs-v030001-id933160-php` | 1 | PHP injection attack: high-risk PHP function call found  
`owasp-crs-v030001-id933170-php` | 1 | PHP injection attack: serialized object injection  
`owasp-crs-v030001-id933180-php` | 1 | PHP injection attack: variable function call found  
`Not included` | 1 | PHP injection attack: variable function call found  
`owasp-crs-v030001-id933151-php` | 2 | PHP injection attack: medium-risk PHP function name found  
`owasp-crs-v030001-id933131-php` | 3 | PHP injection attack: variables found  
`owasp-crs-v030001-id933161-php` | 3 | PHP injection attack: low-value PHP function call found  
`owasp-crs-v030001-id933111-php` | 3 | PHP injection attack: PHP script file upload found  
`Not included` | 3 | PHP injection attack: PHP closing tag found  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('php-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('php-v422-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('php-v422-stable', {'sensitivity': 3})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('php-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('php-v33-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('php-v33-stable', {'sensitivity': 3})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('php-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('php-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('php-stable', {'sensitivity': 3})  
  
### Session fixation

The following table provides the signature ID, sensitivity level, and description of each supported signature in the session fixation preconfigured rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id943100-sessionfixation` | 1 | Possible session fixation attack: setting cookie values in HTML  
`owasp-crs-v042200-id943110-sessionfixation` | 1 | Possible session fixation attack: session ID parameter name with off-domain referer  
`owasp-crs-v042200-id943120-sessionfixation` | 1 | Possible session fixation attack: session ID parameter name with no referer  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id943100-sessionfixation` | 1 | Possible session fixation attack: setting cookie values in HTML  
`owasp-crs-v030301-id943110-sessionfixation` | 1 | Possible session fixation attack: session ID parameter name with off-domain referer  
`owasp-crs-v030301-id943120-sessionfixation` | 1 | Possible session fixation attack: session ID parameter name with no referer  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id943100-sessionfixation` | 1 | Possible session fixation attack: setting cookie values in HTML  
`owasp-crs-v030001-id943110-sessionfixation` | 1 | Possible session fixation attack: session ID parameter name with off-domain referer  
`owasp-crs-v030001-id943120-sessionfixation` | 1 | Possible session fixation attack: session ID parameter name with no referer  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('sessionfixation-v422-stable', {'sensitivity': 1})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('sessionfixation-v33-stable', {'sensitivity': 1})  
  
###  CRS 3.0 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('sessionfixation-stable', {'sensitivity': 1})  
  
### Java attack

The following table provides the signature ID, sensitivity level, and description of each supported signature in the Java attack preconfigured rule.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id944100-java` | 1 | Remote command execution: suspicious Java class detected  
`owasp-crs-v042200-id944110-java` | 1 | Remote command execution: Java process spawn (CVE-2017-9805)  
`owasp-crs-v042200-id944120-java` | 1 | Remote command execution: Java serialization (CVE-2015-4852)  
`owasp-crs-v042200-id944130-java` | 1 | Suspicious Java class detected  
`owasp-crs-v042200-id944140-java` | 1 | Java injection attack: Javascript file upload found  
`owasp-crs-v042200-id944150-java` | 1 | Potential remote command execution: Log4j or Log4shell  
`owasp-crs-v042200-id944151-java` | 2 | Potential remote command execution: Log4j or Log4shell  
`owasp-crs-v042200-id944200-java` | 2 | Magic bytes detected, probable Java serialization in use  
`owasp-crs-v042200-id944210-java` | 2 | Magic bytes detected Base64 encoded, probable Java serialization in use  
`owasp-crs-v042200-id944240-java` | 2 | Remote command execution: Java serialization (CVE-2015-4852)  
`owasp-crs-v042200-id944250-java` | 2 | Remote command execution: suspicious Java method detected  
`owasp-crs-v042200-id944260-java` | 2 | Remote command execution: malicious class-loading payload  
`owasp-crs-v042200-id944300-java` | 3 | Base64 encoded string matched suspicious keyword  
`owasp-crs-v042200-id944152-java` | 4 | Potential remote command execution: Log4j or Log4shell  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id944100-java` | 1 | Remote command execution: suspicious Java class detected  
`owasp-crs-v030301-id944110-java` | 1 | Remote command execution: Java process spawn (CVE-2017-9805)  
`owasp-crs-v030301-id944120-java` | 1 | Remote command execution: Java serialization (CVE-2015-4852)  
`owasp-crs-v030301-id944130-java` | 1 | Suspicious Java class detected  
`owasp-crs-v030301-id944200-java` | 2 | Magic bytes detected, probable Java serialization in use  
`owasp-crs-v030301-id944210-java` | 2 | Magic bytes detected Base64 encoded, probable Java serialization in use  
`owasp-crs-v030301-id944240-java` | 2 | Remote command execution: Java serialization (CVE-2015-4852)  
`owasp-crs-v030301-id944250-java` | 2 | Remote command execution: suspicious Java method detected  
`owasp-crs-v030301-id944300-java` | 3 | Base64 encoded string matched suspicious keyword  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`Not included` | 1 | Remote command execution: suspicious Java class detected  
`Not included` | 1 | Remote command execution: Java process spawn (CVE-2017-9805)  
`Not included` | 1 | Remote command execution: Java serialization (CVE-2015-4852)  
`Not included` | 1 | Suspicious Java class detected  
`Not included` | 2 | Magic bytes detected, probable Java serialization in use  
`Not included` | 2 | Magic bytes detected Base64 encoded, probable Java serialization in use  
`Not included` | 2 | Remote command execution: Java serialization (CVE-2015-4852)  
`Not included` | 2 | Remote command execution: suspicious Java method detected  
`Not included` | 3 | Base64 encoded string matched suspicious keyword  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('java-v422-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('java-v422-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('java-v422-stable', {'sensitivity': 3})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('java-v33-stable', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('java-v33-stable', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('java-v33-stable', {'sensitivity': 3})  
  
### Generic attack

The following table provides the signature ID, sensitivity level, and description of each supported signature in the generic attack preconfigured rule.

**Note:** The `nodejs` rule set in v3.3 was reclassified as `generic` in v4.22. Both versions use the same three-digit number _934_ as the starting digits for the rule ID.

###  CRS 4.22 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v042200-id934100-generic` | 1 | Node.js injection attack 1/2  
`owasp-crs-v042200-id934110-generic` | 1 | Possible server side request forgery (SSRF) attack: cloud provider metadata URL in parameter  
`owasp-crs-v042200-id934130-generic` | 1 | JavaScript prototype pollution  
`owasp-crs-v042200-id934150-generic` | 1 | Ruby injection attack  
`owasp-crs-v042200-id934160-generic` | 1 | Node.js DoS attack  
`owasp-crs-v042200-id934170-generic` | 1 | PHP data scheme attack  
`owasp-crs-v042200-id934101-generic` | 2 | Node.js injection attack 2/2  
`owasp-crs-v042200-id934120-generic` | 2 | Possible server side request forgery (SSRF) attack: URL parameter using IP address  
`owasp-crs-v042200-id934140-generic` | 2 | Perl injection attack  
`owasp-crs-v042200-id934180-generic` | 2 | SSTI attack  
  
###  CRS 3.3 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030301-id934100-nodejs` | 1 | Node.js injection attack  
  
###  CRS 3.0 

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`Not included` | 1 | Node.js injection attack  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

###  CRS 4.22 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('generic-v422-stable', {'sensitivity': 1})  
  
###  CRS 3.3 

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('nodejs-v33-stable', {'sensitivity': 1})  
  
### Cloud Armor WAF rules comparison: CRS 3.3 and CRS 4.22

The following table provides the full list of differences between the Cloud Armor **CRS 3.3** and **CRS 4.22** rule sets.

The `nodejs` category from CRS 3.3 was renamed to `generic` in CRS 4.22, though they share the same rule ID prefix "934". CRS 4.22 is recommended for modern threat protection.

Category | OWASP rule | Rule ID | In CRS 3.3 | In CRS 4.22 | Status  
---|---|---|---|---|---  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941100| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941101| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941110| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941120| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941130| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941140| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941150| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941160| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941170| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941180| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941181| No| Yes| 4.22 Only  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941190| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941200| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941210| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941220| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941230| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941240| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941250| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941260| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941270| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941280| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941290| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941300| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941310| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941320| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941330| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941340| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941350| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941360| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941370| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941380| Yes| Yes| Both  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941390| No| Yes| 4.22 Only  
**Cross-site scripting (XSS)**|  xss-v422-stable| 941400| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934100| Yes| Yes| Both  
**Generic (NodeJS)**|  generic-v422-stable| 934101| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934110| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934120| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934130| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934140| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934150| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934160| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934170| No| Yes| 4.22 Only  
**Generic (NodeJS)**|  generic-v422-stable| 934180| No| Yes| 4.22 Only  
**Java**|  java-v422-stable| 944100| Yes| Yes| Both  
**Java**|  java-v422-stable| 944110| Yes| Yes| Both  
**Java**|  java-v422-stable| 944120| Yes| Yes| Both  
**Java**|  java-v422-stable| 944130| Yes| Yes| Both  
**Java**|  java-v422-stable| 944140| No| Yes| 4.22 Only  
**Java**|  java-v422-stable| 944150| No| Yes| 4.22 Only  
**Java**|  java-v422-stable| 944151| No| Yes| 4.22 Only  
**Java**|  java-v422-stable| 944152| No| Yes| 4.22 Only  
**Java**|  java-v422-stable| 944200| Yes| Yes| Both  
**Java**|  java-v422-stable| 944210| Yes| Yes| Both  
**Java**|  java-v422-stable| 944240| Yes| Yes| Both  
**Java**|  java-v422-stable| 944250| Yes| Yes| Both  
**Java**|  java-v422-stable| 944260| No| Yes| 4.22 Only  
**Java**|  java-v422-stable| 944300| Yes| Yes| Both  
**Local file inclusion (LFI)**|  lfi-v422-stable| 930100| Yes| Yes| Both  
**Local file inclusion (LFI)**|  lfi-v422-stable| 930110| Yes| Yes| Both  
**Local file inclusion (LFI)**|  lfi-v422-stable| 930120| Yes| Yes| Both  
**Local file inclusion (LFI)**|  lfi-v422-stable| 930121| No| Yes| 4.22 Only  
**Local file inclusion (LFI)**|  lfi-v422-stable| 930130| Yes| Yes| Both  
**Method enforcement**|  methodenforcement-v422-stable| 911100| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933100| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933110| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933111| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933120| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933130| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933131| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933135| No| Yes| 4.22 Only  
**PHP**|  php-v422-stable| 933140| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933150| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933151| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933152| No| Yes| 4.22 Only  
**PHP**|  php-v422-stable| 933153| No| Yes| 4.22 Only  
**PHP**|  php-v422-stable| 933160| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933161| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933170| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933180| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933190| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933200| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933210| Yes| Yes| Both  
**PHP**|  php-v422-stable| 933211| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921110| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921120| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921130| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921140| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921150| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921151| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921160| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921170| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921190| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921200| Yes| Yes| Both  
**Protocol attack**|  protocolattack-v422-stable| 921210| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921220| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921230| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921240| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921250| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921421| No| Yes| 4.22 Only  
**Protocol attack**|  protocolattack-v422-stable| 921422| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932100| Yes| No| 3.3 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932105| Yes| No| 3.3 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932106| Yes| No| 3.3 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932110| Yes| No| 3.3 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932115| Yes| No| 3.3 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932120| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932125| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932130| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932131| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932140| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932150| Yes| No| 3.3 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932160| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932161| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932170| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932171| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932175| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932180| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932190| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932200| Yes| Yes| Both  
**Remote code execution (RCE)**|  rce-v422-stable| 932205| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932206| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932207| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932210| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932220| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932230| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932231| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932232| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932235| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932236| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932237| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932238| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932239| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932240| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932250| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932260| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932270| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932271| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932280| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932281| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932300| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932301| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932310| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932311| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932320| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932321| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932330| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932331| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932370| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932371| No| Yes| 4.22 Only  
**Remote code execution (RCE)**|  rce-v422-stable| 932380| No| Yes| 4.22 Only  
**Remote file inclusion (RFI)**|  rfi-v422-stable| 931100| Yes| Yes| Both  
**Remote file inclusion (RFI)**|  rfi-v422-stable| 931110| Yes| Yes| Both  
**Remote file inclusion (RFI)**|  rfi-v422-stable| 931120| Yes| Yes| Both  
**Remote file inclusion (RFI)**|  rfi-v422-stable| 931130| Yes| Yes| Both  
**Remote file inclusion (RFI)**|  rfi-v422-stable| 931131| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942100| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942101| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942110| Yes| No| 3.3 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942120| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942130| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942131| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942140| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942150| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942151| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942152| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942160| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942170| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942180| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942190| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942200| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942210| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942220| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942230| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942240| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942250| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942251| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942260| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942270| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942280| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942290| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942300| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942310| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942320| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942321| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942330| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942340| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942350| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942360| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942361| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942362| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942370| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942380| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942390| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942400| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942410| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942420| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942421| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942430| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942431| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942432| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942440| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942450| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942460| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942470| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942480| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942490| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942500| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942510| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942511| Yes| Yes| Both  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942520| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942521| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942522| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942530| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942540| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942550| No| Yes| 4.22 Only  
**SQL Injection (SQLi)**|  sqli-v422-stable| 942560| No| Yes| 4.22 Only  
**Scanner detection**|  scannerdetection-v422-stable| 913100| Yes| Yes| Both  
**Scanner detection**|  scannerdetection-v422-stable| 913101| Yes| No| 3.3 Only  
**Scanner detection**|  scannerdetection-v422-stable| 913102| Yes| No| 3.3 Only  
**Scanner detection**|  scannerdetection-v422-stable| 913110| Yes| No| 3.3 Only  
**Scanner detection**|  scannerdetection-v422-stable| 913120| Yes| No| 3.3 Only  
**Session fixation**|  sessionfixation-v422-stable| 943100| Yes| Yes| Both  
**Session fixation**|  sessionfixation-v422-stable| 943110| Yes| Yes| Both  
**Session fixation**|  sessionfixation-v422-stable| 943120| Yes| Yes| Both  
  
### CVEs and other vulnerabilities

The following table provides the signature ID, sensitivity level, and description of each supported signature in the React RCE vulnerability rule to help detect and mitigate CVE-2025-55182.

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`google-mrs-v202512-id000001-rce` | 0 | React RCE vulnerability to help detect and mitigate CVE-2025-55182  
`google-mrs-v202512-id000002-rce` | 0 | React RCE vulnerability to help detect and mitigate CVE-2025-55182  
  
Use the following expression to help detect and mitigate CVE-2025-55182:
    
    
    (has(request.headers['next-action']) || has(request.headers['rsc-action-id']) ||request.headers['content-type'].contains('multipart/form-data') || request.headers['content-type'].contains('application/x-www-form-urlencoded') ) && evaluatePreconfiguredWaf('cve-canary',{'sensitivity': 0, 'opt_in_rule_ids': ['google-mrs-v202512-id000001-rce', 'google-mrs-v202512-id000002-rce']})
    

The following table provides the signature ID, sensitivity level, and description of each supported signature in the CVE Log4j RCE vulnerability preconfigured rule.

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-v030001-id044228-cve` | 1 | Base rule to help detect exploit attempts of `CVE-2021-44228` & `CVE-2021-45046`  
`owasp-crs-v030001-id144228-cve` | 1 | Google-provided enhancements to cover more bypass and obfuscation attempts  
`owasp-crs-v030001-id244228-cve` | 3 | Increased sensitivity of detection to target even more bypass and obfuscation attempts, with nominal increase in risk of false positive detection  
`owasp-crs-v030001-id344228-cve` | 3 | Increased sensitivity of detection to target even more bypass and obfuscation attempts using base64 encoding, with nominal increase in risk of false positive detection  
  
You can configure a rule at a particular sensitivity level by using `evaluatePreconfiguredWaf()` with a preset sensitivity parameter. By default, Cloud Armor runs at sensitivity level 4 and evaluates all signatures in a rule set after you enable it. For more information about sensitivity levels, see [Tune Cloud Armor preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning#choose_a_sensitivity_level).

Sensitivity level | Expression  
---|---  
1 | evaluatePreconfiguredWaf('cve-canary', {'sensitivity': 1})  
2 | evaluatePreconfiguredWaf('cve-canary', {'sensitivity': 2})  
3 | evaluatePreconfiguredWaf('cve-canary', {'sensitivity': 3})  
  
### JSON-formatted content SQLi vulnerability

The following table provides the signature ID, sensitivity level, and description of the supported signature [`942550-sqli`](https://github.com/coreruleset/coreruleset/pull/3055), which covers the vulnerability in which malicious attackers can bypass WAF by appending JSON syntax to SQL injection payloads.

Signature ID (Rule ID) | Sensitivity level | Description  
---|---|---  
`owasp-crs-id942550-sqli` | 2 | Detects all JSON-based SQLi vectors, including SQLi signatures found in the URL  
  
Use the following expression to deploy the signature:
    
    
      evaluatePreconfiguredWaf('json-sqli-canary', {'sensitivity':0, 'opt_in_rule_ids': ['owasp-crs-id942550-sqli']})
      

We recommend that you also enable `sqli-v33-stable` at sensitivity level 2 to fully address JSON-based SQL injection bypasses.

## Limitations

Cloud Armor preconfigured WAF rules have the following limitations:

  * WAF rule changes typically take several minutes to propagate.
  * Among the HTTP request types with a request body, Cloud Armor processes only requests with a body. Cloud Armor evaluates preconfigured rules against the first 64 kB of request body content. For more information, see [Request body inspection limitation](https://docs.cloud.google.com/armor/docs/security-policy-overview#request-body).
  * When JSON parsing is enabled, Cloud Armor can parse and apply preconfigured WAF rules to JSON-formatted content. For more information, see [Request body content parsing](https://docs.cloud.google.com/armor/docs/content-parsing).
  * If you [exclude request fields from inspection](https://docs.cloud.google.com/armor/docs/rule-tuning#exclude_request_fields_from_inspection) for a preconfigured WAF rule to reduce false positives, you can't use the `allow` action with that rule. Request fields that are explicitly excluded from inspection are automatically allowed.
  * Cloud Armor preconfigured WAF rules can only be used with backend services behind a load balancer. Therefore, load balancing quotas and limits apply to your deployment. For more information, see the load balancing [quotas](https://docs.cloud.google.com/load-balancing/docs/quotas).



## What's next

  * [Tune preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Configure custom rules language attributes](https://docs.cloud.google.com/armor/docs/rules-language-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
