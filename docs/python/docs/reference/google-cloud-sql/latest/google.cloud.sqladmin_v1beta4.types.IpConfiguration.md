---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.IpConfiguration
title: Class IpConfiguration (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:24.032699+00:00
---

# Class IpConfiguration (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.IpConfiguration

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IpConfiguration (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    IpConfiguration(mapping=None, *, ignore_unknown_fields=False, **kwargs)

IP Management configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`ipv4_enabled` |  `google.protobuf.wrappers_pb2.BoolValue`   
Whether the instance is assigned a public IP address or not.   
`private_network` |  `str`   
The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, `/projects/myProject/global/networks/default`. This setting can be updated, but it cannot be removed after it is set.   
`require_ssl` |  `google.protobuf.wrappers_pb2.BoolValue`   
Use `ssl_mode` instead. Whether SSL/TLS connections over IP are enforced. If set to false, then allow both non-SSL/non-TLS and SSL/TLS connections. For SSL/TLS connections, the client certificate won't be verified. If set to true, then only allow connections encrypted with SSL/TLS and with valid client certificates. If you want to enforce SSL/TLS without enforcing the requirement for valid client certificates, then use the `ssl_mode` flag instead of the legacy `require_ssl` flag.   
`authorized_networks` |  `MutableSequence[[google.cloud.sqladmin_v1beta4.types.AclEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.AclEntry)]`   
The list of external networks that are allowed to connect to the instance using the IP. In 'CIDR' notation, also known as 'slash' notation (for example: `157.197.200.0/24`).   
`allocated_ip_range` |  `str`   
The name of the allocated ip range for the private ip Cloud SQL instance. For example: "google-managed-services-default". If set, the instance ip will be created in the allocated range. The range name must comply with `RFC 1035   
`enable_private_path_for_google_cloud_services` |  `google.protobuf.wrappers_pb2.BoolValue`   
Controls connectivity to private IP instances from Google services, such as BigQuery.   
`ssl_mode` |  `[google.cloud.sqladmin_v1beta4.types.IpConfiguration.SslMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.IpConfiguration.SslMode)`   
Specify how SSL/TLS is enforced in database connections. If you must use the `require_ssl` flag for backward compatibility, then only the following value pairs are valid: For PostgreSQL and MySQL: \- `ssl_mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `require_ssl=false` \- `ssl_mode=ENCRYPTED_ONLY` and `require_ssl=false` \- `ssl_mode=TRUSTED_CLIENT_CERTIFICATE_REQUIRED` and `require_ssl=true` For SQL Server: \- `ssl_mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `require_ssl=false` \- `ssl_mode=ENCRYPTED_ONLY` and `require_ssl=true` The value of `ssl_mode` has priority over the value of `require_ssl`. For example, for the pair `ssl_mode=ENCRYPTED_ONLY` and `require_ssl=false`, `ssl_mode=ENCRYPTED_ONLY` means accept only SSL connections, while `require_ssl=false` means accept both non-SSL and SSL connections. In this case, MySQL and PostgreSQL databases respect `ssl_mode` and accepts only SSL connections.   
`psc_config` |  `[google.cloud.sqladmin_v1beta4.types.PscConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.PscConfig)`   
PSC settings for this instance. This field is a member of `oneof`_ `_psc_config`.   
`server_ca_mode` |  `[google.cloud.sqladmin_v1beta4.types.IpConfiguration.CaMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.IpConfiguration.CaMode)`   
Specify what type of CA is used for the server certificate. This field is a member of `oneof`_ `_server_ca_mode`.   
`custom_subject_alternative_names` |  `MutableSequence[str]`   
Optional. Custom Subject Alternative Name(SAN)s for a Cloud SQL instance.   
`server_ca_pool` |  `str`   
Optional. The resource name of the server CA pool for an instance with `CUSTOMER_MANAGED_CAS_CA` as the `server_ca_mode`. Format: projects/{PROJECT}/locations/{REGION}/caPools/{CA_POOL_ID} This field is a member of `oneof`_ `_server_ca_pool`.   
`server_certificate_rotation_mode` |  `[google.cloud.sqladmin_v1beta4.types.IpConfiguration.ServerCertificateRotationMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.IpConfiguration.ServerCertificateRotationMode)`   
Optional. Controls the automatic server certificate rotation feature. This feature is disabled by default. When enabled, the server certificate will be automatically rotated during Cloud SQL scheduled maintenance or self-service maintenance updates up to six months before it expires. This setting can only be set if server_ca_mode is either GOOGLE_MANAGED_CAS_CA or CUSTOMER_MANAGED_CAS_CA. This field is a member of `oneof`_ `_server_certificate_rotation_mode`.   
  
## Classes 

### CaMode
    
    
    CaMode(value)

Various Certificate Authority (CA) modes for certificate signing.

### ServerCertificateRotationMode
    
    
    ServerCertificateRotationMode(value)

Settings for automatic server certificate rotation.

### SslMode
    
    
    SslMode(value)

The SSL options for database connections.
    
    
        When this value is used, the legacy `require_ssl` flag
        must be false or cleared to avoid a conflict between the
        values of the two flags.
    ENCRYPTED_ONLY (2):
        Only allow connections encrypted with SSL/TLS. For SSL
        connections to MySQL and PostgreSQL, the client certificate
        isn't verified.
    
        When this value is used, the legacy `require_ssl` flag
        must be false or cleared to avoid a conflict between the
        values of the two flags.
    TRUSTED_CLIENT_CERTIFICATE_REQUIRED (3):
        Only allow connections encrypted with SSL/TLS and with valid
        client certificates.
    
        When this value is used, the legacy `require_ssl` flag
        must be true or cleared to avoid the conflict between values
        of two flags. PostgreSQL clients or users that connect using
        IAM database authentication must use either the `Cloud SQL
        Auth
        Proxy <https://cloud.google.com/sql/docs/postgres/connect-auth-proxy>`__
        or `Cloud SQL
        Connectors <https://cloud.google.com/sql/docs/postgres/connect-connectors>`__
        to enforce client identity verification.
    
        Only applicable to MySQL and PostgreSQL. Not applicable to
        SQL Server.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
