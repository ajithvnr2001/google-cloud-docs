---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/postgres/pgxv4/
title: Package cloud.google.com/go/cloudsqlconn/postgres/pgxv4 (v1.25.3) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:39.288035+00:00
---

# Package cloud.google.com/go/cloudsqlconn/postgres/pgxv4 (v1.25.3)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest/postgres/pgxv4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Package cloud.google.com/go/cloudsqlconn/postgres/pgxv4 (v1.25.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.25.3 (latest)  1.25.2  1.24.0  1.23.0  1.22.1  1.21.2  1.20.2  1.19.1  1.18.1  1.17.3  1.16.1  1.15.0  1.14.2  1.13.2  1.12.1  1.11.1  1.10.1  1.9.0  1.8.1  1.7.0  1.6.0  1.5.2  1.4.3  1.3.0  1.2.4  1.1.1  1.0.1  0.5.2  0.4.0  0.3.1  0.2.0  0.1.0 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/cloudsqlconn/postgres/pgxv4). 

Package pgxv4 provides a Cloud SQL Postgres driver that uses pgx v4 and works with the database/sql package. 

Deprecated: pgxv4 is no longer maintained because pgproto3 has reached end-of-life. This package has been rewired to use pgxv5 internally for security reasons. Please use pgxv5 directly instead.

## Functions 

### func RegisterDriver (deprecated)
    
    
    func RegisterDriver(name [string](https://pkg.go.dev/builtin#string), opts ...[cloudsqlconn](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest).[Option](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudsqlconn/latest#cloud_google_com_go_cloudsqlconn_Option)) (func() [error](https://pkg.go.dev/builtin#error), [error](https://pkg.go.dev/builtin#error))

RegisterDriver registers a Postgres driver that uses the cloudsqlconn.Dialer configured with the provided options. The choice of name is entirely up to the caller and may be used to distinguish between multiple registrations of differently configured Dialers. The driver now uses pgx/v5 internally. RegisterDriver returns a cleanup function that should be called one the database connection is no longer needed.

Deprecated: pgxv4 is no longer maintained because pgproto3 has reached end-of-life. This function now uses pgxv5 internally for security reasons. Please use pgxv5.RegisterDriver instead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
