---
url: https://docs.cloud.google.com/access-context-manager/docs/configure-cba-for-workloads/
title: Configure certificate-based access for Workload Identity Federation \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:23:39.393424+00:00
---

# Configure certificate-based access for Workload Identity Federation  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/configure-cba-for-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configure certificate-based access for Workload Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure certificate-based access for [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) using [X.509 certificates](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates).

Certificate-based access uses Mutual TLS (mTLS) to authenticate both the client and server during a TLS handshake. In this process, an mTLS binding incorporates policies based on the transport context and uses the state of the client's certificate within the TLS session to make authorization decisions.

For X.509 Workload Identity Federation, an mTLS binding ensures that the entire authentication flow is securely tied to a trusted workload. This mitigates the risk of credential theft, because the system binds the authentication to a specific, trusted endpoint.

## Certificate-based access for Workload Identity Federation configuration overview

The following provides a high-level overview of the process to configure certificate-based access for Workload Identity Federation:

  1. Establish Workload Identity Federation by configuring trust with the X.509 certificates' trust anchor.

  2. Create an access level for certificate-based access.

  3. Add the access level to a Context-Aware Access policy that enforces the mTLS binding.




## Before you begin

Verify that you have the following prerequisites:

  * The latest version of the Google Cloud CLI.

To update to the latest version of the gcloud CLI, run the following command:
        
        gcloud components update
        

If you need to install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

  * A [Workload Identity Federation configuration](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates) that uses your X.509 certificates trust anchor.

  * To use this feature, complete the [Allowlist request form](https://docs.google.com/forms/d/e/1FAIpQLSet5YP7WzadszM0Qwk7nsJqDabazbPlP-RQrU6Xg15t9UYIVg/viewform?usp=header) to request access.




## Create an access level for certificates

  1. Create an [mTLS](https://docs.cloud.google.com/access-context-manager/docs/understand-mtls) access level. The mTLS access level validates certificates when determining access to resources.

###  Console 

In Access Context Manager, [create a custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level) and enter the following expression in the **CEL expression** field: `request.auth.matchesMtlsTokens(origin) == true`.

###  gcloud 

To create a custom access level, run the following command:
         
         gcloud access-context-manager levels create ACCESS_LEVEL_NAME \
             --title=TITLE \
             --custom-level-spec=FILE \
             --description=DESCRIPTION \
             --policy=POLICY_NAME

Replace the following:

     * `ACCESS_LEVEL_NAME`: the name of the access level.
     * `TITLE`: the title of the access level.
     * `FILE`: a YAML file with the following content: `expression: "request.auth.matchesMtlsTokens(origin) == true"`.
     * `DESCRIPTION`: a description of the access level.
     * `POLICY_NAME`: the name of the access policy.

  2. Export the access level that you created to an environment variable for use in subsequent steps:
         
         export ACCESS_LEVEL_ID=ACCESS_LEVEL_ID
           

Replace `ACCESS_LEVEL_ID` with the access level name—for example, `accessPolicies/12345/accessLevels/acl_1`.




## Create a Context-Aware Access binding for a workload identity pool

  1. Set the following environment variables:
         
         export ORG_ID=ORG_ID
         export CALLER_PROJECT_ID=CALLER_PROJECT_ID
         export FEDERATED_PRINCIPAL=FEDERATED_PRINCIPAL
         

Replace the following:

     * `ORG_ID`: the ID of your organization.
     * `CALLER_PROJECT_ID`: the ID of the project to use to call the APIs.
     * `FEDERATED_PRINCIPAL`: the name of the identity principal in the workload identity pool that adheres to the Context-Aware Access policy. You can use one of the following options:

       * A single identity: `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`
       * All identities in a pool: `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*`

###  gcloud 
    
    gcloud alpha access-context-manager cloud-bindings create \
    --organization=ORG_ID \
    --federated-principal=FEDERATED_PRINCIPAL \
    --level=ACCESS_LEVEL_ID \
    --dry-run-level=DRY_RUN_ACCESS_LEVEL_ID
    

Replace the following:

     * `ACCESS_LEVEL_ID`: the access level name.
     * `DRY_RUN_ACCESS_LEVEL_ID`: the dry run access level name. We recommend that you enable a [dry run policy binding](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups#use_dry_run_access_levels_to_simulate_enforcement) first to understand the potential impact on existing traffic.

###  curl 

     1. Create a JSON file with the Context-Aware Access binding:

You can provide only one access level in a request, even though the field is repeated. You can use the following types of federated principals:

        * Single identity: `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`
        * All identities in a pool: `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*`
    
    cat <<EOF > request.json
    {
      "principal": {
        "federatedPrincipal": "${FEDERATED_PRINCIPAL:?}"
      },
      "accessLevels": ["${ACCESS_LEVEL_ID:?}"]
    }
    EOF
    

     2. Use `curl` to send the following HTTP request:
            
            curl -H "X-Goog-User-Project: ${CALLER_PROJECT_ID:?}" -X POST \
               -H "Authorization: Bearer $(gcloud auth print-access-token)" \
               -H "Content-Type: application/json; charset=utf-8" \
               -d @request.json \
             "https://accesscontextmanager.googleapis.com/v1alpha/organizations/${ORG_ID:?}/gcpUserAccessBindings"
            




## Authorize using the Google Cloud client libraries

To authorize Workload Identity Federation workloads using the Google Cloud client libraries, complete the following steps:

  1. Create an Application Default Credentials (ADC) file configured for Workload Identity Federation authentication:
         
         gcloud iam workload-identity-pools create-cred-config IDENTITY_POOL_ID \
         --credential-cert-path WORKLOAD_CERTIFICATE_PATH \
         --credential-cert-private-key-path WORKLOAD_KEY_PATH \
         --output-file ADC_FILE_OUTPUT_PATH
         

Replace the following:

     * `IDENTITY_POOL_ID`: the ID of your workload identity pool.
     * `WORKLOAD_CERTIFICATE_PATH`: the path to your workload's certificate file.
     * `WORKLOAD_KEY_PATH`: the path to your workload's private key file.
     * `ADC_FILE_OUTPUT_PATH`: the output path for the ADC file.

This command also generates a certificate configuration file in your gcloud CLI default configuration directory. The certificate configuration file supports initial authentication and establishes mTLS handshakes for subsequent requests to Google Cloud resources.

  2. Set an environment variable to point to the ADC file to make your credentials discoverable by Google client libraries:
         
         export GOOGLE_APPLICATION_CREDENTIALS=ADC_FILE_OUTPUT_PATH
         

This step is optional if you omit the `--output-file` argument when you generate the ADC file. If you omit the argument, the gcloud CLI creates and reads the ADC file from your gcloud CLI default configuration directory.

  3. The feature supports the client libraries in Go, Python, and Java. You need to [set the environment variable](https://docs.cloud.google.com/access-context-manager/docs/enable-cba-client-apps#enable_cba_for_the_terraform_cli_and) to turn on mTLS for Python and Java.

  4. To quickly establish and test the mTLS access to the Google Cloud APIs, you can use the following code examples:

###  Go 

     1. Use the following example to create a Go file, such as `golang_test.go`:
            
            package golang_test
            
            import (
                 "io"
                 "log"
                 "testing"
            
                 "cloud.google.com/go/auth/credentials"
                 "cloud.google.com/go/auth/httptransport"
            )
            
            func TestGoExample(t *testing.T) {
            
                 scopes := []string{
                         "https://www.googleapis.com/auth/pubsub", // Scope for Pub/Sub access
                         // Add other scopes as needed
                 }
            
                 dopts := credentials.DetectOptions{
                         Scopes: scopes,
                 }
            
                 // Create httptransport.Options with the scopes
                 opts := &httptransport.Options{
                         DetectOpts: &dopts,
                 }
                 hc, err := httptransport.NewClient(opts)
                 if err != nil {
                         t.Fatalf("NewHTTPClient: %v", err)
                 }
            
                 resp, err := hc.Get("https://pubsub.mtls.googleapis.com/v1/projects/PROJECT_ID/topics")
                 if err != nil {
                         t.Fatalf("Get: %v", err)
                 }
                 t.Logf("Status: %s", resp.Status)
            
                 t.Cleanup(func() {
                        resp.Body.Close()
                 })
            
                 b, err := io.ReadAll(resp.Body)
                 if err != nil {
                        t.Fatal(err)
                 }
                 log.Println(string(b))
            }
            

Replace `PROJECT_ID` with your Google Cloud project ID.

     2. To run a test on a Compute Engine VM, use the following command:
    
    go mod init example.com
    go mod tidy
    go test -v golang_test.go --count=1
    

###  Python 

     1. Use the following example to create a test file, such as `python_test.py`:
            
            import google.auth
            import google.auth.transport.requests
            import requests
            
            def test_python_example():
            # Define the required scopes for your application
            scopes = [
               "https://www.googleapis.com/auth/pubsub",  # Scope for Pub/Sub access
               # Add other scopes as needed
            ]
            
            # Obtain Application Default Credentials (ADC) with the specified scopes
            credentials, _ = google.auth.default(scopes=scopes)
            
            # Create an authorized HTTP session using the ADC credentials
            authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
            
            try:
             # Make a GET request to the Pub/Sub API endpoint
             response = authed_session.get(
                 "https://pubsub.mtls.googleapis.com/v1/projects/PROJECT_ID/topics"
             )
            
             # Check if the request was successful
             response.raise_for_status()  # Raise an exception for error statuses
            
             # Log the response status and content
             print(f"Status: {response.status_code}")
             print(response.text)
            
            except requests.exceptions.RequestException as e:
             print(f"Error making the request: {e}")
            
            if __name__ == "__main__":
            test_python_example()
            

Replace `PROJECT_ID` with your Google Cloud project ID.

     2. To run a test on a Compute Engine VM, complete the following steps:

        1. Set up a Python virtual environment.
        2. Install the required libraries:
               
               pip install google-auth google-auth-httplib2 requests
               

        3. Run the test:
               
               python3 python_test.py
               




## Authorize using plain HTTP requests

To authorize Workload Identity Federation workloads using plain HTTP requests, complete the following steps:

  1. [Obtain a certificate-bound access token](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates#cred-config-access) from Google Cloud Security Token Service through a standard mTLS handshake.

  2. Call the Google Cloud services with the access token you obtained from Security Token Service. This example queries Cloud Storage:
         
         curl --key WORKLOAD_KEY_PATH --cert WORKLOAD_CERTIFICATE_PATH \
          -X GET "https://storage.mtls.googleapis.com/RESOURCE_PATH" \
          -H "Authorization: Bearer $ACCESS_TOKEN"
         

  3. The mTLS binding enforces the use of mTLS. Run the following command to verify that a non-mTLS connection fails with an unauthorized error:
         
         curl -X GET "https://storage.googleapis.com/RESOURCE_PATH" \
          -H "Authorization: Bearer $ACCESS_TOKEN"
         




## List the policy binding

To list the policy binding for Workload Identity Federation, run the following command:

###  gcloud 

The following command lists specific bindings within a given organization, filtering for those that apply to federated principals:
    
    
    gcloud alpha access-context-manager cloud-bindings list \
    --organization=ORG_ID \
    --filter='principal:federatedPrincipal'
    

###  curl 
    
    
    curl -H "X-Goog-User-Project: ${CALLER_PROJECT_ID:?}" -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://accesscontextmanager.googleapis.com/v1alpha/organizations/${ORG_ID:?}/gcpUserAccessBindings?filter=principal%3Afederated_principal"
    

## Update a policy binding

To update a policy binding, complete the following steps:

###  gcloud 
    
    
    gcloud alpha access-context-manager cloud-bindings update \
    --binding=BINDING_ID \
    --organization=ORG_ID \
    --level=NEW_ACCESS_LEVEL_ID
    

###  curl 

Add the new access level to the `request.json` file and run the following command:
    
    
    curl -H "X-Goog-User-Project: ${CALLER_PROJECT_ID:?}" -X PATCH \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
    "https://accesscontextmanager.googleapis.com/v1alpha/organizations/${ORG_ID:?}/gcpUserAccessBindings/${BINDING_ID:?}?updateMask=access_levels"
    

## Delete a policy binding

To delete a policy binding, run the following command:

###  gcloud 
    
    
    gcloud alpha access-context-manager cloud-bindings delete \
    --binding=BINDING_ID \
    --organization=ORG_ID
    

###  curl 
    
    
    curl -H "X-Goog-User-Project: ${CALLER_PROJECT_ID:?}" -X DELETE \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://accesscontextmanager.googleapis.com/v1alpha/organizations/${ORG_ID:?}/gcpUserAccessBindings/${BINDING_ID:?}"
    

## What's next

  * [Troubleshoot certificate-based access for Workload Identity Federation](https://docs.cloud.google.com/access-context-manager/docs/troubleshooting#certificate-based-access-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
