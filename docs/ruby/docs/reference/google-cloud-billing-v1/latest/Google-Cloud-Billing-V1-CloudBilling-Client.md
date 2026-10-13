---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client/
title: Billing V1 API - Class Google::Cloud::Billing::V1::CloudBilling::Client (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:34.365525+00:00
---

# Billing V1 API - Class Google::Cloud::Billing::V1::CloudBilling::Client (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Billing V1 API - Class Google::Cloud::Billing::V1::CloudBilling::Client (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.18.1  0.17.4  0.16.0  0.15.1  0.14.0  0.13.2  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.5 

Reference documentation and code samples for the Billing V1 API class Google::Cloud::Billing::V1::CloudBilling::Client.

Client for the CloudBilling service.

Retrieves the Google Cloud Console billing accounts and associates them with projects.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Billing::V1::CloudBilling::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudBilling Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration "Google::Cloud::Billing::V1::CloudBilling::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudBilling clients
    ::Google::Cloud::Billing::V1::CloudBilling::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudBilling Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client#Google__Cloud__Billing__V1__CloudBilling__Client_configure_class_ "Google::Cloud::Billing::V1::CloudBilling::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration "Google::Cloud::Billing::V1::CloudBilling::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration)) 



### #create_billing_account
    
    
    def create_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount
    def create_billing_account(billing_account: nil, parent: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

This method creates [billing subaccounts](https://cloud.google.com/billing/docs/concepts#subaccounts).

Google Cloud resellers should use the Channel Services APIs, [accounts.customers.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/create) and [accounts.customers.entitlements.create](https://cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements/create).

When creating a subaccount, the current authenticated user must have the `billing.accounts.update` IAM permission on the parent account, which is typically given to billing account [administrators](https://cloud.google.com/billing/docs/how-to/billing-access). This method will return an error if the parent account has not been provisioned for subaccounts.

**Overloads**
    
    
    def create_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `create_billing_account` via a request object, either of type [Google::Cloud::Billing::V1::CreateBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CreateBillingAccountRequest "Google::Cloud::Billing::V1::CreateBillingAccountRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::CreateBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CreateBillingAccountRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_billing_account(billing_account: nil, parent: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `create_billing_account` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **billing_account** ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount), ::Hash) — Required. The billing account resource to create. Currently CreateBillingAccount only supports subaccount creation, so any created billing accounts must be under a provided parent billing account. 
  * **parent** (::String) — 

Optional. The parent to create a billing account from. Format:

    * `billingAccounts/{billing_account_id}`, for example, `billingAccounts/012345-567890-ABCDEF`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::CreateBillingAccountRequest.new
    
    # Call the create_billing_account method.
    result = client.create_billing_account request
    
    # The returned object is of type Google::Cloud::Billing::V1::BillingAccount.
    p result

### #get_billing_account
    
    
    def get_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount
    def get_billing_account(name: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Gets information about a billing account. The current authenticated user must be a [viewer of the billing account](https://cloud.google.com/billing/docs/how-to/billing-access).

**Overloads**
    
    
    def get_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `get_billing_account` via a request object, either of type [GetBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-GetBillingAccountRequest "Google::Cloud::Billing::V1::GetBillingAccountRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::GetBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-GetBillingAccountRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_billing_account(name: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `get_billing_account` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the billing account to retrieve. For example, `billingAccounts/012345-567890-ABCDEF`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::GetBillingAccountRequest.new
    
    # Call the get_billing_account method.
    result = client.get_billing_account request
    
    # The returned object is of type Google::Cloud::Billing::V1::BillingAccount.
    p result

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the access control policy for a billing account. The caller must have the `billing.accounts.getIamPolicy` permission on the account, which is often given to billing account [viewers](https://cloud.google.com/billing/docs/how-to/billing-access).

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-GetIamPolicyRequest "Google::Iam::V1::GetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-GetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** ([::Google::Iam::V1::GetPolicyOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-GetPolicyOptions), ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #get_project_billing_info
    
    
    def get_project_billing_info(request, options = nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo
    def get_project_billing_info(name: nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo

Gets the billing information for a project. The current authenticated user must have the `resourcemanager.projects.get` permission for the project, which can be granted by assigning the [Project Viewer](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles) role.

**Overloads**
    
    
    def get_project_billing_info(request, options = nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo

Pass arguments to `get_project_billing_info` via a request object, either of type [GetProjectBillingInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-GetProjectBillingInfoRequest "Google::Cloud::Billing::V1::GetProjectBillingInfoRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::GetProjectBillingInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-GetProjectBillingInfoRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_project_billing_info(name: nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo

Pass arguments to `get_project_billing_info` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the project for which billing information is retrieved. For example, `projects/tokyo-rain-123`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::GetProjectBillingInfoRequest.new
    
    # Call the get_project_billing_info method.
    result = client.get_project_billing_info request
    
    # The returned object is of type Google::Cloud::Billing::V1::ProjectBillingInfo.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudBilling client object.

**Yields**

  * (config) — Configure the CloudBilling client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-CloudBilling-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Billing::V1::CloudBilling::Client.new do |config|
      config.timeout = 10.0
    end

### #list_billing_accounts
    
    
    def list_billing_accounts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::BillingAccount>
    def list_billing_accounts(page_size: nil, page_token: nil, filter: nil, parent: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::BillingAccount>

Lists the billing accounts that the current authenticated user has permission to [view](https://cloud.google.com/billing/docs/how-to/billing-access).

**Overloads**
    
    
    def list_billing_accounts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::BillingAccount>

Pass arguments to `list_billing_accounts` via a request object, either of type [ListBillingAccountsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ListBillingAccountsRequest "Google::Cloud::Billing::V1::ListBillingAccountsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::ListBillingAccountsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ListBillingAccountsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_billing_accounts(page_size: nil, page_token: nil, filter: nil, parent: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::BillingAccount>

Pass arguments to `list_billing_accounts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **page_size** (::Integer) — Requested page size. The maximum page size is 100; this is also the default. 
  * **page_token** (::String) — A token identifying a page of results to return. This should be a `next_page_token` value returned from a previous `ListBillingAccounts` call. If unspecified, the first page of results is returned. 
  * **filter** (::String) — Options for how to filter the returned billing accounts. This only supports filtering for [subaccounts](https://cloud.google.com/billing/docs/concepts) under a single provided parent billing account. (for example, `master_billing_account=billingAccounts/012345-678901-ABCDEF`). Boolean algebra and other fields are not currently supported. 
  * **parent** (::String) — 

Optional. The parent resource to list billing accounts from. Format:

    * `organizations/{organization_id}`, for example, `organizations/12345678`
    * `billingAccounts/{billing_account_id}`, for example, `billingAccounts/012345-567890-ABCDEF`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::ListBillingAccountsRequest.new
    
    # Call the list_billing_accounts method.
    result = client.list_billing_accounts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Billing::V1::BillingAccount.
      p item
    end

### #list_project_billing_info
    
    
    def list_project_billing_info(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::ProjectBillingInfo>
    def list_project_billing_info(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::ProjectBillingInfo>

Lists the projects associated with a billing account. The current authenticated user must have the `billing.resourceAssociations.list` IAM permission, which is often given to billing account [viewers](https://cloud.google.com/billing/docs/how-to/billing-access).

**Overloads**
    
    
    def list_project_billing_info(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::ProjectBillingInfo>

Pass arguments to `list_project_billing_info` via a request object, either of type [ListProjectBillingInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ListProjectBillingInfoRequest "Google::Cloud::Billing::V1::ListProjectBillingInfoRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::ListProjectBillingInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ListProjectBillingInfoRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_project_billing_info(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Billing::V1::ProjectBillingInfo>

Pass arguments to `list_project_billing_info` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the billing account associated with the projects that you want to list. For example, `billingAccounts/012345-567890-ABCDEF`. 
  * **page_size** (::Integer) — Requested page size. The maximum page size is 100; this is also the default. 
  * **page_token** (::String) — A token identifying a page of results to be returned. This should be a `next_page_token` value returned from a previous `ListProjectBillingInfo` call. If unspecified, the first page of results is returned. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::ListProjectBillingInfoRequest.new
    
    # Call the list_project_billing_info method.
    result = client.list_project_billing_info request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Billing::V1::ProjectBillingInfo.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #move_billing_account
    
    
    def move_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount
    def move_billing_account(name: nil, destination_parent: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Changes which parent organization a billing account belongs to.

**Overloads**
    
    
    def move_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `move_billing_account` via a request object, either of type [MoveBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-MoveBillingAccountRequest "Google::Cloud::Billing::V1::MoveBillingAccountRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::MoveBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-MoveBillingAccountRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def move_billing_account(name: nil, destination_parent: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `move_billing_account` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the billing account to move. Must be of the form `billingAccounts/{billing_account_id}`. The specified billing account cannot be a subaccount, since a subaccount always belongs to the same organization as its parent account. 
  * **destination_parent** (::String) — Required. The resource name of the Organization to move the billing account under. Must be of the form `organizations/{organization_id}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::MoveBillingAccountRequest.new
    
    # Call the move_billing_account method.
    result = client.move_billing_account request
    
    # The returned object is of type Google::Cloud::Billing::V1::BillingAccount.
    p result

### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets the access control policy for a billing account. Replaces any existing policy. The caller must have the `billing.accounts.setIamPolicy` permission on the account, which is often given to billing account [administrators](https://cloud.google.com/billing/docs/how-to/billing-access).

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-SetIamPolicyRequest "Google::Iam::V1::SetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-SetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-Policy), ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Tests the access control policy for a billing account. This method takes the resource and a set of permissions as input and returns the subset of the input permissions that the caller is allowed for that resource.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-TestIamPermissionsRequest "Google::Iam::V1::TestIamPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-TestIamPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::TestIamPermissionsRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Iam::V1::TestIamPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_billing_account
    
    
    def update_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount
    def update_billing_account(name: nil, account: nil, update_mask: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Updates a billing account's fields. Currently the only field that can be edited is `display_name`. The current authenticated user must have the `billing.accounts.update` IAM permission, which is typically given to the [administrator](https://cloud.google.com/billing/docs/how-to/billing-access) of the billing account.

**Overloads**
    
    
    def update_billing_account(request, options = nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `update_billing_account` via a request object, either of type [UpdateBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-UpdateBillingAccountRequest "Google::Cloud::Billing::V1::UpdateBillingAccountRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::UpdateBillingAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-UpdateBillingAccountRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_billing_account(name: nil, account: nil, update_mask: nil) -> ::Google::Cloud::Billing::V1::BillingAccount

Pass arguments to `update_billing_account` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the billing account resource to be updated. 
  * **account** ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount), ::Hash) — Required. The billing account resource to replace the resource on the server. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Protobuf-FieldMask), ::Hash) — The update mask applied to the resource. Only "display_name" is currently supported. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Billing::V1::BillingAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-BillingAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::UpdateBillingAccountRequest.new
    
    # Call the update_billing_account method.
    result = client.update_billing_account request
    
    # The returned object is of type Google::Cloud::Billing::V1::BillingAccount.
    p result

### #update_project_billing_info
    
    
    def update_project_billing_info(request, options = nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo
    def update_project_billing_info(name: nil, project_billing_info: nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo

Sets or updates the billing account associated with a project. You specify the new billing account by setting the `billing_account_name` in the `ProjectBillingInfo` resource to the resource name of a billing account. Associating a project with an open billing account enables billing on the project and allows charges for resource usage. If the project already had a billing account, this method changes the billing account used for resource usage charges.

_Note:_ Incurred charges that have not yet been reported in the transaction history of the Google Cloud Console might be billed to the new billing account, even if the charge occurred before the new billing account was assigned to the project.

The current authenticated user must have ownership privileges for both the [project](https://cloud.google.com/docs/permissions-overview#h.bgs0oxofvnoo) and the [billing account](https://cloud.google.com/billing/docs/how-to/billing-access).

You can disable billing on the project by setting the `billing_account_name` field to empty. This action disassociates the current billing account from the project. Any billable activity of your in-use services will stop, and your application could stop functioning as expected. Any unbilled charges to date will be billed to the previously associated account. The current authenticated user must be either an owner of the project or an owner of the billing account for the project.

Note that associating a project with a _closed_ billing account will have much the same effect as disabling billing on the project: any paid resources used by the project will be shut down. Thus, unless you wish to disable billing, you should always call this method with the name of an _open_ billing account.

**Overloads**
    
    
    def update_project_billing_info(request, options = nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo

Pass arguments to `update_project_billing_info` via a request object, either of type [UpdateProjectBillingInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-UpdateProjectBillingInfoRequest "Google::Cloud::Billing::V1::UpdateProjectBillingInfoRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Billing::V1::UpdateProjectBillingInfoRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-UpdateProjectBillingInfoRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_project_billing_info(name: nil, project_billing_info: nil) -> ::Google::Cloud::Billing::V1::ProjectBillingInfo

Pass arguments to `update_project_billing_info` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the project associated with the billing information that you want to update. For example, `projects/tokyo-rain-123`. 
  * **project_billing_info** ([::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo), ::Hash) — The new billing information for the project. Output-only fields are ignored; thus, you can leave empty all fields except `billing_account_name`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Billing::V1::ProjectBillingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-billing-v1/latest/Google-Cloud-Billing-V1-ProjectBillingInfo)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/billing/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Billing::V1::CloudBilling::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Billing::V1::UpdateProjectBillingInfoRequest.new
    
    # Call the update_project_billing_info method.
    result = client.update_project_billing_info request
    
    # The returned object is of type Google::Cloud::Billing::V1::ProjectBillingInfo.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
