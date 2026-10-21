---
url: https://docs.cloud.google.com/talent-solution/job-search/libs/20160916-jobs-api-nodejs-client-example.txt
title: https://docs.cloud.google.com/talent-solution/job-search/libs/20160916-jobs-api-nodejs-client-example.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:54:54.879382+00:00
---

# https://docs.cloud.google.com/talent-solution/job-search/libs/20160916-jobs-api-nodejs-client-example.txt

> Source: https://docs.cloud.google.com/talent-solution/job-search/libs/20160916-jobs-api-nodejs-client-example.txt

var google = require('googleapis'); var discoveryDoc = 'path/to/discovery.json'; google.discoverAPI(discoveryDoc, function (err, jobs) { if (err) { console.error('Failed to generate jobs client!'); throw err; } var key = require('path/to/your/key.json'); var jwtClient = new google.auth.JWT(key.client_email, null, key.private_key, ["https://www.googleapis.com/auth/jobs"], null); jwtClient.authorize(function(err, tokens) { if (err) { console.log(err); return; } jobs.companies.list({ auth: jwtClient }, function (err, result) { if (err) { console.error('Failed to retrieve companies!'); throw err; } console.log('Companies:', result); }); }); }); 
