---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1
title: Package com.google.cloud.domains.v1beta1 (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:24.083705+00:00
---

# Package com.google.cloud.domains.v1beta1 (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.domains.v1beta1 (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.85.0  1.84.0  1.82.0  1.80.0  1.79.0  1.78.0  1.77.0  1.75.0  1.73.0  1.72.0  1.71.0  1.70.0  1.69.0  1.67.0  1.65.0  1.64.0  1.61.0  1.60.0  1.59.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.6  0.7.0  0.6.1  0.5.4 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-domains/google-cloud-domains/src/main/java/com/google/cloud/domains/v1beta1)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.domains.v1](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1) for new applications.

## Prerelease Implications

This package is a prerelease version! Use with caution.

Prerelease versions are considered unstable as they may be shut down and/or subject to breaking changes when upgrading. Use them only for testing or if you specifically need their experimental features.

## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.cloud.domains.v1beta1.DomainsClient](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient) |  Service Description: The Cloud Domains API enables management and configuration of domain names. This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.domains.v1beta1.ContactSettings](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings) |  Defines the contact information associated with a `Registration`. [ICANN](https://icann.org/) requires all domain names to have associated  
[com.google.cloud.domains.v1beta1.DnsSettings](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings) |  Defines the DNS configuration of a `Registration`, including name servers, DNSSEC, and glue records.   
[com.google.cloud.domains.v1beta1.DomainsSettings](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsSettings) |  Settings class to configure an instance of DomainsClient. The default instance has everything set to sensible defaults:   
[com.google.cloud.domains.v1beta1.ManagementSettings](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ManagementSettings) |  Defines renewal, billing, and transfer settings for a `Registration`.  
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.domains.v1beta1.AuthorizationCode](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode) |  Defines an authorization code.   
[com.google.cloud.domains.v1beta1.AuthorizationCode.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCode.Builder) |  Defines an authorization code.   
[com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest) |  Request for the `ConfigureContactSettings` method.   
[com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequest.Builder) |  Request for the `ConfigureContactSettings` method.   
[com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest) |  Request for the `ConfigureDnsSettings` method.   
[com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequest.Builder) |  Request for the `ConfigureDnsSettings` method.   
[com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest) |  Request for the `ConfigureManagementSettings` method.   
[com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequest.Builder) |  Request for the `ConfigureManagementSettings` method.   
[com.google.cloud.domains.v1beta1.ContactSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings.Builder) |  Defines the contact information associated with a `Registration`. [ICANN](https://icann.org/) requires all domain names to have associated  
[com.google.cloud.domains.v1beta1.ContactSettings.Contact](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings.Contact) |  Details required for a contact associated with a `Registration`.   
[com.google.cloud.domains.v1beta1.ContactSettings.Contact.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings.Contact.Builder) |  Details required for a contact associated with a `Registration`.   
[com.google.cloud.domains.v1beta1.DeleteRegistrationRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequest) |  Request for the `DeleteRegistration` method.   
[com.google.cloud.domains.v1beta1.DeleteRegistrationRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequest.Builder) |  Request for the `DeleteRegistration` method.   
[com.google.cloud.domains.v1beta1.DnsSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.Builder) |  Defines the DNS configuration of a `Registration`, including name servers, DNSSEC, and glue records.   
[com.google.cloud.domains.v1beta1.DnsSettings.CustomDns](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.CustomDns) |  Configuration for an arbitrary DNS provider.   
[com.google.cloud.domains.v1beta1.DnsSettings.CustomDns.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.CustomDns.Builder) |  Configuration for an arbitrary DNS provider.   
[com.google.cloud.domains.v1beta1.DnsSettings.DsRecord](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DsRecord) |  Defines a Delegation Signer (DS) record, which is needed to enable DNSSEC for a domain. It contains a digest (hash) of a DNSKEY record that must be present in the domain's DNS zone.  
[com.google.cloud.domains.v1beta1.DnsSettings.DsRecord.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DsRecord.Builder) |  Defines a Delegation Signer (DS) record, which is needed to enable DNSSEC for a domain. It contains a digest (hash) of a DNSKEY record that must be present in the domain's DNS zone.  
[com.google.cloud.domains.v1beta1.DnsSettings.GlueRecord](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.GlueRecord) |  Defines a host on your domain that is a DNS name server for your domain and/or other domains. Glue records are a way of making the IP address of a name server known, even when it serves DNS queries for its parent domain.  
[com.google.cloud.domains.v1beta1.DnsSettings.GlueRecord.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.GlueRecord.Builder) |  Defines a host on your domain that is a DNS name server for your domain and/or other domains. Glue records are a way of making the IP address of a name server known, even when it serves DNS queries for its parent domain.  
[com.google.cloud.domains.v1beta1.DnsSettings.GoogleDomainsDns](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.GoogleDomainsDns) |  Configuration for using the free DNS zone provided by Google Domains as a `Registration`'s `dns_provider`. You cannot configure the DNS zone itself using the API. To configure the DNS zone, go to  
[com.google.cloud.domains.v1beta1.DnsSettings.GoogleDomainsDns.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.GoogleDomainsDns.Builder) |  Configuration for using the free DNS zone provided by Google Domains as a `Registration`'s `dns_provider`. You cannot configure the DNS zone itself using the API. To configure the DNS zone, go to  
[com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsFixedSizeCollection) |   
[com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPage](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPage) |   
[com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsClient.ListRegistrationsPagedResponse) |   
[com.google.cloud.domains.v1beta1.DomainsGrpc](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsGrpc) |  The Cloud Domains API enables management and configuration of domain names.   
[com.google.cloud.domains.v1beta1.DomainsGrpc.DomainsImplBase](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsGrpc.DomainsImplBase) |  Base class for the server implementation of the service Domains. The Cloud Domains API enables management and configuration of domain names.  
[com.google.cloud.domains.v1beta1.DomainsProto](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsProto) |   
[com.google.cloud.domains.v1beta1.DomainsSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsSettings.Builder) |  Builder for DomainsSettings.  
[com.google.cloud.domains.v1beta1.ExportRegistrationRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequest) |  Request for the `ExportRegistration` method.   
[com.google.cloud.domains.v1beta1.ExportRegistrationRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequest.Builder) |  Request for the `ExportRegistration` method.   
[com.google.cloud.domains.v1beta1.GetRegistrationRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.GetRegistrationRequest) |  Request for the `GetRegistration` method.   
[com.google.cloud.domains.v1beta1.GetRegistrationRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.GetRegistrationRequest.Builder) |  Request for the `GetRegistration` method.   
[com.google.cloud.domains.v1beta1.ListRegistrationsRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequest) |  Request for the `ListRegistrations` method.   
[com.google.cloud.domains.v1beta1.ListRegistrationsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequest.Builder) |  Request for the `ListRegistrations` method.   
[com.google.cloud.domains.v1beta1.ListRegistrationsResponse](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsResponse) |  Response for the `ListRegistrations` method.   
[com.google.cloud.domains.v1beta1.ListRegistrationsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsResponse.Builder) |  Response for the `ListRegistrations` method.   
[com.google.cloud.domains.v1beta1.LocationName](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.LocationName) |   
[com.google.cloud.domains.v1beta1.LocationName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.LocationName.Builder) |  Builder for projects/{project}/locations/{location}.  
[com.google.cloud.domains.v1beta1.ManagementSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ManagementSettings.Builder) |  Defines renewal, billing, and transfer settings for a `Registration`.   
[com.google.cloud.domains.v1beta1.OperationMetadata](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata) |  Represents the metadata of the long-running operation. Output only.   
[com.google.cloud.domains.v1beta1.OperationMetadata.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadata.Builder) |  Represents the metadata of the long-running operation. Output only.   
[com.google.cloud.domains.v1beta1.RegisterDomainRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequest) |  Request for the `RegisterDomain` method.   
[com.google.cloud.domains.v1beta1.RegisterDomainRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequest.Builder) |  Request for the `RegisterDomain` method.   
[com.google.cloud.domains.v1beta1.RegisterParameters](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterParameters) |  Parameters required to register a new domain.   
[com.google.cloud.domains.v1beta1.RegisterParameters.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterParameters.Builder) |  Parameters required to register a new domain.   
[com.google.cloud.domains.v1beta1.Registration](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration) |  The `Registration` resource facilitates managing and configuring domain name registrations.   
[com.google.cloud.domains.v1beta1.Registration.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration.Builder) |  The `Registration` resource facilitates managing and configuring domain name registrations.   
[com.google.cloud.domains.v1beta1.RegistrationName](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegistrationName) |   
[com.google.cloud.domains.v1beta1.RegistrationName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegistrationName.Builder) |  Builder for projects/{project}/locations/{location}/registrations/{registration}.  
[com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest) |  Request for the `ResetAuthorizationCode` method.   
[com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequest.Builder) |  Request for the `ResetAuthorizationCode` method.   
[com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest) |  Request for the `RetrieveAuthorizationCode` method.   
[com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequest.Builder) |  Request for the `RetrieveAuthorizationCode` method.   
[com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest) |  Request for the `RetrieveRegisterParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequest.Builder) |  Request for the `RetrieveRegisterParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse) |  Response for the `RetrieveRegisterParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponse.Builder) |  Response for the `RetrieveRegisterParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest) |  Request for the `RetrieveTransferParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequest.Builder) |  Request for the `RetrieveTransferParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse) |  Response for the `RetrieveTransferParameters` method.   
[com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponse.Builder) |  Response for the `RetrieveTransferParameters` method.   
[com.google.cloud.domains.v1beta1.SearchDomainsRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsRequest) |  Request for the `SearchDomains` method.   
[com.google.cloud.domains.v1beta1.SearchDomainsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsRequest.Builder) |  Request for the `SearchDomains` method.   
[com.google.cloud.domains.v1beta1.SearchDomainsResponse](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse) |  Response for the `SearchDomains` method.   
[com.google.cloud.domains.v1beta1.SearchDomainsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponse.Builder) |  Response for the `SearchDomains` method.   
[com.google.cloud.domains.v1beta1.TransferDomainRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequest) |  Request for the `TransferDomain` method.   
[com.google.cloud.domains.v1beta1.TransferDomainRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequest.Builder) |  Request for the `TransferDomain` method.   
[com.google.cloud.domains.v1beta1.TransferParameters](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferParameters) |  Parameters required to transfer a domain from another registrar.   
[com.google.cloud.domains.v1beta1.TransferParameters.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferParameters.Builder) |  Parameters required to transfer a domain from another registrar.   
[com.google.cloud.domains.v1beta1.UpdateRegistrationRequest](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequest) |  Request for the `UpdateRegistration` method.   
[com.google.cloud.domains.v1beta1.UpdateRegistrationRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequest.Builder) |  Request for the `UpdateRegistration` method.   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.domains.v1beta1.AuthorizationCodeOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.AuthorizationCodeOrBuilder) |   
[com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureContactSettingsRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureDnsSettingsRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ConfigureManagementSettingsRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.ContactSettings.ContactOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettings.ContactOrBuilder) |   
[com.google.cloud.domains.v1beta1.ContactSettingsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactSettingsOrBuilder) |   
[com.google.cloud.domains.v1beta1.DeleteRegistrationRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DeleteRegistrationRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.DnsSettings.CustomDnsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.CustomDnsOrBuilder) |   
[com.google.cloud.domains.v1beta1.DnsSettings.DsRecordOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DsRecordOrBuilder) |   
[com.google.cloud.domains.v1beta1.DnsSettings.GlueRecordOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.GlueRecordOrBuilder) |   
[com.google.cloud.domains.v1beta1.DnsSettings.GoogleDomainsDnsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.GoogleDomainsDnsOrBuilder) |   
[com.google.cloud.domains.v1beta1.DnsSettingsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettingsOrBuilder) |   
[com.google.cloud.domains.v1beta1.DomainsGrpc.AsyncService](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainsGrpc.AsyncService) |  The Cloud Domains API enables management and configuration of domain names.   
[com.google.cloud.domains.v1beta1.ExportRegistrationRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ExportRegistrationRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.GetRegistrationRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.GetRegistrationRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.ListRegistrationsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.ListRegistrationsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ListRegistrationsResponseOrBuilder) |   
[com.google.cloud.domains.v1beta1.ManagementSettingsOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ManagementSettingsOrBuilder) |   
[com.google.cloud.domains.v1beta1.OperationMetadataOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.OperationMetadataOrBuilder) |   
[com.google.cloud.domains.v1beta1.RegisterDomainRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterDomainRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.RegisterParametersOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterParametersOrBuilder) |   
[com.google.cloud.domains.v1beta1.RegistrationOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegistrationOrBuilder) |   
[com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ResetAuthorizationCodeRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveAuthorizationCodeRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveRegisterParametersResponseOrBuilder) |   
[com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RetrieveTransferParametersResponseOrBuilder) |   
[com.google.cloud.domains.v1beta1.SearchDomainsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.SearchDomainsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.SearchDomainsResponseOrBuilder) |   
[com.google.cloud.domains.v1beta1.TransferDomainRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferDomainRequestOrBuilder) |   
[com.google.cloud.domains.v1beta1.TransferParametersOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferParametersOrBuilder) |   
[com.google.cloud.domains.v1beta1.UpdateRegistrationRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.UpdateRegistrationRequestOrBuilder) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.domains.v1beta1.ContactNotice](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactNotice) |  Notices related to contact information.   
[com.google.cloud.domains.v1beta1.ContactPrivacy](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ContactPrivacy) |  Defines a set of possible contact privacy settings for a `Registration`. [ICANN](https://icann.org/) maintains the WHOIS database, a publicly  
[com.google.cloud.domains.v1beta1.DnsSettings.DnsProviderCase](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DnsProviderCase) |   
[com.google.cloud.domains.v1beta1.DnsSettings.DsRecord.Algorithm](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DsRecord.Algorithm) |  List of algorithms used to create a DNSKEY. Certain algorithms are not supported for particular domains.   
[com.google.cloud.domains.v1beta1.DnsSettings.DsRecord.DigestType](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DsRecord.DigestType) |  List of hash functions that may have been used to generate a digest of a DNSKEY.   
[com.google.cloud.domains.v1beta1.DnsSettings.DsState](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DnsSettings.DsState) |  The publication state of DS records for a `Registration`.   
[com.google.cloud.domains.v1beta1.DomainNotice](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.DomainNotice) |  Notices about special properties of certain domains.   
[com.google.cloud.domains.v1beta1.ManagementSettings.RenewalMethod](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.ManagementSettings.RenewalMethod) |  Defines how the `Registration` is renewed.   
[com.google.cloud.domains.v1beta1.RegisterParameters.Availability](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.RegisterParameters.Availability) |  Possible availability states of a domain name.   
[com.google.cloud.domains.v1beta1.Registration.Issue](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration.Issue) |  Possible issues with a `Registration` that require attention.   
[com.google.cloud.domains.v1beta1.Registration.State](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.Registration.State) |  Possible states of a `Registration`.   
[com.google.cloud.domains.v1beta1.TransferLockState](https://cloud.google.com/java/docs/reference/google-cloud-domains/latest/com.google.cloud.domains.v1beta1.TransferLockState) |  Possible states of a `Registration`'s transfer lock.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
