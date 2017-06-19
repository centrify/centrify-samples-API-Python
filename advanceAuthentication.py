# Copyright 2016 Centrify Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import json
import ConfigParser
import sys

# This Python script connects to Centrify 's Identity Service
#/Security/AdvanceAuthentication #Attempts to advance the state of an authentication session.

# reading variables from config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

#params needed to send in AdvanceAuth request
sessionID = sys.argv[1]
mechanismID = sys.argv[2]

# Connect to Cloud Service Tenant
tenant = config.get('Properties', 'c_tenant')
tpsswd = config.get('Properties', 'tpsswd')
c_user = config.get('Properties', 'c_user')
tenant_id = config.get('Properties','tenant_id')
verify = True

url = 'https://%s/security/AdvanceAuthentication/' % tenant

headers = {
  'X-CENTRIFY-NATIVE-CLIENT': '1',
  'Content-Type': 'application/json'
}

r = requests.post(url, json = {
  "TenantId": tenant_id,
  "SessionId": sessionID,
  "MechanismId": mechanismID,
  "Action": "Answer",
  "Answer": tpsswd
}, headers = headers, verify = verify) 

r.raise_for_status
responseObject = r.json()

print '****************************************************************'
print ' '
print url
print ' '
print '****************************************************************'
print ' '
print 'Sending HTTPS POST Request for /Security/AdvanceAuthentication '
print ' '
print '****************************************************************'
print ' '
print 'JSON Response: '
print ' '
print responseObject

print ' '
print ' '
print ' '
print ' '

#EOF
