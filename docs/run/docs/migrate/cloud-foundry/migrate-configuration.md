---
url: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-configuration/
title: Migrate Cloud Foundry configurations to Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:25.517707+00:00
---

# Migrate Cloud Foundry configurations to Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Migrate Cloud Foundry configurations to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** You must have access to the build configuration and source code for the application you want to migrate.

You must complete the configuration migration process for each Cloud Foundry application you are migrating to Cloud Run. The configuration migration consists of the following:

  * Converting a Cloud Foundry `manifest.yaml` to a Cloud Run `service.yaml`.
  * Attaching any backing services to the application for deployment to Cloud Run.
  * Deploying your application to a Cloud Run service.



## Convert `manifest.yaml` to `service.yaml`

You must convert a Cloud Foundry manifest and/or `cf` CLI flags into the equivalent Cloud Run service definition YAML.

Cloud Run requires each application to have its own separate service YAML file. To migrate an application in your Cloud Foundry manifest to a service YAML file:

  1. Gather the properties listed in the following table for your application. Properties that are not modified at the application level may have been overridden by global Cloud Foundry platform configurations. Refer to documentation provided by your platform administrators to get the actual values.

Application Property | `cf` CLI v6 flag(s) | Description   
---|---|---  
`name` | `NAME` argument | The application's unique name in Cloud Foundry.  
`command` | `-c` | A command that'll be executed in `/bin/sh` or `/bin/bash`  
`disk_quota` | `-k` |  The amount of disk that'll be assigned to the application.   
Valid units are: `M`, `MB`, `G` , `r B` **Likely default** : 1G  
`docker.image` | `--docker-image`, `-o` | The image that contains the application to run.  
`health-check-http-endpoint` | N/A |  The endpoint used to determine HTTP health if the health check type is HTTP. **Default** : `/`  
`health-check-invocation-timeout` | N/A |  Time in seconds between individual port and HTTP based health checks. **Default:** 1  
`health-check-type` | `--health-check-type`, `-u` |  Type of health check to perform on the application. Valid values are: `port`, `http`, `none`, `process`. **Default** : `port`  
`instances` | `-i` |  Number of instances of the app that Cloud Foundry will run. **Default:** 1  
`memory` | `-m` |  The per-instance memory limit for the application. Valid units are: `M`, `MB`, `G` , or `GB` **Likely default** : 1G  
`timeout` | `-t` |  Number of seconds allowed between app startup and the first healthy health check. **Likely default** : 60  
  2. Gather the following information for your Google Cloud project and Cloud Run setup:

Property | Description  
---|---  
`project_number` | The project number of the Google Cloud Project you want to deploy to.  
`region` | The region you want to deploy your app to.  
`vpc-access-connector` | The VPC connector name your platform administrator wants applications on.  
`vpc-access-egress` | The VPC egress name your platform administrator wants applications on.  
`custom-audiences` | Custom audiences that can authenticate to your application.  
`serviceAccountName` | The identity your application will act as in Google Cloud.  
`image` | The application image you produced in the previous step.  
  3. Populate the following template into a `service.yaml` file at the root of your project



    
    
    apiVersion: serving.knative.dev/v1
    kind: Service
    metadata:
      # Set this to be the name of your app
      name: "APP_NAME"
      # Set this to be the project number of the project you're deploying to.
      namespace: "PROJECT_NUMBER"
      labels:
        # Set this to be the region you're deploying in.
        cloud.googleapis.com/location: REGION
        migrated-from: cloud-foundry
      annotations:
        run.googleapis.com/ingress: internal-and-cloud-load-balancing
    spec:
      template:
        metadata:
          annotations:
            # Set to the greater of 1 or the `instances` attribute.
            autoscaling.knative.dev/minScale: '1'
            # Set to the greater of 1 or the `instances` attribute.
            autoscaling.knative.dev/maxScale: '1'
            run.googleapis.com/cpu-throttling: CPU_ALLOCATION
            run.googleapis.com/startup-cpu-boost: 'true'
            # Set to true if you rely on sticky sessions. These will be turned
            # on in Cloud Foundry if the server sends a JSESSIONID cookie back
            # on responses.
            run.googleapis.com/sessionAffinity: 'false'
            run.googleapis.com/execution-environment: gen2
            # Set the following values to match what your platform administrator recommends.
            run.googleapis.com/vpc-access-connector: ADMINISTRATOR_PROVIDED
            run.googleapis.com/vpc-access-egress: ADMINISTRATOR_PROVIDED
            run.googleapis.com/custom-audiences: ADMINISTRATOR_PROVIDED
        spec:
          # CF doesn't limit, but CR has a max of 1000.
          containerConcurrency: 1000
          # Default value for gorouter in PCF.
          timeoutSeconds: 900
          # Set the following value to match what your platform administrator recommends.
          serviceAccountName: ADMINISTRATOR_PROVIDED
          containers:
          - name: user-container
            # Set the following value to either:
            # - The image you built for your application in the last section of the guide.
            # - The docker.image attribute of your app's configuration if it's a Docker app.
            image: IMAGE
            # Set `command` based on the following rules:
            # - If your app has no `command` attribute: null.
            # - If your app has a docker.image attribute: ['/bin/sh', '-c']
            # - Otherwise: ['/bin/bash', '-c']
            command: null
            # Set `args` based on the following rules:
            # - If your app has no `command` attribute: null.
            # - If your app has a `command` attribute: ['value of command']
            args: null
            ports:
              # Set name based on the following rules:
              # - If your app is HTTP/2 or gRPC: "h2c"
              # - Else: "http1"
            - name: HTTP1_OR_H2C
              containerPort: 8080
            env:
              # For each key/value pair in your space's running environment variable groups,
              # which can be retried by running `cf running-environment-variable-group`,
              # add the following:
            - name: KEY
              value: VALUE
              # For each key/value pair in your manifest's `env` map, add the following:
            - name: KEY
              value: VALUE
              # Populate MEMORY_LIMIT with the amount of memory supplied to this instance
              # in MiB with 'M' as a suffix.
            - name: MEMORY_LIMIT
              value: '0M'
              # Set the following values in the JSON below:
              # - `application_name` and `name` to match metadata.name in this file.
              # - `application_uris` and `uris` to be the URI you want to assign the app on the
              #    load balancer.
              # - `limits.disk` to be the amount (in MiB) of disk assigned to your app.
              #   The amount will be in the `disk_quota` attribute of the CF manifest, or a
              #   default value for your cluster, typically 1GiB.
              # - `limits.mem` to be the amount (in MiB) of memory assigned to your app.
              #   The amount will be in your `memory` attribute of the CF manifest, or a
              #   default value for your cluster, typically 1GiB.
              # - `space_name` to be the value of metadata.space in this file.
            - name: VCAP_APPLICATION
              value: |-
                      {
                        "application_id": "00000000-0000-0000-0000-000000000000",
                        "application_name": "app-name",
                        "application_uris": [],
                        "limits": {
                          "disk": 1024,
                          "mem": 256
                        },
                        "name": "app-name",
                        "process_id": "00000000-0000-0000-0000-000000000000",
                        "process_type": "web",
                        "space_name": "none",
                        "uris": []
                      }
            resources:
              limits:
                # Set memory limit to be the sum of the memory and disk assigned to your app in CF.
                # 
                # Disk amount will be in the `disk_quota` attribute of the CF manifest, or a
                # default value for your cluster, typically 1GiB.
                #
                # Memory will be in your `memory` attribute of the CF manifest, or a
                # default value for your cluster, typically 1GiB.
                memory: MEMORY_LIMIT
                # Set cpu according to the following calculation:
                #
                # 1. Take the amount of memory in your `memory` attribute of the CF
                #    manifest, or a default value for your cluster, typically 1GiB.
                # 2. Divide that by the total amount of memory on the underlying BOSH VM.
                # 3. Multiply that by the total number of CPUs on the BOSH VM.
                # 4. Find the nearest valid value based on the rules in:
                #    https://docs.cloud.google.com/run/docs/configuring/services/cpu#setting
                cpu: CPU_LIMIT
            # If `health-check-type` is "process" or "none", delete the startupProbe section.
            startupProbe:
              # If `health-check-type` is "port" or blank, delete the httpGet section.
              httpGet:
                # Set to be the value of `health-check-http-endpoint` or / if blank.
                path: CHECK_PATH
                port: 8080
              # If `health-check-type` is "http", delete the tcpSocket section.
              tcpSocket:
                port: 8080
              # Set to the value of `health-check-invocation-timeout` or 1
              timeoutSeconds: 1
              # Set failure threshold to be the following calculation:
              #
              # 1. Take the `timeout` from the CF manifest, use 60 if unset.
              # 2. Divide by 2.
              # 3. Round up to the nearest integer.
              failureThreshold: 1
              successThreshold: 1
              periodSeconds: 2
            # If `health-check-type` is "process" or "none", delete the livenessProbe section.
            livenessProbe:
              # If `health-check-type` is "port" or blank, delete the httpGet section.
              httpGet:
                # Set to be the value of `health-check-http-endpoint` or / if blank.
                path: CHECK_PATH
                port: 8080
              # If `health-check-type` is "http", delete the tcpSocket section.
              tcpSocket:
                port: 8080
              # Set to the value of `health-check-invocation-timeout` or 1.
              timeoutSeconds: 1
              failureThreshold: 1
              successThreshold: 1
              periodSeconds: 30
      traffic:
      - percent: 100
        latestRevision: true
    

## Attach any backing services

You must construct a `VCAP_SERVICES` environment variable to allow for service injection and discovery by your Cloud Foundry application, such as Spring or Steeltoe. You need to do this for each application you are migrating. Refer to the documentation for [Cloud Foundry VCAP_SERVICES](https://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#VCAP-SERVICES) for more information.

If your application is already running in Cloud Foundry and you want to attach to the same services in Cloud Run, you can use your existing environment variable. Otherwise, you'll need to create a new `VCAP_SERVICES`.

To configure the `VCAP_SERVICES` environment variable:

  1. For an existing `VCAP_SERVICES`:

     1. Try getting the `VCAP_SERVICES` environment variable by running `cf env APP_NAME`.
     2. If that doesn't work: 
        1. Connect to your application in Cloud Foundry: `cf ssh APP_NAME`
        2. Run the `env` command and get the output of `VCAP_SERVICES`.
        3. Exit the SSH session by running `exit`.
     3. Save the `VCAP_SERVICES` value into a new file called `vcap.json`.
  2. If you want to add services or connect to different services than in Cloud Foundry, create a new `VCAP_SERVICES`:

     1. In a text editor create an empty JSON map `{}`
     2. For each service you want to add, do the following:
     3. Refer to the documentation for the library your app uses to parse `VCAP_SERVICES` for the type you want to add to understand how it discovers the binding.
     4. Add a key to the map with the name of the service provider if one doesn't already exist, this is usually something like `mysql`, `postgresql`, or `elasticsearch`. Set the value to be an empty array:
     5. Add an object to the array with the following properties:

        1. Metadata that isn't usually used to discover/bind services:

           * `binding_name`, a string representing the resource that grants your application permissions on the service. This could be a username for a database, a firewall rule, a service account name, or something else.
           * `instance_name`, a string representing the name of the backing service. This could be the name of your database, a random value, or a sentinel value for a global service.
           * `name`, The `binding_name` if it exists; otherwise the `instance_name`. This value isn't usually important.
           * `label`, The value of the key in the `VCAP_SERVICES` map this binding is nested under.
           * `plan`, the name of the service plan. Examples include: "user-provided", "high-availability".
        2. Values that are often used to discover/bind services:

           * `tags` A list of tags to help libraries find compatible services. This often includes the common name for the service e.g. `mysql` for MySQL and MariaDB, `redis` for Redis or Cloud Memorystore, or `postgres` for Postgres compatible databases.
           * `credentials` An object containing credentials used by the client library to perform the connection. Most client libraries rely on a `uri` field that contains the service's standard URI or JDBC format.
     6. Save the contents as `vcap.json`.




### Attach credentials to your Cloud Run resource

To attach credentials:

  1. Create a secret to hold your`VCAP_SERVICES` environment variable contents and take note of the version output by the command:
         
         gcloud secrets create APP_NAME-vcap \
           --replication-policy="automatic" \
           --data-file=vcap.json
         

  2. Grant your application's service account permission to read the secret:
         
         gcloud secrets add-iam-policy-binding APP_NAME-vcap \
           --member="serviceaccount:app-service-account" \
           --role="roles/secretmanager.secretAccessor"
         

  3. Add the following environment variable to your application `service.yaml` in the `spec.template.spec.containers[0].env array` :
         
         - name: VCAP_SERVICES
           valueFrom: 
             secretKeyRef:
               key: Version output by step 1
               name: APP_NAME-vcap
         




### Templates for common backing services

The following sections provide information about commonly used backing services

#### MySQL

MySQL libraries usually expect the tag `mysql`. It is common to include the following keys in `credentials`:

  * **`uri`** template: `mysql://username:password@host:port/dbname`. The [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/connecting-using-uri-or-key-value-pairs.html) can help with creating a URI string. The port is usually `3306`.
  * **`username`** The connection username, required by some libraries even if included in `uri`
  * **`password`** The connection password, required by some libraries even if included in `uri`



#### Redis

Redis libraries usually expect the tag `redis`. It's common to include the following keys in `credentials`:

  * **`uri`** Template: `redis://:password@host:port/dbunumber`.



The [IANA Redis URI documentation](https://www.iana.org/assignments/uri-schemes/prov/redis) can help with creating a URI string. The port is usually `6379`.

#### RabbitMQ

RabbitMQ libraries usually expect the tag `rabbitmq` and the following keys in `credentials`:

  * **`uri`** Template: `amqp://username:password@host:port/vhost?query`. 



The [RabbitMQ documentation](https://www.rabbitmq.com/uri-spec.html) can help with creating a URI string. The port is usually `5672`.

#### User provided services

User provided services are a special type of service in Cloud Foundry that allows you to inject any credentials. The label is always `user-provided`. The tags are the values passed in to `cf create-user-provided-service` via the `-t` flag, and the credentials are the contents of the `-p` flag.

## Deploying your application

To deploy the fully migrated Cloud Foundry application to a Cloud Run service:

  1. If you haven't already done so, [set up your Cloud Run environment](https://docs.cloud.google.com/run/docs/setup).

  2. Run the command
         
         gcloud run services replace service.yaml
         

Wait a few moments until the deployment is complete. On success, the command line displays the service URL.

  3. Visit your deployed service by opening the service URL in a web browser.




Congratulations! You have just migrated your Cloud Foundry application to Cloud Run

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
