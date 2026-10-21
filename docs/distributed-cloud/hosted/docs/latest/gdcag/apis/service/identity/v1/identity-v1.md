---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/identity-v1/
title: KRM API iam.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:28.280843+00:00
---

# KRM API iam.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/identity/v1/identity-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API iam.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## iam.gdc.goog/v1

Contains API Schema definitions for the identity API group.

Package v1 contains API Schema definitions for the iam.gdc.goog v1 API group

### ClientAuthConfig

ClientAuthConfig determines the way AIS authenticates itself to the Identity Provider.

_Appears in:_ \- OIDCProviderConfig

Field | Description  
---|---  
`method` _string_ | Type of the ClientAuthentication method. Default method is client_secret_post that sends client_secret in the Token API. Other method supported is private_key_jwt that sends a signed jwt in the Token API. private_key_jwt method requires SigningKey configuration to be valid.  
`signatureAlg` _string_ | Signature Algorithm used to compute the JWT. Only supported algorithm at this point is RS256.  
`signingKey` _ClientAuthSigningKeySecret_ | SigningKey denotes the parameters required to retrieve the key used to sign the JWT. Key is stored as a kubernetes secret.  
  
### ClientAuthSigningKeySecret

ClientAuthSigningKeySecret contains the details of the signing key.

_Appears in:_ \- ClientAuthConfig

Field | Description  
---|---  
`name` _string_ | Name of the secret which stores the SigningKey.  
`namespace` _string_ | Namespace of the secret which stores the SigningKey.  
`kid` _string_ | kid is the unique identifier that represents the signing key. Identity Provider looks up public key corresponding to the kid in order to verify payload.  
  
### CustomRole

Represents a template for a zonal CustomRole Custom roles provide fine-grained control over user permissions, unlike predefined roles. This allows organizations to tailor access rights to their specific needs, balancing operational efficiency with security. By adhering to the principle of least privilege, custom roles significantly enhance security and protect sensitive data.

_Appears in:_ \- CustomRoleList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `CustomRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CustomRoleSpec_ |   
`status` _CustomRoleStatus_ |   
  
### CustomRoleList

Contains a list of `CustomRole` resource

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `CustomRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CustomRole array_ |   
  
### CustomRoleMetadata

Represents the data necessary to create a Custom Role

_Appears in:_ \- CustomRoleSpec

Field | Description  
---|---  
`scope` _CustomRoleScopeType_ | scope of the custom role created which can either be organization or project  
`roleNamespaces` _string array_ | namespace of the role (optional) only required for role deployment if: case 1: when scope is project then it denotes the project namespaces case 2: when scope is project and roleNamespaces contain ['*'] then it denotes all project namespaces case 3: when scope is organization and deployment roleType is role not clusterRole then it denotes literal namespaces  
`title` _string_ | title is a friendly title for the role, such as "My Company Admin".  
`description` _string_ | description is a short description of the role, such as "My custom role description".  
`id` _string_ | id is the name of the role, such as "my-company-admin".  
`stage` _StageType_ | stage indicates the stage of a role in the launch lifecycle which can either be [ALPHA, BETA, GA, DISABLED]  
  
### CustomRoleSpec

Defines the CustomRole data in the `ClusterRoleTemplate` resource

_Appears in:_ \- CustomRole

Field | Description  
---|---  
`metadata` _CustomRoleMetadata_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`zonalRules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ |   
`globalRules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ |   
  
### CustomRoleStatus

Provides a status of CustomRole

_Appears in:_ \- CustomRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this Custom role overall state  
`propagationInfo` _PropagationInfo_ | propagation information of converted template for zonal role template conversion  
  
### DecryptionKeysSecret

DecryptionKeysSecret specifies the namespace, and name of a kubernetes secret that holds the decryption keys for decrypting the encrypted tokens. kid is the unique key identifier for a decryption key that's used by the Provider to let the token recipient know which decryption key needs to be used for decrypting the token(s).

_Appears in:_ \- EncryptedTokensConfig

Field | Description  
---|---  
`name` _string_ | Kubernetes Name of the secret.  
`namespace` _string_ | Kubernetes NameSpace of the secret.  
`kid` _string_ | kid is the unique key identifier that represents a decryption key.  
  
### EncryptedAssertionConfig

EncryptedAssertionConfig provides configuration for the SAML assertion encryption feature.

_Appears in:_ \- SAMLProviderConfig

Field | Description  
---|---  
`enabled` _boolean_ | Specifies if SAML assertions must be decrypted before being parsed. The assertion decryption feature is only enabled when this is set to true.  
`decryptionKeys` _KubernetesSecretConfig array_ | Kubernetes secret where the Assertion encryption certificate, and the assertion decryption key are stored. This secret needs to be of type TLS. (see: https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets).  
  
### EncryptedTokensConfig

EncryptedTokensConfig provides configuration for the OIDC token encryption feature.

_Appears in:_ \- OIDCProviderConfig

Field | Description  
---|---  
`enabled` _boolean_ | Specifies if OIDC token(s) must be decrypted before being parsed. The token decryption feature is only enabled when this field is set to true.  
`decryptionKeys` _DecryptionKeysSecret array_ | Kubernetes secret where the token decryption key(s) is/are stored.  
  
### IdentityProviderConfig

Represents a configuration for an identity provider that supports OIDC or SAML.

_Appears in:_ \- IdentityProviderConfigList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfig`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _IdentityProviderConfigSpec_ |   
`status` _IdentityProviderConfigStatus_ |   
  
### IdentityProviderConfigList

Contains a list of `IdentityProviderConfig` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfigList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _IdentityProviderConfig array_ |   
  
### IdentityProviderConfigSpec

Provides the specification, or desired state, of an `IdentityProviderConfig` resource. Either OIDCConfig or SAMLConfig has to be provided but not both.

_Appears in:_ \- IdentityProviderConfig

Field | Description  
---|---  
`oidc` _OIDCProviderConfig_ | OIDC specific configuration.  
`saml` _SAMLProviderConfig_ | SAML specific configuration.  
  
### IdentityProviderConfigStatus

Provides the status of an `IdentityProviderConfig` resource.

_Appears in:_ \- IdentityProviderConfig

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### KubernetesSecretConfig

KubernetesSecretConfig specifies the namespace, and name of a kubernetes secret.

_Appears in:_ \- EncryptedAssertionConfig \- SignedRequestConfig

Field | Description  
---|---  
`name` _string_ | Kubernetes Name of the secret.  
`namespace` _string_ | Kubernetes NameSpace of the secret.  
  
### OIDCProviderConfig

OIDCProviderConfig contains parameters needed for OIDC Authentication flow.

_Appears in:_ \- IdentityProviderConfigSpec

Field | Description  
---|---  
`clientID` _string_ | ClientID is an ID for OIDC client application.  
`clientSecret` _string_ | ClientSecret is the shared secret between OIDC client application and OIDC provider.  
`certificateAuthorityData` _string_ | CertificateAuthorityData contains a standard Base64 encoded, PEM formatted certificate authority certificate for OIDC provider.  
`issuerURI` _string_ | URI for the OIDC provider. This URI is the prefix of "/.well-known/openid-configuration". For example, if the IDP's well-known configuration endpoint is "https://{oauth-provider-hostname}/.well-known/openid-configuration", then the Issuer URI is "https://{oauth-provider-hostname}".  
`kubectlRedirectURI` _string_ | KubectlRedirectURI is the URI to redirect users authenticating to an OIDC provider with the kubectl plugin.  
`cloudConsoleRedirectURI` _string_ | CloudConsoleRedirectURI is the URI to redirect users going through the OAuth flow using cloud console.  
`scopes` _string_ | Comma-separated list of identifiers used to specify what access privileges are being requested in addition to "openid" scope.  
`extraParams` _string_ | Comma-separated list of key-value pairs that will be query-encoded and sent with the authentication endpoint request.  
`enableAccessToken` _boolean_ | Flag that denotes if the access-token should be included in the request as part of the bearer token by `gcloud anthos auth login` and `kubectl oidc login`. Defaults to false.  
`userClaim` _string_ | Name of the claim in the OIDC ID Token that holds the username. If this is missing from the ID Token, authentication will fail.  
`userPrefix` _string_ | Prefix to prepend to the user name.  
`groupsClaim` _string_ | Name of the claim in the OIDC ID Token that holds the user's groups information.  
`groupPrefix` _string_ | Prefix to prepend to the group name.  
`deployCloudConsoleProxy` _boolean_ | Flag to denote if HTTP reverse proxy is used for connecting to authentication provider. This should be set to true when authentication provider is not reachable by Google Cloud Console.  
`attributeMapping` _object (keys:string, values:string)_ | Optional Common Expression Language (CEL) for mapping user attributes from the identity provider to the web application.  
`clientAuthParams` _ClientAuthConfig_ | Optional ClientAuth params define the way AIS authenticates itself while sending the Token API. Currently used during authorization code flow.  
`encryptedTokens` _EncryptedTokensConfig_ | Optional configuration for the OIDC encrypted token feature.  
  
### PropagationInfo

Provides the information of converted role template

_Appears in:_ \- CustomRoleStatus

Field | Description  
---|---  
`roleName` _string_ | name of the role  
`roleType` _RoleType_ | type of the role, it can be [role, clusterRole, projectRole, organizationRole]  
`namespaces` _string array_ | namespaces of the role where role deployment will occur  
  
### SAMLProviderConfig

SAMLProviderConfig contains parameters needed for SAML Authentication flow.

_Appears in:_ \- IdentityProviderConfigSpec

Field | Description  
---|---  
`idpEntityID` _string_ | The SAML entity ID for the SAML provider, specified in a URI format. For example: https://www.idp.com/saml.  
`idpSingleSignOnURI` _string_ | The URI to the SAML provider's SSO endpoint. For example: https://www.idp.com/saml/sso.  
`idpCertificateDataList` _string array_ | The IDP certificates that will be used to verify the SAML response. These certificates should be standard Base64 encoded, and PEM formatted. Only a maximum of 2 certificates are supported to facilitate IDP certificate rotation.  
`userAttribute` _string_ | Name of the attribute in the SAML response that holds the username. If this attribute is missing from the SAML response, authentication will fail.  
`userPrefix` _string_ | Optional prefix to prepend to the user name.  
`groupsAttribute` _string_ | Name of the attribute in the SAML response that holds the user's groups.  
`groupPrefix` _string_ | Optional prefix to prepend to each group name.  
`attributeMapping` _object (keys:string, values:string)_ | Optional Common Expression Language (CEL) for mapping user attributes from the identity provider to the web application.  
`encryptedAssertions` _EncryptedAssertionConfig_ | Optional configuration for the SAML encrypted assertion feature.  
`signedRequests` _SignedRequestConfig_ | Optional configuration for the SAML authentication request signing feature.  
  
### SignedRequestConfig

SignedRequestConfig provides configuration for the SAML authentication request signing feature.

_Appears in:_ \- SAMLProviderConfig

Field | Description  
---|---  
`enabled` _boolean_ | Specifies if SAML authentication request must be signed. The signed request feature is only enabled when this is set to true.  
`signingKey` _KubernetesSecretConfig_ | Kubernetes secret where the SAML request signing certificate key pair is stored. This secret needs to be of type TLS. (see: https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets).  
  
### StandardClusterRole

Represents a project resource that propagates the `ClusterRole` configuration to all vanilla clusters under the project. The namespace of the `StandardClusterRole` resource corresponds to the project.

_Appears in:_ \- StandardClusterRoleList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `StandardClusterRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _StandardClusterRoleSpec_ |   
`status` _StandardClusterRoleStatus_ |   
  
### StandardClusterRoleBinding

Represents a project resource that propagates the `ClusterRoleBinding` resource configuration to all vanilla clusters in the same project. The namespace for the `StandardClusterRoleBinding` resource corresponds to the project.

_Appears in:_ \- StandardClusterRoleBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `StandardClusterRoleBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _StandardClusterRoleBindingSpec_ |   
`status` _StandardClusterRoleBindingStatus_ |   
  
### StandardClusterRoleBindingList

Contains a list of `StandardClusterRoleBinding` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `StandardClusterRoleBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _StandardClusterRoleBinding array_ |   
  
### StandardClusterRoleBindingSpec

Defines the specification of the `StandardClusterRoleBinding` resource. It is the same definition as a native `ClusterRoleBinding` definition.

_Appears in:_ \- StandardClusterRoleBinding

Field | Description  
---|---  
`subjects` _[Subject](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#subject-v1-rbac) array_ | The subjects of the `RoleBinding` resource created in the cluster.  
`roleRef` _[RoleRef](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#roleref-v1-rbac)_ | The `RoleRef` resource of the `RoleBinding` object to create in the cluster.  
  
### StandardClusterRoleBindingStatus

Defines the observed state of the `StandardClusterRoleBinding` resource.

_Appears in:_ \- StandardClusterRoleBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`clusters` _ClusterStatus array_ | The list of propagation statuses for the clusters.  
`propagatedName` _string_ | The name of the propagated `ClusterRoleBinding` resource realized in the vanilla clusters.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
### StandardClusterRoleList

Contains a list of `StandardClusterRole` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `StandardClusterRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _StandardClusterRole array_ |   
  
### StandardClusterRoleSpec

Defines the rules of a `StandardClusterRole` resource. It is the same definition as a native Kubernetes `ClusterRole`.

_Appears in:_ \- StandardClusterRole

Field | Description  
---|---  
`rules` _[PolicyRule](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#policyrule-v1-rbac) array_ |   
  
### StandardClusterRoleStatus

Defines the observed state of a `StandardClusterRole` resource.

_Appears in:_ \- StandardClusterRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
`clusters` _ClusterStatus array_ | The list of propagation statuses on the clusters.  
`propagatedName` _string_ | The name of the propagated `ClusterRole` resource realized in the vanilla clusters.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
