---
url: https://docs.cloud.google.com/bigtable/docs/audit-log-example/
title: Audit log example \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:55.778114+00:00
---

# Audit log example  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/audit-log-example/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Audit log example

This page shows an example of a Data Access audit log entry that is generated when you send a [write request](https://docs.cloud.google.com/bigtable/docs/writes) to Bigtable. For more details about audit log entries, see [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs). For a list of Bigtable fields that are logged, see [Audit log fields](https://docs.cloud.google.com/bigtable/docs/audit-log-fields).

For brevity, some parts of the log entry are omitted, and some fields are highlighted for emphasis.
    
    
        {
          **pro toPayload**: {
            **@ type: "type.googleapis.com/google.cloud.audit.AuditLog"**,
            status: {},
            authenticationInfo: {
              principalEmail: "user@example.com",
              serviceAccountDelegationInfo: [
                {
                  firstPartyPrincipal: {
                    principalEmail: "service-123@compute-system.iam.gserviceaccount.com"
                  }
                }
              ],
              principalSubject": "serviceAccount:123-compute@developer.gserviceaccount.com"
            },
            requestMetadata: {
              callerIp: "12.586.9.1",
              callerSuppliedUserAgent: "bigtable-1.4.0,jdk-1.8,hbase-1.4.7 grpc-java-netty/1.10.1,gzip(gfe)",
              requestAttributes: {
                time: "2020-12-10T03:22:59.373508362Z",
                auth: {}
              },
              destinationAttributes: {}
            },
            **serviceName: "** bigtable.googleapis.com",
            **methodName: "** google.bigtable.v2.Bigtable.MutateRow",
            authorizationInfo: [
              {
                resource: "projects/test-project/instances/test-instance/tables/test-table",
                permission: "bigtable.tables.mutateRows",
                granted: true,
                resourceAttributes: {}
              }
            ],
            resourceName: "projects/test-project/instances/test-instance/tables/test-table",
            **request: {**
              mutations: [
                {
                  setCell: {
                    familyName: "cf1",
                  }
                }
              ],
              tableName: "projects/test-project/instances/test-instance/tables/test-table",
              @type: "type.googleapis.com/google.bigtable.v2.MutateRowRequest",
              rowKey: "cm93LWtleQ=="
            },
          },
          insertId: "1wt6rdna0",
          resource: {
            **type: "** audited_resource",
            labels: {
              service: "bigtable.googleapis.com",
              project_id: "test-project",
              method: "google.bigtable.v2.Bigtable.MutateRow"
            }
          },
          timestamp: "2019-05-27T16:24:56.135Z",
          severity: "NOTICE",
          **logName: "** projects/test-project/logs/cloudaudit.googleapis.com%2Fdata_access",
          receiveTimestamp: "2020-05-27T04:56:47.427539594Z"
        }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
