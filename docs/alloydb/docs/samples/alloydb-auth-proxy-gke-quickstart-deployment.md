---
url: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-auth-proxy-gke-quickstart-deployment/
title: Connect from Google Kubernetes Engine with a sidecar proxy \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:47.207886+00:00
---

# Connect from Google Kubernetes Engine with a sidecar proxy  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/samples/alloydb-auth-proxy-gke-quickstart-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Samples ](https://docs.cloud.google.com/alloydb/docs/samples)



#  Connect from Google Kubernetes Engine with a sidecar proxy Stay organized with collections  Save and categorize content based on your preferences. 

This manifest defines a Kubernetes Deployment that runs the Auth Proxy as a sidecar container alongside your application. Use this pattern to provide secure, authorized, and encrypted connections from your application in Google Kubernetes Engine to your database instance.

## Code sample

### YAML
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: <YOUR-DEPLOYMENT-NAME>
    spec:
      selector:
        matchLabels:
          app: <YOUR-APPLICATION-NAME>
      template:
        metadata:
          labels:
            app: <YOUR-APPLICATION-NAME>
        spec:
          serviceAccountName: <YOUR-KSA-NAME>
          containers:
          # Your application container goes here.
          - name: <YOUR-APPLICATION-NAME>
            image: <YOUR-APPLICATION-IMAGE-URL>
            env:
            - name: DB_HOST
              # The port value here (5432) should match the --port flag below.
              value: "localhost:5342"
            - name: DB_USER
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: username
            - name: DB_PASS
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: password
            - name: DB_NAME
              valueFrom:
                secretKeyRef:
                  name: <YOUR-DB-SECRET>
                  key: database
          # The Auth Proxy sidecar goes here.
          - name: alloydb-auth-proxy
            # Make sure you have automation that upgrades this version regularly.
            # A new version of the Proxy is released monthly with bug fixes,
            # security updates, and new features.
            image: gcr.io/alloydb-connectors/alloydb-auth-proxy:1.10.1
            args:
              # If you're connecting over public IP, enable this flag.
              # - "--public-ip"
    
              # If you're connecting with PSC, enable this flag:
              # - "--psc"
    
              # If you're using auto IAM authentication, enable this flag:
              # - "--auto-iam-authn"
    
              # Enable structured logging with Google's LogEntry format:
              - "--structured-logs"
    
              # Listen on localhost:5432 by default.
              - "--port=5432"
              # Specify your instance URI, e.g.,
              # "projects/myproject/locations/us-central1/clusters/mycluster/instances/myinstance"
              - "<INSTANCE-URI>"
    
            securityContext:
              # The default AlloyDB Auth Proxy image runs as the "nonroot" user and
              # group (uid: 65532) by default.
              runAsNonRoot: true
            # You should use resource requests/limits as a best practice to prevent
            # pods from consuming too many resources and affecting the execution of
            # other pods. You should adjust the following values based on what your
            # application needs. For details, see
            # https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
            resources:
              requests:
                # The proxy's memory use scales linearly with the number of active
                # connections. Fewer open connections will use less memory. Adjust
                # this value based on your application's requirements.
                memory: "2Gi"
                # The proxy's CPU use scales linearly with the amount of IO between
                # the database and the application. Adjust this value based on your
                # application's requirements.
                cpu:    "1"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=alloydbforpostgresql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
