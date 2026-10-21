---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/k8s-secrets/
title: Storing data in a Kubernetes secret \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:34:10.578932+00:00
---

# Storing data in a Kubernetes secret  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/k8s-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Storing data in a Kubernetes secret Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/k8s-secrets.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/k8s-secrets.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/k8s-secrets.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/k8s-secrets.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/k8s-secrets.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/k8s-secrets.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/k8s-secrets.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/k8s-secrets.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/k8s-secrets.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/k8s-secrets.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/k8s-secrets.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/k8s-secrets.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/k8s-secrets.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/k8s-secrets.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/k8s-secrets.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/k8s-secrets.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/k8s-secrets.html)



This topic explains how to store sensitive data in a [ Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) and retrieve the data from flow variables in an API proxy flow. 

##  Introduction 

There are times when you want to store data for retrieval at runtime—non-expiring data that shouldn't be hard-coded in your API proxy logic. One option is to use the hybrid [key-value map (KVM) feature](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps). If you are already using Kubernetes for secret management in a custom vault for sensitive data, you might want to consider using the Kubernetes secret feature described in this topic. Just like with KVM data, you can access the Kubernetes secret data in API proxy flow variables. 

##  What kinds of data can be stored in a Kubernetes secret? 

Apigee hybrid limits you to storing the following kinds of data files in a Kubernetes secret. They include:

File format | Supported file extensions  
---|---  
TLS certificate and key files | `*.crt`, `*.key`, and `*.pem`  
Property files | `*.properties`  
  
Property files are files that contain key/value pairs. For example: 
    
    
    username=admin
    password=1f2d1e2e7df

##  Creating a Kubernetes secret 

This section explains how to create a Kubernetes secret for storing sensitive data in the cluster.

**Note:** The Kubernetes secret is environment scoped only; organization and proxy scoped secrets are not supported.

  1. Create the file or files that you wish to store in the Kubernetes secret. The files must be one of the supported formats with the file extensions listed in What kinds of data can be stored in a Kubernetes secret.
  2. Execute the `kubectl create secret generic` command. For example: 
         
         kubectl -n namespace create secret generic org-env-policy-secret \
           --from-file=filepath/prop-file.properties \
           --from-file=filepath/key-file.key \
           --from-file="filepath/cert-file.pem
         

Where: 

     * namespace: The Kubernetes namespace where your runtime components are deployed.
     * org: Your Apigee organization name.
     * env: The name of an environment in your org.
     * filepath: The path to the file you wish to include in the secret. You must specify at least one file to include in the secret.
     * prop-file: The name of a properties file to include in the secret.
     * key-file: The name of a TLS key file to include in the secret.
     * cert-file: The name of a TLS certificate file to include in the secret.

You can include one or more files in the secret. For example: 
    
    kubectl -n apigee create secret generic myorg-test-policy-secret \
      --from-file="$policy_secrets_path"/credential.properties \
      --from-file="$policy_secrets_path"/secrets.properties \
      --from-file="$policy_secrets_path"/public.key \
      --from-file="$policy_secrets_path"/fullchain.pem

After creation, it may take up to 90 seconds for the change to be reflected in all the clusters. The message processors poll for secret changes every 30 seconds. If they detect a change, the cache is updated. 




##  Retrieving data from a secret 

Once the secret is created and available (usually about 90 seconds after creation), you can access the secret data in a flow variable in an API proxy flow in the organization/environment in which the secret is stored. For example, assume your secret contains a `*.properties` file called `credentials.properties` with an API key in it, as follows: 
    
    
    apikey=OrxYQptBMlY1TqmiGLTtyFiaLzzrD25Z

You can then retrieve the API key from a flow variable using a policy like [ Assign Message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy). For example:
    
    
    <AssignMessage name="assignvariable-2">
      <AssignVariable>
        <Name>my-apikey</Name>
        <Ref>private.secret.credential.properties.apikey</Ref>
      </AssignVariable>
    </AssignMessage>

The variable name referenced in the `Ref` element, `private.secret.credential.properties.apikey`, is composed of these parts: 

Variable name part | Description  
---|---  
`private.secret` | The fixed namespace of the variable. All Kubernetes secrets stored in the hybrid cluster share this namespace.  
`credential.properties` |  The name of a file stored in the Kubernetes secret.  **Note:** This filename must be in lowercase letters.   
`apikey` | The name of a key stored in a properties file.  
  
In this example, the Assign Message policy retireves the `apikey` value `OrxYQptBMlY1TqmiGLTtyFiaLzzrD25Z` and stores it in the flow variable `my-apikey`. 

###  Updating a secret 

Because `kubectl` does not support updating Kubernetes secrets, you must first delete the existing secret and recreate it by following the steps in Creating a Kubernetes secret. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
