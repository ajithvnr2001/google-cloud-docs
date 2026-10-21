---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170925-job-discovery-v2-nodejs-sample.txt
title: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170925-job-discovery-v2-nodejs-sample.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:05:07.118008+00:00
---

# https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170925-job-discovery-v2-nodejs-sample.txt

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/libs/20170925-job-discovery-v2-nodejs-sample.txt

var google = require('googleapis'); var discoveryDoc = '/path/to/jobs_discovery_v2.json'; google.discoverAPI(discoveryDoc, function (err, jobs) { if (err) { console.error('Failed to generate jobs client!'); throw err; } var key = require('/path/to/key.json'); var jwtClient = new google.auth.JWT(key.client_email, null, key.private_key, ["https://www.googleapis.com/auth/jobs"], null); jwtClient.authorize(function(err, tokens) { if (err) { console.log(err); return; } jobs.companies.list({ auth: jwtClient }, function (err, result) { if (err) { console.error('Failed to retrieve companies!'); throw err; } console.log('Companies:', result); }); }); });
