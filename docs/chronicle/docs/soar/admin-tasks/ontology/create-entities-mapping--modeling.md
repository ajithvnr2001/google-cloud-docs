---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling/
title: Map and model entities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:09:04.445743+00:00
---

# Map and model entities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/create-entities-mapping--modeling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map and model entities

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Entities are objects that represent points of interest extracted from alerts, such as Indicators of Compromise (IoCs) and artifacts. They help security analysts by: 

  * Automatically tracking history.
  * Grouping alerts without human intervention.
  * Hunting for malicious activity based on relationships between entities.
  * Making cases easier to read and enabling seamless playbook creation.



Google Security Operations uses an automated system (ontology) to extract the main objects of interest from the raw alerts to create entities. Each entity is represented by an object that can track its own history for future reference. 

## Configure the entity ontology

To configure the ontology, you'll need to map and model your data. This involves selecting a visual representation for alerts and defining which entities should be extracted. Google SecOps provides pre-configured ontology rules for most popular SIEM products. 

The best time to customize the ontology is after you have a connector pulling data into Google SecOps. The process involves two main steps: 

  1. **Modeling** : Choose the visual representation (model/visual family) for your data.
  2. **Mapping** : Map the fields to support the selected model and extract entities.



##  Supported entities

The following entities are supported:

Entity type | Description | Expected format | Examples  
---|---|---|---  
Address | An IPV4 address. | Depends on the specific type of address being stored. | IP addresses, for example, `192.168.1.1`  
Application | A software application. | Text string. | `nmap`, `Microsoft Word`.  
Cluster | A group of computing resources. | Text string. | Kubernetes cluster name, Cluster name, or Cluster ID.  
Container | A container instance. | Text string. | Docker container ID or name.  
Credit card | A credit card number. | Masked or tokenized string. | Data should be masked or tokenized to avoid storing sensitive PCI data.  
CVE | Common Vulnerabilities and Exposures identifier. | `CVE-YYYY-NNNNN` | `CVE-2023-12345`  
Database | A database instance or system. | Text string. | Database name or connection identifier.  
Deployment | A software deployment. | Text string. | Deployment identifier.  
Destination URL | A Uniform Resource Locator. | Standard URL string. | `https://example.com/path`  
Domain | A network domain name. | Standard domain string. | `example.com`  
Email subject | The subject line of an email message. | Text string. | Subject line of an email.  
File hash | A cryptographic hash of a file. | Hexadecimal string. | MD5, SHA-1, or SHA256 hash.  
Filename | The name of a file. | Text string. | `malware.exe`  
Generic entity | A flexible entity type for data not fitting other categories. | Depends on the data being stored. | N/A  
Hostname | A label assigned to a device on a network. | Standard hostname string. | `workstation-01`, `server.example.com`  
IP set | A collection or group of IP addresses. | Not explicitly defined (for example, comma-separated string, JSON array, reference to a list). | Ranges, CIDR notations, or lists.  
For example, see [Create a Trusted IP list](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/amazon-guard-duty#create_a_trusted_ip_list).  
MAC address | A Media Access Control address. | Six groups of two hexadecimal digits, separated by hyphens or colons. | `00-1B-44-11-3A-B7`, `00:1B:44:11:3A:B7`  
Phone number | A telephone number. | Varies (E.164 is standard). | `+18005550100`  
POD | A group of one or more containers in Kubernetes, often with shared storage/network. | Name string. | Kubernetes POD name.  
Process | An instance of a computer program being executed. | Process ID (PID) or name. | `1234`, `chrome.exe`  
Service | A software service running on a system. | Service name string. | `sshd`, `apache2`  
Threat actor | An individual or group posing a threat. | Name or code string. | `APT28`, `FIN7`  
Threat campaign | A series of related threat activities. | Campaign name or code string. | Campaign name or code.  
Threat signature | A pattern or indicator of a known threat. | Rule ID or signature name. | Short rule ID, YARA-l rule name.  
USB | A Universal Serial Bus device. | Device name, serial number, or other attributes. | USB device identifier.  
User name | An identifier for a user account. | Simple usernames or email addresses. | `jdoe`, `jdoe@example.com`  
  
## Use case: Map and model new data of ingested email 

This use case shows how to map and model new data of an ingested email: 

  1. Go to **Content Hub > Use Cases**.
  2. Run the **Zero to Hero** test case. For details on how to do this, see [Run use cases](https://docs.cloud.google.com/chronicle/docs/soar/marketplace/run-use-cases). 
  3. In the **Cases** tab, select the **Mail** case from the **Cases Queue** and select the **Events** tab. 
  4. Next to the alert, click  settings  **Event Configuration** to open the **Event Configuration** page. 
  5. In the hierarchy list, click **Mail**. This ensures that your configuration will automatically work for every piece of data coming from this product (Email box).  

  6. Assign the visual family that best represents the data. In this use case, because `MailRelayOrTAP` has previously been selected, you can skip this step. 
  7. Switch to **Mapping** and map the following entity fields. Double-click each entity and select the raw data field for that entity in the extracted field. You can provide alternative fields from which to extract the information:
     * `SourceUserName`
     * `DestinationUserName`
     * `DestinationURL`
     * `EmailSubject`
  8. Click **Raw Event Properties** to view the original email fields. 



## Extract regular expressions

Google SecOps doesn't support regular expression groups. To extract text from the event field using regular expression patterns, use `lookahead` and `lookbehind` in the extraction function logic.

In the following example, the event field displays a large chunk of text:  
`Suspicious activity on A16_WWJ - Potential Account Takeover (33120)`

To extract only the text `Suspicious activity on A16_WWJ`, do the following:

  1. Enter the following regular expression in the **Extraction function** value field:  
`Suspicious activity on A16_WWJ(?=.*)`
  2. In the **Transformation function** field, select **To_String**.



To extract only the text after `Suspicious activity on A16_WWJ`, do the following:

  1. Enter the following regular expression in the **Extraction function** value field:  
`(?<=Suspicious activity on A16_WWJ).*`
  2. In the **Transformation function** field, select **To_String**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
