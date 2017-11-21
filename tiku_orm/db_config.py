# coding=utf-8
import pymysql


class DatabaseConfig(object):
    local_db = {
        'host': 'test.wangxiyang.com',
        'user': 'root',
        'port': 3306,
        'password': 'asd123',
        'db': 'tiku-dev',
        'charset': 'utf8mb4',
        'use_unicode': False,
        'cursorclass': pymysql.cursors.DictCursor,
    }

    dev_db = {
        'host': '10.10.228.163',
        'user': 'test',
        'port': 3301,
        'password': 'OnlyKf!@#',
        'db': 'tiku',
        'charset': 'utf8mb4',
        'use_unicode': False,
        'cursorclass': pymysql.cursors.DictCursor,
    }

    QA_db = {
        'host': '10.9.35.226',
        'user': 'test',
        'port': 3329,
        'password': 'qaOnly!@#',
        'db': 'tiku',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }

    # 本地开发速算盒子总库
    dev_susuan_db = {
        'host': 'test.wangxiyang.com',
        'user': 'root',
        'port': 3306,
        'password': 'asd123',
        'db': 'knowboxstore4',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 速算题库总库线上库
    online_susuan_db = {
        'host': '10.19.141.31',
        'user': 'wangxy',
        'port': 3306,
        'password': 'wangxy112',
        'db': 'knowboxstore',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 线上从库
    online_slave_db = {
        'host': '10.215.48.111',
        'user': 'liyj',
        'port': 3306,
        'password': 'liyj123',
        'db': 'tiku',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
