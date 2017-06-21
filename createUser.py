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
#/CDirectoryService/CreateUser
# Creates a user

# reading variables from config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Connect to Cloud Service Tenant
tenant = config.get('Properties', 'c_tenant')
new_user = config.get('Properties', 'new_user')
new_email = config.get('Properties', 'new_email')
new_mobile = config.get('Properties', 'new_mobile')
tenant_id = config.get('Properties','tenant_id')
bearer_token = config.get('Properties','bearer_token')

verify = True

url = 'https://%s/CDirectoryService/CreateUser/' % tenant

headers = {
  'X-CENTRIFY-NATIVE-CLIENT': '1',
  'Content-Type': 'application/json',
 'Authorization': 'Bearer %s' % bearer_token
}

r = requests.post(url, json = {
  "TenantId": tenant, 
  "Name": new_user,
  "Mail" : new_email,
  "MobileNumber" : new_mobile
}, headers = headers, verify = verify) 

r.raise_for_status
responseObject = r.json()

print '****************************************************************'
print ' '
print url
print ' '
print '****************************************************************'
print ' '
print 'Sending HTTPS POST Request for /CDirectoryService/CreateUser '
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
