---
url: https://docs.cloud.google.com/sdk/gcloud/reference/
title: gcloud \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:27.458113+00:00
---

# gcloud  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud - manage Google Cloud resources and developer workflow 
SYNOPSIS
    

`gcloud` `GROUP` | `COMMAND` [`--account`=`ACCOUNT`] [`--billing-project`=`BILLING_PROJECT`] [`--configuration`=`CONFIGURATION`] [`--flags-file`=`YAML_FILE`] [`--flatten`=[`KEY`,…]] [`--format`=`FORMAT`] [`--help`] [`--project`=`PROJECT_ID`] [`--quiet`, `-q`] [`--verbosity`=`VERBOSITY`; default="warning"] [`--version`, `-v`] [`-h`] [`--access-token-file`=`ACCESS_TOKEN_FILE`] [`--impersonate-service-account`=`SERVICE_ACCOUNT_EMAILS`] [`--log-http`] [`--trace-token`=`TRACE_TOKEN`] [`--no-user-output-enabled`]
DESCRIPTION
     The `gcloud` CLI manages authentication, local configuration, developer workflow, and interactions with the Google Cloud APIs. 

For a quick introduction to the `gcloud` CLI, a list of commonly used commands, and a look at how these commands are structured, run `[gcloud cheat-sheet](https://docs.cloud.google.com/sdk/gcloud/reference/cheat-sheet)` or see the [`gcloud` CLI cheat sheet](https://cloud.google.com/sdk/docs/cheatsheet). 

GLOBAL FLAGS
    

`--account`=`ACCOUNT`
     Google Cloud user account to use for invocation. Overrides the default `core/account` property value for this command invocation. 
`--billing-project`=`BILLING_PROJECT`
     The Google Cloud project that will be charged quota for operations performed in `gcloud`. If you need to operate on one project, but need quota against a different project, you can use this flag to specify the billing project. If both `billing/quota_project` and `--billing-project` are specified, `--billing-project` takes precedence. Run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) --help` to see more information about `billing/quota_project`. 
`--configuration`=`CONFIGURATION`
     File name of the configuration to use for this command invocation. For more information on how to use configurations, run: `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)`. You can also use the CLOUDSDK_ACTIVE_CONFIG_NAME environment variable to set the equivalent of this flag for a terminal session. 
`--flags-file`=`YAML_FILE`
     A YAML or JSON file that specifies a `--flag`:`value` dictionary. Useful for specifying complex flag values with special characters that work with any command interpreter. Additionally, each `--flags-file` arg is replaced by its constituent flags. See $ [gcloud topic flags-file](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) for more information. 
`--flatten`=[`KEY`,…]
     Flatten `name`[] output resource slices in `KEY` into separate records for each item in each slice. Multiple keys and slices may be specified. This also flattens keys for `--format` and `--filter`. For example, `--flatten=abc.def` flattens `abc.def[].ghi` references to `abc.def.ghi`. A resource record containing `abc.def[]` with N elements will expand to N records in the flattened output. This allows us to specify what `resource-key` the `filter` will operate on. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--format`=`FORMAT`
     Sets the format for printing command output resources. The default is a command-specific human-friendly output format. If both `core/format` and `--format` are specified, `--format` takes precedence. `--format` and `core/format` both take precedence over `core/default_format`. The supported formats are limited to: `config`, `csv`, `default`, `diff`, `disable`, `flattened`, `get`, `json`, `list`, `multi`, `none`, `object`, `table`, `text`, `value`, `yaml`. For more details run $ gcloud topic formats. Run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) --help` to see more information about `core/format`
`--help`
     Display detailed help. 
`--project`=`PROJECT_ID`
     The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

`--quiet`, `-q`
     Disable all interactive prompts when running `gcloud` commands. If input is required, defaults will be used, or an error will be raised. 

Overrides the default core/disable_prompts property value for this command invocation. This is equivalent to setting the environment variable `CLOUDSDK_CORE_DISABLE_PROMPTS` to 1. 

`--verbosity`=`VERBOSITY`; default="warning"
     Override the default verbosity for this command. Overrides the default `core/verbosity` property value for this command invocation. `VERBOSITY` must be one of: `debug`, `info`, `warning`, `error`, `critical`, `none`. 
`--version`, `-v`
     Print version information and exit. This flag is only available at the global level. 
`-h`
     Print a summary help and exit. 
OTHER FLAGS
    

`--access-token-file`=`ACCESS_TOKEN_FILE`
     A file path to read the access token. Use this flag to authenticate `gcloud` with an access token. The credentials of the active account (if exists) will be ignored. The file should only contain an access token with no other information. Overrides the default `auth/access_token_file` property value for this command invocation. 
`--impersonate-service-account`=`SERVICE_ACCOUNT_EMAILS`
     For this `gcloud` invocation, all API requests will be made as the given service account or target service account in an impersonation delegation chain instead of the currently selected account. You can specify either a single service account as the impersonator, or a comma-separated list of service accounts to create an impersonation delegation chain. The impersonation is done without needing to create, download, and activate a key for the service account or accounts. 

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

`[access-approval](https://docs.cloud.google.com/sdk/gcloud/reference/access-approval)`
     Manage Access Approval requests and settings. 
`[access-context-manager](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager)`
     Manage Access Context Manager resources. 
`[active-directory](https://docs.cloud.google.com/sdk/gcloud/reference/active-directory)`
     Manage Managed Microsoft AD resources. 
`[agent-identity](https://docs.cloud.google.com/sdk/gcloud/reference/agent-identity)`
     Manage Agent Identity resources. 
`[agent-registry](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry)`
     Manage Agent Registry resources. 
`[ai](https://docs.cloud.google.com/sdk/gcloud/reference/ai)`
     Manage entities in Vertex AI. 
`[ai-platform](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform)`
     Manage AI Platform jobs and models. 
`[alloydb](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb)`
     Create and manage AlloyDB databases. 
`[alpha](https://docs.cloud.google.com/sdk/gcloud/reference/alpha)`
     `(ALPHA)` Alpha versions of gcloud commands. 
`[anthos](https://docs.cloud.google.com/sdk/gcloud/reference/anthos)`
     Anthos command Group. 
`[api-gateway](https://docs.cloud.google.com/sdk/gcloud/reference/api-gateway)`
     Manage Cloud API Gateway resources. 
`[apigee](https://docs.cloud.google.com/sdk/gcloud/reference/apigee)`
     Manage Apigee resources. 
`[apihub](https://docs.cloud.google.com/sdk/gcloud/reference/apihub)`
     Manage Apihub resources. 
`[app](https://docs.cloud.google.com/sdk/gcloud/reference/app)`
     Manage your App Engine deployments. 
`[app-topology](https://docs.cloud.google.com/sdk/gcloud/reference/app-topology)`
     Manage App Topology resources and query topology graphs. 
`[apphub](https://docs.cloud.google.com/sdk/gcloud/reference/apphub)`
     Manage App Hub resources. 
`[artifacts](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts)`
     Manage Artifact Registry resources. 
`[asset](https://docs.cloud.google.com/sdk/gcloud/reference/asset)`
     Manage the Cloud Asset Inventory. 
`[assured](https://docs.cloud.google.com/sdk/gcloud/reference/assured)`
     Read and manipulate Assured Workloads data controls. 
`[audit-manager](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager)`
     Enroll resources, audit workloads and generate reports. 
`[auth](https://docs.cloud.google.com/sdk/gcloud/reference/auth)`
     Manage oauth2 credentials for the Google Cloud CLI. 
`[backup-dr](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr)`
     Manage Backup and DR resources. 
`[batch](https://docs.cloud.google.com/sdk/gcloud/reference/batch)`
     Manage Batch resources. 
`[beta](https://docs.cloud.google.com/sdk/gcloud/reference/beta)`
     `(BETA)` Beta versions of gcloud commands. 
`[beyondcorp](https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp)`
     Manage Beyondcorp resources. 
`[biglake](https://docs.cloud.google.com/sdk/gcloud/reference/biglake)`
     Create and manage Google Cloud BigLake resources. 
`[bigtable](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable)`
     Manage your Cloud Bigtable storage. 
`[billing](https://docs.cloud.google.com/sdk/gcloud/reference/billing)`
     Manage billing accounts and associate them with projects. 
`[bms](https://docs.cloud.google.com/sdk/gcloud/reference/bms)`
     Manage Bare Metal Solution resources. 
`[bq](https://docs.cloud.google.com/sdk/gcloud/reference/bq)`
     Manage Bq resources. 
`[builds](https://docs.cloud.google.com/sdk/gcloud/reference/builds)`
     Create and manage builds for Google Cloud Build. 
`[certificate-manager](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager)`
     Manage SSL certificates for your Google Cloud projects. 
`[cloud-shell](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell)`
     Manage Google Cloud Shell. 
`[cloudlocationfinder](https://docs.cloud.google.com/sdk/gcloud/reference/cloudlocationfinder)`
     Manage Cloudlocationfinder resources. 
`[cluster-director](https://docs.cloud.google.com/sdk/gcloud/reference/cluster-director)`
     Manage Cluster Director resources. 
`[colab](https://docs.cloud.google.com/sdk/gcloud/reference/colab)`
     Manage Colab Enterprise resources. 
`[compliance-manager](https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager)`
     Manage Compliance Manager resources. 
`[components](https://docs.cloud.google.com/sdk/gcloud/reference/components)`
     List, install, update, or remove Google Cloud CLI components. 
`[composer](https://docs.cloud.google.com/sdk/gcloud/reference/composer)`
     Create and manage Cloud Composer Environments. 
`[compute](https://docs.cloud.google.com/sdk/gcloud/reference/compute)`
     Create and manipulate Compute Engine resources. 
`[config](https://docs.cloud.google.com/sdk/gcloud/reference/config)`
     View and edit Google Cloud CLI properties. 
`[container](https://docs.cloud.google.com/sdk/gcloud/reference/container)`
     Deploy and manage clusters of machines for running containers. 
`[data-catalog](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog)`
     Manage Data Catalog resources. 
`[database-migration](https://docs.cloud.google.com/sdk/gcloud/reference/database-migration)`
     Manage Database Migration Service resources. 
`[dataflow](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow)`
     Manage Google Cloud Dataflow resources. 
`[datalineage](https://docs.cloud.google.com/sdk/gcloud/reference/datalineage)`
     Manage Google Cloud Data Lineage resources. 
`[dataplex](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex)`
     Manage Dataplex resources. 
`[dataproc](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc)`
     Create and manage Google Cloud Dataproc clusters and jobs. 
`[datastore](https://docs.cloud.google.com/sdk/gcloud/reference/datastore)`
     Manage your Cloud Datastore resources. 
`[datastream](https://docs.cloud.google.com/sdk/gcloud/reference/datastream)`
     Manage Cloud Datastream resources. 
`[deploy](https://docs.cloud.google.com/sdk/gcloud/reference/deploy)`
     Create and manage Cloud Deploy resources. 
`[deployment-manager](https://docs.cloud.google.com/sdk/gcloud/reference/deployment-manager)`
     Manage deployments of cloud resources. 
`[design-center](https://docs.cloud.google.com/sdk/gcloud/reference/design-center)`
     Manage Application Design Center resources. 
`[developer-connect](https://docs.cloud.google.com/sdk/gcloud/reference/developer-connect)`
     Manage Developer Connect resources. 
`[developer-knowledge](https://docs.cloud.google.com/sdk/gcloud/reference/developer-knowledge)`
     Manage Developer Knowledge resources and query knowledge base. 
`[dns](https://docs.cloud.google.com/sdk/gcloud/reference/dns)`
     Manage your Cloud DNS managed-zones and record-sets. 
`[domains](https://docs.cloud.google.com/sdk/gcloud/reference/domains)`
     Manage domains for your Google Cloud projects. 
`[edge-cache](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache)`
     Manage Media CDN resources. 
`[edge-cloud](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud)`
     Manage edge-cloud resources. 
`[emulators](https://docs.cloud.google.com/sdk/gcloud/reference/emulators)`
     Set up your local development environment using emulators. 
`[endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints)`
     Create, enable and manage API services. 
`[essential-contacts](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts)`
     Manage Essential Contacts. 
`[eventarc](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc)`
     Manage Eventarc resources. 
`[filestore](https://docs.cloud.google.com/sdk/gcloud/reference/filestore)`
     Create and manipulate Filestore resources. 
`[firebase](https://docs.cloud.google.com/sdk/gcloud/reference/firebase)`
     Work with Google Firebase. 
`[firestore](https://docs.cloud.google.com/sdk/gcloud/reference/firestore)`
     Manage your Cloud Firestore resources. 
`[functions](https://docs.cloud.google.com/sdk/gcloud/reference/functions)`
     Manage Google Cloud Functions. 
`[gemini](https://docs.cloud.google.com/sdk/gcloud/reference/gemini)`
     Manage resources associated with Gemini Code Assist and Gemini Cloud Assist. 
`[healthcare](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare)`
     Manage Cloud Healthcare resources. 
`[iam](https://docs.cloud.google.com/sdk/gcloud/reference/iam)`
     Manage IAM service accounts and keys. 
`[iap](https://docs.cloud.google.com/sdk/gcloud/reference/iap)`
     Manage IAP policies. 
`[identity](https://docs.cloud.google.com/sdk/gcloud/reference/identity)`
     Manage Cloud Identity Groups and Memberships resources. 
`[ids](https://docs.cloud.google.com/sdk/gcloud/reference/ids)`
     Manage Cloud IDS. 
`[infra-manager](https://docs.cloud.google.com/sdk/gcloud/reference/infra-manager)`
     Manage Infra Manager resources. 
`[kms](https://docs.cloud.google.com/sdk/gcloud/reference/kms)`
     Manage cryptographic keys in the cloud. 
`[logging](https://docs.cloud.google.com/sdk/gcloud/reference/logging)`
     Manage Cloud Logging. 
`[looker](https://docs.cloud.google.com/sdk/gcloud/reference/looker)`
     Manage Looker resources. 
`[lustre](https://docs.cloud.google.com/sdk/gcloud/reference/lustre)`
     Manage Lustre resources. 
`[managed-kafka](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka)`
     Administer Managed Service for Apache Kafka clusters, topics, and consumer groups. 
`[memcache](https://docs.cloud.google.com/sdk/gcloud/reference/memcache)`
     Manage Cloud Memorystore Memcached resources. 
`[memorystore](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore)`
     Manage Memorystore resources. 
`[metastore](https://docs.cloud.google.com/sdk/gcloud/reference/metastore)`
     Manage Dataproc Metastore resources. 
`[migration](https://docs.cloud.google.com/sdk/gcloud/reference/migration)`
     The root group for various Cloud Migration teams. 
`[ml](https://docs.cloud.google.com/sdk/gcloud/reference/ml)`
     Use Google Cloud machine learning capabilities. 
`[model-armor](https://docs.cloud.google.com/sdk/gcloud/reference/model-armor)`
     Model Armor is a service offering LLM-agnostic security and AI safety measures to mitigate risks associated with the use of large language models (LLMs). 
`[monitoring](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring)`
     Manage Cloud Monitoring dashboards. 
`[netapp](https://docs.cloud.google.com/sdk/gcloud/reference/netapp)`
     Create and manipulate Cloud NetApp Files resources. 
`[network-connectivity](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity)`
     Manage Network Connectivity resources. 
`[network-management](https://docs.cloud.google.com/sdk/gcloud/reference/network-management)`
     Manage Network Management resources. 
`[network-security](https://docs.cloud.google.com/sdk/gcloud/reference/network-security)`
     Manage Network Security resources. 
`[network-services](https://docs.cloud.google.com/sdk/gcloud/reference/network-services)`
     Manage Network Services resources. 
`[notebooks](https://docs.cloud.google.com/sdk/gcloud/reference/notebooks)`
     Notebooks Command Group. 
`[observability](https://docs.cloud.google.com/sdk/gcloud/reference/observability)`
     Manage Observability resources. 
`[oracle-database](https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database)`
     Manage Oracle Database resources. 
`[org-policies](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies)`
     Create and manage Organization Policies. 
`[organizations](https://docs.cloud.google.com/sdk/gcloud/reference/organizations)`
     Create and manage Google Cloud Platform Organizations. 
`[pam](https://docs.cloud.google.com/sdk/gcloud/reference/pam)`
     Manage Privileged Access Manager (PAM) entitlements and grants. 
`[parametermanager](https://docs.cloud.google.com/sdk/gcloud/reference/parametermanager)`
     Parameter Manager is a single source of truth for your parameters. 
`[policy-intelligence](https://docs.cloud.google.com/sdk/gcloud/reference/policy-intelligence)`
     A platform to help better understand, use, and manage policies at scale. 
`[policy-troubleshoot](https://docs.cloud.google.com/sdk/gcloud/reference/policy-troubleshoot)`
     Troubleshoot Google Cloud Platform policies. 
`[preview](https://docs.cloud.google.com/sdk/gcloud/reference/preview)`
     `(PREVIEW)` Preview versions of gcloud commands. 
`[privateca](https://docs.cloud.google.com/sdk/gcloud/reference/privateca)`
     Manage private Certificate Authorities on Google Cloud. 
`[projects](https://docs.cloud.google.com/sdk/gcloud/reference/projects)`
     Create and manage project access policies. 
`[publicca](https://docs.cloud.google.com/sdk/gcloud/reference/publicca)`
     Manage accounts for Google Trust Services' Certificate Authority. 
`[pubsub](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub)`
     Manage Cloud Pub/Sub topics, subscriptions, and snapshots. 
`[quotas](https://docs.cloud.google.com/sdk/gcloud/reference/quotas)`
     Manage Cloud Quotas quota info, quota preferences and quota adjuster settings. 
`[recaptcha](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha)`
     Manage reCAPTCHA Enterprise Keys. 
`[recommender](https://docs.cloud.google.com/sdk/gcloud/reference/recommender)`
     Manage Cloud recommendations and recommendation rules. 
`[redis](https://docs.cloud.google.com/sdk/gcloud/reference/redis)`
     Manage Cloud Memorystore Redis resources. 
`[resource-manager](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager)`
     Manage Cloud Resources. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/run)`
     Manage your Cloud Run applications. 
`[scc](https://docs.cloud.google.com/sdk/gcloud/reference/scc)`
     Manage Cloud SCC resources. 
`[scheduler](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler)`
     Manage Cloud Scheduler jobs and schedules. 
`[secrets](https://docs.cloud.google.com/sdk/gcloud/reference/secrets)`
     Manage secrets on Google Cloud. 
`[service-directory](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory)`
     Command groups for Service Directory. 
`[service-extensions](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions)`
     Manage Service Extensions resources. 
`[service-health](https://docs.cloud.google.com/sdk/gcloud/reference/service-health)`
     Request events that are relevant to your project or organization. 
`[services](https://docs.cloud.google.com/sdk/gcloud/reference/services)`
     List, enable and disable APIs and services. 
`[source](https://docs.cloud.google.com/sdk/gcloud/reference/source)`
     Cloud git repository commands. 
`[source-manager](https://docs.cloud.google.com/sdk/gcloud/reference/source-manager)`
     Manage Secure Source Manager resources. 
`[spanner](https://docs.cloud.google.com/sdk/gcloud/reference/spanner)`
     Command groups for Cloud Spanner. 
`[sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql)`
     Create and manage Google Cloud SQL databases. 
`[storage](https://docs.cloud.google.com/sdk/gcloud/reference/storage)`
     Create and manage Cloud Storage buckets and objects. 
`[support](https://docs.cloud.google.com/sdk/gcloud/reference/support)`
     Manage Support resources. 
`[tasks](https://docs.cloud.google.com/sdk/gcloud/reference/tasks)`
     Manage Cloud Tasks queues and tasks. 
`[topic](https://docs.cloud.google.com/sdk/gcloud/reference/topic)`
     gcloud supplementary help. 
`[transcoder](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder)`
     Manage Transcoder jobs and job templates. 
`[transfer](https://docs.cloud.google.com/sdk/gcloud/reference/transfer)`
     Manage Transfer Service jobs, operations, and agents. 
`[vector-search](https://docs.cloud.google.com/sdk/gcloud/reference/vector-search)`
     Manage Vector Search data objects. 
`[vmware](https://docs.cloud.google.com/sdk/gcloud/reference/vmware)`
     Manage Google Cloud VMware Engine resources. 
`[workbench](https://docs.cloud.google.com/sdk/gcloud/reference/workbench)`
     Workbench Command Group. 
`[workflows](https://docs.cloud.google.com/sdk/gcloud/reference/workflows)`
     Manage your Cloud Workflows resources. 
`[workload-identity](https://docs.cloud.google.com/sdk/gcloud/reference/workload-identity)`
     Manage Workload Identity. 
`[workspace-add-ons](https://docs.cloud.google.com/sdk/gcloud/reference/workspace-add-ons)`
     Manage Google Workspace Add-ons resources. 
`[workstations](https://docs.cloud.google.com/sdk/gcloud/reference/workstations)`
     Manage Cloud Workstations resources. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[cheat-sheet](https://docs.cloud.google.com/sdk/gcloud/reference/cheat-sheet)`
     Display gcloud cheat sheet. 
`[docker](https://docs.cloud.google.com/sdk/gcloud/reference/docker)`
     `(DEPRECATED)` Enable Docker CLI access to Google Container Registry. 
`[feedback](https://docs.cloud.google.com/sdk/gcloud/reference/feedback)`
     Provide feedback to the Google Cloud CLI team. 
`[help](https://docs.cloud.google.com/sdk/gcloud/reference)`
     Search gcloud help text. 
`[info](https://docs.cloud.google.com/sdk/gcloud/reference/info)`
     Display information about the current gcloud environment. 
`[init](https://docs.cloud.google.com/sdk/gcloud/reference/init)`
     Initialize or reinitialize gcloud. 
`[survey](https://docs.cloud.google.com/sdk/gcloud/reference/survey)`
     Invoke a customer satisfaction survey for Google Cloud CLI. 
`[version](https://docs.cloud.google.com/sdk/gcloud/reference/version)`
     Print version information for Google Cloud CLI components. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
