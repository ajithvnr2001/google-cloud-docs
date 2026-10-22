---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-rest/
title: TIPCommon.rest \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:08.479126+00:00
---

# TIPCommon.rest  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.rest

### TIPCommon.rest.auth.build_credentials_from_sa

`TIPCommon.rest.auth.build_credentials_from_sa(user_service_account: MutableMapping[str, Any] | None = None, target_principal: str | None = None, source_credentials: Credentials | None = None, quota_project_id: str | None = None, scopes: list[str] | None = None, verify_ssl: bool | None = True, **service_account_attr: Any)→ Credentials`

Builds a credentials object from a service account, workload identity email, or service account attributes.

**Note** Either `user_service_account`, `target_principal`, or `service_account_attr` (using `**kwargs`) must be provided. Otherwise, an `EmptyMandatoryValues` exception will be raised.

#### Parameters

Parameters  
---  
`user_service_account` | `SingleJson | None`The user service account JSON.  
`target_principal` | `str | None`The workload identity email.  
`source_credentials` | `google.auth.Credentials | None`The source credential used to acquire the impersonated credentials. If `None` provided, the system attempts to use application default credentials.  
`quota_project_id` | `str | None`The project ID used for quota and billing.  
`scopes` | `list[str]`The Google Cloud credentials scopes. Defaults to `['https://www.googleapis.com/auth/cloud-platform']`.  
`verify_ssl` | `bool`Define whether to verify SSL certificate. Defaults to `True`.  
`service_account_attr` | `dict[str, Any]`Key-value pairs of destructured service account fields.  
  
#### Raises

`EmptyMandatoryValues` – When there is no service account or workload identity email, or if mandatory fields for the service account are missing. `google.auth.exceptions.RefreshError` – When the credentials couldn't be refreshed.

#### Returns

A credentials object.

#### Return type

`service_account.Credentials`

### TIPCommon.rest.auth.build_credentials_from_sa_attr

`TIPCommon.rest.auth.build_credentials_from_sa_attr(account_type: str, project_id: str, private_key_id: str, private_key: str, client_email: str, client_id: str, auth_uri: str, token_uri: str, auth_provider_x509_url: str, client_x509_cert_url: str, scopes: list[str] | None = None, quota_project_id: str | None = None)→ Credentials`

Builds a credentials object from service account attributes.

#### Parameters

Parameters  
---  
`account_type` | `str`The service account type.  
`project_id` | `str`The service account project ID.  
`private_key_id` | `str`The service account private key ID.  
`private_key` | `str`The service account private key.  
`client_email` | `str`The service account client email.  
`client_id` | `str`The service account client ID.  
`auth_uri` | `str`The service account auth URI.  
`token_uri` | `str`The service account token URI.  
`auth_provider_x509_url` | `str`The service account auth provider x509 cert URL.  
`client_x509_cert_url` | `str`The service account client x509 cert URL.  
`scopes` | `list[str], optional`The Google Cloud credentials scopes. Defaults to `['https://www.googleapis.com/auth/cloud-platform']`.  
`quota_project_id` | `str | None`The project ID used for quota and billing.  
  
#### Raises

`EmptyMandatoryValues` – When mandatory fields for the service account are missing.

#### Returns

A credentials object.

#### Return type

`service_account.Credentials`

### TIPCommon.rest.auth.generate_jwt_from_credentials

`TIPCommon.rest.auth.generate_jwt_from_credentials(credentials: Credentials, verify_ssl: bool = True)→ bytes`

Generates a JSON Web Token to access Google Cloud API resources using REST.

#### Parameters

Parameters  
---  
`credentials` | `google.oauth2.credentials.Credentials`A `google.oauth2.credentials.Credentials` object.  
`verify_ssl` | `bool`Define whether to refresh the credentials token over SSL. Defaults to `True`.  
  
#### Returns

A JWT token to use in the Authorization header.

#### Return type

`bytes`

### TIPCommon.rest.auth.generate_jwt_from_sa

`TIPCommon.rest.auth.generate_jwt_from_sa(service_account, expiry_length=3600, audience=None)`

Generates a JSON Web Token to access Google Cloud API resources using REST.

Parameters  
---  
`service_account` | `str | dict`Google Cloud project service account with the necessary Identity and Access Management roles.  
`expiry_length` | `int`Time set until the token expires in seconds. Default is 1 hour.  
`audience` | `str`Google Cloud scope. If not provided, falls back to `https://www.googleapis.com/auth/cloud-platform`.  
  
#### Returns

A JWT token to use in the authorization header.

#### Return type

`bytes`

### TIPCommon.rest.auth.get_adc

`TIPCommon.rest.auth.get_adc(scopes: Sequence[str] | None = None, request: Request | None = None, quota_project_id: str | None = None)→ Tuple[Credentials, str | None]`

Gets Application Default Credentials (ADC) of the runtime environment. This is a wrapper function for `google.auth.default`.

#### Parameters

Parameters  
---  
`scopes` | `Sequence[str] | None`The list of scopes for the credentials. If specified, the credentials automatically scope when necessary.  
`request` | `google.auth.transport.Request | None` An object used to make HTTP requests. This is used to either detect whether the application runs on Compute Engine or to determine the associated project ID for a workload identity pool resource (external account credentials). If not specified, it uses either the standard library HTTP client for Compute Engine credentials or a `google.auth.transport.requests.Request` client for external account credentials.  
`quota_project_id` | `str | None`The project ID used for quota and billing.  
  
#### Returns

The current environment's credentials and project ID. Project ID may be `None`, which indicates that the Project ID couldn't be ascertained from the environment.

#### Return type

`Tuple[google.auth.credentials.Credentials, str]`

#### Raises

`google.auth.exceptions.DefaultCredentialsError` – When no credentials were found, or if the credentials found were invalid.

### TIPCommon.rest.auth.get_auth_request

`TIPCommon.rest.auth.get_auth_request(verify_ssl: bool = True)→ Request`

Creates an authorized HTTP request to a Google Cloud resource API.

#### Parameters

Parameters  
---  
`verify_ssl` | `bool, optional`Verifies SSL certificate. Defaults to `True`.  
  
#### Returns

An authorized request object.

#### Return type

`google.auth.transport.requests.Request`

### TIPCommon.rest.auth.get_impersonated_credentials

`TIPCommon.rest.auth.get_impersonated_credentials(target_principal: str, source_credentials: google.auth.Credentials | None = None, target_scopes: Sequence[str] | None = None, delegates: Sequence[str] | None = None, quota_project_id: str | None = None)→ impersonated_credentials.Credentials`

Gets a short-lived Credentials object using Google Cloud ServiceAccount Impersonation.

#### Parameters

Parameters  
---  
`target_principal` | `str`The service account to impersonate.  
`source_credentials` | `google.auth.Credentials | None`The source credential used to acquire the impersonated credentials. If nothing is provided, the system attempts to use application default credentials.  
`target_scopes` | `Sequence[str] | None`The scopes to request during the authorization grant. If `None` provided, the default `https://www.googleapis.com/auth/cloud-platform` scope is used.  
`delegates` | `Sequence[str] | None`The chained list of delegates required to grant the final access token. If set, the sequence of identities must have `Service Account Token Creator` capability granted to the preceding identity. For example, if set to `[serviceAccountB, serviceAccountC]`, the `source_credential` must have the Token Creator role on `serviceAccountB`. `serviceAccountB` must have the Token Creator on `serviceAccountC`. Finally, `C` must have Token Creator on `target_principal`. If left unset, `source_credential` must have that role on `target_principal`.  
`quota_project_id` | `str | None`The project ID used for quota and billing. Note: This project may be different from the project used to create the credentials.  
  
#### Returns

A short-lived Credentials object of the target principal.

#### Return type

`impersonated_credentials.Credentials`

### TIPCommon.rest.auth.get_secops_siem_tenant_credentials

`TIPCommon.rest.auth.get_secops_siem_tenant_credentials(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, target_scopes: Sequence[str] | None = None, quota_project_id: str | None = None)→ Credentials`

Gets the SIEM tenant short-lived service account credentials of the Google SecOps instance.

#### Parameters

Parameters  
---  
`chronicle_soar` | `TIPCommon.types.ChronicleSOAR`The Google SecOps SDK object.  
`target_scopes` | `Sequence[str] | None`The scopes to request during the authorization grant.  
`quota_project_id` | `str | None`The project ID used for quota and billing. Note: This project may be different from the project used to create the credentials.  
  
#### Returns

SIEM tenant short-lived service account credentials.

#### Return type

`impersonated_credentials.Credentials`

## _class_ TIPCommon.rest.gcp.GcpErrorReason

_class_ `TIPCommon.rest.gcp.GcpErrorReason`

Bases: **object**

The Google Cloud Error Reason constants namespace.

### Constants

  * `IAM_PERMISSION_DENIED = 'IAM_PERMISSION_DENIED'`



## _class_ TIPCommon.rest.gcp.GcpPermissions

_class_ `TIPCommon.rest.gcp.GcpPermissions`

Bases: **object**

The Google Cloud Permissions constants namespace.

### Constants

  * `IAM_SA_GET_ACCESS_TOKEN = 'iam.serviceAccounts.getAccessToken'`



### TIPCommon.rest.gcp.extract_project_id_from_sa_email

`TIPCommon.rest.gcp.extract_project_id_from_sa_email(service_account_email: str)→ str`

Extracts the project ID from the service account email.

#### Parameters

Parameters  
---  
`service_account_email` | `str`The service account email.  
  
#### Returns

The project ID.

#### Return type

`str`

#### Raises

`NotFoundError` – When it can't parse the project name out of the SA email.

### TIPCommon.rest.gcp.extract_project_id_from_sa_key

`TIPCommon.rest.gcp.extract_project_id_from_sa_key(service_account_json: MutableMapping[str, Any])→ str`

Extracts the project ID from the service account JSON key.

#### Parameters

Parameters  
---  
`service_account_json` | `SingleJson`The Service Account JSON key.  
  
#### Returns

Project ID field from the service account key.

#### Return type

`str`

#### Raises

`NotFoundError` – When it can't find the "project_id" field in the Service Account key.

### TIPCommon.rest.gcp.get_http_client

`TIPCommon.rest.gcp.get_http_client(credentials: Credentials, verify_ssl: bool = True)→ Http | AuthorizedHttp`

Gets a Google Cloud Authorized HTTP client.

#### Parameters

Parameters  
---  
`credentials` | `service_account.Credentials`A Google Cloud Credentials object.  
`verify_ssl` | `bool`, optionalVerifies SSL certificate. Defaults to `True`.  
  
#### Returns

The authorized HTTP client.

#### Return type

`Union[httplib2.Http, google_auth_httplib2.AuthorizedHttp]`

### TIPCommon.rest.gcp.get_workload_sa_email

`TIPCommon.rest.gcp.get_workload_sa_email(default_sa_to_return: str | None = None)→ str`

Retrieves the Workload service account email from the Google Cloud metadata server.

#### Parameters

Parameters  
---  
`default_sa_to_return` | `str | None`Default service account to return if not found. Defaults to `None`.  
  
#### Returns

The Workload service account email.

#### Return type

`str`

#### Raises

`GoogleCloudException` – When unable to get the GCP Workload service Account email.

### TIPCommon.rest.gcp.retrieve_project_id

`TIPCommon.rest.gcp.retrieve_project_id(user_service_account: MutableMapping[str, Any] | None = None, service_account_email: str | None = None, default_project_id: str | None = None)→ str | None`

Gets the project ID from a service account or workload identity email.

#### Parameters

Parameters  
---  
`user_service_account` | `SingleJson | None`The user service account JSON.  
`service_account_email` | `str | None`The workload identity email.  
`default_project_id` | `str | None`The default project ID to return if not found. If provided, this function won't raise `NotFoundError`. Defaults to `None`.  
  
#### Returns

The project ID of the service account or workload identity email. If not found, returns `None`.

#### Return type

`str | None`

#### Raises

`NotFoundError` – When unable to parse the project name out of the SA email.

### TIPCommon.rest.gcp.validate_impersonation

`TIPCommon.rest.gcp.validate_impersonation(content: dict, default_error_msg: str = 'Service Account Impersonation failed')→ None`

Validates Service Account impersonation from an HTTP authorized response.

**Note:** This function raises `ImpersonationUnauthorizedError` only if SA impersonation is not authorized. Otherwise, it returns `None`.

#### Parameters

Parameters  
---  
`content` | `dict`The HTTP authorized response content.  
`default_error_msg` | `str, optional`An error message to raise if not found in response content. Defaults to `"Service Account Impersonation failed"`.  
  
#### Returns

`None` if Service Account impersonation is authorized.

#### Return type

`None`

#### Raises

`ImpersonationUnauthorizedError` – When Service Account impersonation is not authorized.

### TIPCommon.rest.httplib.get_auth_session

`TIPCommon.rest.httplib.get_auth_session(service_account, audience=None, verify_ssl=True)`

Creates an authorized HTTP session to a Google Cloud resource API.

Parameters  
---  
`service_account` | `str | dict`A Google Cloud project service account with the necessary Identity and Access Management roles.  
`audience` | `str`The Google Cloud scope.  
`verify_ssl` | `bool`Defines whether to create a session with SSL encryption.  
**Note:** Either `service_account` or `credentials` must be provided and either type of credentials object that you use must possess the necessary Identity and Access Management roles.

#### Returns

An authorized session object.

#### Return type

`requests.Session`

#### Raises

`ValueError` \- When credentials and service account are not provided.

## _exception_ TIPCommon.rest.soar_api.SoarApiServerError

Bases: **Exception**

Errors from Google SecOps's API calls to the server.

### TIPCommon.rest.soar_api.batch_set_custom_field_values

`TIPCommon.rest.soar_api.batch_set_custom_field_values(chronicle_soar, identifier: int, parent: str, custom_fields_values_mapping: dict[int, list[str]])→ list[CustomFieldValue]`

Batches set custom field values.

#### Parameters

Parameters  
---  
`chronicle_soar` | A Google SecOps SDK object.  
`identifier` | `int`The parent identifier.  
`parent` | `str`The parent path for custom field value (e.g. `cases/1`, `cases/1/alerts/1`).  
`custom_fields_values_mapping` | `dict[int, list[str]]`Custom field IDs to values mapping.  
  
#### Returns

List of CustomFieldValue objects.

#### Return type

`list[CustomFieldValue]`

### TIPCommon.rest.soar_api.get_alert_events

`TIPCommon.rest.soar_api.get_alert_events(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: str | int, alert_identifier: str)→ list[AlertEvent]`

Gets specific alert's events.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_id` | `str | int`The case ID. Example: `13`, `"41"`.  
`alert_identifier` | `str` The alert's identifier (e.g., `'{alert.name}_{alert.id}'`). Example: `alert.name=SERVICE_ACCOUNT_USED alert.id=c3b80f09-38d3-4328-bddb-b938ccee0256 identifier=SERVICE_ACCOUNT_USED_c3b80f09-38d3-4328-bddb-b938ccee0256`.  
  
#### Returns

The request's response JSON. A list of events' JSONs.

#### Return type

`list[SingleJson]`

#### Raises

`requests.HTTPError` – When the server returns a non-success status code. `json.JSONDecodeError` – When the returned value is not a valid JSON.

### TIPCommon.rest.soar_api.get_case_attachments

`TIPCommon.rest.soar_api.get_case_attachments(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: int)→ MutableMapping[str, Any]`

Gets case attachments.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_id` | `int`The Google SecOps case ID.  
  
#### Returns

A mutable mapping representing the case attachments.

#### Return type

`MutableMapping[str, Any]`

### TIPCommon.rest.soar_api.get_case_overview_details

`TIPCommon.rest.soar_api.get_case_overview_details(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: int | str) → [CaseDetails](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-data-models-module#data-models-case-details)`

Get case overview details by case ID.

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google Security Operations SDK object.  
`case_id` | `int | str`The Google SecOps case ID.  
  
#### Returns

The case details object.

#### Return type

([`CaseDetails`](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-data-models-module#data-models_case-details))

#### Raises

`requests.HTTPError` \- When a request fails or the request status is not 200. `json.JSONDecoderError` \- When parsing the response fails.

### TIPCommon.rest.soar_api.get_connector_cards

`TIPCommon.rest.soar_api.get_connector_cards(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, integration_name: str | None = None, connector_identifier: str | None = None)→ list[ConnectorCard]`

Gets all the connector cards.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`integration_name` | `str | None`The integration name.  
`connector_identifier` | `str | None`The connector ID.  
  
#### Returns

A list of all the connector cards.

#### Return type

`list[ConnectorCard]`

### TIPCommon.rest.soar_api.get_entity_data

`TIPCommon.rest.soar_api.get_entity_data(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, entity_identifier: str, entity_environment: str, entity_type: str | None = None, last_case_type: int = 0, case_distribution_type: int = 0)→ MutableMapping[str, Any]`

Fetches entity data.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`entity_identifier` | `int`The entity identifier.  
`entity_environment` | `str`The entity environment.  
`entity_type` | `str`The entity type.  
`last_case_type` | `int`The last case type.  
`case_distribution_type` | `int`The case distribution type.  
  
#### Returns

A mutable mapping representing the entity data.

#### Return type

`dict`

#### Raises

`requests.HTTPError` – When the server returns a non-success status code.

### TIPCommon.rest.soar_api.get_env_action_def_files

`TIPCommon.rest.soar_api.get_env_action_def_files(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob)→ list[Dict[str, Any]]`

Retrieves a list of environment action definition files.

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
  
#### Returns

A list of `SingleJson` objects representing the action definition files.

#### Return type

`(list[SingleJson])`

#### Raises

`requests.HTTPError` \- When the server returns a non-success status code. `json.JSONDecodeError` – When the returned value is not valid JSON.

### TIPCommon.rest.soar_api.get_federation_cases

`TIPCommon.rest.soar_api.get_federation_cases(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob)→ MutableMapping[str, Any]`

Gets federation cases.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
  
#### Returns

Response JSON.

#### Return type

`SingleJson`

### TIPCommon.rest.soar_api.get_full_case_details

`TIPCommon.rest.soar_api.get_full_case_details(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: int)→ MutableMapping[str, Any]`

Gets full case details.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_id` | `int`The Google SecOps case ID.  
  
#### Returns

A mutable mapping representing the full case details.

#### Return type

`MutableMapping[str, Any]`

### TIPCommon.rest.soar_api.get_installed_integrations_of_environment

`TIPCommon.rest.soar_api.get_installed_integrations_of_environment(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, environment: str, integration_identifier: str | None = None)→ list[InstalledIntegrationInstance]`

Fetches all integrations installed for provided environments.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`environment` | `str`The instance environments list.  
`integration_identifier` | `str | None`The integration ID.  
  
#### Returns

A list of dictionary objects representing integration instances.

#### Return type

`list[InstalledIntegrationInstance]`

### TIPCommon.rest.soar_api.get_installed_jobs

`TIPCommon.rest.soar_api.get_installed_jobs(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob)→ list[Dict[str, Any]]`

Retrieves a list of environment action definition files.

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
  
#### Returns

A list of `SingleJson` objects representing the action definition files.

#### Return type

`(list[SingleJson])`

#### Raises

`requests.HTTPError` \- When the server returns a non-success status code. `json.JSONDecodeError` – When the returned value is not valid JSON.

### TIPCommon.rest.soar_api.get_integration_full_details

`TIPCommon.rest.soar_api.get_integration_full_details(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, integration_identifier: str)→ Dict[str, Any]`

Retrieves the full details file of the integration.

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`integration_identifier` | `str`The integration ID.  
  
#### Returns

A JSON response containing the full details of the integration.

#### Return type

`(SingleJSON)`

#### Raises

`requests.HTTPError` \- When the server returns a non-success status code. `json.JSONDecodeError` – When the returned value is not valid JSON.

### TIPCommon.rest.soar_api.get_user_profile_cards

`TIPCommon.rest.soar_api.get_user_profile_cards(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, search_term: str = '', requested_page: int = 0, page_size: int = 20, filter_by_role: bool = False, filter_disabled_users: bool = False, filter_support_users: bool = False, fetch_only_support_users: bool = False, filter_permission_types: list[int] = None)→ MutableMapping[str, Any]`

Retrieves user profile cards by page and filter.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`search_term` | `str`The search terms.  
`requested_page` | `int`The starting offset for returning a users' page.  
`page_size` | `int`The number of users to return.  
`filter_by_role` | `bool`Define whether to filter out by role.  
`filter_disabled_users` | `bool`Define whether to filter out disabled users.  
`filter_support_users` | `bool`Define whether to filter out support users.  
`fetch_only_support_users` | `bool`Define whether to return support users only.  
`filter_permission_types` | `list[int] | None`A list of filter permission types (e.g. `0`).  
  
#### Returns

The response from SOAR server - the user profile card.

#### Return type

`SingleJson`

#### Raises

`requests.HTTPError` – When the server returns a non-success status code. `json.JSONDecodeError` – When the returned value is not valid JSON.

#### Example

An example of the response JSON:
    
    
    {
      "objectsList": [
        { "firstName": "string", "lastName": "string", "userName": "string", "accountState": 0 }
      ],
      "metadata": {
        "totalNumberOfPages": 0,
        "totalRecordsCount": 0,
        "pageSize": 0
      }
    }
    

### TIPCommon.rest.soar_api.get_workflow_instance_card

`TIPCommon.rest.soar_api.get_workflow_instance_card(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: int, alert_identifier: str)→ MutableMapping[str, Any]`

Gets a workflow instance card.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_id` | `int`The Google SecOps case ID.  
`alert_identifier` | `str`The Google SecOps alert ID.  
  
#### Returns

A mutable mapping representing the workflow instance card.

#### Return type

`MutableMapping[str, Any]`

### TIPCommon.rest.soar_api.list_custom_field_values

`TIPCommon.rest.soar_api.list_custom_field_values(chronicle_soar, parent: str)→ list[CustomFieldValue]`

Gets custom field values for a case or alert.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`parent` | `str`The parent path for the custom field value (e.g.: `cases/1`, `cases/1/alerts/1`).  
  
#### Returns

The case details object.

#### Return type

`list[CustomFieldValue]`

#### Raises

`requests.HTTPError` – When the request fails or the request status is not 200. `json.JSONDecoderError` – When parsing the response fails.

### TIPCommon.rest.soar_api.list_custom_fields

`TIPCommon.rest.soar_api.list_custom_fields(chronicle_soar, filter_: str | None = None)→ list[CustomField]`

Lists custom fields.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`filter_` | `str | None`The filter value for the search.  
  
#### Returns

The case details object.

#### Return type

`list[CustomField]`

#### Raises

`requests.HTTPError` – When the request fails or the request status is not 200. `json.JSONDecoderError` – When parsing the response fails.

### TIPCommon.rest.soar_api.remove_case_tag

`TIPCommon.rest.soar_api.remove_case_tag(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: int, tag: str, alert_identifier: str | None = None)→ None`

Removes a case tag.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_id` | `int`The Google SecOps case ID.  
`tag` | `str`A tag to remove.  
`alert_identifier` | `str | None`{The {google_secops_soar_name}} alert ID.  
  
#### Returns

None.

#### Return type

`None`

#### Raises

`requests.HTTPError` – When the server returns a non-success status code.

### TIPCommon.rest.soar_api.save_attachment_to_case_wall

`TIPCommon.rest.soar_api.save_attachment_to_case_wall(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, attachment_data: CaseWallAttachment)→ MutableMapping[str, Any]`

Saves a file directly to the case wall.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`attachment_data` | `CaseWallAttachment`A `CaseWallAttachment` object.  
  
#### Returns

A mutable mapping representing the API response.

#### Return type

`MutableMapping[str, Any]`

### TIPCommon.rest.soar_api.set_alert_priority

`TIPCommon.rest.soar_api.set_alert_priority(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_id: int, alert_identifier: str, alert_name: str, priority: int)→ None`

Sets alert priority.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_id` | `int`The Google SecOps case ID.  
`alert_identifier` | `str`The Google SecOps alert ID.  
`alert_name` | `str`The Google SecOps alert name.  
`priority` | `int`The Google SecOps priority enum value.  
  
#### Returns

None.

#### Return type

`None`

#### Raises

`requests.HTTPError` – When the server returns a non-success status code.

### TIPCommon.rest.soar_api.set_case_score_bulk

`TIPCommon.rest.soar_api.set_case_score_bulk(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, case_score_mapping: list[dict[str, int | float]])→ MutableMapping[str, Any]`

Sets case scores in bulk.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`case_score_mapping` | `list[dict[str, int | float]]`A Google SecOps case ID to Score mapping.  
  
#### Returns

A response JSON containing the success status and, if applicable, lists of failed cases.

#### Return type

`MutableMapping[str, Any]`

#### Raises

`requests.HTTPError` – When the server returns a non-success status code.

#### Example
    
    
    {
      case_score_mapping = [
      {
        "caseId": 1, "score": 1.0
      }
    
    ]
    }
    

### TIPCommon.rest.soar_api.set_custom_field_values

`TIPCommon.rest.soar_api.set_custom_field_values(chronicle_soar: ChronicleSOAR, parent: str, custom_field_id: int, values: list[str])→ CustomFieldValue`

Sets custom field values.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`parent` | `str`The parent path for custom field value, e.g.: `cases/1`, `cases/1/alerts/1`.  
`custom_field_id` | `int`The custom field ID.  
`values` | `list[str]`A list of custom field values to set.  
  
#### Returns

A CustomFieldValue object.

#### Return type

`CustomFieldValue`

### TIPCommon.rest.soar_api.validate_response

`TIPCommon.rest.soar_api.validate_response(response: Response, validate_json: bool = False) → None`

Validates the response and returns it as JSON.

Parameters  
---  
`response` | `requests.Response`The response to validate.  
  
#### Raises

`HTTPError` \- When the response status code indicates a failure.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
