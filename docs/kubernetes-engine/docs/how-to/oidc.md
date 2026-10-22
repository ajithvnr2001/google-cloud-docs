---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc/
title: Use external identity providers to authenticate to GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:32:03.252082+00:00
---

# Use external identity providers to authenticate to GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Use external identity providers to authenticate to GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to configure authentication to Google Kubernetes Engine (GKE) clusters from external identity providers (IdPs).

This page is intended for Platform admins and operators and Identity and account admins who use an external IdP that supports OpenID Connect (OIDC) or Security Assertion Markup Language (SAML) 2.0.

Before reading this page, ensure that you're familiar with the following authentication and OpenID concepts:

  * [OAuth 2.0](https://oauth.net/2/)
  * [SAML 2.0](https://en.wikipedia.org/wiki/SAML_2.0)
  * [OpenID Connect](https://openid.net/connect/)
  * [OIDC scopes and claims](https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims)
  * [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)



## External IdP authentication methods in GKE

Recommended — Workforce Identity Federation

Workforce Identity Federation is an IAM feature that lets you authenticate to Google Cloud from any external IdP that supports OIDC or SAML 2.0. Workforce Identity Federation doesn't require any in-cluster installation, works with Autopilot clusters and Standard clusters, and is built into Google Cloud. For details, see the IAM documentation about [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

Not recommended — Identity Service for GKE (deprecated)

**Caution:** Starting on July 1, 2026, Identity Service for GKE is deprecated and is unsupported in GKE version 1.37 and later. For more information, see [Identity Service for GKE deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service).

In GKE Standard clusters only, GKE also supports Identity Service for GKE. Identity Service for GKE is limited to OIDC IdPs and installs additional components in your cluster. GKE strongly recommends using Workforce Identity Federation instead of Identity Service for GKE. Also note a known limitation with Identity Service for GKE that prevents autoscaling.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Considerations

Headless systems are unsupported with both Workforce Identity Federation and Identity Service for GKE. A browser-based authentication flow prompts you for consent and to authorize your user account.

## Use Workforce Identity Federation in GKE

To use Workforce Identity Federation in your GKE clusters, do the following:

  1. Set up Workforce Identity Federation for your organization and external IdP. For instructions, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).
  2. Set up access from your external IdP to the Google Cloud Workforce Identity Federation console. For details, see [Set up user access to the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso#inform-users).
  3. Configure user access by using one the following authorization mechanisms:

     * Kubernetes RBAC
     * [IAM allow policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#grant-iam-roles)
  4. Tell your users to access clusters by completing the following steps:

     1. [Sign in to the gcloud CLI with the federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).
     2. Configure kubectl to authenticate to a specific cluster by running [`gcloud container clusters get-credentials`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials).



### Configure user access to clusters using RBAC

Google Cloud uses _principal identifiers_ to identify users in your workforce identity pools. You can refer to these principal identifiers in your Kubernetes RBAC policies or in IAM policies to give permissions to individuals or to groups of users. With RBAC, you can't reference any other custom assertions that your IdP tokens contain. RBAC supports principal identifiers only for users and groups.

The following table shows example principal identifiers for single users and for groups:

Identity | Principal identifier  
---|---  
Single user | 
    
    
    principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_IDENTITY_POOL/subject/SUBJECT_ATTRIBUTE_VALUE

Replace the following:

  * `WORKFORCE_IDENTITY_POOL`: the name of the workforce identity pool.
  * `SUBJECT_ATTRIBUTE_VALUE`: the value of an attribute in the subject assertion of the identity token. For example, this might be the value of the `NameID` field in a SAML 2.0 assertion.

For example:
    
    
    principal://iam.googleapis.com/locations/global/workforcePools/full-time-employees/subject/amal@example.com  
  
All users in a group | 
    
    
    principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_IDENTITY_POOL/group/GROUP_NAME

Replace the following:

  * `WORKFORCE_IDENTITY_POOL`: the name of the workforce identity pool.
  * `GROUP_NAME`: the name of a group in which the authenticating user is a member. The assertion in your IdP token must have an [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) to the Google Cloud `google.groups` attribute.

For example:
    
    
    principalSet://iam.googleapis.com/locations/global/workforcePools/full-time-employees/group/sre  
  
For every principal identifier that Workforce Identity Federation supports, see [Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).

The following example shows you how to give cluster-wide read-only access on Secrets to any entities in the `full-time-employees` workforce pool that are part of the group `sre` in their IdP token.

  1. Save the following ClusterRole manifest as `secret-viewer-cluster-role.yaml`:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: secret-viewer
         rules:
         - apiGroups: [""]
           resources: ["secrets"]
           verbs: ["get", "watch", "list"]
         

Any principal to which you bind this ClusterRole can view Secrets.

  2. Save the following ClusterRoleBinding manifest as `secret-viewer-cluster-role-binding.yaml`:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name:  users-view-secrets
         subjects:
         - kind: Group
           name: principalSet://iam.googleapis.com/locations/global/workforcePools/full-time-employees/group/sre
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: ClusterRole
           name: secret-viewer
           apiGroup: rbac.authorization.k8s.io
         

This ClusterRoleBinding grants the `secret-viewer` ClusterRole to any user who is part of the group `sre`.

  3. Deploy the ClusterRole and the ClusterRoleBinding:
         
         kubectl apply -f secret-viewer-cluster-role.yaml
         kubectl apply -f secret-viewer-cluster-role-binding.yaml
         




### Sign in and authenticate to the cluster

  1. Have the user [sign in using the Google Cloud CLI](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#access-token).
  2. The user can configure kubectl to authenticate to the cluster by using the following:
         
         gcloud container clusters get-credentials
         




## Use Identity Service for GKE

**Caution:** Starting on July 1, 2026, Identity Service for GKE is deprecated and is unsupported in GKE version 1.37 and later. Use Workforce Identity Federation instead. For more information, see [Identity Service for GKE deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service).

To set up and use Identity Service for GKE on your GKE Standard mode cluster, **cluster administrators** do the following:

  1. Enable Identity Service for GKE on a cluster.
  2. Configure Identity Service for GKE.
  3. Create an RBAC policy for your cluster.



After cluster administrators configure Identity Service for GKE, **developers** can log in and authenticate to the cluster.

### Kubernetes objects created by Identity Service for GKE

The following table describes the Kubernetes objects created when you enable Identity Service for GKE on a cluster:

Kubernetes objects  
---  
`anthos-identity-service` | `Namespace`  
Used for the Identity Service for GKE deployments.  
`kube-public` | `Namespace`  
Used for the `default` client configuration file.  
`gke-oidc-envoy` | `LoadBalancer`  
The endpoint for OIDC requests. External by default. If created in a cluster with no external IP endpoint, the endpoint is internal to the cluster Virtual Private Cloud.  
Created in the `anthos-identity-service` namespace.  
`gke-oidc-service` | `ClusterIP`  
Facilitates communication between the `gke-oidc-envoy` Deployment and the `gke-oidc-service` Deployment.  
Created in the `anthos-identity-service` namespace.  
`gke-oidc-envoy` | `Deployment`  
Runs a proxy exposed to the `gke-oidc-envoy` LoadBalancer. Communicates with `gke-oidc-service` to validate identity tokens. Acts as a proxy for the Kubernetes API server, and [impersonates users](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) when passing on requests to the API server.  
Created in the `anthos-identity-service` namespace.  
`gke-oidc-service` | `Deployment`  
Validates identity tokens, and provides a [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) for `ClientConfig` resources.  
Created in the `anthos-identity-service` namespace.  
`gke-oidc-operator` | `Deployment`  
Reconciles the client configuration and the `gke-oidc-envoy` LoadBalancer.   
Created in the `anthos-identity-service` namespace.  
`gke-oidc-certs` | `Secret`  
Contains the cluster certificate authority (CA) and TLS certificates for the LoadBalancer.   
Created in the `anthos-identity-service` namespace  
`default` | `ClientConfig CRD`  
Contains OIDC parameters such as preferred authentication method, identity provider configuration, and user and group claims mappings. Used for identity token validation. Used by cluster administrators to configure OIDC settings before distributing to developers.   
Created in the `kube-public` namespace  
  
### Enable Identity Service for GKE on a cluster

By default, Identity and Access Management (IAM) is configured as the identity provider for cluster authentication. If you want to use OIDC with third-party identity providers, you can enable Identity Service for GKE on new or existing clusters using the Google Cloud CLI.

**Note:** For Identity Service for GKE to function correctly, GKE deploys Pods to your nodes that have elevated [RBAC permissions](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb), such as the ability to impersonate users and groups. These permissions are required for Identity Service for GKE to facilitate identity validation and communication based on your configuration.

#### Enable Identity Service for GKE on a new cluster

To create a cluster with Identity Service for GKE enabled, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-identity-service
    

Replace `CLUSTER_NAME` with the name of your new cluster.

#### Enable Identity Service for GKE on an existing cluster

To enable Identity Service for GKE on an existing cluster, run the following command
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-identity-service
    

Replace `CLUSTER_NAME` with the name of your cluster.

### Configure Identity Service for GKE

You can configure Identity Service for GKE parameters by downloading and modifying the `default` ClientConfig.

  1. Download the `default` ClientConfig:
         
         kubectl get clientconfig default -n kube-public -o yaml > client-config.yaml
         

  2. Update the `spec.authentication` section with your preferred settings:
         
         apiVersion: authentication.gke.io/v2alpha1
         kind: ClientConfig
         metadata:
           name: default
           namespace: kube-public
         spec:
           name: cluster-name
           server: https://192.168.0.1:6443
           authentication:
           - name: oidc
             oidc:
               clientID: CLIENT_ID
               certificateAuthorityData: OIDC_PROVIDER_CERTIFICATE
               extraParams: EXTRA_PARAMS
               issuerURI:  ISSUER_URI
               cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
               kubectlRedirectURI: KUBECTL_REDIRECT_URL
               scopes: SCOPES
               userClaim: USER
               groupsClaim: GROUPS
               userPrefix: USER_PREFIX
               groupPrefix: GROUP_PREFIX
         

Replace the following:

     * `CLIENT_ID`: the ID of the client application that makes authentication requests to the OIDC provider.
     * `OIDC_PROVIDER_CERTIFICATE`: (Optional) a [PEM certificate](https://wikipedia.org/wiki/Privacy-Enhanced_Mail) for the OIDC provider. This field might be useful if your OIDC provider uses self-signed certificates. Identity Service for GKE includes a set of public roots by default.
     * `EXTRA_PARAMS`: additional key-value parameters to send to the OIDC provider. 
       * To authorize groups, use `resource=token-groups-claim`.
       * To authenticate Microsoft Azure and Okta, use `prompt=consent`.
       * For Cloud Identity, use `prompt=consent,access_type=offline`.
     * `ISSUER_URI`: the URL to send OIDC authorization requests, such as `https://example.com/adfs`. The Kubernetes API server uses this URL to discover public keys for verifying tokens. The URI must use HTTPS. For Cloud Identity, use `https://accounts.google.com`.
     * `KUBECTL_REDIRECT_URL`: the redirect URL that `kubectl oidc login` uses for authorization. This is typically of the format `http://localhost:PORT/callback`, where `PORT` is any port greater than `1024` that will be available on developer workstations, for example `http://localhost:10000/callback`. You must register the URL with your OIDC provider as an authorized redirect URL for the client application. If you use Google Identity as your OIDC provider, read [Set a redirect URI](https://developers.google.com/identity/protocols/oauth2/openid-connect) for instructions.
     * `SCOPES`: the additional scopes to send to the OIDC provider. 
       * Microsoft Azure and Okta require the `offline_access` scope.
       * For Cloud Identity, use `openid, email` to obtain ID tokens that contain the email address in the `email` claim.
     * `USER`: the user claim from the identity token.
     * `GROUPS`: the group claim from the identity token.
     * `USER_PREFIX`: prefix prepended to user claims to prevent conflicts with existing names. By default, an issuer prefix is appended to the `userID` given to the Kubernetes API server (unless the user claim is `email`). The resulting user identifier is `ISSUER_URI#USER`. We recommend using a prefix, but you can disable the prefix by setting `USER_PREFIX` to `-`.
     * `GROUP_PREFIX`: prefix prepended to group claims to prevent clashes with existing names. For example, if you have two groups named `foobar`, add a prefix `gid-`. The resulting group is `gid-foobar`.
  3. Apply the updated configuration:
         
         kubectl apply -f client-config.yaml
         

After you apply this configuration, Identity Service for GKE runs inside your cluster and serves requests behind the `gke-oidc-envoy` load balancer. The IP address in the `spec.server` field must be the IP address of the load balancer. If you change the `spec.server` field, `kubectl` commands might fail.

  4. Make a copy of the `client-config.yaml` configuration file:
         
         cp client-config.yaml login-config.yaml
         

  5. Update the `login-config.yaml` configuration file with the `clientSecret` setting in the `spec.authentication.oidc` section.
         
         clientSecret: CLIENT_SECRET
         

Replace `CLIENT_SECRET` with the shared secret between the OIDC client application and the OIDC provider.

  6. Distribute the updated `login-config.yaml` file to your developers.




#### Configure Identity Service for GKE on clusters with strict policies

To configure Identity Service for GKE to work as expected on clusters that have strict network policies in place, do the following:

  1. [Add a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules) for TCP port `15000` to allow your control plane to communicate with the `ClientConfig` validation webhook.
  2. If the `gke-oidc-envoy` is created as an internal load balancer, [expose it on your VPC](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks).
  3. If you have policies that deny traffic within your cluster, add a firewall rule for TCP port `8443` to allow the `gke-oidc-envoy` deployment to communicate with the `gke-oidc-service` deployment.



Identity Service for GKE component version 0.2.20 and later does not use TCP port `15000`. If your component version is 0.2.20 or later, you don't need to add a firewall rule for port `15000`. To check your component version, run the following command:
    
    
    kubectl describe deployment gke-oidc-envoy -n anthos-identity-service \
        | grep "components.gke.io/component-name: gke-oidc" -A1
    

#### Add custom properties to the load balancer

After you configure Identity Service for GKE, you can add custom annotations and properties, such as a static IP address, to the `gke-oidc-envoy` load balancer. To edit the `gke-oidc-envoy` service, run the following command:
    
    
    kubectl edit service gke-oidc-envoy -n anthos-identity-service
    

Consult [LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters) for more information about configuring TCP/UDP load balancing for GKE.

### Create an RBAC policy for your cluster

Administrators can use [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) to grant access to authenticated cluster users. To configure RBAC for your cluster, you must grant RBAC roles for each developer. To grant access to resources in a particular namespace, create a [Role](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#role-v1-rbac-authorization-k8s-io) and a [RoleBinding](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#rolebinding-v1-rbac-authorization-k8s-io) . To grant access to resources across an entire cluster, create a [ClusterRole](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#clusterrole-v1-rbac-authorization-k8s-io) and a [ClusterRoleBinding](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#clusterrolebinding-v1-rbac-authorization-k8s-io).

For example, consider a user who needs to view all Secret objects across the cluster. The following steps grant the required RBAC roles to this user.

  1. Save the following ClusterRole manifest as `secret-viewer-cluster-role.yaml`. A person who is granted this role can get, watch, and list any Secret in the cluster.
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: secret-viewer
         rules:
         - apiGroups: [""]
           # The resource type for which access is granted
           resources: ["secrets"]
           # The permissions granted by the ClusterRole
           verbs: ["get", "watch", "list"]
         

  2. Apply the ClusterRole manifest:
         
         kubectl apply -f secret-viewer-cluster-role.yaml
         

  3. Save the following ClusterRoleBinding manifest as `secret-viewer-cluster-role-binding.yaml`. The binding grants the `secret-viewer` role to a username defined in the client configuration file.
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name:  people-who-view-secrets
         subjects:
         - kind: User
           name: ISSUER_URI#USER
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: ClusterRole
           name: secret-viewer
           apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `ISSUER_URI`: the issuer URI from `spec.authentication.oidc.issuerURI` in the client configuration file.
     * `USER`: the user identifier in the token under the claim name configured in `spec.authentication.oidc.userClaim` in the client configuration file.
  4. Apply the ClusterRoleBinding manifest:
         
         kubectl apply -f secret-viewer-cluster-role-binding.yaml
         




### Sign in and authenticate to the cluster

As a developer who receives the OIDC configuration file from your administrator, you can authenticate to your clusters.

  1. Download the `login-config.yaml` file provided by your administrator.

  2. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/install) SDK, which offers a separate OIDC component. You can install this by running the following command:
         
         gcloud components install kubectl-oidc
         

  3. Authenticate into your cluster:
         
         kubectl oidc login --cluster=CLUSTER_NAME --login-config=login-config.yaml
         

A web browser opens to complete the authentication process.

  4. After you are authenticated, you can run `kubectl` commands, for example:
         
         kubectl get pods
         




### Disable Identity Service for GKE

You can disable Identity Service for GKE with the gcloud CLI. To disable Identity Service for GKE, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --no-enable-identity-service
    

### Known limitations

The `gke-oidc-envoy` component, which is responsible for authenticating to your cluster using Identity Service for GKE, has a fixed number of replicas. This means that it does not autoscale to handle increased traffic. In regional clusters, this component is deployed with three replicas.

You cannot directly scale the `gke-oidc-envoy` deployment. We strongly recommend migrating to Workforce Identity Federation for a scalable and more robust solution.

## What's next

  * Learn more about [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).
  * Learn more about [deploying workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
