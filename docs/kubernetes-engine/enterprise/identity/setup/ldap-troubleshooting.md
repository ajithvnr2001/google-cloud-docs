---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap-troubleshooting/
title: Troubleshooting LDAP server issues \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:17.823089+00:00
---

# Troubleshooting LDAP server issues  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Troubleshooting LDAP server issues Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting guidance for LDAP server issues when accessing your fleet member clusters. This document applies only to [supported cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

## Connectivity issue

You might run into connectivity issues while trying to connect to an LDAP server. The connectivity issue can also occur when the certificate used to identify the LDAP server doesn't match the certificate mentioned in the ClientConfig.

### Error message

The following messages are applicable to errors that occur when the `gcloud anthos auth login` command is executed.

  * `ERROR: LDAP login failed: could not obtain an STS token: Post "https://127.0.0.1:15001/sts/v1beta/token": failed to obtain an endpoint for deployment anthos-identity-service/ais: Unauthorized`
  * `ERROR: Configuring Anthos authentication failed`



### Solution

You can resolve the issues in one of the following ways:

  * If the cluster can't connect to the LDAP server, do the following: 
    * To verify if any network traffic can reach the LDAP server (identity provider) from the cluster, use `telnet`, `nc`, or a similar command to connect to the LDAP server. To connect to the LDAP server, you need to execute the command in the node or Pod where the identity service Pod is running.
    * If the command is successful, then the identity service Pod should connect to the LDAP server.
    * If the command fails, it indicates that there's an issue with network connectivity. You need to check your network settings or reach out to your network administrator to resolve the connection issue.
  * Verify that the public certificate in the configuration is [formatted correctly](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/format-certificates) and matches your LDAP server for the following cases: 
    * You use LDAP with TLS.
    * You authenticate to LDAP with a service account. You use a certificate to identify the service account with the LDAP server.



## Authentication issue

An authentication issue occurs in one of the following cases:

  * The LDAP provider settings are incorrectly configured in the ClientConfig.
  * The user credentials you provided do not exist on the LDAP server.
  * The LDAP server is down.

**Note:** Although issues related to connectivity and authentication have similar causes, you can further qualify these issues from the logs.

### Error message

The following messages are applicable to errors that occur when the `gcloud anthos auth login` command is executed.

  * `ERROR: LDAP login failed: could not obtain an STS token: Post "https://127.0.0.1:15001/sts/v1beta/token": failed to obtain an endpoint for deployment anthos-identity-service/ais: Unauthorized`
  * `ERROR: Configuring Anthos authentication failed`



### Solution

As a cluster administrator, review the identity service Pod logs and resolve the authentication issues in the following ways:

  * `Can't contact LDAP server`: for more information on how to resolve this issue, see connectivity issues.
  * `Attempting to bind as the LDAP service account`: the cluster is attempting to connect to the LDAP server using the service account credentials provided in the ClientConfig. The absence of this log message indicates there's a connectivity issue.
  * `Successfully completed BIND as LDAP service account`: the cluster is able to successfully connect to the LDAP server and use its service account for user authentication. The absence of this log message indicates there's a configuration issue.
  * `Successfully found an entry for the user in the database`: a user entry exists on the LDAP server. This implies that the `baseDN`, `filter`, and `loginAttribute` fields are configured correctly to retrieve users. This message is displayed only when the logging verbosity is above the default level. For more information on enabling logs, see [Enable the debug log](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting#enable_the_debug_log).
  * `Attempting to BIND as the user to verify their credentials`: the cluster is attempting to verify user credentials.
  * `Successfully completed LDAP authentication`: user authentication is successful. The absence of this log message indicates invalid credentials.



## Authentication token has expired

Despite a successful login, you can run into issues where the authentication token has expired.

### Error message

`ERROR: You must be logged in to the server (Unauthorized)`

### Solution

You can resolve the issue by logging in again to the server.

## Issue with RBAC role binding to the user or group

This issue occurs when your authentication is successful but authorization fails due to the absence of RBAC roles binding to the user or group. For instance, this issue persists when you try to issue the command `kubectl get pods`.

### Error message

`Error from server (Forbidden): <SERVICE or PODS> is forbidden: <MORE DETAILS>`

### Solution

You can resolve the issue by doing the following:

  1. Sign in to your LDAP server to view the target user's groups.
  2. Verify if your Kubernetes role and role bindings are defined correctly and match the values in your LDAP directory. An administrator can help verify the role bindings through Kubernetes [User Impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation).
  3. Update the role binding such that the target user's group is authorized to perform the required action.
  4. Verify that the values for `baseDN` and optionally the `filter` and `identifierAttribute` for groups are correct. The cluster uses the group configuration from these fields to query all groups that the user belongs to. If `baseDN` is empty, then no groups are provided to the Kubernetes API server. There are no messages logged in such a case. If `baseDN` is not empty, then the cluster queries the database for the user's groups. 
     * If the query is successful, then the groups are provided to the Kubernetes API server.
     * If the query is unsuccessful, the groups are not provided to the Kubernetes API server. In this case, you need to fix the `baseDN` and `filter` configuration values for groups.



## User belongs to multiple groups

This issue occurs when a user belongs to multiple groups.

### Error message

`could not obtain an STS token: STS token exceeds allowed size limit. Possibility of too many groups associated with the credentials provided.`

### Solution

As a cluster administrator, you need to configure the `filter` field in the ClientConfig to reduce the number of groups returned by the query to the LDAP server.

## Version compatibility issue

This issue occurs when there is a version compatibility mismatch between the identity service component and the installed Google Cloud CLI version.

### Error message

  * `unable to parse STS Token Response`
  * `could not obtain an STS token: JSON parse error: The request was malformed.`
  * `could not obtain an STS token: Grant type must confirm that the request is intended for a token exchange.`
  * `could not obtain an STS token: Requested token type must correspond to an access token.`
  * `could not obtain an STS token: Subject token type must be a valid token type supported for token exchange.`



### Solution

You need to upgrade the gcloud utility and the cluster to the latest available version.

## 401 authentication failed status code

This issue occurs when the Kubernetes API server is unable to authenticate the service and returns a 401 error code.

### Error message

  * `ERROR: LDAP login failed: STSToken() failed: could not obtain an STS token: Post "https://127.0.0.1:15001/sts/v1beta/token": DialContext() failed: podEndpoint() failed to obtain an endpoint for deployment anthos-identity-service/ais: Unauthorized`

  * `ERROR: Configuring Anthos authentication failed`




### Solution

You can resolve this issue in one of the following ways:

  * Check if the identity service Pod is in the `running` state by using the following command: 
        
        kubectl get pods -l k8s-app=ais -n anthos-identity-service --kubeconfig USER_CLUSTER_KUBECONFIG

  * Check the LDAP configuration in the ClientConfig by using the following command: 
        
        kubectl get clientconfig -n kube-public -o jsonpath='{.items[].spec.authentication[].ldap}' --kubeconfig USER_CLUSTER_KUBECONFIG

  * Review the logs for detailed information regarding the error. For more information on logging, see [Using logging and monitoring for system components](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/logging-and-monitoring). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
