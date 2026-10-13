---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auth/latest/credentials/externalaccount/
title: Package cloud.google.com/go/auth/credentials/externalaccount (v0.24.1) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:35.012073+00:00
---

# Package cloud.google.com/go/auth/credentials/externalaccount (v0.24.1)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auth/latest/credentials/externalaccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Package cloud.google.com/go/auth/credentials/externalaccount (v0.24.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.1 (latest)  0.24.0  0.23.3  0.22.0  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.5  0.15.0  0.14.1  0.13.0  0.12.1  0.11.0  0.10.2  0.9.9  0.8.1  0.7.3  0.6.1  0.5.2  0.4.2  0.3.0  0.2.2  0.1.1 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/auth/credentials/externalaccount). 

Package externalaccount provides support for creating workload identity federation and workforce identity federation token providers that can be used to access Google Cloud resources from external identity providers. 

## Workload Identity Federation

Using workload identity federation, your application can access Google Cloud resources from Amazon Web Services (AWS), Microsoft Azure or any identity provider that supports OpenID Connect (OIDC) or SAML 2.0. Traditionally, applications running outside Google Cloud have used service account keys to access Google Cloud resources. Using identity federation, you can allow your workload to impersonate a service account. This lets you access Google Cloud resources directly, eliminating the maintenance and security burden associated with service account keys. 

Follow the detailed instructions on how to configure Workload Identity Federation in various platforms: 

\- Amazon Web Services (AWS): <https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#aws>

  * Microsoft Azure: <https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#azure>
  * OIDC identity provider: <https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#oidc>
  * SAML 2.0 identity provider: <https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#saml>

For OIDC and SAML providers, the library can retrieve tokens in fours ways: from a local file location (file-sourced credentials), from a server (URL-sourced credentials), from a local executable (executable-sourced credentials), or from a user defined function that returns an OIDC or SAML token. For file-sourced credentials, a background process needs to be continuously refreshing the file location with a new OIDC/SAML token prior to expiration. For tokens with one hour lifetimes, the token needs to be updated in the file every hour. The token can be stored directly as plain text or in JSON format. For URL-sourced credentials, a local server needs to host a GET endpoint to return the OIDC/SAML token. The response can be in plain text or JSON. Additional required request headers can also be specified. For executable-sourced credentials, an application needs to be available to output the OIDC/SAML token and other information in a JSON format. For more information on how these work (and how to implement executable-sourced credentials), please check out: <https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#create_a_credential_configuration>

To use a custom function to supply the token, define a struct that implements the SubjectTokenProvider interface for OIDC/SAML providers, or one that implements AwsSecurityCredentialsProvider for AWS providers. This can then be used when building a Options.The [cloud.google.com/go/auth.Credentials](https://pkg.go.dev/cloud.google.com/go/auth#Credentials) created from the options using NewCredentials can then be used to access Google Cloud resources. For instance, you can create a new client from the [cloud.google.com/go/storage](https://pkg.go.dev/cloud.google.com/go/storage) package and pass in option.WithTokenProvider(yourTokenProvider)) 

## Workforce Identity Federation

Workforce identity federation lets you use an external identity provider (IdP) to authenticate and authorize a workforce—a group of users, such as employees, partners, and contractors—using IAM, so that the users can access Google Cloud services. Workforce identity federation extends Google Cloud's identity capabilities to support syncless, attribute-based single sign on. 

With workforce identity federation, your workforce can access Google Cloud resources using an external identity provider (IdP) that supports OpenID Connect (OIDC) or SAML 2.0 such as Azure Active Directory (Azure AD), Active Directory Federation Services (AD FS), Okta, and others. 

Follow the detailed instructions on how to configure Workload Identity Federation in various platforms: 

    * [Amazon Web Services (AWS)](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#aws)
    * [Azure AD](https://cloud.google.com/iam/docs/workforce-sign-in-azure-ad)
    * [Okta](https://cloud.google.com/iam/docs/workforce-sign-in-okta)
    * [OIDC identity provider](https://cloud.google.com/iam/docs/configuring-workforce-identity-federation#oidc)
    * [SAML 2.0 identity provider](https://cloud.google.com/iam/docs/configuring-workforce-identity-federation#saml)

For workforce identity federation, the library can retrieve tokens in three ways: from a local file location (file-sourced credentials), from a server (URL-sourced credentials), or from a local executable (executable-sourced credentials). For file-sourced credentials, a background process needs to be continuously refreshing the file location with a new OIDC/SAML token prior to expiration. For tokens with one hour lifetimes, the token needs to be updated in the file every hour. The token can be stored directly as plain text or in JSON format. For URL-sourced credentials, a local server needs to host a GET endpoint to return the OIDC/SAML token. The response can be in plain text or JSON. Additional required request headers can also be specified. For executable-sourced credentials, an application needs to be available to output the OIDC/SAML token and other information in a JSON format. For more information on how these work (and how to implement executable-sourced credentials), please check out: <https://cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#generate_a_configuration_file_for_non-interactive_sign-in>

## Security considerations

Note that this library does not perform any validation on the token_url, token_info_url, or service_account_impersonation_url fields of the credential configuration. It is not recommended to use a credential configuration that you did not generate with the gcloud CLI unless you verify that the URL fields point to a googleapis.com domain. 




## Functions 

### func NewCredentials 
    
    
    func NewCredentials(opts *Options) (*[auth](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auth/latest).[Credentials](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/auth/latest#cloud_google_com_go_auth_Credentials), [error](https://pkg.go.dev/builtin#error))

NewCredentials returns a [cloud.google.com/go/auth.Credentials] configured with the provided options.

## AwsSecurityCredentials
    
    
    type AwsSecurityCredentials struct {
    	// AccessKeyId is the AWS Access Key ID - Required.
    	AccessKeyID [string](https://pkg.go.dev/builtin#string) `json:"AccessKeyID"`
    	// SecretAccessKey is the AWS Secret Access Key - Required.
    	SecretAccessKey [string](https://pkg.go.dev/builtin#string) `json:"SecretAccessKey"`
    	// SessionToken is the AWS Session token. This should be provided for
    	// temporary AWS security credentials - Optional.
    	SessionToken [string](https://pkg.go.dev/builtin#string) `json:"Token"`
    }

AwsSecurityCredentials models AWS security credentials.

## AwsSecurityCredentialsProvider
    
    
    type AwsSecurityCredentialsProvider interface {
    	// AwsRegion should return the AWS region or an error.
    	AwsRegion(ctx context.Context, opts *RequestOptions) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))
    	// GetAwsSecurityCredentials should return a valid set of
    	// AwsSecurityCredentials or an error. The external account token provider
    	// does not cache the returned security credentials, so caching logic should
    	// be implemented in the provider to prevent multiple requests for the
    	// same security credentials.
    	AwsSecurityCredentials(ctx context.Context, opts *RequestOptions) (*AwsSecurityCredentials, [error](https://pkg.go.dev/builtin#error))
    }

AwsSecurityCredentialsProvider can be used to supply AwsSecurityCredentials and an AWS Region to exchange for a GCP access token.

## CertificateConfig
    
    
    type CertificateConfig struct {
    	// UseDefaultCertificateConfig, if true, attempts to load the default
    	// certificate configuration. It checks the GOOGLE_API_CERTIFICATE_CONFIG
    	// environment variable first, then a conventional default file location.
    	// Cannot be true if CertificateConfigLocation is set.
    	UseDefaultCertificateConfig [bool](https://pkg.go.dev/builtin#bool) `json:"use_default_certificate_config"`
    	// CertificateConfigLocation specifies the path to the client certificate
    	// and private key file. Must be set if UseDefaultCertificateConfig is
    	// false or unset.
    	CertificateConfigLocation [string](https://pkg.go.dev/builtin#string) `json:"certificate_config_location"`
    	// TrustChainPath specifies the path to a PEM-formatted file containing
    	// the X.509 certificate trust chain. This file should contain any
    	// intermediate certificates required to complete the trust chain between
    	// the leaf certificate (used for mTLS) and the root certificate(s) in
    	// your workload identity pool's trust store. The leaf certificate and
    	// any certificates already present in the workload identity pool's trust
    	// store are optional in this file. Certificates should be ordered with the
    	// leaf certificate (or the certificate which signed the leaf) first.
    	TrustChainPath [string](https://pkg.go.dev/builtin#string) `json:"trust_chain_path"`
    }

CertificateConfig represents the options used to set up X.509-based workload credentials. It specifies how to locate and use the client certificate, private key, and optional trust chain for mTLS authentication. This configuration is used within the [CredentialSource] struct.

## CredentialSource
    
    
    type CredentialSource struct {
    	// File is the location for file sourced credentials.
    	// One field amongst File, URL, Executable, Certificate, or EnvironmentID should be
    	// provided, depending on the kind of credential in question.
    	File [string](https://pkg.go.dev/builtin#string)
    	// Url is the URL to call for URL sourced credentials.
    	// One field amongst File, URL, Executable, Certificate, or EnvironmentID should be
    	// provided, depending on the kind of credential in question.
    	URL [string](https://pkg.go.dev/builtin#string)
    	// Executable is the configuration object for executable sourced credentials.
    	// One field amongst File, URL, Executable, Certificate, or EnvironmentID should be
    	// provided, depending on the kind of credential in question.
    	Executable *ExecutableConfig
    	// EnvironmentID is the EnvironmentID used for AWS sourced credentials.
    	// This should start with "AWS".
    	// One field amongst File, URL, Executable, Certificate, or EnvironmentID should be
    	// provided, depending on the kind of credential in question.
    	EnvironmentID [string](https://pkg.go.dev/builtin#string)
    	// Certificate is the configuration object for certificate sourced credentials.
    	// One field amongst File, URL, Executable, Certificate, or EnvironmentID should be
    	// provided, depending on the kind of credential in question.
    	Certificate *CertificateConfig
    
    	// Headers are the headers to attach to the request for URL sourced
    	// credentials.
    	Headers map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string)
    	// RegionURL is the metadata URL to retrieve the region from for EC2 AWS
    	// credentials.
    	RegionURL [string](https://pkg.go.dev/builtin#string)
    	// RegionalCredVerificationURL is the AWS regional credential verification
    	// URL, will default to `https://sts.{region}.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15`
    	// if not provided.
    	RegionalCredVerificationURL [string](https://pkg.go.dev/builtin#string)
    	// IMDSv2SessionTokenURL is the URL to retrieve the session token when using
    	// IMDSv2 in AWS.
    	IMDSv2SessionTokenURL [string](https://pkg.go.dev/builtin#string)
    	// Format is the format type for the subject token. Used for File and URL
    	// sourced credentials.
    	Format *Format
    }

CredentialSource stores the information necessary to retrieve the credentials for the STS exchange.

## ExecutableConfig
    
    
    type ExecutableConfig struct {
    	// Command is the the full command to run to retrieve the subject token.
    	// This can include arguments. Must be an absolute path for the program. Required.
    	Command [string](https://pkg.go.dev/builtin#string)
    	// TimeoutMillis is the timeout duration, in milliseconds. Defaults to 30000 milliseconds when not provided. Optional.
    	TimeoutMillis [int](https://pkg.go.dev/builtin#int)
    	// OutputFile is the absolute path to the output file where the executable will cache the response.
    	// If specified the auth libraries will first check this location before running the executable. Optional.
    	OutputFile [string](https://pkg.go.dev/builtin#string)
    }

ExecutableConfig contains information needed for executable sourced credentials.

## Format
    
    
    type Format struct {
    	// Type should be either "text" or "json". This determines whether the file
    	// or URL sourced credentials expect a simple text subject token or if the
    	// subject token will be contained in a JSON object. When not provided
    	// "text" type is assumed.
    	Type [string](https://pkg.go.dev/builtin#string)
    	// SubjectTokenFieldName is only required for JSON format. This is the field
    	// name that the credentials will check for the subject token in the file or
    	// URL response. This would be "access_token" for azure.
    	SubjectTokenFieldName [string](https://pkg.go.dev/builtin#string)
    }

Format contains information needed to retrieve a subject token for URL or File sourced credentials.

## Options
    
    
    type Options struct {
    	// Audience is the Secure Token Service (STS) audience which contains the
    	// resource name for the workload identity pool or the workforce pool and
    	// the provider identifier in that pool. Required.
    	Audience [string](https://pkg.go.dev/builtin#string)
    	// SubjectTokenType is the STS token type based on the Oauth2.0 token
    	// exchange spec. Expected values include:
    	// - “urn:ietf:params:oauth:token-type:jwt”
    	// - “urn:ietf:params:oauth:token-type:id-token”
    	// - “urn:ietf:params:oauth:token-type:saml2”
    	// - “urn:ietf:params:aws:token-type:aws4_request”
    	// Required.
    	SubjectTokenType [string](https://pkg.go.dev/builtin#string)
    	// TokenURL is the STS token exchange endpoint. If not provided, will
    	// default to https://sts.UNIVERSE_DOMAIN/v1/token, with UNIVERSE_DOMAIN set
    	// to the default service domain googleapis.com unless UniverseDomain is
    	// set. Optional.
    	TokenURL [string](https://pkg.go.dev/builtin#string)
    	// TokenInfoURL is the token_info endpoint used to retrieve the account
    	// related information (user attributes like account identifier, eg. email,
    	// username, uid, etc). This is needed for gCloud session account
    	// identification. Optional.
    	TokenInfoURL [string](https://pkg.go.dev/builtin#string)
    	// ServiceAccountImpersonationURL is the URL for the service account
    	// impersonation request. This is only required for workload identity pools
    	// when APIs to be accessed have not integrated with UberMint.
    	ServiceAccountImpersonationURL [string](https://pkg.go.dev/builtin#string)
    	// ServiceAccountImpersonationLifetimeSeconds is the number of seconds the
    	// service account impersonation token will be valid for.
    	ServiceAccountImpersonationLifetimeSeconds [int](https://pkg.go.dev/builtin#int)
    	// ClientSecret is currently only required if token_info endpoint also
    	// needs to be called with the generated GCP access token. When provided,
    	// STS will be called with additional basic authentication using client_id
    	// as username and client_secret as password. Optional.
    	ClientSecret [string](https://pkg.go.dev/builtin#string)
    	// ClientID is only required in conjunction with ClientSecret, as described
    	// above. Optional.
    	ClientID [string](https://pkg.go.dev/builtin#string)
    	// CredentialSource contains the necessary information to retrieve the token
    	// itself, as well as some environmental information. Optional.
    	CredentialSource *CredentialSource
    	// QuotaProjectID is injected by gCloud. If the value is non-empty, the Auth
    	// libraries will set the x-goog-user-project which overrides the project
    	// associated with the credentials. Optional.
    	QuotaProjectID [string](https://pkg.go.dev/builtin#string)
    	// Scopes contains the desired scopes for the returned access token.
    	// Optional.
    	Scopes [][string](https://pkg.go.dev/builtin#string)
    	// WorkforcePoolUserProject should be set when it is a workforce pool and
    	// not a workload identity pool. The underlying principal must still have
    	// serviceusage.services.use IAM permission to use the project for
    	// billing/quota. Optional.
    	WorkforcePoolUserProject [string](https://pkg.go.dev/builtin#string)
    	// UniverseDomain is the default service domain for a given Cloud universe.
    	// This value will be used in the default STS token URL. The default value
    	// is "googleapis.com". It will not be used if TokenURL is set. Optional.
    	UniverseDomain [string](https://pkg.go.dev/builtin#string)
    	// SubjectTokenProvider is an optional token provider for OIDC/SAML
    	// credentials. One of SubjectTokenProvider, AWSSecurityCredentialProvider
    	// or CredentialSource must be provided. Optional.
    	SubjectTokenProvider SubjectTokenProvider
    	// AwsSecurityCredentialsProvider is an AWS Security Credential provider
    	// for AWS credentials. One of SubjectTokenProvider,
    	// AWSSecurityCredentialProvider or CredentialSource must be provided. Optional.
    	AwsSecurityCredentialsProvider AwsSecurityCredentialsProvider
    
    	// Client configures the underlying client used to make network requests
    	// when fetching tokens. Optional.
    	Client *http.Client
    	// Logger is used for debug logging. If provided, logging will be enabled
    	// at the loggers configured level. By default logging is disabled unless
    	// enabled by setting GOOGLE_SDK_GO_LOGGING_LEVEL in which case a default
    	// logger will be used. Optional.
    	Logger *slog.Logger
    }

Options for creating a [cloud.google.com/go/auth.Credentials].

## RequestOptions
    
    
    type RequestOptions struct {
    	// Audience is the requested audience for the external account credential.
    	Audience [string](https://pkg.go.dev/builtin#string)
    	// Subject token type is the requested subject token type for the external
    	// account credential. Expected values include:
    	// “urn:ietf:params:oauth:token-type:jwt”
    	// “urn:ietf:params:oauth:token-type:id-token”
    	// “urn:ietf:params:oauth:token-type:saml2”
    	// “urn:ietf:params:aws:token-type:aws4_request”
    	SubjectTokenType [string](https://pkg.go.dev/builtin#string)
    }

RequestOptions contains information about the requested subject token or AWS security credentials from the Google external account credential.

## SubjectTokenProvider
    
    
    type SubjectTokenProvider interface {
    	// SubjectToken should return a valid subject token or an error.
    	// The external account token provider does not cache the returned subject
    	// token, so caching logic should be implemented in the provider to prevent
    	// multiple requests for the same subject token.
    	SubjectToken(ctx context.Context, opts *RequestOptions) ([string](https://pkg.go.dev/builtin#string), [error](https://pkg.go.dev/builtin#error))
    }

SubjectTokenProvider can be used to supply a subject token to exchange for a GCP access token.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
