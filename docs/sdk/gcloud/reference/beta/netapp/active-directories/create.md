---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/active-directories/create/
title: gcloud beta netapp active-directories create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:47.542020+00:00
---

# gcloud beta netapp active-directories create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/active-directories/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp active-directories create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp active-directories create - create a Cloud NetApp Active Directory 
SYNOPSIS
    

`gcloud beta netapp active-directories create` (`ACTIVE_DIRECTORY` : `--location`=`LOCATION`) `--dns`=`DNS` `--domain`=`DOMAIN` `--net-bios-prefix`=`NET_BIOS_PREFIX` `--password`=`PASSWORD` `--username`=`USERNAME` [`--administrators`=[`ADMINISTRATOR`,…]] [`--async`] [`--backup-operators`=[`BACKUP_OPERATOR`,…]] [`--description`=`DESCRIPTION`] [`--enable-aes`=`ENABLE_AES`] [`--enable-ldap-signing`=`ENABLE_LDAP_SIGNING`] [`--encrypt-dc-connections`=`ENCRYPT_DC_CONNECTIONS`] [`--kdc-hostname`=`KDC_HOSTNAME`] [`--kdc-ip`=`KDC_IP`] [`--labels`=[`KEY`=`VALUE`,…]] [`--nfs-users-with-ldap`=`NFS_USERS_WITH_LDAP`] [`--organizational-unit`=`ORGANIZATIONAL_UNIT`] [`--security-operators`=[`SECURITY_OPERATOR`,…]] [`--site`=`SITE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates an AD (Active Directory) config for Cloud NetApp Volumes. 
EXAMPLES
     The following command creates an AD named AD_NAME with the required arguments: 
    
    
    gcloud beta netapp active-directories create AD_NAME --location=us-central1 --domain=example-domain.com --dns=0.0.0.0 --net-bios-prefix=prefix-1 --enable-aes=true --username=user1 --password="secure1" --backup-operators=backup_op1,backup_op2 --security-operators=sec_op1,sec_op2 --enable-ldap-signing=false

POSITIONAL ARGUMENTS
    

Active directory resource - The Active Directory to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `active_directory` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ACTIVE_DIRECTORY`
     ID of the active_directory or fully qualified identifier for the active_directory. 

To set the `active_directory` attribute: 

  * provide the argument `active_directory` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the active_directory. 

To set the `location` attribute: 

  * provide the argument `active_directory` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--dns`=`DNS`
     A comma separated list of DNS server IP addresses for the Active Directory domain. 
`--domain`=`DOMAIN`
     The Active Directory domain. 
`--net-bios-prefix`=`NET_BIOS_PREFIX`
     NetBIOS prefix name of the server. 
`--password`=`PASSWORD`
     Password of the Active Directory domain administrator. 
`--username`=`USERNAME`
     Username of the Active Directory domain administrator. 
OPTIONAL FLAGS
    

`--administrators`=[`ADMINISTRATOR`,…]
     Members of the Active Directory built-in Administrators group. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--backup-operators`=[`BACKUP_OPERATOR`,…]
     Users to be added to the Built-in Backup Operator Active Directory group. 
`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Active Directory 
`--enable-aes`=`ENABLE_AES`
     The Boolean value indiciating whether AES encryption will be enabled for SMB communication. 
`--enable-ldap-signing`=`ENABLE_LDAP_SIGNING`
     Boolean flag that specifies whether or not LDAP traffic needs to be signed. 
`--encrypt-dc-connections`=`ENCRYPT_DC_CONNECTIONS`
     Boolean flag that specifies whether traffic between SMB server to Domain Controller (DC) will be encrypted. 
`--kdc-hostname`=`KDC_HOSTNAME`
     Name of the Active Directory machine. 
`--kdc-ip`=`KDC_IP`
     KDC server IP address for the Active Directory machine. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--nfs-users-with-ldap`=`NFS_USERS_WITH_LDAP`
     Boolean flag that allows access to local users and LDAP users. If access is needed only for LDAP users, it has to be disabled. 
`--organizational-unit`=`ORGANIZATIONAL_UNIT`
     The Organizational Unit (OU) within the Windows Active Directory the user belongs to. 
`--security-operators`=[`SECURITY_OPERATOR`,…]
     Domain users to be given the Security privilege. 
`--site`=`SITE`
     The Active Directory site the service will limit Domain Controller discovery to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud netapp active-directories create](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/active-directories/create)
    
    
    [gcloud alpha netapp active-directories create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/active-directories/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
