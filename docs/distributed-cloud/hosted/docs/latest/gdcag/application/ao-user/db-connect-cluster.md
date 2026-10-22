---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-connect-cluster/
title: Connect to a database cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:54.199408+00:00
---

# Connect to a database cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-connect-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Connect to a database cluster Stay organized with collections  Save and categorize content based on your preferences. 

By default, a database cluster only allows connection from within the [user cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy#cluster) and the same project.

To enable connections to all database clusters in your project from another project, see [Enable cross-project connections](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-cross-project-connect).

To enable connections to a database cluster from IP addresses outside your GDC organization, see [Enable external connections](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-external-project-connect).

Sign in to the GDC console with an account bound to the Project DB Admin role to find the following information for connecting to your database cluster. This information is in the **Connectivity** section of the **Database Service** page.

These steps include an example for connecting to the database using `psql`. The exact steps will vary depending on the client software you choose.

### Console

  1. Navigate to the **Connectivity** section of the **Database Service** page for the database cluster. This page includes:

     * The password of the administrator account (the username is `dbsadmin`)
     * Hostname and port number of the database cluster's primary endpoint
     * If the database cluster allows external connection from outside of the organization.
     * A `psql` command for connecting to the cluster
     * A link to download the certificate authority (CA) certificate of the database cluster
  2. Download the CA certificate from the GDC console in the **Connectivity** section of the **Database Service** page for your database cluster.

  3. Configure your client to use the CA certificate to verify the database. For `psql` clients, set the `PGSSLROOTCERT` env variable to the path of the certificate file and the `PGSSLMODE` env variable to your preference:
         
         export PGSSLROOTCERT=path/to/accounts_cert.pem
         export PGSSLMODE="verify-full"
         

  4. Connect to the database from your client software. If you're using `psql`, run the following command:
         
         PGPASSWORD=DB_PASSWORD psql -h DB_HOSTNAME -p PORT -U USERNAME -d postgres
         




Replace the following variables:

  * `path/to/`: the path to the `accounts_cert.pem` certificate.
  * `DB_PASSWORD`: the password from the console.
  * `DB_HOSTNAME`: the database hostname from the console.
  * `DB_PORT`: the database port number from the console.
  * `DB_USERNAME`: the database username from the console.



###  API 

  1. Retrieve the database endpoint from the database cluster status:
         
         kubectl get dbcluster.postgresql.dbadmin.gdc.goog DBCLUSTER_NAME -n USER_PROJECT -o=jsonpath='{.status.primary.url}'
         

  2. Download the CA certificate from the Kubernetes secret:
         
         kubectl get secret dbs-certificates -n USER_PROJECT -o json | jq -r '.data."dbs-pg-cert-DBCLUSTER_NAME"' | base64 -d > path/to/ca.crt
         

  3. Configure your client to use the CA certificate to verify the database. For `psql` clients, you can set the `PGSSLROOTCERT` env variable to the path of the certificate file and the `PGSSLMODE` env variable to your preference:
         
         export PGSSLROOTCERT=path/to/ca.crt
         export PGSSLMODE="verify-full"
         

  4. Connect to the database from your client software. If you're using `psql`, run the following command:
         
         PGPASSWORD=DB_PASSWORD psql -h DB_HOSTNAME -p DB_PORT -U DB_USERNAME -d postgres
         




Replace the following variables:

  * `USER_PROJECT`: the name of the user project where the database cluster was created.
  * `DBCLUSTER_NAME`: the name of the database cluster.
  * `path/to/`: the path to the database CA certificate.
  * `DB_PASSWORD`: database password for administrator user.
  * `DB_HOSTNAME`: the hostname from the database cluster status.
  * `DB_PORT`: the database port number from the database cluster status.
  * `DB_USERNAME`: with the database username (default is `dbsadmin`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
