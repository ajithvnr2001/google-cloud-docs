---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-credential-rotation/
title: Troubleshooting Cassandra credential rotation \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:28.689389+00:00
---

# Troubleshooting Cassandra credential rotation  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-credential-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Troubleshooting Cassandra credential rotation Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

During multi-region Cassandra credential rotation in Apigee hybrid, after the first region is rotated, rotations in subsequent regions fail and errors are logged in the secret rotation pod logs. 

## Error message

You see the following in the logs:
    
    
    failed to run secret rotation: failed to create new users: failed to create new users

## Workaround for Known Issue 397693324

### Diagnosis

The `SecretRotation` resource indicates a failure in the `Status` field: 
    
    
    Status:
      Message:  initiated automated rollback
      State:    error

The secret rotation job pod logs contain the following error: 
    
    
    failed to run secret rotation: failed to create new users: failed to create new users

The `create-new-users-job` pod logs contain the following error: 
    
    
    Error creating clients with updated password: gocql: unable to create session: unable to discover protocol version: Provided username cassandra and/or password are incorrect

### Resolution

Perform the following steps. 

  1. In every region except the first, update the default Cassandra user (`cassandra`) password to the **new** rotated value in the **old** `Secret`. 
         
         apiVersion: v1
             kind: Secret
             metadata:
               name: OLD_SECRET_NAME   # oldSecretRef
               namespace: APIGEE_NAMESPACE
             type: Opaque
             data:
               default.password: NEW_DEFAULT_PASSWORD   #base64-encoded string
               admin.user: OLD_ADMIN_USERNAME   #base64-encoded string
               admin.password: OLD_ADMIN_PASSWORD   #base64-encoded string
               dml.user: OLD_DML_USERNAME   #base64-encoded string
               dml.password: OLD_DML_PASSWORD   #base64-encoded string
               ddl.user: OLD_DDL_USERNAME   #base64-encoded string
               ddl.password: OLD_DDL_PASSWORD   #base64-encoded string
               jmx.user: OLD_JMX_USERNAME   #base64-encoded string
               jmx.password: OLD_JMX_PASSWORD   #base64-encoded string
               jolokia.user: OLD_JOLOKIA_USERNAME   #base64-encoded string
               jolokia.password: OLD_JOLOKIA_PASSWORD   #base64-encoded string
               

  2. Apply the updated `Secret`: 
         
         kubectl apply -f OLD_SECRET_FILE

  3. Continue with the normal rotation process and it should succeed. 




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  * In addition to the usual data you might be asked to provide, collect the logs from all the secret rotation pods. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
