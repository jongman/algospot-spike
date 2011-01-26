#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

TABLES = {"problems": ["no", "uploaded", "opened", "author", "source",
    "language", "name", "description", "input", "output", "sample_input",
    "sample_output", "note", "judge_module", "time_limit", "memory_limit",
    "accepted", "submissions"]}

def main():
    if len(sys.argv) != 5:
        print "Dumps all algospot-related MySQL entries into JSON."
        print "Usage) %s (host) (db) (username) (password)" % sys.argv[0]
        return
    _, host, db, username, password = sys.argv
    import MySQLdb
    conn = MySQLdb.connect(host, username, password, db)
    res = {}
    for table, columns in TABLES.iteritems():
        conn.query("SELECT %s FROM %s;" % (",".join(columns), table))
        results = conn.store_result()
        res[table] = [dict(zip(columns, results.fetch_row()[0]))
                for i in xrange(results.num_rows())]
    import myjson
    print myjson.dumps(res)

if __name__ == "__main__":
    main()
