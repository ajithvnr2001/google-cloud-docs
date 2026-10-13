---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication/
title: UserDefinedAuthentication v1.7.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:31.378353+00:00
---

# UserDefinedAuthentication v1.7.0 custom resource definition  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  UserDefinedAuthentication v1.7.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.7.0/userdefinedauthentication)



## Spec schema

UserDefinedAuthenticationSpec defines the selected state of UserDefinedAuthentication.
    
    
    dbclusterRef: string
    keytabSecretRef: string
    pgHbaEntries:
    - string
    pgIdentEntries:
    - string
    ldapConfiguration:
      cacheTTLSeconds: integer
      enableGroupMapping: boolean
      enableLdapOptReferrals: boolean
      ldapBaseDN: string
      ldapBindDN: string
      ldapBindPasswordSecretRef:
        name: string
      ldapURI: string
      ldapsCertificateSecretRef:
        name: string
    
    

FieldType  
Required or optional |  Description  
---|---  
`dbclusterRef`  
`object`  
 _Required_ |  DBClusterRef is a reference to the target DBCluster in the same namespace to which these authentication settings apply.   
`dbclusterRef.name`  
`string`  
 _Required_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`keytabSecretRef`  
`object`  
 _Required_ |  KeytabSecretRef is a reference to the Secret resource in the same namespace containing the Kerberos keytab file. The Secret must have a data field named 'krb5.keytab'.   
`keytabSecretRef.name`  
`string`  
 _Required_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`pgHbaEntries`  
`list (string)`  
_Required_ |  PgHbaEntries is a list of pg_hba.conf entries that will be applied to the target DBCluster for this authentication method. Each string in the list represents a separate line in the pg_hba.conf file.   
`pgIdentEntries`  
`list (string)`  
_Optional_ |  PgIdentEntries is an optional list of pg_ident.conf entries (user name maps) that will be applied to the target DBCluster. Each string in the list represents a separate line in the pg_ident.conf file.   
`ldapConfiguration`  
`object`  
 _Optional_ |  LDAPConfiguration holds the settings for group mapping. These settings configure the google_pg_auth extension to perform LDAP lookups for AD group synchronization after a successful GSSAPI login.   
`ldapConfiguration.allowUnmappedUsersLogin`  
`boolean`  
 _Optional_ |  AllowUnmappedUsersLogin determines whether to enable unmapped users to login. Defaults to false.   
`ldapConfiguration.cacheTTLSeconds`  
`integer`  
 _Optional_ |  CacheTTLSeconds is the time-to-live for the user-to-group mapping cache in seconds.   
`ldapConfiguration.enableGroupMapping`  
`boolean`  
 _Optional_ |  EnableGroupMapping is the switch to turn the AD group synchronization feature on or off.   
`ldapConfiguration.enableLdapOptReferrals`  
`boolean`  
 _Optional_ |  EnableLdapOptReferrals determines whether to enable the LDAP referrals option.   
`ldapConfiguration.ldapBaseDN`  
`string`  
 _Optional_ |  LDAPBaseDN is the Base Distinguished Name for LDAP searches. e.g., "DC=my-corp,DC=com"   
`ldapConfiguration.ldapBindDN`  
`string`  
 _Optional_ |  LDAPBindDN is the Distinguished Name to bind as for the LDAP search. This is the service account user that will perform the group lookups. e.g., "setupadmin@ad-controller.my-corp.com"   
`ldapConfiguration.ldapBindPasswordSecretRef`  
`object`  
 _Optional_ |  LDAPBindPasswordSecretRef is a reference to the Secret in the same namespace that contains the password for the LDAP bind user. The Secret must have a data field named 'password'.   
`ldapConfiguration.ldapBindPasswordSecretRef.name`  
`string`  
 _Optional_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`ldapConfiguration.ldapURI`  
`string`  
 _Optional_ |  LDAPURI is the URI for the LDAPS or LDAP server. e.g., "ldap://ad-controller.my-corp.com"   
`ldapConfiguration.ldapsCertificateSecretRef`  
`object`  
 _Optional_ |  LDAPSCertificateSecretRef is an optional reference to the Secret in the same namespace that contains the CA certificate for LDAPS. The Secret must have a data field named 'ldap.crt'.   
`ldapConfiguration.ldapsCertificateSecretRef.name`  
`string`  
 _Optional_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
  
## Status schema

UserDefinedAuthenticationStatus defines the observed state of UserDefinedAuthentication.
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
    criticalIncidents:
    - code: string
      createTime: string
      message: string
      messageTemplateParams: object
      resource:
        component: string
        location:
          cluster: string
          group: string
          kind: string
          name: string
          namespace: string
          version: string
      stackTrace:
      - component: string
        message: string
      transientUntil: string
    message: string
    observedGeneration: integer
    reconciled: boolean
    state: string
    

FieldType  
Required or optional |  Description  
---|---  
`conditions[]`  
`object`  
 _Optional_ |  Conditions represents the latest available observations of the entity's current state.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another, which occurs when the underlying condition changed. If the time when the underlying condition changed is unknown, use the time when the API field changed.   
`conditions[].message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This can be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For example, if .metadata.generation is 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types can define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value must be a CamelCase string. This field might not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available. Because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression that it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`criticalIncidents[]`  
`object`  
 _Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are `DBSE+numeric` strings, like `DBSE1012`.   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident, as well as information about the Kubernetes resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location.   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  The name of the cluster of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  The Group name of the Kubernetes resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  The Kind of the Kubernetes resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  The name of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  The namespace of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  The Version of the Kubernetes resource.   
`criticalIncidents[].stackTrace[]`  
`object`  
 _Optional_ |  An unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace[].component`  
`string`  
 _Optional_ |  The name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`message`  
`string`  
 _Optional_ |  Message provides a human-readable message detailing the current state or any errors.   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`state`  
`string`  
 _Optional_ |  State represents the current state of the UserDefinedAuthentication resource. The values are: `Processing`, `Ready`, `Failed`, and `Unknown`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
