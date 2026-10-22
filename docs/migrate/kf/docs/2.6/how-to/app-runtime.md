---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/app-runtime/
title: App runtime \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:03.276537+00:00
---

# App runtime  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/app-runtime/

Version 2.6

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.6/reference)



Send feedback 

#  App runtime Stay organized with collections  Save and categorize content based on your preferences. 

The app runtime is the environment apps are executed in.

| Buildpack Apps | Container Image Apps  
---|---|---  
System libraries | Provided by the Stack | Provided in the container  
Network access | Full access through Envoy sidecar | Full access through Envoy sidecar  
File system | Ephemeral storage | Ephemeral storage  
Language runtime | Supplied by the Stack or Buildpack | Built into the container  
User | Specified by the Stack | Specified on the container  
Isolation mechanism | Kubernetes Pod | Kubernetes Pod  
DNS | Provided by Kubernetes | Provided by Kubernetes  
  
## Environment variables

Environment variables are injected into the app at runtime by Kubernetes. Variables are added based on the following order, where later values override earlier ones with the same name:

  1. Space (set by administrators)
  2. App (set by developers)
  3. System (set by Kf)



Kf provides the following system environment variables:

Variable | Purpose  
---|---  
`CF_INSTANCE_ADDR` | The cluster-visible IP:PORT of the App instance.  
`CF_INSTANCE_GUID` | The UUID of the App instance.  
`INSTANCE_GUID` | Alias of `CF_INSTANCE_GUID`.  
`CF_INSTANCE_INDEX` | The index number of the App instance, this will ALWAYS be 0.  
`INSTANCE_INDEX` | Alias of `CF_INSTANCE_INDEX`.  
`CF_INSTANCE_IP` | The cluster-visible IP of the App instance.  
`CF_INSTANCE_INTERNAL_IP` | Alias of `CF_INSTANCE_IP`  
`VCAP_APP_HOST` | Alias of `CF_INSTANCE_IP`  
`CF_INSTANCE_PORT` | The cluster-visible port of the App instance. In Kf this is the same as `PORT`.  
`DATABASE_URL` | The first URI found in a `VCAP_SERVICES` credential.  
`LANG` | Required by Buildpacks to ensure consistent script load order.  
`MEMORY_LIMIT` | The maximum amount of memory in MB the App can consume.  
`PORT` | The port the App should listen on for requests.  
`VCAP_APP_PORT` | Alias of `PORT`.  
`VCAP_APPLICATION` | A JSON structure containing App metadata.  
`VCAP_SERVICES` | A JSON structure specifying bound services.  
  
Service credentials from bound services get injected into Apps via the `VCAP_SERVICES` environment variable. The variable is a valid JSON object with the following structure.

### VCAPServices

A JSON object where the keys are Service labels and the values are an array of `VCAPService`. The array represents every bound service with that label. [User provided services](https://docs.cloud.google.com/migrate/kf/docs/2.6/concepts/user-provided-services) are placed under the label `user-provided`.

**Example**
    
    
    {
      "mysql": [...],
      "postgresql": [...],
      "user-provided": [...]
    }
    

### VCAPService

This type represents a single bound service instance.

**Example**
    
    
    {
      "binding_name": string,
      "instance_name": string,
      "name": string,
      "label": string,
      "tags": string[],
      "plan": string,
      "credentials": object
    }
    

**Fields**

Field | Type | Description  
---|---|---  
`binding_name` | `string` | The name assigned to the service binding by the user.  
`instance_name` | `string` | The name assigned to the service instance by the user.  
`name` | `string` | The `binding_name` if it exists; otherwise the `instance_name`.  
`label` | `string` | The name of the service offering.  
`tags` | `string[]` | An array of strings an app can use to identify a service instance.  
`plan` | `string[]` | The service plan selected when the service instance was created.  
`credentials` | `object` | The service-specific credentials needed to access the service instance.  
**Note:** Use the `tags` field to discover services in your App rather than filtering by plan/label so you can swap implementations and providers per environment.**Note:** The `credentials` field is _often_ an object with string keys and values. However, the values are allowed to be [any type](https://github.com/openservicebrokerapi/servicebroker/blob/v2.15/spec.md#body-9).

### VCAP_APPLICATION

The`VCAP_APPLICATION` environment variable is a JSON object containing metadata about the App.

**Example**
    
    
    {
      "application_id": "12345",
      "application_name": "my-app",
      "application_uris": ["my-app.example.com"],
      "limits": {
        "disk": 1024,
        "mem": 256
      },
      "name": "my-app",
      "process_id": "12345",
      "process_type": "web",
      "space_name": "my-ns",
      "uris": ["my-app.example.com"]
    }
    

**Fields**

Field | Type | Description  
---|---|---  
`application_id` | `string` | The GUID identifying the App.  
`application_name` | `string` | The name assigned to the App when it was pushed.  
`application_uris` | `string[]` | The URIs assigned to the App.  
`limits` | `object` | The limits to disk space, and memory permitted to the App. Memory and disk space limits are supplied when the App is deployed, either on the command line or in the App manifest. Disk and memory limits are represented as integers, with an assumed unit of MB.  
`name` | `string` | Identical to `application_name`.  
`process_id` | `string` | The UID identifying the process. Only present in running App containers.  
`process_type` | `string` | The type of process. Only present in running App containers.  
`space_name` | `string` | The human-readable name of the Space where the App is deployed.  
`uris` | `string[]` | Identical to `application_uris`.  
  
**Missing Fields**

Some fields in `VCAP_APPLICATION` that are in Cloud Foundry are currently not supported in Kf.

Besides CF-specific and deprecated fields (`cf_api`, `host`, `users`) the fields that are not supported in Kf are:

  * `application_version` (identical to `version`)
  * `organization_id`
  * `organization_name`
  * `space_id`
  * `start` (identical to `started_at`)
  * `started_at_timestamp` (identical to `state_timestamp`)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
