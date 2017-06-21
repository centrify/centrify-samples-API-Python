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
#/UserMgmt/InviteUsers
# Invites one or more users to the cloud portal 

# reading variables from config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Connect to Cloud Service Tenant
tenant = config.get('Properties', 'c_tenant')
tpsswd = config.get('Properties', 'tpsswd')
c_user = config.get('Properties', 'c_user')
tenant_id = config.get('Properties','tenant_id')
bearer_token = config.get('Properties','bearer_token')
uuid = config.get('Properties','uuid')
guid = config.get('Properties','guid')

verify = True

url = 'https://%s/UserMgmt/InviteUsers/' % tenant

headers = {
  'X-CENTRIFY-NATIVE-CLIENT': '1',
  'Content-Type': 'application/json',
 'Authorization': 'Bearer %s' % bearer_token
}

# uuid can be retrieved for a list of users by calling /CDirectoryService/GetUsers

r = requests.post(url, json = {

  "Entities": [
    { 
        "Type": 'Role',
        "Guid": guid
    },
    {
        "Type": "User",
        "Guid": uuid,
        "Name": c_user
    }
  ],
  "EmailInvite": "True",
  "SmsInvite": "True",
  "GroupInvite": "True"
   
}, headers = headers, verify = verify) 

r.raise_for_status
responseObject = r.json()

print '****************************************************************'
print ' '
print url
print ' '
print '****************************************************************'
print ' '
print 'Sending HTTPS POST Request for /UserMgmt/InviteUsers '
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
