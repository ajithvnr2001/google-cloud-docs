---
url: https://docs.cloud.google.com/static/feeds/developer-connect-security-bulletins.xml
title: Developer Connect - Security Bulletins
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:05:13.234112+00:00
---

# Developer Connect - Security Bulletins

> Source: https://docs.cloud.google.com/static/feeds/developer-connect-security-bulletins.xml

tag:google.com,2016:developer-connect-security-bulletinsDeveloper Connect - Security BulletinsGoogle Cloud Documentation2026-07-13T15:34:30.404844+00:00GCP-2026-048tag:google.com,2016:developer-connect-security-bulletins#GCP-2026-0482026-07-13T00:00:00+00:00**Published:** 2026-07-13

### Description

Description | Severity | Notes  
---|---|---  
When you create or update repository connections, Developer Connect uses Secret Manager secrets to authenticate to third-party Git providers. For GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections, these referenced secrets were previously retrieved by the Developer Connect service agent (P4SA) on your behalf. This meant that permission checks were performed against the P4SA's credentials rather than those of the calling principal. This could allow a principal with limited permissions to read referenced Secret Manager secrets by pointing the repository connection host URI to an attacker-controlled endpoint. To mitigate this vulnerability and adhere to the security principle of least privilege, Developer Connect now checks permissions against both the calling principal's credentials (using end-user credentials) and the P4SA when calling repository connection APIs for GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections. Specifically, the server now verifies that both the caller and the P4SA possess the `secretmanager.versions.access` IAM permission on the referenced Secret Manager secrets. **What should I do?** No action is required for existing repository connections. If you encounter permission errors when creating or updating GitLab Enterprise (GLE) or Bitbucket Data Center (BBDC) repository connections, grant the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role on the referenced secrets to the user or service account creating or updating the connections. **What vulnerabilities are addressed by this patch?** This vulnerability allowed users with repository connection administrator access to read referenced Secret Manager secrets because the permission checks were only performed against the P4SA's credentials. By requiring permission checks against both the calling principal (using end-user credentials) and the P4SA for GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections, only users authorized with the `secretmanager.versions.access` IAM permission on the secrets (in addition to the P4SA itself) can use them in repository connections. | Medium |   
]]>
