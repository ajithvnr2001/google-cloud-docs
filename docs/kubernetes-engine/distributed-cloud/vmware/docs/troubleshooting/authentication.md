---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/authentication/
title: Troubleshoot Google Distributed Cloud authentication issues \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:24.539936+00:00
---

# Troubleshoot Google Distributed Cloud authentication issues  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot Google Distributed Cloud authentication issues Stay organized with collections  Save and categorize content based on your preferences. 

This document helps troubleshoot authentication issues in Google Distributed Cloud. General troubleshooting information and guidance is provided, along with specific information for OpenID Connect (OIDC) and Lightweight Directory Access Protocol (LDAP).

OIDC and LDAP authentication uses GKE Identity Service. Before you can use GKE Identity Service with Google Distributed Cloud, you must configure an identity provider. If you haven't configured an identity provider for GKE Identity Service, follow the instructions for one of the more common following providers:

  * [Google OIDC](https://developers.google.com/identity/protocols/oauth2/openid-connect)
  * [Microsoft ADFS](https://docs.cloud.google.com/anthos/identity/setup/provider#microsoft-ad-fs)
  * [Azure AD](https://docs.cloud.google.com/anthos/identity/setup/provider#azure-ad)
  * [Okta](https://developer.okta.com/docs/guides/quickstart/main/)



Review the [GKE Identity Service identity provider troubleshooting guide](https://docs.cloud.google.com/anthos/identity/setup/user-access-troubleshooting#troubleshoot_identity_providers) for information on how to enable and review identity logs and test connectivity.

## General troubleshooting

The following troubleshooting tips can help with general authentication and authorization issues with Google Distributed Cloud. If these issues don't apply or you have issues with OIDC or LDAP, continue to the section on troubleshooting GKE Identity Service.

### Keep `gcloud anthos auth` up-to-date

You can avoid many common issues by verifying that the components of your `gcloud anthos auth` installation are up to date.

There are two pieces that must be verified. The `gcloud anthos auth` command has logic in the Google Cloud CLI core component, and a separately packaged `anthos-auth` component.

  1. To update the Google Cloud CLI:
         
         gcloud components update
         

  2. To update the `anthos-auth` component:
         
         gcloud components install anthos-auth
         




### Invalid provider configuration

If your identity provider configuration is invalid, you will see an error screen from your identity provider after you click **LOGIN**. Follow the provider-specific instructions to correctly configure the provider or your cluster.

### Invalid configuration

If Google Cloud console can't read the OIDC configuration from your cluster, the **LOGIN** button is disabled. To troubleshooting your cluster OIDC configuration, see the following troubleshoot OIDC section in this document.

### Invalid permissions

If you complete the authentication flow, but still don't see the details of the cluster, make sure you granted the correct RBAC permissions to the account that you used with OIDC. This might be a different account from the one you use to access Google Cloud console.

### Missing refresh token

The following issue occurs when the authorization server prompts for consent, but the required authentication parameter wasn't provided.
    
    
    Error: missing 'RefreshToken' field in 'OAuth2Token' in credentials struct
    

To resolve this issue, in your `ClientConfig` resource, add `prompt=consent` to the `authentication.oidc.extraParams` field. Then regenerate the client authentication file.

### Refresh token expired

The following issue occurs when the refresh token in the kubeconfig file has expired:
    
    
    Unable to connect to the server: Get {DISCOVERY_ENDPOINT}: x509:
        certificate signed by unknown authority
    

To resolve this issue, run the `gcloud anthos auth login` command again.

### gcloud anthos auth login fails with `proxyconnect tcp`

This issue occurs when there's an error in the `https_proxy` or `HTTPS_PROXY` environment variable configurations. If there's an `https://` specified in the environment variables, then the GoLang HTTP client libraries might fail if the proxy is configured to handle HTTPS connections using other protocols such as SOCK5.

The following example error message might be returned:
    
    
    proxyconnect tcp: tls: first record does not look like a TLS handshake
    

To resolve this issue, modify the `https_proxy` and `HTTPS_PROXY` environment variables to omit the `https:// prefix`. On Windows, modify the system environment variables. For example, change the value of the `https_proxy` environment variable from `https://webproxy.example.com:8000` to `webproxy.example.com:8000`.

### Cluster access fails when using kubeconfig generated by `gcloud anthos auth login`

This issue occurs when the Kubernetes API server is unable to authorize the user. This can happen if the appropriate RBACs are missing or incorrect, or there's an error in the OIDC configuration for the cluster. The following example error might be displayed:
    
    
    Unauthorized
    

To resolve this issue, complete the following steps:

  1. In the kubeconfig file generated by `gcloud anthos auth login`, copy the value of `id-token`.
         
         kind: Config
         ...
         users:
         - name: ...
           user:
             auth-provider:
               config:
                 id-token: xxxxyyyy
         

  2. Install [jwt-cli](https://www.npmjs.com/package/jwt-cli) and run:
         
         jwt ID_TOKEN
         

  3. Verify OIDC configuration.

The `ClientConfig` resource has the `group` and `username` fields. These fields are used to set the `--oidc-group-claim` and `--oidc-username-claim` flags in the Kubernetes API server. When the API server is presented with the token, it forwards the token to GKE Identity Service, which returns the extracted `group-claim` and `username-claim` back to the API server. The API server uses the response to verify that the corresponding group or user has the correct permissions.

Verify that the claims set for `group` and `user` in the `ClientConfig` resource are present in the ID token.

  4. Check RBACs that were applied.

Verify that there's an RBAC with the correct permissions for either the user specified by `username-claim` or one of the groups listed `group-claim` from the previous step. The name of the user or group in the RBAC should be prefixed with the `usernameprefix` or `groupprefix` that was specified in the `ClientConfig` resource.

If `usernameprefix` is blank, and `username` is a value other than `email`, the prefix defaults to `issuerurl#`. To disable username prefixes, set `usernameprefix` to `-`.

For more information about user and group prefixes, see [Authenticating with OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

**Note:** The Kubernetes API server treats a backslash as an escape character. If the name of the user or group contains `\\`, the API server reads it as a single `\` when parsing the ID token. Therefore, the RBAC role binding applied for this user or group should only contain a single backslash, or you might see an `Unauthorized` error.

`ClientConfig` resource:
         
         oidc:
           ...
           username: "unique_name"
           usernameprefix: "-"
           group: "group"
           groupprefix: "oidc:"
         

ID token:
         
         {
           ...
           "email": "cluster-developer@example.com",
           "unique_name": "EXAMPLE\cluster-developer",
           "group": [
             "Domain Users",
             "EXAMPLE\developers"
           ],
         ...
         }
         

The following RBAC bindings grant this group and user the `pod-reader` cluster role. Note the single slash in the name field instead of a double slash:

Group ClusterRoleBinding:
         
         apiVersion:
         kind: ClusterRoleBinding
         metadata:
           name: example-binding
         subjects:
         - kind: Group
           name: "oidc:EXAMPLE\developers"
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: ClusterRole
           name: pod-reader
           apiGroup: rbac.authorization.k8s.io
         

User ClusterRoleBinding:
         
         apiVersion:
         kind: ClusterRoleBinding
         metadata:
           name: example-binding
         subjects:
         - kind: User
           name: "EXAMPLE\cluster-developer"
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: ClusterRole
           name: pod-reader
           apiGroup: rbac.authorization.k8s.io
         

  5. Check the Kubernetes API server logs.

If the OIDC plugin configured in the Kubernetes API server doesn't start up correctly, the API server returns an `Unauthorized` error when presented with the ID token. To see if there were any issues with the OIDC plugin in the API server, run:
         
         kubectl logs statefulset/kube-apiserver -n USER_CLUSTER_NAME \
           --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of your user cluster to view logs for.
     * `ADMIN_CLUSTER_KUBECONFIG`: The admin cluster kubeconfig file.



### gkectl create-login-config fails to get clientconfig

This issue occurs when the kubeconfig file passed to `gkectl create-login-config` isn't for a user cluster or the `ClientConfig` resource didn't come up during cluster creation.
    
    
    Error getting clientconfig using KUBECONFIG
    

To resolve this issue, make sure you have the correct kubeconfig file for your user cluster. Then check to see whether the `ClientConfig` resource is in the cluster:
    
    
    kubectl get clientconfig default -n kube-public \
      --kubeconfig USER_CLUSTER_KUBECONFIG
    

Replace `USER_CLUSTER_KUBECONFIG` with the path to your user cluster kubeconfig file.

### gkectl create-login-config fails because of duplicate cluster name

This issue occurs if you attempt to write login configuration data that contains a cluster name that already exists in the destination file. Each login configuration file must contain unique cluster names.
    
    
    error merging with file MERGE_FILE because MERGE_FILE contains a cluster with
      the same name as the one read from KUBECONFIG. Please write to a new
      output file
    

To resolve this issue, use the `--output` flag to specify a new destination file.

If you don't provide `--output`, this login configuration data is written to a file named `kubectl-anthos-config.yaml` in the current directory.

## Troubleshoot OIDC

When OIDC authentication isn't working for Google Distributed Cloud, typically the OIDC specification in the `ClientConfig` resource has been improperly configured. The `ClientConfig` resource provides instructions for reviewing logs and the OIDC specification to help identify the cause of an OIDC problem.

Review the [GKE Identity Service identity provider troubleshooting guide](https://docs.cloud.google.com/anthos/identity/setup/user-access-troubleshooting#troubleshoot_identity_providers) for information on how to enable and review identity logs and test connectivity. After you confirm that GKE Identity Service works as expected or you identify an issue, review the following OIDC troubleshooting information.

### Check the OIDC specification in your cluster

The OIDC information for your cluster is specified in the `ClientConfig` resource in the `kube-public` namespace.

  1. Use `kubectl get` to print the OIDC resource for your user cluster:
         
         kubectl --kubeconfig KUBECONFIG -n kube-public get \
           clientconfig.authentication.gke.io default -o yaml
         

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.

  2. Review the field values to confirm that the specification is configured correctly for your OIDC provider.

  3. If you identify a configuration issue in the specification, [reconfigure OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

  4. If you're unable to diagnose and resolve the problem yourself, [contact Google Cloud support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support). 

Google Cloud support needs the [GKE Identity Service logs](https://docs.cloud.google.com/anthos/identity/setup/user-access-troubleshooting#check_the_container_log) and the OIDC specification to diagnose and resolve OIDC problems.




### Verify that OIDC authentication is enabled

Before you test OIDC authentication, verify that OIDC authentication is enabled in your cluster.

  1. Examine the GKE Identity Service logs:
         
         kubectl logs -l k8s-app=ais -n anthos-identity-service
         

The following example output shows that OIDC authentication is correctly enabled:
         
         ...
         I1011 22:14:21.684580      33 plugin_list.h:139] OIDC_AUTHENTICATION[0] started.
         ...
         

If OIDC authentication isn't enabled correctly, errors similar to the following example are displayed:
         
         Failed to start the OIDC_AUTHENTICATION[0] authentication method with error:
         

Review the specific errors reported and try to correct them.




### Test the OIDC authentication

To use the OIDC feature, use a workstation with the UI and browser enabled. You can't perform these steps from a text-based SSH session. To test that OIDC works correctly in your cluster, complete the following steps:

  1. [Download](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. To generate the login config file, run the following [`gcloud anthos create-login-config`](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/create-login-config) command:
         
         gcloud anthos create-login-config \
           --output user-login-config.yaml \
           --kubeconfig KUBECONFIG
         

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.

  3. To authenticate the user, run the following command:
         
         gcloud anthos auth login --cluster CLUSTER_NAME \
           --login-config user-login-config.yaml \
           --kubeconfig AUTH_KUBECONFIG
         

Replace the following:

     * CLUSTER_NAME with the name of your user cluster to connect to.
     * AUTH_KUBECONFIG with the new kubeconfig file to create that includes the credentials for accessing your cluster. For more information, see [Authenticate to the cluster](https://docs.cloud.google.com/anthos/identity/accessing#plugin_to_authenticate).
  4. You should receive a sign-in consent page open in the default web browser of your local workstation. Provide valid authentication information for a user in this sign in prompt.

After you successfully complete the previous sign-in step, a kubeconfig file is generated in your current directory.

  5. To test the new kubeconfig file that includes your credentials, list the Pods in your user cluster:
         
         kubectl get pods --kubeconfig AUTH_KUBECONFIG
         

Replace AUTH_KUBECONFIG with the path to your new kubeconfig file that was generated in the previous step.

The following example message might be returned that shows you can successfully authenticate, but there are no role-based access controls (RBACs) assigned to the account:
         
         Error from server (Forbidden): pods is forbidden: User "XXXX" cannot list resource "pods" in API group "" at the cluster scope
         




### Review OIDC authentication logs

If you're unable to authenticate with OIDC, GKE Identity Service logs provide the most relevant and useful information for debugging the problem.

  1. Use `kubectl logs` to print the GKE Identity Service logs:
         
         kubectl --kubeconfig KUBECONFIG \
           -n anthos-identity-service logs \
           deployment/ais --all-containers=true
         

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.

  2. Review the logs for errors that can help you diagnose OIDC problems.

For example, the `ClientConfig` resource might have a typo in the `issuerURL` field, such as `htps://accounts.google.com` (missing a `t` in `https`). The GKE Identity Service logs would contain an entry like the following example:
         
         OIDC (htps://accounts.google.com) - Unable to fetch JWKs needed to validate OIDC ID token.
         

  3. If you identify a configuration issue in the logs, [Reconfigure OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster) and correct the configuration issues.

  4. If you're unable to diagnose and resolve the problem yourself, [contact Google Cloud support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support). 

Google Cloud support needs the GKE Identity Service logs and the OIDC specification to diagnose and resolve OIDC problems.




### Common OIDC issues

If you have problems with OIDC authentication, review the following common issues. Follow any guidance for how to resolve the issue.

#### No endpoints available for service "ais"

When you save the `ClientConfig` resource, the following error message is returned:
    
    
      Error from server (InternalError): Internal error occurred: failed calling webhook "clientconfigs.validation.com":
      failed to call webhook: Post "https://ais.anthos-identity-service.svc:15000/admission?timeout=10s":
      no endpoints available for service "ais"
    

This error is caused by the unhealthy GKE Identity Service endpoint. The GKE Identity Service Pod is unable to serve the validation webhook.

  1. To confirm that the GKE Identity Service Pod is unhealthy, run the following command:
         
         kubectl get pods -n anthos-identity-service \
           --kubeconfig KUBECONFIG
         

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.

The following example output means that your GKE Identity Service Pod is crashing:
         
         NAME                  READY  STATUS            RESTARTS  AGE
         ais-5949d879cd-flv9w  0/1    ImagePullBackOff  0         7m14s
         

  2. To understand why the Pod has a problem, look at the Pod events:
         
         kubectl describe pod -l k8s-app=ais \
           -n anthos-identity-service \
           --kubeconfig KUBECONFIG
         

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.

The following example output reports a permission error when pulling the image:
         
         Events:
           Type     Reason     Age                     From               Message
           ----     ------     ----                    ----               -------
           Normal   Scheduled  10m                     default-scheduler  Successfully assigned anthos-identity-service/ais-5949d879cd-flv9w to pool-1-76bbbb8798-dknz5
           Normal   Pulling    8m23s (x4 over 10m)     kubelet            Pulling image "gcr.io/gke-on-prem-staging/ais:hybrid_identity_charon_20220808_2319_RC00"
           Warning  Failed     8m21s (x4 over 10m)     kubelet            Failed to pull image "gcr.io/gke-on-prem-staging/ais:hybrid_identity_charon_20220808_2319_RC00": rpc error: code = Unknown desc = failed to pull and unpack image "gcr.io/gke-on-prem-staging/ais:hybrid_identity_charon_20220808_2319_RC00": failed to resolve reference "gcr.io/gke-on-prem-staging/ais:hybrid_identity_charon_20220808_2319_RC00": pulling from host gcr.io failed with status code [manifests hybrid_identity_charon_20220808_2319_RC00]: 401 Unauthorized
           Warning  Failed     8m21s (x4 over 10m)     kubelet            Error: ErrImagePull
           Warning  Failed     8m10s (x6 over 9m59s)   kubelet            Error: ImagePullBackOff
           Normal   BackOff    4m49s (x21 over 9m59s)  kubelet            Back-off pulling image "gcr.io/gke-on-prem-staging/ais:hybrid_identity_charon_20220808_2319_RC00"
         

  3. If the Pod events report a problem, continue troubleshooting in the affected areas. If you need additional assistance, [contact Google Cloud support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support). 




#### Failed reading response bytes from server

You might see the following errors in the GKE Identity Service logs:
    
    
      E0516 07:24:38.314681      65 oidc_client.cc:207] Failed fetching the Discovery URI
      "https://oidc.idp.cloud.example.com/auth/idp/k8sIdp/.well-known/openid-configuration" with error:
      Failed reading response bytes from server.
    
      E0516 08:24:38.446504      65 oidc_client.cc:223] Failed to fetch the JWKs URI
      "https://oidc.idp.cloud.example.com/auth/idp/k8sIdp/certs" with error:
      Failed reading response bytes from server.
    

These network errors might appear in the logs in one of the following ways:

  * **Sparsely appear in the log:** Spare errors likely aren't the main issue, and could be intermittent network problems.

The GKE Identity Service OIDC plugin has a daemon process to periodically synchronize the OIDC discovery URL every 5 seconds. If the network connection is unstable, this egress request might fail. Occasional failure does not affect the OIDC authentication. The existing cached data can be reused.

If you encounter spare errors in the logs, continue with additional troubleshooting steps.

  * **Constantly appear in the log, or GKE Identity Service never successfully reaches the well-known endpoint:** These constant issues indicate a connectivity issue between GKE Identity Service and your OIDC identity provider.

The following troubleshooting steps can help diagnose these connectivity issues:

    1. Make sure that a firewall isn't blocking the outbound requests from GKE Identity Service.
    2. Check that the identity provider server is running correctly.
    3. Verify that the OIDC issuer URL in the `ClientConfig` resource is configured correctly.
    4. If you enabled the proxy field in the `ClientConfig` resource, review the status or log of your egress proxy server.
    5. Test the connectivity between your GKE Identity Service pod and OIDC identity provider server.



#### You must be logged in to the server (Unauthorized)

When you try to sign in using OIDC authentication, you might receive the following error message:
    
    
      You must be logged in to the server (Unauthorized)
    

This error is a general Kubernetes authentication problem that doesn't give any additional information. However, this error does indicate a configuration problem.

To determine the problem, review the previous sections to Check the OIDC specification in your cluster and ​​[Configure the `ClientConfig` resource](https://docs.cloud.google.com/anthos/identity/setup/per-cluster).

#### Failed to make webhook authenticator request

In the GKE Identity Service logs, you might see the following error:
    
    
      E0810 09:58:02.820573       1 webhook.go:127] Failed to make webhook authenticator request:
      error trying to reach service: net/http: TLS handshake timeout
    

This error indicates that the API server can't establish the connection with the GKE Identity Service Pod.

  1. To verify if the GKE Identity Service endpoint can be reached from the outside, run the following `curl` command:
         
         curl -k  -s -o /dev/null -w "%{http_code}" -X POST \
           https://APISERVER_HOST/api/v1/namespaces/anthos-identity-service/services/https:ais:https/proxy/authenticate -d '{}'
         

Replace `APISERVER_HOST` with the address of your API server.

The expected response is an `HTTP 400` status code. If the request timed out, restart the GKE Identity Service Pod. If the error continues, it means that the GKE Identity Service HTTP server fails to start. For additional assistance, [contact Google Cloud support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support). 




#### Sign-in URL not found

The following issue occurs when Google Cloud console can't reach the identity provider. An attempt to sign in is redirected to a page with a `URL not found` error.

To resolve this issue, review the following troubleshooting steps. After each step, try to sign in again:

  1. If the identity provider isn't reachable over the public internet, enable the OIDC HTTP proxy to sign in using Google Cloud console. Edit the `ClientConfig` custom resource and set `useHTTPProxy` to `true`:
         
         kubectl edit clientconfig default -n kube-public --kubeconfig USER_CLUSTER_KUBECONFIG
         

Replace `USER_CLUSTER_KUBECONFIG` with the path to your user cluster kubeconfig file.

  2. If the HTTP proxy is enabled and you still experience this error, there might be an issue with the proxy starting up. View the logs of the proxy:
         
         kubectl logs deployment/clientconfig-operator -n kube-system --kubeconfig USER_CLUSTER_KUBECONFIG
         

Replace `USER_CLUSTER_KUBECONFIG` with the path to your user cluster kubeconfig file.

Even if your identity provider has a well-known CA, you must provide a value for `oidc.caPath` in your `ClientConfig` custom resource for the HTTP proxy to successfully start.

  3. If the authorization server prompts for consent, and you haven't included the `extraparam` `prompt=consent` parameters, edit the `ClientConfig` custom resource, and add `prompt=consent` to `extraparams` parameters:
         
         kubectl edit clientconfig default -n kube-public --kubeconfig USER_CLUSTER_KUBECONFIG
         

Replace `USER_CLUSTER_KUBECONFIG` with the path to your user cluster kubeconfig file.

  4. If configuration settings are changed on storage service, you might need to explicitly sign out of existing sessions. In the Google Cloud console, go to the cluster details page, and select **Log out**.




## Troubleshoot LDAP

If you have issues with LDAP authentication, make sure that you have set up your environment by following one of the appropriate configuration documents:

  * [OpenLDAP](https://www.openldap.org/doc/)
  * [Azure AD](https://azure.microsoft.com/en-us/services/active-directory/)
  * [Microsoft Active Directory](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/active-directory-overview)
  * [Google LDAP](https://support.google.com/a/topic/9173976?ref_topic=9048334)



You also need to make sure that you [populate the LDAP service account secret](https://docs.cloud.google.com/anthos/identity/setup/ldap#populate_the_ldap_service_account_secret) and have [configured the `ClientConfig` resource to enable LDAP authentication.](https://docs.cloud.google.com/anthos/identity/setup/ldap#configure_the_cluster)

Review the [GKE Identity Service identity provider troubleshooting guide](https://docs.cloud.google.com/anthos/identity/setup/user-access-troubleshooting#troubleshoot_identity_providers) for information on how to enable and review identity logs and test connectivity. After you confirm that GKE Identity Service works as expected or you identify an issue, review the following LDAP troubleshooting information.

### Verify that LDAP authentication is enabled

Before you test LDAP authentication, verify that LDAP authentication is enabled in your cluster.

  1. Examine the GKE Identity Service logs:
         
         kubectl logs -l k8s-app=ais -n anthos-identity-service
         

The following example output shows that LDAP authentication is correctly enabled:
         
         ...
         I1012 00:14:11.282107      34 plugin_list.h:139] LDAP[0] started.
         ...
         

If LDAP authentication isn't enabled correctly, errors similar to the following example are displayed:
         
         Failed to start the LDAP_AUTHENTICATION[0] authentication method with error:
         

Review the specific errors reported and try to correct them.




### Test the LDAP authentication

To use the LDAP feature, use a workstation with the UI and browser enabled. You can't perform these steps from a text-based SSH session. To test that LDAP authentication works correctly in your cluster, complete the following steps:

  1. [Download](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. To generate the login config file, run the following [gcloud anthos create-login-config](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/create-login-config) command:
         
         gcloud anthos create-login-config \
           --output user-login-config.yaml \
           --kubeconfig KUBECONFIG
         

Replace `KUBECONFIG` with the path to your user cluster kubeconfig file.

  3. To authenticate the user, run the following command:
         
         gcloud anthos auth login --cluster CLUSTER_NAME \
           --login-config user-login-config.yaml \
           --kubeconfig AUTH_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME` with the name of your user cluster to connect to.
     * `AUTH_KUBECONFIG` with the new kubeconfig file to create that includes the credentials for accessing your cluster. For more information, see [Authenticate to the cluster](https://docs.cloud.google.com/anthos/identity/accessing#plugin_to_authenticate).
  4. You should receive a sign-in consent page open in the default web browser of your local workstation. Provide valid authentication information for a user in this sign in prompt.

After you successfully complete the previous sign-in step, a kubeconfig file is generated in your current directory.

  5. To test the new kubeconfig file that includes your credentials, list the Pods in your user cluster:
         
         kubectl get pods --kubeconfig AUTH_KUBECONFIG
         

Replace AUTH_KUBECONFIG with the path to your user cluster kubeconfig that was generated in the previous step.
         
         Error from server (Forbidden): pods is forbidden: User "XXXX" cannot list resource "pods" in API group "" at the cluster scope
         




### Common LDAP issues

If you have problems with LDAP authentication, review the following common issues. Follow any guidance for how to resolve the issue.

#### Users can't authenticate with commas in their CN

When you use LDAP, you might have problems where users can't authenticate if their CN contains a comma, like `CN="a,b"`. If you enable the debugging log for GKE Identity Service, the following error message is reported:
    
    
      I0207 20:41:32.670377 30 authentication_plugin.cc:977] Unable to query groups from the LDAP server directory.example.com:636, using the LDAP service account
      'CN=svc.anthos_dev,OU=ServiceAccount,DC=directory,DC=example,DC=com'.
      Encountered the following error: Empty entries.
    

This problem occurs because the GKE Identity Service LDAP plugin double escapes the comma. This issue only happens in versions Google Distributed Cloud 1.13 and earlier.

To fix this problem, complete one of the following steps:

  1. Upgrade your cluster to Google Distributed Cloud 1.13 or later.
  2. Choose a different `identifierAttribute`, like `sAMAccountName`, instead of using the CN.
  3. Remove the commas from inside the CN in your LDAP directory.



#### Authentication failure with Google Cloud CLI 1.4.2

With Google Cloud CLI `anthos-auth` 1.4.2, you might see the following error message when you run the `gcloud anthos auth login` command:
    
    
      Error: LDAP login failed: could not obtain an STS token: Post "https://127.0.0.1:15001/sts/v1beta/token":
      failed to obtain an endpoint for deployment anthos-identity-service/ais: Unauthorized
      ERROR: Configuring Anthos authentication failed
    

In the GKE Identity Service log, you also see the following error:
    
    
      I0728 12:43:01.980012      26 authentication_plugin.cc:79] Stopping STS   authentication, unable to decrypt the STS token:
      Decryption failed, no keys in the current key set could decrypt the payload.
    

To resolve this error, complete the following steps:

  1. Check if you use the Google Cloud CLI `anthos-auth` version 1.4.2:
         
         gcloud anthos auth version
         

The following example output shows that the version is 1.4.2:
         
         Current Version: v1.4.2
         

  2. If you run the Google Cloud CLI `anthos-auth` version 1.4.2, upgrade to version 1.4.3 or later.




## Common issues

This section details common authentication issue and how to resolve them.

### Lost access to admin workstation due to SSH key `permission denied` error

The following error occurs when you try to connect to your admin workstation and receive a `"Permission denied"` message similar to the following example:
    
    
    Authorized users only. All activity may be monitored and reported.
    TARGET_MACHINE: Permission denied (publickey).
    

This error occurs due to using a wrong private key, or no key, when you connect to the admin workstation using SSH.

To resolve this issue, find and use the correct SSH key. If you can't find the correct SSH key, generate a new SSH key pair for the admin workstation using the following steps:

  1. Create a temporary rescue VM. This rescue VM must connect to the same **Network** and **Datastore** as the current admin workstation VM.

  2. Power off the admin workstation VM and the rescue VM.

  3. Attach the data disk of the admin workstation VM to the rescue VM. The data disk is generally 512 MB unless you specified a different disk size in the [admin workstation configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file#adminworkstationdatadiskmb), which is distinct from the boot disk.

  4. Power on the rescue VM.

  5. Connect to the rescue VM using SSH.

  6. On your local computer, [generate a new SSH key pair](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys#create_an_ssh_key_pair).

  7. On your local computer, copy the new SSH public key to the rescue VM using the `ssh-copy-id` command:
         
         ssh-copy-id -i ~/.ssh/NEW_SSH_KEY ubuntu@RESCUE_VM
         

Replace the following:

     * `NEW_SSH_KEY` with the name of the new SSH key that you created in the previous step.
     * `RESCUE_VM` with the IP address or FQDN of your rescue VM.
  8. On the rescue VM, mount the data disk on the rescue VM:
         
         sudo mkdir -p /mnt/ext-disk
         sudo mount DEVICE /mnt/ext-disk
         

Replace `DEVICE` with the unique identifier of your own disk, such as `/dev/sdb1`.

  9. On the rescue VM, copy the new SSH public key into the `authorized_keys` file on the mounted data disk from your admin workstation VM.

View the contents of the `authorized_keys` file on the rescue VM, which includes the new SSH public key copied using the `ssh-copy-id` command in a previous step:
         
         ls ~/.ssh/authorized_keys
         

Copy the last SSH public key entry from the `authorized_keys` file, then close the file.

  10. Edit the `authorized_keys` file on the mounted data disk from your admin workstation VM:
         
         vi /mnt/ext-disk/.ssh/authorized_keys
         

Paste the contents of the SSH public key from the `authorized_keys` file of your rescue VM.

  11. Save and close the `authorized_keys` file on the mounted data disk from your admin workstation VM.

  12. Verify that the files in `/mnt/ext-disk/.ssh/` have the correct permissions applied to them:
         
         chown -R ubuntu /mnt/ext-disk/.ssh/*
         chmod -R 600 /mnt/ext-disk/.ssh/*
         

  13. Exit your SSH connection to the rescue VM.

  14. Shut down the rescue VM.

  15. Detach the data disk from the rescue VM and re-attach the disk to the admin workstation VM.

  16. Power on the admin workstation.

  17. After the VM is successfully running, connect to the admin workstation using SSH and the new SSH key pair.
         
         ssh -i ~/.ssh/NEW_SSH_KEY ubuntu@ADMIN_VM
         

Replace the following:

     * `NEW_SSH_KEY` with the name of the new SSH key that you created in a previous step and copied to the admin workstation VM.
     * `RESCUE_VM` with the IP address or FQDN of your admin workstation VM.

Verify that you can successfully connect using SSH.

  18. Delete the rescue VM.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
