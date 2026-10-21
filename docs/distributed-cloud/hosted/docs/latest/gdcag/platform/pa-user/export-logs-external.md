---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/export-logs-external/
title: Export logs to a SIEM system \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:05.105110+00:00
---

# Export logs to a SIEM system  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/export-logs-external/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Export logs to a SIEM system Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to export logs from Google Distributed Cloud (GDC) air-gapped to an external Security Information and Event Management (SIEM) system. This integration allows for centralized log analysis and enhanced security monitoring.

The core of log export involves deploying a `SIEMOrgForwarder` custom resource. This resource acts as a configuration file, specifying the details of the external SIEM instance designated to receive the logs. By defining these parameters within the `SIEMOrgForwarder` file, administrators can establish a streamlined and secure log export pipeline.

## Before you begin

To get the permissions that you need to manage `SIEMOrgForwarder` custom resources, ask your Organization IAM Admin to grant you one of the associated SIEM Export Org roles.

Depending on the level of access and permissions you need, you might obtain creator, editor, or viewer roles for this resource in your project namespace. For more information, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-iam-permissions).

After obtaining the necessary permissions, complete these steps prior to exporting logs to an external SIEM system:

  1. **Establish connectivity** : Ensure a connection exists between GDC and the external SIEM destination. If needed, collaborate with the Infrastructure Operator (IO) to establish an uplink connection to your customer network.

  2. **Set environment variables** : Set the following environment variables to run the commands from this page:

     * The path of the kubeconfig file:
           
           export KUBECONFIG=KUBECONFIG_PATH
           

Replace `KUBECONFIG_PATH` with the path to the kubeconfig file for the Management API server.

     * Your project namespace:
           
           export PROJECT_NAMESPACE=PROJECT_NAMESPACE
           




## Configure log export

**Important:** The logging stack limits the number of retries to establish a connection with the SIEM solution and send an audit log. The Infrastructure Operator can manually configure the exact number of retries, but the default is set to _five_. If the connection fails after the specified retries, the logging stack doesn't send audit logs to the SIEM solution.

Export logs to an external SIEM system:

  1. Provide a token to connect the logging stack to the SIEM system. To perform this action, you must create a secret in your project namespace to store the token in case of Splunk and password in case of Elastic SIEM:
         
         cat <<EOF | kubectl --kubeconfig=${KUBECONFIG} apply -f -
         apiVersion: v1
         kind: Secret
         metadata:
           name: SECRET_NAME
           namespace: ${PROJECT_NAMESPACE}
         type: Opaque
         stringData:
           SECRET_FIELD: FIELD_VALUE
         EOF
         

Replace the following:

     * `SECRET_NAME`: the name of your secret.
     * `SECRET_FIELD`: the name of the field where you want to store the secret. It is username in case of Elastic.
     * `FIELD_VALUE`: FIELD_VALUE is token in case of Splunk and password for Elastic.
     * `TOKEN`: your token.
**Note:** Consider using separate tokens for audit and operational logs, deploying two secrets accordingly. You must reference the corresponding secret name in the `SIEMOrgForwarder` custom resource.
  2. Deploy the `SIEMOrgForwarder` custom resource in your project namespace. You must specify the log type by choosing between audit or operational logs. To configure the log export for both log types, you must deploy a `SIEMOrgForwarder` resource for each type.

**Important:** The `SIEMOrgForwarder` custom resource must be in the same namespace as the `Secret` you created in the previous step.

> [!WARNING] From release 1.17, specifying `splunkOutputs` directly under `spec` is not supported. You must use `splunkOutputs` under the `destinations` field.

The following example shows how to apply a configuration to a `SIEMOrgForwarder` custom resource for Splunk:
         
         cat <<EOF | kubectl --kubeconfig=${KUBECONFIG} apply -f -
           apiVersion: logging.gdc.goog/v1
           kind: SIEMOrgForwarder
           metadata:
             name: SIEM_ORG_FORWARDER
             namespace: ${PROJECT_NAMESPACE}
           spec:
             source: LOG_TYPE
             destinations:
               splunkOutputs:
                 - host: SIEM_HOST
                   token:
                     name: SECRET_NAME
                     field: SECRET_FIELD
                   tls: "TLS"
                   netConnectTimeout: NET_CONNECT_TIMEOUT
           EOF
         

Replace the following:

     * `SIEM_ORG_FORWARDER`: the name of the `SIEMOrgForwarder` definition file.
     * `LOG_TYPE`: the log type you are exporting. Accepted values are `audit` and `operational`.
     * `SIEM_HOST`: the name of the SIEM host.
     * `SECRET_NAME`: the name of your secret.
     * `SECRET_FIELD`: the name of the field where you stored the secret.
     * `TLS`: the status of the Transport Layer Security (TLS). Accepted values are `"On"` and `"Off"`.
     * `NET_CONNECT_TIMEOUT`: the maximum time in seconds to wait for a connection to be established. For example, a value of `180` means to wait 180 seconds.

The following example shows how to apply a configuration to a `SIEMOrgForwarder` custom resource for Elastic:
    
    cat <<EOF | kubectl --kubeconfig=${KUBECONFIG} apply -f -
      apiVersion: logging.gdc.goog/v1
      kind: SIEMOrgForwarder
      metadata:
        name: SIEM_ORG_FORWARDER
        namespace: ${PROJECT_NAMESPACE}
      spec:
        source: LOG_TYPE
        destinations:
          elasticOutputs:
            - host: SIEM_HOST
              port: SIEM_PORT
              http_credential:
                http_user: HTTP_USER_NAME
                http_passwd: SECRET_NAME
              tls: "TLS"
              netConnectTimeout: NET_CONNECT_TIMEOUT
              index: INDEX
      EOF
    

Replace the following:

     * `SIEM_ORG_FORWARDER`: the name of the `SIEMOrgForwarder` definition file.
     * `LOG_TYPE`: the log type you are exporting. Accepted values are `audit` and `operational`.
     * `SIEM_HOST`: the name of the SIEM host.
     * `SIEM_PORT`: the port of the SIEM instance.
     * `HTTP_USER_NAME`: the username of the SIEM instance.
     * `SECRET_NAME`: the name of your secret.
     * `TLS`: the status of the Transport Layer Security (TLS). Accepted values are `"On"` and `"Off"`.
     * `NET_CONNECT_TIMEOUT`: the maximum time in seconds to wait for a connection to be established. For example, a value of `180` means to wait 180 seconds.
     * `INDEX`: the index for the Elastic instance. If not specified, the log type (`audit` or `operational`) will be used. This field is optional.
  3. Verify the status of the deployed `SIEMOrgForwarder` custom resource:
         
         kubectl --kubeconfig=${KUBECONFIG} describe siemorgforwarder/SIEM_ORG_FORWARDER \
               -n ${PROJECT_NAMESPACE}
         

According to the log type, check for the following status:

     * **Audit logs** : Check the `AuditLoggingReady` status.
     * **Operational logs** : Check the `OperationalLoggingReady` status.

**Note:** It might take a few minutes for changes to propagate and the status to update.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
