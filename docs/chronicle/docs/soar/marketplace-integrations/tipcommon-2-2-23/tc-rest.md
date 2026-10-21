---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-rest/
title: TIPCommon.rest \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:15:04.697032+00:00
---

# TIPCommon.rest  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.rest

The **TIPCommon.rest** module serves as the central hub for managing network requests and interactions within the Google Security Operations platform. It contains specialized sub-modules for handling Google Cloud identity services, secure session management, and a robust library of functions for manipulating data using the unified Chronicle API.

## Authentication utilities

The authentication sub-module provides a suite of functions designed to manage Google Cloud service accounts, workload identities, and token generation. It facilitates the construction of `Credentials` objects required for making authorized calls to Google SecOps resources.

The following functions establish secure identity contexts and generate authorization tokens for API communication:

Functions  
---  
`build_credentials_from_sa(user_service_account, target_principal, source_credentials, quota_project_id, scopes, verify_ssl, **service_account_attr)` | Returns: `Credentials` Builds a credentials object from a service account JSON, workload identity email, or specific attributes. Note that either a service account or workload identity must be provided to avoid an `EmptyMandatoryValues` error.  
`build_credentials_from_sa_attr(account_type, project_id, private_key_id, private_key, client_email, client_id, auth_uri, token_uri, auth_provider_x509_url, client_x509_cert_url, scopes, quota_project_id)` | Returns: `Credentials` Explicitly constructs a credentials object using individual service account fields for environments where a JSON key file is not directly available.  
`generate_jwt_from_credentials(credentials, verify_ssl=True)` | Returns: `bytes` Generates a JSON Web Token (JWT) from a provided Google credentials object for use in Authorization headers when accessing REST resources.  
`generate_jwt_from_sa(service_account_, expiry_length=3600, audience=None)` | Returns: `bytes` Creates a JSON Web Token (JWT) directly from service account data, allowing for custom expiry times and specific audience scopes.  
`get_adc(scopes=None, request=None, quota_project_id=None)` | Returns: `Tuple[Credentials, str | None]` A wrapper for `google.auth.default` that retrieves the Application Default Credentials (ADC) and the associated project ID from the local environment.  
`get_auth_request(verify_ssl=True)` | Returns: `google.auth.transport.requests.Request` Creates an authorized HTTP request object specifically for Google Cloud resource APIs, typically used for refreshing credentials.  
`get_impersonated_credentials(target_principal, source_credentials, target_scopes, delegates, quota_project_id)` | Returns: `impersonated_credentials.Credentials` Obtains short-lived credentials by impersonating a target service account. This supports chained delegation through multiple identities.  
`get_secops_siem_tenant_credentials(chronicle_soar, target_scopes=None, quota_project_id=None)` | Returns: `Credentials` Retrieves the short-lived service account credentials for the SIEM tenant associated with the current Google SecOps instance.  
  
## Google Cloud environment helpers

The environment sub-module contains utility functions for resource identification, project metadata extraction, and the creation of authorized HTTP clients. These tools help integrations navigate the Google Cloud ecosystem dynamically and ensure requests are routed to the correct project instances.

The following functions facilitate project and identity discovery within Google Cloud:

Functions  
---  
`extract_project_id_from_sa_email(service_account_email)` | Returns: `str` Parses a service account email string to extract the associated Google Cloud Project ID. Raises `NotFoundError` if the project name cannot be parsed.  
`extract_project_id_from_sa_key(service_account_json)` | Returns: `str` Retrieves the `project_id` field directly from a service account JSON key structure. Raises `NotFoundError` if the field is missing.  
`get_http_client(credentials, verify_ssl=True)` | Returns: `Http | AuthorizedHttp` Returns an authorized HTTP client based on the provided credentials. Supports both `httplib2.Http` and `google_auth_httplib2.AuthorizedHttp`.  
`get_workload_sa_email(default_sa_to_return=None)` | Returns: `str` Queries the Google Cloud metadata server to retrieve the email address of the current Workload service account. Raises `GoogleCloudException` on failure.  
`retrieve_project_id(user_service_account, service_account_email, default_project_id=None)` | Returns: `str | None` A composite function that attempts to find a Project ID from either a service account JSON or an email, falling back to a default value if provided.  
`validate_impersonation(content, default_error_msg='Service Account Impersonation failed')` | Returns: `None` Validates an HTTP authorized response to ensure service account impersonation was successful. Raises `ImpersonationUnauthorizedError` if unauthorized.  
  
The following namespaces provide constants for managing Google Cloud permissions and identifying common error reasons:

Namespaces  
---  
`GcpErrorReason` | Contains error constants used for identifying specific Google Cloud failures. **Constants:** `IAM_PERMISSION_DENIED`  
`GcpPermissions` | Defines permission strings required for specific resource actions. **Constants:** `IAM_SA_GET_ACCESS_TOKEN` (maps to `iam.serviceAccounts.getAccessToken`)  
  
## HTTP library integration

This sub-module provides utilities for creating authorized sessions compatible with standard Python HTTP libraries like `requests`. Establishing a consistent session object ensures that authentication headers and SSL verification are handled automatically for all outgoing communication with Google Cloud services.

The following function generates an authenticated session for external API communication:

Functions  
---  
`get_auth_session(credentials=None, service_account=None, audience=None, verify_ssl=True)` | Returns: `requests.Session` Creates an authorized HTTP session to a Google Cloud resource API. This function requires either `service_account` or `credentials` to be provided; otherwise, it raises a `ValueError`. **Note:** The provided credentials must have the necessary IAM roles configured for the target resource.   
  
## Chronicle API interface

This sub-module provides a high-level interface for interacting with Google SecOps services. It abstracts complex REST calls into Python functions for managing cases, entities, and platform configurations through the unified Chronicle API.

The following functions manage individual cases, their lifecycle, and specialized data retrieval within the platform:

Case Lifecycle and Federation  
---  
`add_or_update_case_task_v5(chronicle_soar: ChronicleSOAR, owner: str, title: str, content: str, due_date_unix_in_ms: int, case_id: str) → None` | Updates or creates a specific task associated with a case ID. **Note:** `ChronicleSOAR` accepts `SiemplifyAction`, `SiemplifyConnectorExecution`, or `SiemplifyJob`.   
`add_or_update_case_task_v6(chronicle_soar: ChronicleSOAR, owner: str, title: str, content: str, due_date_unix_in_ms: int, case_id: str) → None` | An updated version of the case task function for enhanced platform compatibility.  
`add_tags_to_case_in_bulk(chronicle_soar: ChronicleSOAR, case_ids: list[int], tags: list[str]) → MutableMapping[str, Any]` | Applies a collection of tags to multiple cases simultaneously.  
`assign_case_to_user(chronicle_soar: ChronicleSOAR, case_id: int, assign_to: str, alert_identifier: str | None = None) → MutableMapping[str, Any]` | Assigns a specific case to a designated user within the platform.  
`change_case_description(chronicle_soar: ChronicleSOAR, case_id: int, description: str) → MutableMapping[str, Any]` | Updates the primary description field for a specific case ID.  
`execute_bulk_assign(chronicle_soar: ChronicleSOAR, case_ids: list[int], user_name: str) → MutableMapping[str, Any]` | Assigns a list of cases to a single user in one operation.  
`execute_bulk_close_case(chronicle_soar: ChronicleSOAR, case_ids: list[int], close_reason: str | None = None, root_cause: str | None = None, close_comment: str | None = None) → MutableMapping[str, Any]` | Closes multiple cases with a shared reason, root cause, and analyst comment.  
`get_all_case_overview_details(chronicle_soar: ChronicleSOAR, case_id: int | str, case_expand: list[str] | None = None, alert_expand: list[str] | None = None, wall_expand: list[str] | None = None, entity_expand: list[str] | None = None) → CaseDetails` | Retrieves comprehensive case details using explicit expansion for alerts, wall records, and entities.  
`get_case_activities(chronicle_soar: ChronicleSOAR, case_id: int, query_params: dict[str, str] | None = None) → MutableMapping[str, Any]` | Fetches a list of activities (logs, comments) for a case, supporting OData-style filtering.  
`get_case_insights(chronicle_soar: ChronicleSOAR, case_id: int) → MutableMapping[str, Any]` | Retrieves specific insights and metadata associated with a case.  
`get_case_overview_details(chronicle_soar: ChronicleSOAR, case_id: int | str, case_expand: list[str] | None = None, alert_expand: list[str] | None = None) → CaseDetails` | Retrieves a summarized view of case details with optional alert expansion.  
`get_cases_by_timestamp_filter(chronicle_soar: ChronicleSOAR, start_time: int, end_time: int, time_range_filter: int, environments: list[MutableMapping[str, Any]], case_ids: list[int] | None = None) → list[MutableMapping[str, Any]]` | Filters cases based on a Unix timestamp range and specific environments.  
`get_federation_cases(chronicle_soar: ChronicleSOAR, continuation_token: str) → MutableMapping[str, Any]` | Retrieves federated cases using a pagination continuation token.  
`get_full_case_details(chronicle_soar: ChronicleSOAR, case_id: int, case_type: str | None = None, case_expand: list[str] | None = None, alert_expand: list[str] | None = None) → MutableMapping[str, Any]` | Retrieves all available case data with granular control over expanded fields.  
`import_simulator_custom_case(chronicle_soar: ChronicleSOAR, simulated_case_data: MutableMapping[str, Any]) → None` | Imports case data into the platform for simulation or testing purposes.  
`patch_federation_cases(chronicle_soar: ChronicleSOAR, cases_payload: MutableMapping[str, Any], api_root: str | None = None, api_key: str | None = None) → MutableMapping[str, Any]` | Updates federated cases with a new data payload.  
`remove_case_tag(chronicle_soar: ChronicleSOAR, case_id: int, tag: str, alert_identifier: str | None = None) → None` | Deletes a specific tag from a case or alert.  
`rename_case(chronicle_soar: ChronicleSOAR, case_id: int, case_title: str) → MutableMapping[str, Any]` | Modifies the title of an existing case.  
`search_cases_by_everything(chronicle_soar: ChronicleSOAR, search_payload: MutableMapping[str, Any]) → MutableMapping[str, Any]` | Performs a deep search for cases across the platform using a flexible criteria payload.  
`set_case_score_bulk(chronicle_soar: ChronicleSOAR, case_id: int, score: float) → MutableMapping[str, Any]` | Sets the priority or severity score for multiple cases; returns a success report.  
  
The following functions facilitate entity management, investigation, and collaborative entity notes:

Entities and Investigation  
---  
`add_comment_to_entity(chronicle_soar: ChronicleSOAR, content: str, entity_id: int = 0, author: str | None = None, entity_type: str | None = None, entity_identifier: str | None = None, entity_environment: str = 'Default Environment') → MutableMapping[str, Any]` | Attaches a manual or automated comment to a specific entity record.  
`add_entities_to_custom_list(chronicle_soar: ChronicleSOAR, identifier: str | None = None, category: str | None = None, environment: str | None = None) → MutableMapping[str, Any]` | Inserts entities into a designated custom list for whitelist or watchlist management.  
`create_entity(chronicle_soar: ChronicleSOAR, entity: CreateEntity) → None` | Creates a new entity object and maps it into the case graph.  
`get_alert_events(chronicle_soar: ChronicleSOAR, case_id: str | int, alert_identifier: str) → list[AlertEvent]` | Retrieves the specific security events that triggered a given alert.  
`get_case_wall_records(chronicle_soar: ChronicleSOAR, case_id: int | str, wall_expand: list[str] | None = None) → MutableMapping[str, Any]` | Retrieves all records (comments, logs, and evidence links) from a case's wall. **Note:** You can use `wall_expand=["*"]` to retrieve all fields or provide a list of specific field names to expand.  
`get_entity_cards(chronicle_soar: ChronicleSOAR, case_id: int) → list[EntityCard]` | Retrieves metadata for entity cards displayed in the case interface.  
`get_entity_data(chronicle_soar: ChronicleSOAR, entity_identifier: str, entity_environment: str, entity_type: str | None = None, last_case_type: int = 0, case_distribution_type: int = 0) → MutableMapping[str, Any]` | Fetches detailed profile data for an entity within a specific environment.  
`get_entity_expand_cards(chronicle_soar: ChronicleSOAR, case_id: int | str, entity_expand: list[str] | None = None) → MutableMapping[str, Any]` | Retrieves expanded metadata for all entities within a case graph.  
`get_investigator_data(chronicle_soar: ChronicleSOAR, case_id: int, alert_identifier: str) → MutableMapping[str, Any]` | Retrieves data used to populate the Investigator view for a specific alert.  
`get_security_events(chronicle_soar: ChronicleSOAR, case_id: int) → list[MutableMapping[str, Any]]` | Lists all security events associated with a case.  
`get_traking_list_record(chronicle_soar: ChronicleSOAR, category_name: str = '', entity_id: str = '') → MutableMapping[str, Any]` | Retrieves a specific record from the platform tracking list.  
`get_traking_list_records_filtered(chronicle_soar: ChronicleSOAR, category_name: str = '', entity_id: str = '', environment: str | None = None) → MutableMapping[str, Any]` | Retrieves filtered tracking list records based on category or environment.  
`remove_entities_from_custom_list(chronicle_soar: ChronicleSOAR, list_entities_data: list[MutableMapping[str, Any]] | None = None) → MutableMapping[str, Any]` | Deletes specified entities from a custom list.  
  
The following functions manage case evidence, playbooks, and Service Level Agreements (SLA):

Evidence and SLA Management  
---  
`add_attachment_to_case_wall(chronicle_soar: ChronicleSOAR, attachment: Attachment) → str` | Uploads and pins a file attachment to the case evidence wall.  
`attach_playbook_to_the_case(chronicle_soar: ChronicleSOAR, case_id: int, alert_group_identifier: str, alert_identifier: str, playbook_name: str, should_run_automatic: bool) → None` | Manually attaches a specific playbook to a case or alert.  
`get_attachments_metadata(chronicle_soar: ChronicleSOAR, case_id: int) → list[AttachmentMetadata]` | Retrieves metadata for all files currently attached to a case.  
`get_workflow_instance_card(chronicle_soar: ChronicleSOAR, case_id: int, alert_identifier: str) → MutableMapping[str, Any]` | Retrieves metadata for a playbook workflow instance running on an alert.  
`pause_alert_sla(chronicle_soar: ChronicleSOAR, case_id: int, alert_identifier: str, message: str) → MutableMapping[str, Any]` | Stops the SLA timer for an alert. A justification message is required.  
`resume_alert_sla(chronicle_soar: ChronicleSOAR, case_id: int, alert_identifier: str, message: str) → MutableMapping[str, Any]` | Restarts a previously paused SLA timer.  
`save_attachment_to_case_wall(chronicle_soar: ChronicleSOAR, attachment_data: CaseWallAttachment) → MutableMapping[str, Any]` | Directly saves a `CaseWallAttachment` data model to the evidence wall.  
`set_alert_priority(chronicle_soar: ChronicleSOAR, case_id: int, alert_identifier: str, alert_name: str, priority: int) → None` | Updates the priority level of an alert within an active case.  
  
The following utilities manage administrative metadata, custom fields, and platform configurations:

Administration and Platform Configuration  
---  
`batch_set_custom_field_values(chronicle_soar: ChronicleSOAR, identifier: int, parent: str, custom_fields_values_mapping: dict[int, list[str]]) → list[CustomFieldValue]` | Sets multiple custom field values for a case or alert in a single request.  
`get_connector_cards(chronicle_soar: ChronicleSOAR, integration_name: str | None = None, connector_identifier: str | None = None) → list[ConnectorCard]` | Retrieves metadata for all installed connector instances.  
`get_domain_alias(chronicle_soar: ChronicleSOAR, page_count: int = 0) → MutableMapping[str, Any]` | Retrieves configured domain aliases for environment management.  
`get_email_template(chronicle_soar: ChronicleSOAR) → EmailTemplate` | Retrieves the standard email template used for platform notifications.  
`get_env_action_def_files(chronicle_soar: ChronicleSOAR) → list[MutableMapping[str, Any]]` | Retrieves the action definition files configured for the environment.  
`get_installed_integrations_of_environment(chronicle_soar: ChronicleSOAR, environment: str, integration_identifier: str = '-') → list[InstalledIntegrationInstance]` | Lists all integrations installed in a specific SOAR environment.  
`get_installed_jobs(chronicle_soar: ChronicleSOAR, job_instance_id: int | None = None) → list[MutableMapping[str, Any]] | MutableMapping[str, Any]` | Retrieves metadata for scheduled jobs running in the environment.  
`get_integration_full_details(chronicle_soar: ChronicleSOAR, integration_identifier: str) → MutableMapping[str, Any]` | Fetches the complete configuration and metadata for a specific integration.  
`get_integration_instance_details_by_id(chronicle_soar: ChronicleSOAR, integration_identifier: str, instance_id: str, environments: list[str] | None = None) → MutableMapping[str, Any] | None` | Retrieves instance-specific details using a unique instance ID.  
`get_integration_instance_details_by_name(chronicle_soar: ChronicleSOAR, integration_identifier: str, instance_display_name: str, environments: list[str] | None = None) → MutableMapping[str, Any] | None` | Retrieves instance-specific details using the instance display name.  
`get_siemplify_user_details(chronicle_soar: ChronicleSOAR, search_term: str, filter_by_role: bool, requested_page: int, page_size: int, should_hide_disabled_users: str) → UserDetails` | Retrieves detailed profile data for platform users.  
`get_user_profile_cards(chronicle_soar: ChronicleSOAR, search_term: str = '', requested_page: int = 0, page_size: int = 20, filter_by_role: bool = False, filter_disabled_users: bool = False, filter_support_users: bool = False, fetch_only_support_users: bool = False, filter_permission_types: list[int] = None) → MutableMapping[str, Any]` | Retrieves a paginated list of user profile cards with advanced filtering options. **Example response:**
    
    
    {
      "objectsList": [
        {
          "firstName": "string",
          "lastName": "string",
          "userName": "string",
          "accountState": 0
        }
      ],
      "metadata": {
        "totalNumberOfPages": 0,
        "totalRecordsCount": 0,
        "pageSize": 0
      }
    }
       
  
`get_users_profile(chronicle_soar: ChronicleSOAR, display_name: str, search_term: str, filter_by_role: bool, requested_page: int, page_size: int, should_hide_disabled_users: bool) → MutableMapping[str, Any]` | Fetches basic profile information for a group of users.  
`list_custom_field_values(chronicle_soar: ChronicleSOAR, parent: str) → list[CustomFieldValue]` | Lists the values assigned to custom fields for a specific parent (case or alert).  
`list_custom_fields(chronicle_soar: ChronicleSOAR, filter_: str | None = None) → list[CustomField]` | Lists all available custom fields in the platform.  
`set_custom_field_values(chronicle_soar: ChronicleSOAR, parent: str, custom_field_id: int, values: list[str]) → CustomFieldValue` | Assigns specific values to a custom field.  
`validate_response(response: Response, validate_json: bool = False) → None` | Validates an API response. Raises an exception if the status code indicates failure.  
  
## Exceptions

The module utilizes custom exceptions to handle specific API failures returned by the server. Handling these specifically allows for better error categorization within Google SecOps integrations.

The following error class is used for server-level communication issues:

Exceptions  
---  
`SoarApiServerError` | Bases: `Exception` Raised when a request to the Google SecOps API returns an error response or a non-success status code from the server.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
