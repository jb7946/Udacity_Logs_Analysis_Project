#!/usr/bin/env python3

import psycopg2

# schema in postgres database that contains tables for queries to execute
dbSchema = "news"

# sql for question 1:
# 1. What are the most popular three articles of all time?
popularArticlesSql = '''
select articles.title as article_title,
     concat(to_char(logs.count_slug,'999,999'),' ','views')
     as article_views
from articles
inner join (select substring(path,10) as log_slug, count(path) as count_slug
            from log
            where path like '/article/%'
            group by path) logs
            on articles.slug=logs.log_slug
order by logs.count_slug desc
limit 3;
'''

# sql for question 2:
# 2. Who are the most popular article authors of all time?
popularAuthorsSql = '''
select authors.name as author_name,
     concat(to_char(sum(logs.count_slug),'999,999'),' ','views')
     as article_views
from articles
inner join authors on articles.author=authors.id
inner join (select substring(path,10) as log_slug, count(path) as count_slug
            from log where path like '/article/%'
            group by path) logs
            on logs.log_slug=articles.slug
group by authors.name
order by sum(logs.count_slug) desc;
'''

# sql for question 3:
# 3. On which days did more than 1% of requests lead to errors?
responseErrorPercentSql = '''
select to_char(traffic_analysis.dayactivity, 'Mon dd, yyyy') as date_activity,
     concat(traffic_analysis.prcnt,' % errors') as percent_errors
from (select alltraffic.dayactivity, alltraffic.dayresponse,
      errtraffic.errresponse,
      round((cast(errtraffic.errresponse
      as numeric) / cast(alltraffic.dayresponse
      as numeric)) * 100,1) as prcnt
      from (select time::timestamp::date as dayactivity,
      count(status) as dayresponse
      from log
      group by time::timestamp::date) alltraffic
inner join (select time::timestamp::date as erractivity,
            count(status) as errresponse
            from log
            where status != '200 OK'
            group by time::timestamp::date) errtraffic
            on alltraffic.dayactivity=errtraffic.erractivity
            where round((cast(errtraffic.errresponse
            as numeric) /
            cast(alltraffic.dayresponse as numeric))*100,1) >= 1)
            traffic_analysis;
'''


# function to create header for each report
def report_header(subtitle, mytype):

    if (mytype == "initial"):
        print("\nLog Analysis Project Report:")
    elif (mytype == "body"):
        print("\n" + subtitle + ":\n")
    else:
        print("")


# function to create footer for report
def report_footer():
    print("\nReport created by John Bitner.\n")


# function to connect to the postgres database, send sql and return response
def db_connect(sql):

    db = psycopg2.connect(database=dbSchema)
    c = db.cursor()
    c.execute(sql)
    return c.fetchall()
    db.close()


# function to execute report, print header and report response
def print_report(type, subtitle, sql):

    if (type != "NA"):
        report_header(subtitle, type)
    if (sql != "NA"):
        db_result = db_connect(sql)
    if (sql != "NA"):
        for db_row in db_result:
            print ('\t' + str(db_row[0]) + ' - ' + str(db_row[1]))


# This section executes reports and prints output to screen
print_report("initial", "NA", "NA")
print_report("body", "Most popular three articles of all time",
             popularArticlesSql)
print_report("body", "Most popular article authors of all time",
             popularAuthorsSql)
print_report("body", "Days where more than 1% of http requests led to errors",
             responseErrorPercentSql)
#report_footer()
