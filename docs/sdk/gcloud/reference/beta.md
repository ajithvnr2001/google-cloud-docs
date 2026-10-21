---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/
title: gcloud beta \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:29.910619+00:00
---

# gcloud beta  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta - beta versions of gcloud commands 
SYNOPSIS
    

`gcloud beta` `GROUP` | `COMMAND` [`--account`=`ACCOUNT`] [`--billing-project`=`BILLING_PROJECT`] [`--configuration`=`CONFIGURATION`] [`--flags-file`=`YAML_FILE`] [`--flatten`=[`KEY`,…]] [`--format`=`FORMAT`] [`--help`] [`--project`=`PROJECT_ID`] [`--quiet`, `-q`] [`--verbosity`=`VERBOSITY`; default="warning"] [`--version`, `-v`] [`-h`] [`--access-token-file`=`ACCESS_TOKEN_FILE`] [`--impersonate-service-account`=`SERVICE_ACCOUNT_EMAILS`] [`--log-http`] [`--trace-token`=`TRACE_TOKEN`] [`--no-user-output-enabled`]
DESCRIPTION
     `(BETA)` Beta versions of gcloud commands. 
GLOBAL FLAGS
    

`--account`=`ACCOUNT`
     Google Cloud user account to use for invocation. Overrides the default `core/account` property value for this command invocation. 
`--billing-project`=`BILLING_PROJECT`
     The Google Cloud project that will be charged quota for operations performed in `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)`. If you need to operate on one project, but need quota against a different project, you can use this flag to specify the billing project. If both `billing/quota_project` and `--billing-project` are specified, `--billing-project` takes precedence. Run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) --help` to see more information about `billing/quota_project`. 
`--configuration`=`CONFIGURATION`
     File name of the configuration to use for this command invocation. For more information on how to use configurations, run: `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)`. You can also use the CLOUDSDK_ACTIVE_CONFIG_NAME environment variable to set the equivalent of this flag for a terminal session. 
`--flags-file`=`YAML_FILE`
     A YAML or JSON file that specifies a `--flag`:`value` dictionary. Useful for specifying complex flag values with special characters that work with any command interpreter. Additionally, each `--flags-file` arg is replaced by its constituent flags. See $ [gcloud topic flags-file](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) for more information. 
`--flatten`=[`KEY`,…]
     Flatten `name`[] output resource slices in `KEY` into separate records for each item in each slice. Multiple keys and slices may be specified. This also flattens keys for `--format` and `--filter`. For example, `--flatten=abc.def` flattens `abc.def[].ghi` references to `abc.def.ghi`. A resource record containing `abc.def[]` with N elements will expand to N records in the flattened output. This allows us to specify what `resource-key` the `filter` will operate on. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--format`=`FORMAT`
     Sets the format for printing command output resources. The default is a command-specific human-friendly output format. If both `core/format` and `--format` are specified, `--format` takes precedence. `--format` and `core/format` both take precedence over `core/default_format`. The supported formats are limited to: `config`, `csv`, `default`, `diff`, `disable`, `flattened`, `get`, `json`, `list`, `multi`, `none`, `object`, `table`, `text`, `value`, `yaml`. For more details run $ [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference) topic formats. Run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) --help` to see more information about `core/format`
`--help`
     Display detailed help. 
`--project`=`PROJECT_ID`
     The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

`--quiet`, `-q`
     Disable all interactive prompts when running `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` commands. If input is required, defaults will be used, or an error will be raised. 

Overrides the default core/disable_prompts property value for this command invocation. This is equivalent to setting the environment variable `CLOUDSDK_CORE_DISABLE_PROMPTS` to 1. 

`--verbosity`=`VERBOSITY`; default="warning"
     Override the default verbosity for this command. Overrides the default `core/verbosity` property value for this command invocation. `VERBOSITY` must be one of: `debug`, `info`, `warning`, `error`, `critical`, `none`. 
`--version`, `-v`
     Print version information and exit. This flag is only available at the global level. 
`-h`
     Print a summary help and exit. 
OTHER FLAGS
    

`--access-token-file`=`ACCESS_TOKEN_FILE`
     A file path to read the access token. Use this flag to authenticate `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` with an access token. The credentials of the active account (if exists) will be ignored. The file should only contain an access token with no other information. Overrides the default `auth/access_token_file` property value for this command invocation. 
`--impersonate-service-account`=`SERVICE_ACCOUNT_EMAILS`
     For this `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` invocation, all API requests will be made as the given service account or target service account in an impersonation delegation chain instead of the currently selected account. You can specify either a single service account as the impersonator, or a comma-separated list of service accounts to create an impersonation delegation chain. The impersonation is done without needing to create, download, and activate a key for the service account or accounts. 

In order to make API requests as a service account, your currently selected account must have an IAM role that includes the `iam.serviceAccounts.getAccessToken` permission for the service account or accounts. 

The `roles/iam.serviceAccountTokenCreator` role has the `iam.serviceAccounts.getAccessToken permission`. You can also create a custom role. 

You can specify a list of service accounts, separated with commas. This creates an impersonation delegation chain in which each service account delegates its permissions to the next service account in the chain. Each service account in the list must have the `roles/iam.serviceAccountTokenCreator` role on the next service account in the list. For example, when `--impersonate-service-account=` ``SERVICE_ACCOUNT_1``,``SERVICE_ACCOUNT_2``, the active account must have the `roles/iam.serviceAccountTokenCreator` role on ``SERVICE_ACCOUNT_1``, which must have the `roles/iam.serviceAccountTokenCreator` role on ``SERVICE_ACCOUNT_2``. ``SERVICE_ACCOUNT_1`` is the impersonated service account and ``SERVICE_ACCOUNT_2`` is the delegate. 

Overrides the default `auth/impersonate_service_account` property value for this command invocation. 

`--log-http`
     Log all HTTP server requests and responses to stderr. Overrides the default `core/log_http` property value for this command invocation. 
`--trace-token`=`TRACE_TOKEN`
     Token used to route traces of service requests for investigation of issues. Overrides the default `core/trace_token` property value for this command invocation. 
`--user-output-enabled`
     Print user intended output to the console. Overrides the default `core/user_output_enabled` property value for this command invocation. Use `--no-user-output-enabled` to disable. 
GROUPS
     ``GROUP`` is one of the following: 

`[access-approval](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-approval)`
     `(BETA)` Manage Access Approval requests and settings. 
`[access-context-manager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager)`
     `(BETA)` Manage Access Context Manager resources. 
`[active-directory](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory)`
     `(BETA)` Manage Managed Microsoft AD resources. 
`[agent-identity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/agent-identity)`
     `(BETA)` Manage Agent Identity resources. 
`[ai](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai)`
     `(BETA)` Manage entities in Vertex AI. 
`[ai-platform](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform)`
     `(BETA)` Manage AI Platform jobs and models. 
`[alloydb](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb)`
     `(BETA)` Create and manage AlloyDB databases. 
`[anthos](https://docs.cloud.google.com/sdk/gcloud/reference/beta/anthos)`
     `(BETA)` Anthos command Group. 
`[api-gateway](https://docs.cloud.google.com/sdk/gcloud/reference/beta/api-gateway)`
     `(BETA)` Manage Cloud API Gateway resources. 
`[api-registry](https://docs.cloud.google.com/sdk/gcloud/reference/beta/api-registry)`
     `(BETA)` Manage Cloud API Registry Command Group. 
`[apigee](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee)`
     `(BETA)` Manage Apigee resources. 
`[app](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app)`
     `(BETA)` Manage your App Engine deployments. 
`[app-lifecycle-manager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager)`
     `(BETA)` Commands for App Lifecycle Manager. 
`[app-optimize](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-optimize)`
     `(BETA)` The App Optimize API lets developers and platform administrators monitor and analyze cost and resource utilization data and identify cost optimization opportunities for their applications. 
`[app-topology](https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-topology)`
     `(BETA)` Manage App Topology resources and query topology graphs. 
`[artifacts](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts)`
     `(BETA)` Manage Artifact Registry resources. 
`[asset](https://docs.cloud.google.com/sdk/gcloud/reference/beta/asset)`
     `(BETA)` Manage the Cloud Asset Inventory. 
`[assured](https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured)`
     `(BETA)` Read and manipulate Assured Workloads data controls. 
`[auth](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth)`
     `(BETA)` Manage oauth2 credentials for the Google Cloud CLI. 
`[backup-dr](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr)`
     `(BETA)` Manage Backup and DR resources. 
`[batch](https://docs.cloud.google.com/sdk/gcloud/reference/beta/batch)`
     `(BETA)` Manage Batch resources. 
`[beyondcorp](https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp)`
     `(BETA)` Manage secure access to applications with integrated threat and data protection. 
`[biglake](https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake)`
     `(BETA)` Create and manage Google Cloud BigLake resources. 
`[bigtable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable)`
     `(BETA)` Manage your Cloud Bigtable storage. 
`[billing](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing)`
     `(BETA)` Manage billing accounts and associate them with projects. 
`[bq](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bq)`
     `(BETA)` Manage Bq resources. 
`[builds](https://docs.cloud.google.com/sdk/gcloud/reference/beta/builds)`
     `(BETA)` Create and manage builds for Google Cloud Build. 
`[certificate-manager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager)`
     `(BETA)` Manage SSL certificates for your Google Cloud projects. 
`[cloud-shell](https://docs.cloud.google.com/sdk/gcloud/reference/beta/cloud-shell)`
     `(BETA)` Manage Google Cloud Shell. 
`[cluster-director](https://docs.cloud.google.com/sdk/gcloud/reference/beta/cluster-director)`
     `(BETA)` Manage Cluster Director resources. 
`[code](https://docs.cloud.google.com/sdk/gcloud/reference/beta/code)`
     `(BETA)` Create and manage a local development environment for Cloud Run. 
`[colab](https://docs.cloud.google.com/sdk/gcloud/reference/beta/colab)`
     `(BETA)` Manage Colab Enterprise resources. 
`[composer](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer)`
     `(BETA)` Create and manage Cloud Composer Environments. 
`[compute](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute)`
     `(BETA)` Create and manipulate Compute Engine resources. 
`[config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/config)`
     `(BETA)` View and edit Google Cloud CLI properties. 
`[container](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container)`
     `(BETA)` Deploy and manage clusters of machines for running containers. 
`[data-catalog](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog)`
     `(BETA)` Manage Data Catalog resources. 
`[data-fusion](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion)`
     `(BETA)` Create and manage Cloud Data Fusion Instances. 
`[dataflow](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow)`
     `(BETA)` Manage Google Cloud Dataflow resources. 
`[datalineage](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datalineage)`
     `(BETA)` Manage Google Cloud Data Lineage resources. 
`[datapipelines](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datapipelines)`
     `(BETA)` Manage Data Pipelines resources. 
`[dataproc](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc)`
     `(BETA)` Create and manage Google Cloud Dataproc clusters and jobs. 
`[datastore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastore)`
     `(BETA)` Manage your Cloud Datastore resources. 
`[datastream](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream)`
     `(BETA)` Manage Cloud Datastream resources. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deploy)`
     `(BETA)` Create and manage Cloud Deploy resources. 
`[deployment-manager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/deployment-manager)`
     `(BETA)` Manage deployments of cloud resources. 
`[developer-connect](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-connect)`
     `(BETA)` Manage Developer Connect resources. 
`[developer-knowledge](https://docs.cloud.google.com/sdk/gcloud/reference/beta/developer-knowledge)`
     `(BETA)` Manage Developer Knowledge resources and query knowledge base. 
`[device-run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/device-run)`
     `(BETA)` Manage automation sessions and jobs on devices. 
`[dns](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns)`
     `(BETA)` Manage your Cloud DNS managed-zones and record-sets. 
`[domains](https://docs.cloud.google.com/sdk/gcloud/reference/beta/domains)`
     `(BETA)` Manage domains for your Google Cloud projects. 
`[emulators](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators)`
     `(BETA)` Set up your local development environment using emulators. 
`[endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/beta/endpoints)`
     `(BETA)` Create, enable and manage API services. 
`[error-reporting](https://docs.cloud.google.com/sdk/gcloud/reference/beta/error-reporting)`
     `(BETA)` Manage Stackdriver Error Reporting. 
`[essential-contacts](https://docs.cloud.google.com/sdk/gcloud/reference/beta/essential-contacts)`
     `(BETA)` Manage Essential Contacts. 
`[eventarc](https://docs.cloud.google.com/sdk/gcloud/reference/beta/eventarc)`
     `(BETA)` Manage Eventarc resources. 
`[filestore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore)`
     `(BETA)` Create and manipulate Filestore resources. 
`[firebase](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase)`
     `(BETA)` Work with Google Firebase. 
`[firebase-data-connect](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase-data-connect)`
     `(BETA)` Manage Firebase Data Connect resources. 
`[firestore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firestore)`
     `(BETA)` Manage your Cloud Firestore resources. 
`[functions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions)`
     `(BETA)` Manage Google Cloud Functions. 
`[gemini](https://docs.cloud.google.com/sdk/gcloud/reference/beta/gemini)`
     `(BETA)` Manage resources associated with Gemini Code Assist and Gemini Cloud Assist. 
`[healthcare](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare)`
     `(BETA)` Manage Cloud Healthcare resources. 
`[iam](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam)`
     `(BETA)` Manage IAM service accounts and keys. 
`[iap](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap)`
     `(BETA)` Manage IAP policies. 
`[identity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/identity)`
     `(BETA)` Manage Cloud Identity Groups and Memberships resources. 
`[ids](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ids)`
     `(BETA)` Manage Cloud IDS. 
`[kms](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms)`
     `(BETA)` Manage cryptographic keys in the cloud. 
`[logging](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging)`
     `(BETA)` Manage Cloud Logging. 
`[managed-kafka](https://docs.cloud.google.com/sdk/gcloud/reference/beta/managed-kafka)`
     `(BETA)` Administer Managed Service for Apache Kafka clusters, topics, and consumer groups. 
`[memcache](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memcache)`
     `(BETA)` Manage Cloud Memorystore Memcached resources. 
`[memorystore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore)`
     `(BETA)` Manage Memorystore resources. 
`[metastore](https://docs.cloud.google.com/sdk/gcloud/reference/beta/metastore)`
     `(BETA)` Manage Dataproc Metastore resources. 
`[ml](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml)`
     `(BETA)` Use Google Cloud machine learning capabilities. 
`[model-armor](https://docs.cloud.google.com/sdk/gcloud/reference/beta/model-armor)`
     `(BETA)` Model Armor is a service offering LLM-agnostic security and AI safety measures to mitigate risks associated with the use of large language models (LLMs). 
`[monitoring](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring)`
     `(BETA)` Manage Cloud Monitoring dashboards and notification channels. 
`[netapp](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp)`
     `(BETA)` Create and manipulate Cloud NetApp Files resources. 
`[network-connectivity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity)`
     `(BETA)` Manage Network Connectivity resources. 
`[network-management](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-management)`
     `(BETA)` Manage Network Management resources. 
`[network-security](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security)`
     `(BETA)` Manage Network Security resources. 
`[network-services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services)`
     `(BETA)` Manage Network Services resources. 
`[notebooks](https://docs.cloud.google.com/sdk/gcloud/reference/beta/notebooks)`
     `(BETA)` `(DEPRECATED)` Notebooks Command Group. 
`[observability](https://docs.cloud.google.com/sdk/gcloud/reference/beta/observability)`
     `(BETA)` Manage Observability resources. 
`[orchestration-pipelines](https://docs.cloud.google.com/sdk/gcloud/reference/beta/orchestration-pipelines)`
     `(BETA)` Manage Orchestration Pipelines resources. 
`[organizations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/organizations)`
     `(BETA)` Create and manage Google Cloud Platform Organizations. 
`[pam](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam)`
     `(BETA)` Manage Privileged Access Manager (PAM) entitlements and grants. 
`[parametermanager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/parametermanager)`
     `(BETA)` Parameter Manager is a single source of truth for your parameters. 
`[policy-intelligence](https://docs.cloud.google.com/sdk/gcloud/reference/beta/policy-intelligence)`
     `(BETA)` A platform to help better understand, use, and manage policies at scale. 
`[policy-troubleshoot](https://docs.cloud.google.com/sdk/gcloud/reference/beta/policy-troubleshoot)`
     `(BETA)` Troubleshoot Google Cloud Platform policies. 
`[projects](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects)`
     `(BETA)` Create and manage project access policies. 
`[publicca](https://docs.cloud.google.com/sdk/gcloud/reference/beta/publicca)`
     `(BETA)` Manage accounts for Google Trust Services' Certificate Authority. 
`[pubsub](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub)`
     `(BETA)` Manage Cloud Pub/Sub topics, subscriptions, and snapshots. 
`[quotas](https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas)`
     `(BETA)` Manage Cloud Quotas quota info, quota preferences and quota adjuster settings. 
`[recommender](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender)`
     `(BETA)` Manage Cloud recommendations and recommendation rules. 
`[redis](https://docs.cloud.google.com/sdk/gcloud/reference/beta/redis)`
     `(BETA)` Manage Cloud Memorystore Redis resources. 
`[resource-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-config)`
     `(BETA)` Commands for declarative management of Google Cloud Platform resources. 
`[resource-manager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager)`
     `(BETA)` Manage Cloud Resources. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run)`
     `(BETA)` Manage your Cloud Run applications. 
`[runtime-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config)`
     `(BETA)` Manage runtime configuration resources. 
`[scc](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc)`
     `(BETA)` Manage Cloud SCC resources. 
`[scheduler](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scheduler)`
     `(BETA)` Manage Cloud Scheduler jobs and schedules. 
`[secrets](https://docs.cloud.google.com/sdk/gcloud/reference/beta/secrets)`
     `(BETA)` Manage secrets on Google Cloud. 
`[service-directory](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-directory)`
     `(BETA)` Command groups for Service Directory. 
`[service-extensions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-extensions)`
     `(BETA)` Manage Service Extensions resources. 
`[service-health](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-health)`
     `(BETA)` Request events that are relevant to your project or organization. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services)`
     `(BETA)` List, enable and disable APIs and services. 
`[source](https://docs.cloud.google.com/sdk/gcloud/reference/beta/source)`
     `(BETA)` Cloud git repository commands. 
`[source-manager](https://docs.cloud.google.com/sdk/gcloud/reference/beta/source-manager)`
     `(BETA)` Manage Secure Source Manager resources. 
`[spanner](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner)`
     `(BETA)` Command groups for Cloud Spanner. 
`[sql](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql)`
     `(BETA)` Create and manage Google Cloud SQL databases. 
`[support](https://docs.cloud.google.com/sdk/gcloud/reference/beta/support)`
     `(BETA)` Manage Support resources. 
`[tasks](https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks)`
     `(BETA)` Manage Cloud Tasks queues and tasks. 
`[terraform](https://docs.cloud.google.com/sdk/gcloud/reference/beta/terraform)`
     `(BETA)` Commands related to Terraform management of Google Cloud Platform resources. 
`[topic](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic)`
     `(BETA)` gcloud supplementary help. 
`[vector-search](https://docs.cloud.google.com/sdk/gcloud/reference/beta/vector-search)`
     `(BETA)` Manage Vector Search data objects. 
`[workbench](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workbench)`
     `(BETA)` Workbench Command Group. 
`[workflows](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workflows)`
     `(BETA)` Manage your Cloud Workflows resources. 
`[workload-identity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workload-identity)`
     `(BETA)` Manage Workload Identity. 
`[workstations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workstations)`
     `(BETA)` Manage Cloud Workstations resources. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[help](https://docs.cloud.google.com/sdk/gcloud/reference/beta)`
     `(BETA)` Search gcloud help text. 
`[init](https://docs.cloud.google.com/sdk/gcloud/reference/beta/init)`
     `(BETA)` Initialize or reinitialize gcloud. 
`[interactive](https://docs.cloud.google.com/sdk/gcloud/reference/beta/interactive)`
     `(BETA)` Start the gcloud interactive shell. 
`[survey](https://docs.cloud.google.com/sdk/gcloud/reference/beta/survey)`
     `(BETA)` Invoke a customer satisfaction survey for Google Cloud CLI. 
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
