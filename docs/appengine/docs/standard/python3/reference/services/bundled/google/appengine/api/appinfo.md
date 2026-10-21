---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/
title: Module: google.appengine.api.appinfo \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:03:02.777536+00:00
---

# Module: google.appengine.api.appinfo  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.appinfo Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/appinfo.py) AppInfo tools. This library allows you to work with AppInfo records in memory, as well as store and load from configuration files.

## Modules

[`appinfo_errors`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo_errors) module: Errors used in the Python appinfo API, used by app developers.

## Classes

[`class AdminConsole`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AdminConsole): Class representing an admin console directives in application info. [`class AdminConsolePage`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AdminConsolePage): Class representing the admin console page in an `AdminConsole` object. [`class ApiConfigHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ApiConfigHandler): Class representing `api_config` handler directives in application info. [`class AppInclude`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInclude): Class representing the contents of an included `app.yaml` file. [`class AppInfoExternal`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInfoExternal): Class representing users application info. [`class AppInfoSummary`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AppInfoSummary): This class contains only basic summary information about an app. [`class AutomaticScaling`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/AutomaticScaling): Class representing automatic scaling settings in AppInfoExternal. [`class BasicScaling`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BasicScaling): Class representing basic scaling settings in AppInfoExternal. [`class BetaSettings`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BetaSettings): Class for Beta (internal or unreleased) settings. [`class BuiltinHandler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/BuiltinHandler): Class representing built-in handler directives in application info. [`class CpuUtilization`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/CpuUtilization): Class representing the configuration of VM CPU utilization. [`class CustomMetric`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/CustomMetric): Class representing CustomMetrics in AppInfoExternal. [`class EndpointsApiService`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/EndpointsApiService): Class representing EndpointsApiService in AppInfoExternal. [`class EnvironmentVariables`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/EnvironmentVariables): Class representing a mapping of environment variable key/value pairs. [`class ErrorHandlers`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ErrorHandlers): Class representing error handler directives in application info. [`class HandlerBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/HandlerBase): Base class for URLMap and ApiConfigHandler. [`class HealthCheck`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/HealthCheck): Class representing the health check configuration. [`class HttpHeadersDict`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/HttpHeadersDict): A dict that limits keys and values to what `http_headers` allows. [`class Library`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/Library): Class representing the configuration of a single library. [`class LivenessCheck`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/LivenessCheck): Class representing the liveness check configuration. [`class ManualScaling`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ManualScaling): Class representing manual scaling settings in AppInfoExternal. [`class Network`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/Network): Class representing the VM network configuration. [`class ReadinessCheck`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ReadinessCheck): Class representing the readiness check configuration. [`class Resources`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/Resources): Class representing the configuration of VM resources. [`class RuntimeConfig`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/RuntimeConfig): Class for "vanilla" runtime configuration. [`class URLMap`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/URLMap): Maps from URLs to handlers. [`class VmHealthCheck`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/VmHealthCheck): Class representing the configuration of the VM health check. [`class VmSettings`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/VmSettings): Class for VM settings. [`class Volume`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/Volume): Class representing the configuration of a volume. [`class VpcAccessConnector`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/VpcAccessConnector): Class representing the VPC Access connector configuration.

## Functions

[`EnsureAsciiString(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/EnsureAsciiString): Ensure s contains only ASCII-safe characters; return it as bytes-type. [`GetAllRuntimes(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/GetAllRuntimes): Returns the list of all valid runtimes. [`LoadAppInclude(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/LoadAppInclude): Loads a single `AppInclude` object where one and only one is expected. [`LoadSingleAppInfo(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/LoadSingleAppInfo): Loads a single `AppInfo` object where one and only one is expected. [`ParseExpiration(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ParseExpiration): Parses an expiration delta string. [`ValidFilename(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ValidFilename): Determines if a file name is valid. [`ValidateCombinedSourceReferencesString(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ValidateCombinedSourceReferencesString): Determines if `source_refs` contains a valid list of source references. [`ValidateHandlers(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ValidateHandlers): Validates a list of handler (`URLMap`) objects. [`ValidateSourceReference(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/appinfo/ValidateSourceReference): Determines if a source reference is valid. | 

## Other Members  
  
---  
  
ADMIN_CONSOLE |  `'admin_console'`  
ALTERNATE_HOSTNAME_SEPARATOR |  `'-dot-'`  
API_CONFIG |  `'api_config'`  
API_ENDPOINT |  `'api_endpoint'`  
API_VERSION |  `'api_version'`  
API_VERSION_RE_STRING |  `'[\\w.]{1,32}'`  
APPLICATION |  `'application'`  
APPLICATION_READABLE |  `'application_readable'`  
APPLICATION_RE_STRING |  `'(?:[a-z\\d\\-]{1,100}\\~)?(?:(?!\\-)[a-z\\d\\-\\.]{1,100}:)?(?!-)[a-z\\d\\-]{0,99}[a-z\\d]'`  
APP_ENGINE_APIS |  `'app_engine_apis'`  
APP_ID_MAX_LEN |  `100`  
APP_START_TIMEOUT_SEC |  `'app_start_timeout_sec'`  
AUTH_FAIL_ACTION |  `'auth_fail_action'`  
AUTH_FAIL_ACTION_REDIRECT |  `'redirect'`  
AUTH_FAIL_ACTION_UNAUTHORIZED |  `'unauthorized'`  
AUTOMATIC_SCALING |  `'automatic_scaling'`  
BACKENDS |  `'backends'`  
BASIC_SCALING |  `'basic_scaling'`  
BETA_SETTINGS |  `'beta_settings'`  
BUILD_ENV_VARIABLES |  `'build_env_variables'`  
BUILTINS |  `'builtins'`  
BUILTIN_NAME_PREFIX |  `'ah-builtin'`  
CHECK_INTERVAL_SEC |  `'check_interval_sec'`  
CODE_LOCK |  `'code_lock'`  
CONFIG_ID |  `'config_id'`  
COOL_DOWN_PERIOD_SEC |  `'cool_down_period_sec'`  
CPU |  `'cpu'`  
CPU_UTILIZATION |  `'cpu_utilization'`  
CPU_UTILIZATION_AGGREGATION_WINDOW_LENGTH_SEC |  `'aggregation_window_length_sec'`  
CPU_UTILIZATION_UTILIZATION |  `'target_utilization'`  
CUSTOM_METRICS |  `'custom_metrics'`  
CUSTOM_METRIC_UTILIZATION |  `'target_utilization'`  
DATASTORE_AUTO_ID_POLICY |  `'auto_id_policy'`  
DATASTORE_ID_POLICY_DEFAULT |  `'default'`  
DATASTORE_ID_POLICY_LEGACY |  `'legacy'`  
DEFAULT_EXPIRATION |  `'default_expiration'`  
DEFAULT_MODULE |  `'default'`  
DEFAULT_NOBUILD_FILES |  `'^$'`  
DEFAULT_SKIP_FILES |  `'^(.*/)?((#.*#)|(.*~)|(.*\\.py[co])|(.*/RCS/.*)|(\\..*)|)$'`  
DERIVED_FILE_TYPE |  `'derived_file_type'`  
DISK_SIZE_GB |  `'disk_size_gb'`  
DISPLAY_APP_ID_RE_STRING |  `'(?!-)[a-z\\d\\-]{0,99}[a-z\\d]'`  
DOMAIN_RE_STRING |  `'(?!\\-)[a-z\\d\\-\\.]{1,100}:'`  
DOMAIN_RE_STRING_WITHOUT_SEPARATOR |  `'(?!\\-)[a-z\\d\\-\\.]{1,100}'`  
DOMAIN_SEPARATOR |  `':'`  
EGRESS_SETTING_ALL_TRAFFIC |  `'all-traffic'`  
EGRESS_SETTING_PRIVATE_RANGES_ONLY |  `'private-ranges-only'`  
ENABLE_HEALTH_CHECK |  `'enable_health_check'`  
ENDPOINTS_API_SERVICE |  `'endpoints_api_service'`  
ENDPOINTS_NAME |  `'name'`  
ENTRYPOINT |  `'entrypoint'`  
ENV |  `'env'`  
ENV_RE_STRING |  `'(1|2|standard|flex|flexible)'`  
ENV_VARIABLES |  `'env_variables'`  
ERROR_CODE |  `'error_code'`  
ERROR_HANDLERS |  `'error_handlers'`  
EXPIRATION |  `'expiration'`  
FAILURE_THRESHOLD |  `'failure_threshold'`  
FILE |  `'file'`  
FILTER |  `'filter'`  
FORWARDED_PORTS |  `'forwarded_ports'`  
GCE_RESOURCE_NAME_REGEX |  `'^[a-z]([a-z\\d-]{0,61}[a-z\\d])?$'`  
GCE_RESOURCE_PATH_REGEX |  `'^[a-z\\d-]+(/[a-z\\d-]+)*$'`  
HANDLERS |  `'handlers'`  
HANDLER_API_ENDPOINT |  `'api_endpoint'`  
HANDLER_SCRIPT |  `'script'`  
HANDLER_STATIC_DIR |  `'static_dir'`  
HANDLER_STATIC_FILES |  `'static_files'`  
HEALTHY_THRESHOLD |  `'healthy_threshold'`  
HEALTH_CHECK |  `'health_check'`  
HOST |  `'host'`  
HTTP_HEADERS |  `'http_headers'`  
IDLE_TIMEOUT |  `'idle_timeout'`  
INCLUDES |  `'includes'`  
INITIAL_DELAY_SEC |  `'initial_delay_sec'`  
INSTANCES |  `'instances'`  
INSTANCE_CLASS |  `'instance_class'`  
INSTANCE_TAG |  `'instance_tag'`  
JAVA_PRECOMPILED |  `'java_precompiled'`  
LIBRARIES |  `'libraries'`  
LIVENESS_CHECK |  `'liveness_check'`  
LOGIN |  `'login'`  
LOGIN_ADMIN |  `'admin'`  
LOGIN_OPTIONAL |  `'optional'`  
LOGIN_REQUIRED |  `'required'`  
MAIN |  `'main'`  
MAJOR_VERSION |  `'major_version'`  
MANUAL_SCALING |  `'manual_scaling'`  
MAXIMUM_CONCURRENT_REQUEST |  `'max_concurrent_requests'`  
MAXIMUM_IDLE_INSTANCES |  `'max_idle_instances'`  
MAXIMUM_PENDING_LATENCY |  `'max_pending_latency'`  
MAX_INSTANCES |  `'max_instances'`  
MAX_NUM_INSTANCES |  `'max_num_instances'`  
MAX_URL_MAPS |  `100`  
MEMORY_GB |  `'memory_gb'`  
METRIC_NAME |  `'metric_name'`  
MIME_TYPE |  `'mime_type'`  
MINIMUM_IDLE_INSTANCES |  `'min_idle_instances'`  
MINIMUM_PENDING_LATENCY |  `'min_pending_latency'`  
MINOR_VERSION |  `'minor_version'`  
MIN_NUM_INSTANCES |  `'min_num_instances'`  
MODULE |  `'module'`  
MODULE_ID_MAX_LEN |  `63`  
MODULE_ID_RE_STRING |  `'^(?!-)[a-z\\d\\-]{0,62}[a-z\\d]$'`  
MODULE_SEPARATOR |  `':'`  
MODULE_VERSION_ID_MAX_LEN |  `63`  
MODULE_VERSION_ID_RE_STRING |  `'^(?!-)[a-z\\d\\-]{0,62}[a-z\\d]$'`  
NAME |  `'name'`  
NETWORK |  `'network'`  
NETWORK_NAME |  `'name'`  
NOBUILD_FILES |  `'nobuild_files'`  
OFF |  `'off'`  
OFF_ALIASES |  `['no', 'n', 'False', 'f', '0', 'false']`  
ON |  `'on'`  
ON_ALIASES |  `['yes', 'y', 'True', 't', '1', 'true']`  
PAGES |  `'pages'`  
PARTITION_RE_STRING |  `'[a-z\\d\\-]{1,100}\\~'`  
PARTITION_RE_STRING_WITHOUT_SEPARATOR |  `'[a-z\\d\\-]{1,100}'`  
PARTITION_SEPARATOR |  `'~'`  
PATH |  `'path'`  
POSITION |  `'position'`  
POSITION_HEAD |  `'head'`  
POSITION_TAIL |  `'tail'`  
PROJECT |  `'project'`  
PYTHON_PRECOMPILED |  `'python_precompiled'`  
READINESS_CHECK |  `'readiness_check'`  
REDIRECT_HTTP_RESPONSE_CODE |  `'redirect_http_response_code'`  
REQUIRED_LIBRARIES | 
    
    
    {
     ('django', '1.11'): [('pytz', '2017.2')],
     ('flask', '0.12'): [('click', '6.6'), ('itsdangerous', '0.24'), ('jinja2', '2.6'), ('werkzeug', '0.11.10')],
     ('grpcio', '1.0.0'): [('protobuf', '3.0.0'), ('enum', '0.9.23'), ('futures', '3.0.5'), ('six', 'latest'), ('setuptools', '36.6.0')],
     ('grpcio', 'latest'): [('protobuf', 'latest'), ('enum', 'latest'), ('futures', 'latest'), ('six', 'latest'), ('setuptools', 'latest')],
     ('jinja2', '2.6'): [('markupsafe', '0.15'), ('setuptools', '0.6c11')],
     ('jinja2', 'latest'): [('markupsafe', 'latest'), ('setuptools', 'latest')],
     ('matplotlib', '1.2.0'): [('numpy', '1.6.1')],
     ('matplotlib', 'latest'): [('numpy', 'latest')],
     ('protobuf', '3.0.0'): [('six', 'latest')],
     ('protobuf', 'latest'): [('six', 'latest')]
    }
      
  
REQUIRE_MATCHING_FILE |  `'require_matching_file'`  
RESOURCES |  `'resources'`  
RESTART_THRESHOLD |  `'restart_threshold'`  
ROLLOUT_STRATEGY |  `'rollout_strategy'`  
ROLLOUT_STRATEGY_FIXED |  `'fixed'`  
ROLLOUT_STRATEGY_MANAGED |  `'managed'`  
RUNTIME |  `'runtime'`  
RUNTIME_CHANNEL |  `'runtime_channel'`  
RUNTIME_CONFIG |  `'runtime_config'`  
RUNTIME_RE_STRING |  `'((gs://[a-z0-9\\-\\._/]+)|([a-z][a-z0-9\\-\\.]{0,29}))'`  
SCRIPT |  `'script'`  
SECURE |  `'secure'`  
SECURE_DEFAULT |  `'default'`  
SECURE_HTTP |  `'never'`  
SECURE_HTTPS |  `'always'`  
SECURE_HTTP_OR_HTTPS |  `'optional'`  
SERVICE |  `'service'`  
SERVICEACCOUNT |  `'service_account'`  
SERVICES |  `'inbound_services'`  
SESSION_AFFINITY |  `'session_affinity'`  
SINGLE_INSTANCE_ASSIGNMENT |  `'single_instance_assignment'`  
SIZE_GB |  `'size_gb'`  
SKIP_FILES |  `'skip_files'`  
SKIP_NO_FILES |  `'(?!)'`  
SOURCE_LANGUAGE |  `'source_language'`  
SOURCE_LANGUAGE_RE_STRING |  `'[\\w.\\-]{1,32}'`  
SOURCE_REFERENCES_MAX_SIZE |  `2048`  
SOURCE_REPO_RE_STRING |  `'^[a-z][a-z0-9\\-\\+\\.]*:[^#]*$'`  
SOURCE_REVISION_RE_STRING |  `'^[0-9a-fA-F]+$'`  
STANDARD_MAX_INSTANCES |  `'max_instances'`  
STANDARD_MIN_INSTANCES |  `'min_instances'`  
STANDARD_TARGET_CPU_UTILIZATION |  `'target_cpu_utilization'`  
STANDARD_TARGET_THROUGHPUT_UTILIZATION |  `'target_throughput_utilization'`  
STANDARD_WEBSOCKET |  `'standard_websocket'`  
STATIC_DIR |  `'static_dir'`  
STATIC_FILES |  `'static_files'`  
SUBNETWORK_NAME |  `'subnetwork_name'`  
SUCCESS_THRESHOLD |  `'success_threshold'`  
TARGET_CONCURRENT_REQUESTS |  `'target_concurrent_requests'`  
TARGET_DISK_READ_BYTES_PER_SEC |  `'target_disk_read_bytes_per_sec'`  
TARGET_DISK_READ_OPS_PER_SEC |  `'target_disk_read_ops_per_sec'`  
TARGET_DISK_WRITE_BYTES_PER_SEC |  `'target_disk_write_bytes_per_sec'`  
TARGET_DISK_WRITE_OPS_PER_SEC |  `'target_disk_write_ops_per_sec'`  
TARGET_NETWORK_RECEIVED_BYTES_PER_SEC |  `'target_network_received_bytes_per_sec'`  
TARGET_NETWORK_RECEIVED_PACKETS_PER_SEC |  `'target_network_received_packets_per_sec'`  
TARGET_NETWORK_SENT_BYTES_PER_SEC |  `'target_network_sent_bytes_per_sec'`  
TARGET_NETWORK_SENT_PACKETS_PER_SEC |  `'target_network_sent_packets_per_sec'`  
TARGET_REQUEST_COUNT_PER_SEC |  `'target_request_count_per_sec'`  
TARGET_TYPE |  `'target_type'`  
TARGET_TYPE_REGEX |  `'^(GAUGE|DELTA_PER_SECOND|DELTA_PER_MINUTE)$'`  
THREADSAFE |  `'threadsafe'`  
TIMEOUT_SEC |  `'timeout_sec'`  
TRACE_SAMPLING |  `'trace_sampling'`  
UNHEALTHY_THRESHOLD |  `'unhealthy_threshold'`  
UPLOAD |  `'upload'`  
URL |  `'url'`  
VERSION |  `'version'`  
VERSION_SEPARATOR |  `'.'`  
VM |  `'vm'`  
VM_HEALTH_CHECK |  `'vm_health_check'`  
VM_SETTINGS |  `'vm_settings'`  
VOLUMES |  `'volumes'`  
VOLUME_NAME |  `'name'`  
VOLUME_TYPE |  `'volume_type'`  
VPC_ACCESS_CONNECTOR |  `'vpc_access_connector'`  
VPC_ACCESS_CONNECTOR_EGRESS_SETTING |  `'egress_setting'`  
VPC_ACCESS_CONNECTOR_NAME |  `'name'`  
VPC_ACCESS_CONNECTOR_NAME_REGEX |  `'^[a-z\\d-]+(/.+)*$'`  
ZONES |  `'zones'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
