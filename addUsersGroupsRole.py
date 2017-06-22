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
#/SaasManage/AddUsersAndGroupsToRole
# Add principals to a role

# reading variables from config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Connect to Cloud Service Tenant
tenant = config.get('Properties', 'c_tenant')
tpsswd = config.get('Properties', 'tpsswd')
c_user = config.get('Properties', 'c_user')
tenant_id = config.get('Properties','tenant_id')
bearer_token = config.get('Properties','bearer_token')
guid = config.get('Properties', 'guid')
uuid = config.get('Properties','uuid')

verify = True

url = 'https://%s/SaasManage/AddUsersAndGroupsToRole/' % tenant

headers = {
  'X-CENTRIFY-NATIVE-CLIENT': '1',
  'Content-Type': 'application/json',
 'Authorization': 'Bearer %s' % bearer_token
}

# guid = UUID of Role
# Name (string): Role UUID ,
# Users (Array[string], optional): List of user UUIDs or Names to add to the role (default=null) ,
# Groups (Array[string], optional): List of group UUIDs or Names to add to the role (default=null) ,
# Roles (Array[string], optional): List of role UUIDs or Names to add to the role (default=null)

r = requests.post(url, json = {
  "Name": guid,
  "Users": [uuid]
}, headers = headers, verify = verify) 

r.raise_for_status
responseObject = r.json()

print '****************************************************************'
print ' '
print url
print ' '
print '****************************************************************'
print ' '
print 'Sending HTTPS POST Request for /SaasManage/AddUsersAndGroupsToRole '
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
