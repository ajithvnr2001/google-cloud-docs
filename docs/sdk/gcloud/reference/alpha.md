---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/
title: gcloud alpha \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:49.663434+00:00
---

# gcloud alpha  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha - alpha versions of gcloud commands 
SYNOPSIS
    

`gcloud alpha` `GROUP` | `COMMAND` [`--account`=`ACCOUNT`] [`--billing-project`=`BILLING_PROJECT`] [`--configuration`=`CONFIGURATION`] [`--flags-file`=`YAML_FILE`] [`--flatten`=[`KEY`,…]] [`--format`=`FORMAT`] [`--help`] [`--project`=`PROJECT_ID`] [`--quiet`, `-q`] [`--verbosity`=`VERBOSITY`; default="warning"] [`--version`, `-v`] [`-h`] [`--access-token-file`=`ACCESS_TOKEN_FILE`] [`--impersonate-service-account`=`SERVICE_ACCOUNT_EMAILS`] [`--log-http`] [`--trace-token`=`TRACE_TOKEN`] [`--no-user-output-enabled`]
DESCRIPTION
     `(ALPHA)` Alpha versions of gcloud commands. 
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

`[access-approval](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-approval)`
     `(ALPHA)` Manage Access Approval requests and settings. 
`[access-context-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager)`
     `(ALPHA)` Manage Access Context Manager resources. 
`[active-directory](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory)`
     `(ALPHA)` Manage Managed Microsoft AD resources. 
`[agent-identity](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-identity)`
     `(ALPHA)` Manage Agent Identity resources. 
`[agent-registry](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry)`
     `(ALPHA)` Manage Agent Registry resources. 
`[ai](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai)`
     `(ALPHA)` Manage entities in Vertex AI. 
`[ai-platform](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform)`
     `(ALPHA)` Manage AI Platform jobs and models. 
`[alloydb](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb)`
     `(ALPHA)` Create and manage AlloyDB databases. 
`[anthos](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/anthos)`
     `(ALPHA)` Anthos command Group. 
`[api-gateway](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/api-gateway)`
     `(ALPHA)` Manage Cloud API Gateway resources. 
`[api-registry](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/api-registry)`
     `(ALPHA)` Manage Cloud API Registry Command Group. 
`[apigee](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee)`
     `(ALPHA)` Manage Apigee resources. 
`[apihub](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub)`
     `(ALPHA)` Manage Apihub resources. 
`[app](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app)`
     `(ALPHA)` Manage your App Engine deployments. 
`[app-topology](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/app-topology)`
     `(ALPHA)` Manage App Topology resources and query topology graphs. 
`[apphub](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apphub)`
     `(ALPHA)` Manage App Hub resources. 
`[artifacts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts)`
     `(ALPHA)` Manage Artifact Registry resources. 
`[asset](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/asset)`
     `(ALPHA)` Manage the Cloud Asset Inventory. 
`[assured](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured)`
     `(ALPHA)` Read and manipulate Assured Workloads data controls. 
`[audit-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/audit-manager)`
     `(ALPHA)` Enroll resources, audit workloads and generate reports. 
`[auth](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/auth)`
     `(ALPHA)` Manage oauth2 credentials for the Google Cloud CLI. 
`[backup-dr](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr)`
     `(ALPHA)` Manage Backup and DR resources. 
`[batch](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch)`
     `(ALPHA)` Manage Batch resources. 
`[beyondcorp](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp)`
     `(ALPHA)` Manage secure access to applications with integrated threat and data protection. 
`[biglake](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake)`
     `(ALPHA)` Create and manage Google Cloud BigLake resources. 
`[bigtable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bigtable)`
     `(ALPHA)` Manage your Cloud Bigtable storage. 
`[billing](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing)`
     `(ALPHA)` Manage billing accounts and associate them with projects. 
`[blockchain-node-engine](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine)`
     `(ALPHA)` Create and manipulate Blockchain Node Engine resources. 
`[blockchain-validator](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator)`
     `(ALPHA)` `(DEPRECATED)` Manage blockchain validator configurations. 
`[bms](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bms)`
     `(ALPHA)` Manage Bare Metal Solution resources. 
`[bq](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq)`
     `(ALPHA)` Interact with and manage resources in Google BigQuery. 
`[builds](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/builds)`
     `(ALPHA)` Create and manage builds for Google Cloud Build. 
`[certificate-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager)`
     `(ALPHA)` Manage SSL certificates for your Google Cloud projects. 
`[cloud-shell](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell)`
     `(ALPHA)` Manage Google Cloud Shell. 
`[cloudlocationfinder](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloudlocationfinder)`
     `(ALPHA)` Manage Cloudlocationfinder resources. 
`[cluster-director](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director)`
     `(ALPHA)` Manage Cluster Director resources. 
`[code](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/code)`
     `(ALPHA)` Create and manage a local development environment for Cloud Run. 
`[composer](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer)`
     `(ALPHA)` Create and manage Cloud Composer Environments. 
`[compute](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute)`
     `(ALPHA)` Create and manipulate Compute Engine resources. 
`[config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/config)`
     `(ALPHA)` View and edit Google Cloud CLI properties. 
`[container](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container)`
     `(ALPHA)` Deploy and manage clusters of machines for running containers. 
`[data-catalog](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog)`
     `(ALPHA)` Manage Data Catalog resources. 
`[database-migration](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/database-migration)`
     `(ALPHA)` Manage Database Migration Service resources. 
`[dataflow](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow)`
     `(ALPHA)` Manage Google Cloud Dataflow resources. 
`[datalineage](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datalineage)`
     `(ALPHA)` Manage Google Cloud Data Lineage resources. 
`[dataplex](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex)`
     `(ALPHA)` Manage Dataplex resources. 
`[dataproc](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc)`
     `(ALPHA)` Create and manage Google Cloud Dataproc clusters and jobs. 
`[datastore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/datastore)`
     `(ALPHA)` Manage your Cloud Datastore resources. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deploy)`
     `(ALPHA)` Create and manage Cloud Deploy resources. 
`[deployment-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager)`
     `(ALPHA)` Manage deployments of cloud resources. 
`[design-center](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/design-center)`
     `(ALPHA)` Manage Application Design Center resources. 
`[developer-connect](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-connect)`
     `(ALPHA)` Manage Developer Connect resources. 
`[developer-knowledge](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/developer-knowledge)`
     `(ALPHA)` Manage Developer Knowledge resources and query knowledge base. 
`[device-run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/device-run)`
     `(ALPHA)` Manage automation sessions and jobs on devices. 
`[dialogflow](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dialogflow)`
     `(ALPHA)` Interact with and manage Dialogflow agents, entities, and intents. 
`[dlp](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp)`
     `(ALPHA)` Manage sensitive data with Cloud Data Loss Prevention. 
`[dns](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns)`
     `(ALPHA)` Manage your Cloud DNS managed-zones and record-sets. 
`[domains](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/domains)`
     `(ALPHA)` Manage domains for your Google Cloud projects. 
`[edge-cache](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache)`
     `(ALPHA)` Manage Media CDN resources. 
`[edge-cloud](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud)`
     `(ALPHA)` Manage edge-cloud resources. 
`[emulators](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators)`
     `(ALPHA)` Set up your local development environment using emulators. 
`[endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/endpoints)`
     `(ALPHA)` Create, enable and manage API services. 
`[essential-contacts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/essential-contacts)`
     `(ALPHA)` Manage Essential Contacts. 
`[fault-testing](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/fault-testing)`
     `(ALPHA)` Manage Fault Testing resources. 
`[filestore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore)`
     `(ALPHA)` Create and manipulate Filestore resources. 
`[firebase](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase)`
     `(ALPHA)` Work with Google Firebase. 
`[firebase-data-connect](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase-data-connect)`
     `(ALPHA)` Manage Firebase Data Connect resources. 
`[firestore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firestore)`
     `(ALPHA)` Manage your Cloud Firestore resources. 
`[functions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/functions)`
     `(ALPHA)` Manage Google Cloud Functions. 
`[healthcare](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/healthcare)`
     `(ALPHA)` Manage Cloud Healthcare resources. 
`[iam](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam)`
     `(ALPHA)` Manage IAM service accounts and keys. 
`[iap](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap)`
     `(ALPHA)` Manage IAP policies. 
`[identity](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/identity)`
     `(ALPHA)` Manage Cloud Identity Groups and Memberships resources. 
`[ids](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ids)`
     `(ALPHA)` Manage Cloud IDS. 
`[infra-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/infra-manager)`
     `(ALPHA)` Manage Infra Manager resources. 
`[kms](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms)`
     `(ALPHA)` Manage cryptographic keys in the cloud. 
`[logging](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging)`
     `(ALPHA)` Manage Cloud Logging. 
`[looker](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/looker)`
     `(ALPHA)` Manage Looker resources. 
`[lustre](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/lustre)`
     `(ALPHA)` Manage Lustre resources. 
`[managed-kafka](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka)`
     `(ALPHA)` Administer Managed Service for Apache Kafka clusters, topics, and consumer groups. 
`[media](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/media)`
     `(ALPHA)` Manage Cloud Media Services. 
`[memcache](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memcache)`
     `(ALPHA)` Manage Cloud Memorystore Memcached resources. 
`[memorystore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore)`
     `(ALPHA)` Manage Memorystore resources. 
`[metastore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/metastore)`
     `(ALPHA)` Manage Dataproc Metastore resources. 
`[migration](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/migration)`
     `(ALPHA)` The root group for various Cloud Migration teams. 
`[ml](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml)`
     `(ALPHA)` Use Google Cloud machine learning capabilities. 
`[mldiagnostics](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mldiagnostics)`
     `(ALPHA)` Use Google Cloud ML Diagnostics capabilities. 
`[model-armor](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/model-armor)`
     `(ALPHA)` Model Armor is a service offering LLM-agnostic security and AI safety measures to mitigate risks associated with the use of large language models (LLMs). 
`[monitoring](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring)`
     `(ALPHA)` Manage Cloud Monitoring alerting policies, dashboards, notification channels, and uptime checks. 
`[mps](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/mps)`
     `(ALPHA)` Manage Marketplace Solutions resources. 
`[netapp](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp)`
     `(ALPHA)` Create and manipulate Cloud NetApp Files resources. 
`[network-connectivity](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-connectivity)`
     `(ALPHA)` Manage Network Connectivity Center resources. 
`[network-management](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management)`
     `(ALPHA)` Manage Network Management resources. 
`[network-security](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security)`
     `(ALPHA)` Manage Network Security resources. 
`[network-services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services)`
     `(ALPHA)` Manage Network Services resources. 
`[notebooks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/notebooks)`
     `(ALPHA)` `(DEPRECATED)` Notebooks Command Group. 
`[number-registry](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry)`
     `(ALPHA)` Manage Cloud Number Registry resources. 
`[observability](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/observability)`
     `(ALPHA)` Manage Observability resources. 
`[onboarding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/onboarding)`
     `(ALPHA)` Manage user onboarding sessions on Google Cloud. 
`[organizations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/organizations)`
     `(ALPHA)` Create and manage Google Cloud Platform Organizations. 
`[pam](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam)`
     `(ALPHA)` Manage Privileged Access Manager (PAM) entitlements and grants. 
`[policy-troubleshoot](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/policy-troubleshoot)`
     `(ALPHA)` Troubleshoot Google Cloud Platform policies. 
`[projects](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects)`
     `(ALPHA)` Create and manage project access policies. 
`[publicca](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/publicca)`
     `(ALPHA)` Manage accounts for Google Trust Services' Certificate Authority. 
`[pubsub](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub)`
     `(ALPHA)` Manage Cloud Pub/Sub topics, subscriptions, and snapshots. 
`[quotas](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas)`
     `(ALPHA)` Manage Cloud Quotas quota info and quota preferences. 
`[recaptcha](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha)`
     `(ALPHA)` Manage reCAPTCHA Enterprise Keys. 
`[recommender](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recommender)`
     `(ALPHA)` Manage Cloud recommendations and recommendation rules. 
`[redis](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/redis)`
     `(ALPHA)` Manage Cloud Memorystore Redis resources. 
`[resource-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-config)`
     `(ALPHA)` Commands for declarative management of Google Cloud Platform resources. 
`[resource-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager)`
     `(ALPHA)` Manage Cloud Resources. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run)`
     `(ALPHA)` Manage your Cloud Run applications. 
`[scc](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc)`
     `(ALPHA)` Manage Cloud SCC resources. 
`[scheduler](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scheduler)`
     `(ALPHA)` Manage Cloud Scheduler jobs and schedules. 
`[secrets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/secrets)`
     `(ALPHA)` Manage secrets on Google Cloud. 
`[service-directory](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-directory)`
     `(ALPHA)` Command groups for Service Directory. 
`[service-extensions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-extensions)`
     `(ALPHA)` Manage Service Extensions resources. 
`[service-health](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-health)`
     `(ALPHA)` Request events that are relevant to your project or organization. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services)`
     `(ALPHA)` List, enable and disable APIs and services. 
`[software-delivery-trust](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/software-delivery-trust)`
     `(ALPHA)` Manage Software Delivery Trust resources. 
`[source](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source)`
     `(ALPHA)` Cloud git repository commands. 
`[source-manager](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager)`
     `(ALPHA)` Manage Secure Source Manager resources. 
`[spanner](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner)`
     `(ALPHA)` Command groups for Cloud Spanner. 
`[sql](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql)`
     `(ALPHA)` Create and manage Google Cloud SQL databases. 
`[storage](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage)`
     `(ALPHA)` Create and manage Cloud Storage buckets and objects. 
`[tasks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks)`
     `(ALPHA)` Manage Cloud Tasks queues and tasks. 
`[terraform](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/terraform)`
     `(ALPHA)` Commands related to Terraform management of Google Cloud Platform resources. 
`[topic](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic)`
     `(ALPHA)` gcloud supplementary help. 
`[trace](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/trace)`
     `(ALPHA)` Manage Stackdriver Trace. 
`[transfer](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer)`
     `(ALPHA)` Manage Transfer Service jobs, operations, and agents. 
`[web-security-scanner](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/web-security-scanner)`
     `(ALPHA)` Manage Cloud Web Security Scanner resources. 
`[workload-identity](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/workload-identity)`
     `(ALPHA)` Manage Workload Identity. 
`[workstations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/workstations)`
     `(ALPHA)` Manage Cloud Workstations resources. 
`[zone-management](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/zone-management)`
     `(ALPHA)` Zone Management gcloud commands. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[help](https://docs.cloud.google.com/sdk/gcloud/reference/alpha)`
     `(ALPHA)` Search gcloud help text. 
`[init](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/init)`
     `(ALPHA)` Initialize or reinitialize gcloud. 
`[interactive](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/interactive)`
     `(ALPHA)` Start the gcloud interactive shell. 
`[survey](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/survey)`
     `(ALPHA)` Invoke a customer satisfaction survey for Google Cloud CLI. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
