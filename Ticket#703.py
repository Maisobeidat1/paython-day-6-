ticket#704
import logging
logging.basicConfig(filename="system.log",level=logging.INFO,format='%(asctime)s -  %(message)s ')
with open("grades.txt","w") as f:
    f.write("Ali.A")
    logging.info("Ali.A")