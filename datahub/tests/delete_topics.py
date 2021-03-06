#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import sys
import traceback

from datahub import DataHub
from datahub.utils import Configer
from datahub.models import Project, Topic, RecordType, FieldType, RecordSchema, TupleRecord, CursorType
from datahub.errors import DatahubException, ObjectAlreadyExistException

configer = Configer('datahub.ini')
access_id = configer.get('datahub', 'access_id', '')
access_key = configer.get('datahub', 'access_key', '')
endpoint = configer.get('datahub', 'endpoint', '')
project_name = configer.get('datahub', 'project_name', 'meter_project_test')
topic_name = configer.get('datahub', 'topic_name', 'meter_topic_test')

print "======================================="
print "access_id: %s" % access_id
print "access_key: %s" % access_key
print "endpoint: %s" % endpoint
print "project_name: %s" % project_name
print "topic_name: %s" % topic_name
print "=======================================\n\n"

if not access_id or not access_key or not endpoint:
    print "access_id and access_key and endpoint must be set!"
    sys.exit(-1)

dh = DataHub(access_id, access_key, endpoint)

try:
    for pi in range(1,10):
        project_name = "meter_project_test_%d" % pi
        for ti in range(1,100):
            topic_name = "meter_topic_test_%d_%d" %(pi, ti)
            try:
                dh.delete_topic(topic_name, project_name)
                print "delete topic %s success!" % topic_name
            except Exception, e:
                print "delete %s failed!" % topic_name
                print traceback.format_exc()
            print "=======================================\n\n"
except Exception, e:
    print traceback.format_exc()
    sys.exit(-1)
