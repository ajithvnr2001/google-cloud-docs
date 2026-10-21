---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/stig/
title: AlloyDB Omni STIG compliance \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:27.037098+00:00
---

# AlloyDB Omni STIG compliance  |  AlloyDB Omni using the container orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/stig/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/resources)



Send feedback 

#  AlloyDB Omni STIG compliance Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/stig)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/stig)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/stig)

The Security Technical Implementation Guide (STIG) compliance matrix for AlloyDB Omni outlines implementation details for security-relevant controls at the database and system level. For more information, see the [PostgreSQL 9.x on Red Hat Enterprise Linux Security Technical Implementation Guide (STIG) compliance checklist](https://ncp.nist.gov/checklist/802). 

All controls that are managed by Google are fully implemented and verified continuously. To maintain compliance, the customer must configure and manage controls requiring customer action. For more information, see [STIG shared responsibility](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/shared-responsibility#stig-shared-responsibility).

## STIG compliance matrix

The following table provides STIG IDs, descriptions, enforcement statuses by operator, customer responsibility requirements, and severity:

STIG ID | Security control description | Enforced by default | Customer responsibility | Severity  
---|---|---|---|---  
V-214151 | Access to database files must be limited to relevant processes and to authorized, administrative users. | Yes | No | Medium  
V-214127 | Access to external executables must be disabled or restricted. | Yes | No | Medium  
V-214154 | Audit records must be generated when categorized information—for example, classification levels and security levels—is deleted. | Yes | No | Medium  
V-214150 | Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data transfer policy. | No | No | Medium  
V-214074 | Database objects—including but not limited to tables, indexes, storage, trigger procedures, functions, and links to software external to PostgreSQL—must be owned by database and DBMS principals authorized for ownership. | Yes | No | Medium  
V-214076 | Database software, including PostgreSQL configuration files, must be stored in dedicated directories separate from the host OS and other applications. | No | No | Medium  
V-214078 | Execution of software modules—to include functions and trigger procedures—with elevated privileges must be restricted to necessary cases only. | No | No | Medium  
V-214130 | If passwords are used for authentication, PostgreSQL must store only hashed, salted representations of passwords. | Yes | No | High  
V-214056 | If passwords are used for authentication, PostgreSQL must transmit only encrypted representations of passwords. | Yes | No | High  
V-214064 | PostgreSQL and associated applications must reserve the use of dynamic code execution for situations that require it. | No | No | Medium  
V-214065 | PostgreSQL and associated applications, when making use of dynamic code execution, must scan input data for invalid values that might indicate a code injection attack. | No | No | Medium  
V-214066 | PostgreSQL must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements. | No | Yes | Medium  
V-214071 | PostgreSQL must let only the Information System Security Manager (ISSM)—or individuals or roles appointed by the ISSM—select which auditable events are to be audited. | No | Yes | Medium  
V-214129 | PostgreSQL must associate organization-defined types of security labels having organization-defined security label values with information in process. | No | Yes | Medium  
V-214062 | PostgreSQL must associate organization-defined types of security labels having organization-defined security label values with information in storage. | No | Yes | Medium  
V-214058 | PostgreSQL must associate organization-defined types of security labels having organization-defined security label values with information in transmission. | No | Yes | Medium  
V-214147 | PostgreSQL must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect. | Yes | No | Medium  
V-214096 | PostgreSQL must be able to generate audit records when privileges and permissions are retrieved. | Yes | No | Medium  
V-214101 | PostgreSQL must be able to generate audit records when security objects are accessed. | Yes | No | Medium  
V-214048 | PostgreSQL must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and vulnerability assessments. | Yes | No | Medium  
V-214063 | PostgreSQL must check the validity of all data inputs except those specifically identified by the organization. | No | No | Medium  
V-214131 | PostgreSQL must enforce access restrictions associated with changes to the configuration of PostgreSQL or database. | Yes | No | Medium  
V-214057 | PostgreSQL must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. | No | No | High  
V-214136 | PostgreSQL must enforce authorized access to all PKI private keys stored and used by PostgreSQL. | Yes | No | High  
V-214067 | PostgreSQL must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects. | Yes | No | Medium  
V-214156 | PostgreSQL must generate audit records for all direct access to the database. | Yes | No | Medium  
V-214099 | PostgreSQL must generate audit records for all privileged activities or other system-level access. | Yes | No | Medium  
V-214088 | PostgreSQL must generate audit records that show the starting and ending time for user access to the database. | Yes | No | Medium  
V-214085 | PostgreSQL must generate audit records when categorized information—for example, classification levels and security levels—is accessed. | Yes | No | Medium  
V-214108 | PostgreSQL must generate audit records when categorized information—for example, classification levels and security levels—is modified. | No | Yes | Medium  
V-214103 | PostgreSQL must generate audit records when concurrent sign-ins and connections by the same user from different workstations occur. | Yes | No | Medium  
V-214090 | PostgreSQL must generate audit records when privileges and permissions are added. | Yes | No | Medium  
V-214102 | PostgreSQL must generate audit records when privileges and permissions are deleted. | Yes | No | Medium  
V-214105 | PostgreSQL must generate audit records when privileges and permissions are modified. | Yes | No | Medium  
V-214093 | PostgreSQL must generate audit records when security objects are deleted. | Yes | No | Medium  
V-214107 | PostgreSQL must generate audit records when security objects are modified. | Yes | No | Medium  
V-214155 | PostgreSQL must generate audit records when successful accesses to objects occur. | Yes | No | Medium  
V-214092 | PostgreSQL must generate audit records when successful signins or connections occur. | Yes | No | Medium  
V-214098 | PostgreSQL must generate audit records when unsuccessful accesses to objects occur. | Yes | No | Medium  
V-214100 | PostgreSQL must generate audit records when unsuccessful attempts to access categorized information—for example, classification levels and security levels—occur. | Yes | No | Medium  
V-214086 | PostgreSQL must generate audit records when unsuccessful attempts to access security objects occur. | Yes | No | Medium  
V-214110 | PostgreSQL must generate audit records when unsuccessful attempts to add privileges and permissions occur. | Yes | No | Medium  
V-214091 | PostgreSQL must generate audit records when unsuccessful attempts to delete categorized information—for example, classification levels/security levels—occur. | Yes | No | Medium  
V-214095 | PostgreSQL must generate audit records when unsuccessful attempts to delete privileges and permissions occur. | Yes | No | Medium  
V-214104 | PostgreSQL must generate audit records when unsuccessful attempts to delete security objects occur. | Yes | No | Medium  
V-214106 | PostgreSQL must generate audit records when unsuccessful attempts to execute privileged activities or other system-level access occur. | Yes | No | Medium  
V-214097 | PostgreSQL must generate audit records when unsuccessful attempts to modify categorized information—for example, classification levels/security levels—occur. | Yes | No | Medium  
V-214109 | PostgreSQL must generate audit records when unsuccessful attempts to modify privileges and permissions occur. | Yes | No | Medium  
V-214089 | PostgreSQL must generate audit records when unsuccessful attempts to modify security objects occur. | Yes | No | Medium  
V-214094 | PostgreSQL must generate audit records when unsuccessful attempts to retrieve privileges and permissions occur. | Yes | No | Medium  
V-214087 | PostgreSQL must generate audit records when unsuccessful sign-ins or connection attempts occur. | Yes | No | Medium  
V-214115 | PostgreSQL must generate time stamps for audit records and application data with a minimum granularity of one second. | Yes | No | Medium  
V-214139 | PostgreSQL must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components. | Yes | No | Medium  
V-214124 | PostgreSQL must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest—to include, at a minimum, PII and classified information—on organization-defined information system components. | Yes | No | Medium  
V-214117 | PostgreSQL must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to generate and validate cryptographic hashes. | No | No | High  
V-214119 | PostgreSQL must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to protect unclassified information requiring confidentiality and cryptographic protection, in accordance with the data owners' requirements. | No | No | High  
V-214077 | PostgreSQL must include additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject. | No | Yes | Medium  
V-214123 | PostgreSQL must initiate session auditing upon startup. | Yes | No | Medium  
V-214052 | PostgreSQL must integrate with an organization-level authentication and access mechanism providing account management and automation for all users, groups, roles, and any other principals. | No | No | High  
V-214140 | PostgreSQL must invalidate session identifiers upon user sign-out or other session termination. | Yes | No | Medium  
V-214081 | PostgreSQL must isolate security functions from non-security functions. | Yes | No | Medium  
V-214055 | PostgreSQL must limit privileges to change functions and triggers, and links to software external to PostgreSQL. | Yes | No | Medium  
V-214059 | PostgreSQL must limit the number of concurrent sessions to an organization-defined number per user for all accounts and account types. | No | No | Medium  
V-214145 | PostgreSQL must maintain the authenticity of communications sessions by guarding against on-path attacks that guess at Session ID values. | Yes | No | Medium  
V-214113 | PostgreSQL must maintain the confidentiality and integrity of information during preparation for transmission. | Yes | No | Medium  
V-214073 | PostgreSQL must maintain the confidentiality and integrity of information during reception. | Yes | No | Medium  
V-214149 | PostgreSQL must map the PKI-authenticated identity to an associated user account. | No | No | Medium  
V-214144 | PostgreSQL must off-load audit data to a separate log management facility. This must be continuous and in near real time for systems with a network connection to the storage facility. The offload must occur weekly or more often for stand-alone systems. | No | Yes | Medium  
V-214137 | PostgreSQL must only accept end entity certificates issued by PKI or approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions. | No | No | Medium  
V-214148 | PostgreSQL must prevent non-privileged users from executing privileged functions, which includes disabling, circumventing, or altering implemented security safeguards and countermeasures. | Yes | No | High  
V-214116 | PostgreSQL must produce audit records containing sufficient information to establish the identity of any user, subject, or process associated with the event. | Yes | No | Medium  
V-214049 | PostgreSQL must produce audit records containing sufficient information to establish the outcome (success or failure) of the events. | Yes | No | Medium  
V-214125 | PostgreSQL must produce audit records containing sufficient information to establish the sources or origins of the events. | Yes | No | Medium  
V-214138 | PostgreSQL must produce audit records containing sufficient information to establish what type of events occurred. | Yes | No | Medium  
V-214112 | PostgreSQL must produce audit records containing sufficient information to establish where the events occurred. | Yes | No | Medium  
V-214142 | PostgreSQL must produce audit records containing time stamps to establish when the events occurred. | Yes | No | Medium  
V-214082 | PostgreSQL must produce audit records of its enforcement of access restrictions associated with changes to the configuration of PostgreSQL or databases. | Yes | No | Medium  
V-214121 | PostgreSQL must prohibit user installation of logic modules— for example, functions, trigger procedures, and views— without explicit privileged status. | Yes | No | Medium  
V-214132 | PostgreSQL must protect against a user falsely repudiating having performed organization-defined actions. | Yes | No | Medium  
V-214152 | PostgreSQL must protect its audit configuration from unauthorized modification. | Yes | No | Medium  
V-214141 | PostgreSQL must protect its audit features from unauthorized access. | Yes | No | Medium  
V-214143 | PostgreSQL must protect its audit features from unauthorized removal. | Yes | No | Medium  
V-214120 | PostgreSQL must protect the confidentiality and integrity of all information at rest. | Yes | No | High  
V-214072 | PostgreSQL must provide an immediate real-time alert to appropriate support staff of all audit log failures. | No | Yes | Medium  
V-214114 | PostgreSQL must provide audit record generation capability for organization-defined auditable events in all DBMS and database components. | No | No | Medium  
V-214053 | PostgreSQL must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that might be exploited by adversaries. | Yes | No | Medium  
V-214069 | PostgreSQL must record time stamps, in audit records and application data, that can be mapped to Coordinated Universal Time (UTC, formerly GMT). | Yes | No | Medium  
V-214135 | PostgreSQL must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. | Yes | No | Medium  
V-214070 | PostgreSQL must reveal detailed error messages only to the ISSO, ISSM, SA and DBA. | Yes | No | Medium  
V-214122 | PostgreSQL must separate user functionality—including user interface services—from database management functionality. | Yes | No | Medium  
V-214061 | PostgreSQL must uniquely identify and authenticate non-organizational users or processes acting on behalf of non-organizational users. | Yes | No | Medium  
V-214146 | PostgreSQL must uniquely identify and authenticate organizational users or processes acting on behalf of organizational users. | Yes | No | Medium  
V-214153 | PostgreSQL must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations. | No | No | High  
V-220321 | PostgreSQL must use NSA-approved cryptography to protect classified information in accordance with the data owners' requirements. | No | No | Medium  
V-214080 | PostgreSQL must use centralized management of the content captured in audit records generated by all components of PostgreSQL. | No | No | Medium  
V-214111 | PostgreSQL, when using PKI-based authentication, must validate certificates by performing RFC 5280-compliant certification path validation. | No | No | Medium  
V-214054 | Privileges to change PostgreSQL software modules must be limited. | Yes | No | Medium  
V-214050 | Security-relevant software updates to PostgreSQL must be installed in the time period directed by an authoritative source—for example, IAVM, CTOs, DTMs, and STIGs. | Yes | No | High  
V-214068 | The audit information produced by PostgreSQL must be protected from unauthorized deletion. | Yes | No | Medium  
V-214051 | The audit information produced by PostgreSQL must be protected from unauthorized modification. | Yes | No | Medium  
V-214083 | The audit information produced by PostgreSQL must be protected from unauthorized read access. | Yes | No | Medium  
V-214157 | The DBMS must be configured on a platform that has a NIST certified FIPS 140-2 or 140-3 installation of OpenSSL. | No | No | High  
V-214075 | The PostgreSQL software installation account must be restricted to authorized users. | No | No | High  
V-214060 | The roles and groups used to modify database structure—including but not necessarily limited to tables, indexes, and storage—and logic modules—for example, functions, trigger procedures, and links to software external to PostgreSQL—must be restricted to authorized users. | Yes | No | Medium  
V-214133 | The system must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75% of maximum audit record storage capacity. | No | Yes | Medium  
V-214128 | Unused database components which are integrated in PostgreSQL and can't be uninstalled must be disabled. | No | No | Medium  
V-214126 | Unused database components, PostgreSQL software, and database objects must be removed. | Yes | No | Medium  
V-214079 | When invalid inputs are received, PostgreSQL must behave in a predictable and documented manner that reflects organizational and system objectives. | Yes | No | Medium  
V-214084 | When updates are applied to PostgreSQL software, any software components that have been replaced or made unnecessary must be removed. | No | No | Medium  
  
## What's next

  * Learn about [STIG shared responsibility](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/shared-responsibility#stig-shared-responsibility).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
