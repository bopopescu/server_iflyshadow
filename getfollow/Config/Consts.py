# -*- coding: utf-8 -*-
import os
from sqlalchemy import *

BASE_DIR = os.path.dirname(__file__)
GLOBAL_CONFIG_FILE = BASE_DIR + "/config_local.yaml"
import GetFollowConfig
import MySqlConfig
import SecurityConfig

MYSQL_CONFIG = MySqlConfig.MySqlConfig()
GET_FOLLOW_CONFIG = GetFollowConfig.GetFollowConfig()
SECURITY_CONFIG = SecurityConfig.SecurityConfig()

MYSQL_ENGINE = create_engine('mysql+mysqlconnector://' + MYSQL_CONFIG.USER + ':' + MYSQL_CONFIG.PASSWORD
                             + '@' + MYSQL_CONFIG.HOST + ':3306/' + MYSQL_CONFIG.SCHEMA)