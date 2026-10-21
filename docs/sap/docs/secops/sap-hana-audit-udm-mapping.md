---
url: https://docs.cloud.google.com/sap/docs/secops/sap-hana-audit-udm-mapping/
title: SAP HANA Audit UDM mapping \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:02.581963+00:00
---

# SAP HANA Audit UDM mapping  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/sap-hana-audit-udm-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP HANA Audit UDM mapping Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `SAP_HANA_AUDIT` parser captures security-relevant events within the SAP HANA database, such as system configuration changes, user authorization modifications, and access to sensitive data.

For information about Google SecOps for SAP, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Field mapping reference

The following tables describe the mapping between SAP HANA Audit log fields and Google SecOps UDM fields.

### Log format 1

Log field | UDM mapping | Logic  
---|---|---  
`column1[event_timestamp]` | `event.idm.read_only_udm.metadata.event_timestamp` | This is the primary timestamp indicating when the audited event actually occurred within the SAP HANA system.  
`column2[service_name]` | `event.idm.read_only_udm.target.application` | The event happens within a specific service component of the SAP HANA database. target.application denotes the application or service being interacted with.  
`column3[hostname_csv]` | `event.idm.read_only_udm.target.hostname` | This is the hostname of the system running the SAP HANA service, making it the target system.  
`column4[system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The SAP System ID (SID) is a key identifier for the target SAP instance.  
`column5[instance_number]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Similar to SID, the instance number is a specific identifier for the target SAP instance, best stored as a label.  
`column6[port_number]` | `event.idm.read_only_udm.target.port` | This is the TCP port number on the target hostname used by the service.  
`column7[database_name]` | `event.idm.read_only_udm.target.resource.name` | This field holds the name of the database being affected or accessed, which is a resource within the target system.  
`column8[client_ip_address]` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | The IP address of the entity initiating the request, which is the principal.  
`column9[client_name]` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | The hostname of the entity initiating the request.  
`column10[client_process_id]` | `event.idm.read_only_udm.principal.process.pid` | The process ID on the client system that initiated the action.  
`column11[client_port_number]` | `event.idm.read_only_udm.principal.port` | The source port used by the client.  
`column12[policy_name]` | `event.idm.read_only_udm.security_result.rule_name` | This field names the specific audit policy in SAP that triggered the log.  
`column13[audit_level]` | `event.idm.read_only_udm.security_result.severity` | This indicates the severity of the audited event, which maps to UDM's severity levels.  
`column14[audit_action]` | `event.idm.read_only_udm.metadata.product_event_type` | This captures the vendor-specific action being audited (e.g., CREATE TABLE).  
`column15[session_user]` | `event.idm.read_only_udm.principal.user.userid` | The database user account used to establish the connection.  
`column16[target_schema]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The schema within the database where the action is taking place.  
`column17[target_object]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The name of the specific database object.  
`column22[action_status]` | `event.idm.read_only_udm.security_result.action_details`, `event.idm.read_only_udm.security_result.action` | `event.idm.read_only_udm.security_result.action` is set to "ALLOW" if value is "SUCCESSFUL".  
`column29[executed_statement]` | `event.idm.read_only_udm.additional.fields` | To store the raw SQL query because no standard UDM field exists for this purpose.  
`column30[session_id]` | `event.idm.read_only_udm.network.session_id` | The unique identifier for the database session.  
`column31[application_user_name]` | `event.idm.read_only_udm.principal.user.user_display_name` | Represents the OS user on the client side, potentially different from the DB user.  
`column36[xs_application_user_name]` | `event.idm.read_only_udm.additional.fields` | "XS Application User Name" refers to the user identity specifically within the context of an application running.  
`column37[application_name]` | `event.idm.read_only_udm.principal.application` | The name of the client application making the database request.  
`column38[statement_user_name]` | `event.idm.read_only_udm.additional.fields` | The database user context under which the SQL statement was actually executed.  
`_time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Represents when the log was ingested by the collection system.  
`source` | `event.idm.read_only_udm.observer.file.full_path` | The full path to the log file on the system reporting the log (the observer).  
`host` | `event.idm.read_only_udm.observer.hostname` | The hostname of the machine where the log collection agent resides.  
`clz_dir` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`clz_subdir` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`clzfilename` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`2024-06-17T23:21:22.488929+00:00 (time)` | `event.idm.read_only_udm.metadata.event_timestamp` | Header timestamp which is same as the timestamp in csv message.  
`sanitized53v029 (syslog_host)` | `event.idm.read_only_udm.intermediary.hostname` | This is the host where the SAP HANA process runs, acting as the intermediary system processing the request.  
`HDB_SYSTEMDB (process_name)` | `event.idm.read_only_udm.intermediary.application` | This identifies the database process name acting as the intermediary application or service.  
`25913 (pid)` | `event.idm.read_only_udm.intermediary.process.pid` | The PID of the intermediary database process.  
  
### Log format 2

Log field | UDM mapping | Logic  
---|---|---  
`column1 [event_timestamp]` | `event.idm.read_only_udm.metadata.event_timestamp` | This is the primary timestamp indicating when the audited event actually occurred within the SAP HANA system.  
`column2 [service_name]` | `event.idm.read_only_udm.target.application` | The event happens within a specific service component of the SAP HANA database. target.application denotes the application or service being interacted with.  
`column3 [hostname_csv]` | `event.idm.read_only_udm.target.hostname` | This is the hostname of the system running the SAP HANA service, making it the target system.  
`column4 [system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The SAP System ID (SID) is a key identifier for the target SAP instance.  
`column5 [instance_number]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Similar to SID, the instance number is a specific identifier for the target SAP instance, best stored as a label.  
`column6 [port_number]` | `event.idm.read_only_udm.target.port` | This is the TCP port number on the target hostname used by the service.  
`column7 [client_ip_address]` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | The IP address of the entity initiating the request, which is the principal.  
`column8 [client_name]` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | The hostname of the entity initiating the request.  
`column9 [client_process_id]` | `event.idm.read_only_udm.principal.process.pid` | The process ID on the client system that initiated the action.  
`column10 [client_port_number]` | `event.idm.read_only_udm.principal.port` | The source port used by the client.  
`column11 [policy_name]` | `event.idm.read_only_udm.security_result.rule_name` | This field names the specific audit policy in SAP that triggered the log.  
`column12 [audit_level]` | `event.idm.read_only_udm.security_result.severity` | This indicates the severity of the audited event, which maps to UDM's severity levels.  
`column13 [audit_action]` | `event.idm.read_only_udm.metadata.product_event_type` | This captures the vendor-specific action being audited (e.g., CREATE TABLE).  
`column14 [session_user]` | `event.idm.read_only_udm.principal.user.userid` | The database user account used to establish the connection.  
`column20 [target_user]` | `event.idm.read_only_udm.target.user.userid` | Name of the target user of the action.  
`column21 [action_status]` | `event.idm.read_only_udm.security_result.action_details`, `event.idm.read_only_udm.security_result.action` | `event.idm.read_only_udm.security_result.action` is set to "ALLOW" if value is "SUCCESSFUL".  
`column27 [executed_statement]` | `event.idm.read_only_udm.additional.fields` | To store the raw SQL query because no standard UDM field exists for this purpose.  
`column28 [session_id]` | `event.idm.read_only_udm.network.session_id` | The unique identifier for the database session.  
  
### Log format 3

Log field | UDM mapping | Logic  
---|---|---  
`column1 [event_timestamp]` | `event.idm.read_only_udm.metadata.event_timestamp` | This is the primary timestamp indicating when the audited event actually occurred within the SAP HANA system.  
`column2 [service_name]` | `event.idm.read_only_udm.target.application` | The event happens within a specific service component of the SAP HANA database. target.application denotes the application or service being interacted with.  
`column3 [hostname_csv]` | `event.idm.read_only_udm.target.hostname` | This is the hostname of the system running the SAP HANA service, making it the target system.  
`column4 [system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The SAP System ID (SID) is a key identifier for the target SAP instance.  
`column5 [instance_number]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Similar to SID, the instance number is a specific identifier for the target SAP instance, best stored as a label.  
`column6 [port_number]` | `event.idm.read_only_udm.target.port` | This is the TCP port number on the target hostname used by the service.  
`column7 [database_name]` | `event.idm.read_only_udm.target.resource.name` | This field holds the name of the database being affected or accessed, which is a resource within the target system.  
`column8 [client_ip_address]` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | The IP address of the entity initiating the request, which is the principal.  
`column9 [client_name]` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | The hostname of the entity initiating the request.  
`column10 [client_process_id]` | `event.idm.read_only_udm.principal.process.pid` | The process ID on the client system that initiated the action.  
`column11 [client_port_number]` | `event.idm.read_only_udm.principal.port` | The source port used by the client.  
`column12 [policy_name]` | `event.idm.read_only_udm.security_result.rule_name` | This field names the specific audit policy in SAP that triggered the log.  
`column13 [audit_level]` | `event.idm.read_only_udm.security_result.severity` | This indicates the severity of the audited event, which maps to UDM's severity levels.  
`column14 [audit_action]` | `event.idm.read_only_udm.metadata.product_event_type` | This captures the vendor-specific action being audited (e.g., CREATE TABLE).  
`column15 [session_user]` | `event.idm.read_only_udm.principal.user.userid` | The database user account used to establish the connection.  
`column16 [target_schema]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The schema within the database where the action is taking place.  
`column17 [target_object]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The name of the specific database object.  
`column22 [action_status]` | `event.idm.read_only_udm.security_result.action_details`, `event.idm.read_only_udm.security_result.action` | `event.idm.read_only_udm.security_result.action` is set to "ALLOW" if value is "SUCCESSFUL".  
`column29 [executed_statement1]` | `event.idm.read_only_udm.additional.fields` | To store the raw SQL query because no standard UDM field exists for this purpose.  
`column30 [executed_statement2]` | `event.idm.read_only_udm.additional.fields` | To store the raw SQL query because no standard UDM field exists for this purpose.  
`column32 [session_id]` | `event.idm.read_only_udm.network.session_id` | The unique identifier for the database session.  
`column33 [application_user_name]` | `event.idm.read_only_udm.principal.user.user_display_name` | Represents the OS user on the client side, potentially different from the DB user.  
`column38 [xs_application_user_name]` | `event.idm.read_only_udm.additional.fields` | "XS Application User Name" refers to the user identity specifically within the context of an application running.  
`column39 [application_name]` | `event.idm.read_only_udm.principal.application` | The name of the client application making the database request.  
`column40 [statement_user_name]` | `event.idm.read_only_udm.additional.fields` | The database user context under which the SQL statement was actually executed.  
`_time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Represents when the log was ingested by the collection system.  
`source` | `event.idm.read_only_udm.observer.file.full_path` | The full path to the log file on the system reporting the log (the observer).  
`host` | `event.idm.read_only_udm.observer.hostname` | The hostname of the machine where the log collection agent resides.  
`clz_dir` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`clz_subdir` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`clzfilename` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`2024-06-17T23:21:23.570507+00:00(time)` | `event.idm.read_only_udm.metadata.event_timestamp` | Header timestamp which is same as the timestamp in csv message.  
`sanitized53v029(syslog_host)` | `event.idm.read_only_udm.intermediary.hostname` | This is the host where the SAP HANA process runs, acting as the intermediary system processing the request.  
`HDB_TENANTDB (process_name)` | `event.idm.read_only_udm.intermediary.application` | This identifies the database process name acting as the intermediary application or service.  
`28699(pid)` | `event.idm.read_only_udm.intermediary.process.pid` | The PID of the intermediary database process.  
  
### Log format 4

Log field | UDM mapping | Logic  
---|---|---  
`appname` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "appname" present, hence mapping it to additional.  
`hostname` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "hostname" present, hence mapping it to additional.  
`message` | `event.idm.read_only_udm.metadata.description` | Extracted CSV fields from the message field.  
`priority` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "priority" present, hence mapping it to additional.  
`proc_id` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "proc_id" present, hence mapping it to additional.  
`facility` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "facility" present, hence mapping it to additional.  
`column1[event_timestamp]` | `event.idm.read_only_udm.metadata.event_timestamp` | This is the primary timestamp indicating when the audited event actually occurred within the SAP HANA system.  
`column2[service_name]` | `event.idm.read_only_udm.target.application` | The event happens within a specific service component of the SAP HANA database. target.application denotes the application or service being interacted with.  
`column3[hostname_csv]` | `event.idm.read_only_udm.target.hostname` | This is the hostname of the system running the SAP HANA service, making it the target system.  
`column4[system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The SAP System ID (SID) is a key identifier for the target SAP instance.  
`column5[instance_number]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Similar to SID, the instance number is a specific identifier for the target SAP instance, best stored as a label.  
`column6[port_number]` | `event.idm.read_only_udm.target.port` | This is the TCP port number on the target hostname used by the service.  
`column7[database_name]` | `event.idm.read_only_udm.target.resource.name` | This field holds the name of the database being affected or accessed, which is a resource within the target system.  
`column8[client_ip_address]` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | The IP address of the entity initiating the request, which is the principal.  
`column9[client_name]` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | The hostname of the entity initiating the request.  
`column10[client_process_id]` | `event.idm.read_only_udm.principal.process.pid` | The process ID on the client system that initiated the action.  
`column11[client_port_number]` | `event.idm.read_only_udm.principal.port` | The source port used by the client.  
`column12[policy_name]` | `event.idm.read_only_udm.security_result.rule_name` | This field names the specific audit policy in SAP that triggered the log.  
`column13[audit_level]` | `event.idm.read_only_udm.security_result.severity` | This indicates the severity of the audited event, which maps to UDM's severity levels.  
`column14[audit_action]` | `event.idm.read_only_udm.metadata.product_event_type` | This captures the vendor-specific action being audited (e.g., CREATE TABLE).  
`column15[session_user]` | `event.idm.read_only_udm.principal.user.userid` | The database user account used to establish the connection.  
`column21[target_user]` | `event.idm.read_only_udm.target.user.userid` | Name of the target user of the action.  
`column22[action_status]` | `event.idm.read_only_udm.security_result.action_details`, `event.idm.read_only_udm.security_result.action` | `event.idm.read_only_udm.security_result.action` is set to "ALLOW" if value is "SUCCESSFUL".  
`column30[session_id]` | `event.idm.read_only_udm.network.session_id` | The unique identifier for the database session.  
`column31[application_user_name]` | `event.idm.read_only_udm.principal.user.user_display_name` | Represents the OS user on the client side, potentially different from the DB user.  
`column36[xs_application_user_name]` | `event.idm.read_only_udm.additional.fields` | "XS Application User Name" refers to the user identity specifically within the context of an application running.  
`column37[application_name]` | `event.idm.read_only_udm.principal.application` | The name of the client application making the database request.  
`column38[statement_user_name]` | `event.idm.read_only_udm.additional.fields` | The database user context under which the SQL statement was actually executed.  
  
### Log format 5

Log field | UDM mapping | Logic  
---|---|---  
`appname` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "appname" present, hence mapping it to additional.  
`hostname` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "hostname" present, hence mapping it to additional.  
`message` | `event.idm.read_only_udm.metadata.description` | Mapped to description when the message does not contain CSV data.  
`priority` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "priority" present, hence mapping it to additional.  
`proc_id` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "proc_id" present, hence mapping it to additional.  
`facility` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "facility" present, hence mapping it to additional.  
  
### Log format 6

Log field | UDM mapping | Logic  
---|---|---  
`_time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Represents when the log was ingested by the collection system.  
`source` | `event.idm.read_only_udm.observer.file.full_path` | The full path to the log file on the system reporting the log (the observer).  
`host` | `event.idm.read_only_udm.observer.hostname` | The hostname of the machine where the log collection agent resides.  
`clz_dir` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`clz_subdir` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`clzfilename` | `event.idm.read_only_udm.observer.resource.attribute.labels` | Customer-specific context about the log's organization. Mapped as a label.  
`2026-03-05T14:55:29.728423+00:00` | `event.idm.read_only_udm.metadata.event_timestamp` | Header timestamp.  
`hec45v300257(principal_hostname)` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | The hostname of the system where the event described in _raw originated, which is running the ldapsearch command.  
`ldapsearch(principal_application)` | `event.idm.read_only_udm.principal.application` | The name of the application or process that generated the log message within the _raw string.  
`message repeated 2 times: [ DIGEST-MD5 common mech free] (desc)` | `event.idm.read_only_udm.metadata.description` | This is a free-text message content from the ldapsearch output in the _raw string.  
  
### Log format 7

Log field | UDM mapping | Logic  
---|---|---  
`appname` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "appname" present, hence mapping it to additional.  
`hostname` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "hostname" present, hence mapping it to additional.  
`priority` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "priority" present, hence mapping it to additional.  
`proc_id` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "proc_id" present, hence mapping it to additional.  
`facility` | `event.idm.read_only_udm.additional.fields` | This is the enrichment from BindPlane as discussed with the SAP team and there is no formal explanation for "facility" present, hence mapping it to additional.  
`column1[event_timestamp]` | `event.idm.read_only_udm.metadata.event_timestamp` | This is the primary timestamp indicating when the audited event actually occurred within the SAP HANA system.  
`column2[service_name]` | `event.idm.read_only_udm.target.application` | The event happens within a specific service component of the SAP HANA database. target.application denotes the application or service being interacted with.  
`column3[hostname_csv]` | `event.idm.read_only_udm.target.hostname` | This is the hostname of the system running the SAP HANA service, making it the target system.  
`column4[system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The SAP System ID (SID) is a key identifier for the target SAP instance.  
`column5[instance_number]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Similar to SID, the instance number is a specific identifier for the target SAP instance, best stored as a label.  
`column6[port_number]` | `event.idm.read_only_udm.target.port` | This is the TCP port number on the target hostname used by the service.  
`column7[database_name]` | `event.idm.read_only_udm.target.resource.name` | This field holds the name of the database being affected or accessed, which is a resource within the target system.  
`column8[client_ip_address]` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | The IP address of the entity initiating the request, which is the principal.  
`column9[client_name]` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | The hostname of the entity initiating the request.  
`column10[client_process_id]` | `event.idm.read_only_udm.principal.process.pid` | The process ID on the client system that initiated the action.  
`column11[client_port_number]` | `event.idm.read_only_udm.principal.port` | The source port used by the client.  
`column12[policy_name]` | `event.idm.read_only_udm.security_result.rule_name` | This field names the specific audit policy in SAP that triggered the log.  
`column13[audit_level]` | `event.idm.read_only_udm.security_result.severity` | This indicates the severity of the audited event, which maps to UDM's severity levels.  
`column14[audit_action]` | `event.idm.read_only_udm.metadata.product_event_type` | This captures the vendor-specific action being audited (e.g., CREATE TABLE).  
`column21[target_user]` | `event.idm.read_only_udm.target.user.userid` | Name of the target user of the action.  
`column22[action_status]` | `event.idm.read_only_udm.security_result.action_details`, `event.idm.read_only_udm.security_result.action` | `event.idm.read_only_udm.security_result.action` is set to "ALLOW" if value is "SUCCESSFUL".  
`column27[new_value]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The new value of the changed parameter and should be under labels.  
`column28[comment]` | `event.idm.read_only_udm.security_result.description` | Additional information about the event, especially failures.  
`column31[application_user_name]` | `event.idm.read_only_udm.principal.user.user_display_name` | Represents the OS user on the client side, potentially different from the DB user.  
`column37[application_name]` | `event.idm.read_only_udm.principal.application` | The name of the client application making the database request.  
`column38[statement_user_name]` | `event.idm.read_only_udm.additional.fields` | The database user context under which the SQL statement was actually executed.  
  
### Additional Fields mappings

Log field | UDM mapping | Logic  
---|---|---  
`column18[privilege_name]` | `event.idm.read_only_udm.security_result.detection_fields` | The "Privilege Name" field contains the name of the database privilege being acted upon (e.g., SELECT, INSERT, DELETE). In UDM, actions on specific permissions/rights are often detailed in the security_result.  
`column19[grantable]` | `event.idm.read_only_udm.security_result.detection_fields` | This field indicates if a privilege was granted with the ADMIN/GRANT option.  
`column20[role_name]` | `event.idm.read_only_udm.target.resource.attribute.roles` | Mapping this to the repeated field `target.resource.attribute.roles` correctly associates the role with the target database resource.  
`column23[component]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Name of the file being targeted.  
`column24[section]` | `event.idm.read_only_udm.target.resource.attribute.labels` | This specifies the section within a configuration file.  
`column25[parameter]` | `event.idm.read_only_udm.target.resource.attribute.labels` | Similar to "Section", this is the specific parameter name within a configuration section.  
`column26[old_value]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The old value of the changed parameter and should be under labels.  
`column32[role_schema_name]` | `event.idm.read_only_udm.additional.fields` | This is the schema to which the database role belongs. Since there isn't a dedicated UDM field to store this, `additional.fields` is the most suitable place to store this.  
`column33[grantee_schema_name]` | `event.idm.read_only_udm.target.resource.attribute.labels` | The schema to which the "Target Principal" belongs. This is best placed as a label.  
`column34[origin_database_name]` | `event.idm.read_only_udm.src.resource.name` | For cross-database queries, this identifies the source database. `src` noun is used for the origin of the data or connection.  
`column35[origin_user_name]` | `event.idm.read_only_udm.src.user.userid` | The user in the origin database initiating the cross-database query, mapping to `src.user.userid`.  
`column39[create_time]` | `event.idm.read_only_udm.additional.fields` | Specific to XSA events, this timestamp indicates the event time on the client side. Since it's XSA-specific and might differ from the main `event_timestamp`, `additional.fields` is appropriate.  
`column40[xsa_message_ip]` | `event.idm.read_only_udm.additional.fields` | The IP address related to the XSA event.  
`column41[xsa_tenant]` | `event.idm.read_only_udm.additional.fields` | XSA-specific tenant identifier, best stored as additional fields.  
`column42[xsa_uuid]` | `event.idm.read_only_udm.metadata.product_log_id` | A unique identifier for the XSA audit log message, fitting for `metadata.product_log_id`.  
`column43[xsa_channel]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column44[xsa_attachment_id]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column45[xsa_attachment_name]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column46[xsa_organization_id]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column47[xsa_space_id]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column48[xsa_instance_id]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column49[xsa_binding_id]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column50[xsa_object]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
`column51[xsa_data_subject]` | `event.idm.read_only_udm.additional.fields` | XSA specific fields might fit best in `additional.fields`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
