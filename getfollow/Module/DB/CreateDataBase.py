# -*- coding: utf-8 -*-
import MySQLdb
from getfollow.Module.Data.MainAccount import *
from getfollow.Module.Data.Invoice import *
from getfollow.Module.Data.Asset import *
from getfollow.Module.Data.InstagramAccount import *
from getfollow.Config.Consts import *


class CreateDataBase():
    def __init__(self):
        try:
            print 'Create Database starting ...', MYSQL_CONFIG.HOST
            conn = MySQLdb.connect(host=MYSQL_CONFIG.HOST, user=MYSQL_CONFIG.USER,
                                   passwd=MYSQL_CONFIG.PASSWORD, charset='utf8')
            cur = conn.cursor()
            cur.execute('create database if not exists getFollow character set utf8')
            conn.select_db('getFollow')

            # 1. main_account
            create_main_account_sql = 'create table if not exists main_account(' \
                                      'mid int unsigned primary key auto_increment, ' \
                                      'ip_address varchar(25),' \
                                      'last_access_time int' \
                                      ') default charset=utf8'
            cur.execute(create_main_account_sql)
            create_main_account_idx_uid_sql = 'CREATE INDEX idx_main_account_uid ON main_account (uid)'
            cur.execute(create_main_account_idx_uid_sql)

            # 2. invoice
            create_invoice_sql = 'create table if not exists invoice(' \
                                 'id int unsigned primary key auto_increment, ' \
                                 'mid int unsigned, ' \
                                 'invoice_type varchar(25),' \
                                 'amount DECIMAL(10,2),' \
                                 'date_time int' \
                                 ') default charset=utf8'
            cur.execute(create_invoice_sql)
            create_invoice_idx_mid_sql = 'CREATE INDEX idx_invoice_mid ON invoice (mid)'
            cur.execute(create_invoice_idx_mid_sql)
            create_invoice_idx_date_time_sql = 'CREATE INDEX idx_invoice_date_time ON invoice (date_time)'
            cur.execute(create_invoice_idx_date_time_sql)

            # 3. assets
            create_assets_sql = 'create table if not exists assets(' \
                                'id int unsigned primary key auto_increment, ' \
                                'mid int unsigned, ' \
                                'asset_group varchar(50),' \
                                'amount int,' \
                                'expire_time int,' \
                                'date_time int' \
                                ') default charset=utf8'
            cur.execute(create_assets_sql)
            create_assets_idx_mid_sql = 'CREATE INDEX idx_assets_mid ON assets (mid)'
            cur.execute(create_assets_idx_mid_sql)

            # 4. instagram_account
            create_instagram_account_sql = 'create table if not exists instagram_account(' \
                                           'uid varchar(50) primary key, ' \
                                           'mid int unsigned,' \
                                           'user_name varchar(50),' \
                                           'full_name varchar(50),' \
                                           'bio varchar(255),' \
                                           'website varchar(255),' \
                                           'profile_picutre varchar(255),' \
                                           'followed_by int,' \
                                           'follows int,' \
                                           'latitude double(10,6),' \
                                           'longitude double(10,6),' \
                                           'access_token varchar(50)' \
                                           ') default charset=utf8'
            cur.execute(create_instagram_account_sql)
            create_instagram_account_idx_mid_sql = 'CREATE INDEX idx_instagram_account_mid ON instagram_account (mid)'
            cur.execute(create_instagram_account_idx_mid_sql)

            cur.close()
            conn.close()
            print("create db finished")
        except Exception, e:
            print "Mysql Error %s" % (e.args[0])


MainAccount.metadata.create_all(MYSQL_ENGINE)
InstagramAccount.metadata.create_all(MYSQL_ENGINE)
Invoice.metadata.create_all(MYSQL_ENGINE)
Asset.metadata.create_all(MYSQL_ENGINE)

