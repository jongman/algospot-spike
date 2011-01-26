#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

TABLES = {"GDN_Problem": ["no", ("ID", "key"), "state", "author",
    "updated", "state", "author", "source", "name", "description",
    "name", "description", "input", "output",
    ("sampleinput", "sample_input"), ("sampleoutput", "sample_output"),
    "note",
    ("judgemodule", "judge_module"),
    ("timelimit", "time_limit"),
    ("memorylimit", "memory_limit"), "accepted", "submissions"]}

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
        old_cols = [col if isinstance(col, basestring) else col[0] for col in
                columns]
        new_cols = [col if isinstance(col, basestring) else col[1] for col in
                columns]
        conn.query("SELECT %s FROM %s;" % (",".join(old_cols), table))
        results = conn.store_result()
        res[table] = [dict(zip(new_cols, results.fetch_row()[0]))
                for i in xrange(results.num_rows())]
    import myjson
    print myjson.dumps(res)

if __name__ == "__main__":
    main()
