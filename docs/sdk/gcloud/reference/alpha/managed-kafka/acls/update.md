---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/acls/update/
title: gcloud alpha managed-kafka acls update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:31:35.982197+00:00
---

# gcloud alpha managed-kafka acls update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka/acls/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha managed-kafka acls update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha managed-kafka acls update - update a Managed Service for Apache Kafka acl 
SYNOPSIS
    

`gcloud alpha managed-kafka acls update` (`ACL` : `--cluster`=`CLUSTER` `--location`=`LOCATION`) `--etag`=`ETAG` (`--acl-entries-from-file`=`PATH_TO_FILE` | `--acl-entry`=[`host`=`HOST`],[`operation`=`OPERATION`],[`permission-type`=`PERMISSION-TYPE`],[`principal`=`PRINCIPAL`]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Managed Service for Apache Kafka acl. 

NOTE: update performs a FULL REPLACEMENT of acl entries. For incremental updates, use add-acl-entry and remove-acl-entry commands. 

EXAMPLES
     To update an acl for the Kafka cluster resource pattern, with etag W/XYZ123 returned from a previous create or describe command, in a cluster named mycluster located in us-central1, run the following: 
    
    
    gcloud alpha managed-kafka acls update cluster --cluster=mycluster --location=us-central1 --acl-entry=principal='User:admin@project.iam.gserviceaccount.com',operation=ALL,permission-type=ALLOW,host='*' --etag=W/XYZ123

POSITIONAL ARGUMENTS
    

Acl resource - Identifies the name of the acl that this command updates. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `acl` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ACL`
     ID of the acl or fully qualified identifier for the acl. 

To set the `acl` attribute: 

  * provide the argument `acl` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--cluster`=`CLUSTER`
     The cluster name. To set the `cluster` attribute: 

  * provide the argument `acl` on the command line with a fully specified name; 
  * provide the argument `--cluster` on the command line. 


`--location`=`LOCATION`
     ID of the location of the Managed Service for Apache Kafka resource. See <https://cloud.google.com/managed-service-for-apache-kafka/docs/locations> for a list of supported locations. To set the `location` attribute: 

  * provide the argument `acl` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--etag`=`ETAG`
     etag returned in the response to a previous create or describe command. The etag is used for concurrency control, to ensure that the client and server agree on the current set of acl entries in the Kafka cluster, before full replacement in the update command. 
Exactly one of these must be specified: 

`--acl-entries-from-file`=`PATH_TO_FILE`
     Path to a JSON or YAML file containing the acl entries to use in the acl. Use a full or relative path to a local file containing the value of acl_entries. 
`--acl-entry`=[`host`=`HOST`],[`operation`=`OPERATION`],[`permission-type`=`PERMISSION-TYPE`],[`principal`=`PRINCIPAL`]
     An acl entry that configures access for a principal, for a specific operation on the acl's resource pattern. This flag can be repeated. 

``PRINCIPAL`` is the principal. Specified as Google Cloud account, with the Kafka StandardAuthorizer prefix "User:". For example: "User:admin@project.iam.gserviceaccount.com". Can be the wildcard "User:`*`" to refer to all users. 

``OPERATION`` is the operation type. Allowed values are: ALL, READ, WRITE, CREATE, DELETE, ALTER, DESCRIBE, CLUSTER_ACTION, DESCRIBE_CONFIGS, ALTER_CONFIGS, IDEMPOTENT_WRITE. 

``PERMISSION-TYPE`` is the permission type. Allowed values are: ALLOW, DENY. 

``HOST`` is the host. Must be set to "`*`" for Managed Service for Apache Kafka. 

Example acl-entry: "principal=User:admin@project.iam.gserviceaccount.com,operation=ALL,permission-type=ALLOW,host=`*`" 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedkafka/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-service-for-apache-kafka/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud managed-kafka acls update](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update)
    
    
    [gcloud beta managed-kafka acls update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka/acls/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
