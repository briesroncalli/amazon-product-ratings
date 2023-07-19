from pyspark import SparkContext
import sys

if __name__ == "__main__":
    # display usage of spark application
    if len(sys.argv) != 3:
        sys.stderr.write("Error: usage <input> <output>")
        exit(-1)
    
    sc = SparkContext()
    
    try:
        # ignore first line (column titles)
        # map to (product_id, star_rating) & group records w/ same key
        # compute avg star_rating for each key
        avgrating = sc.textFile(sys.argv[1]) \
            .filter(lambda line : "product_id" not in line)\
            .map(lambda line : (line.split("\t")[3], int(line.split("\t")[7]))) \
            .groupByKey(1)\
            .map(lambda vals : (vals[0], sum(vals[1]) / len(vals[1]), len(vals[1])))\
            .sortByKey()
        
        # write to output file
        avgrating.saveAsTextFile(sys.argv[2])
    except:
        print("Unable to read line")
    
    sc.stop()